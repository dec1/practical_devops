from flask import Flask, redirect, request, session, url_for, jsonify
import requests

class FrontendApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'supersecretkey'  # Used to sign session cookies for security
        self.KEYCLOAK_SERVER_URL = "http://localhost:8080/auth/"
        self.CLIENT_ID = "myapp"
        self.REALM_NAME = "mycompany"
        self.REDIRECT_URI = "http://localhost:5000/on_auth_code"
        self.BACKEND_URL = "http://localhost:5001"

        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/login', 'login', self.login)
        self.app.add_url_rule('/on_auth_code', 'on_auth_code', self.on_auth_code)
        self.app.add_url_rule('/secure-resource', 'secure_resource', self.secure_resource)
        self.app.add_url_rule('/logout', 'logout', self.logout)

    def index(self):
        return 'Welcome to the Frontend of the Flask + Keycloak integration example.'

    def login(self):
        # Store the original requested URL to redirect after login
        next_url = request.args.get('next', url_for('index'))
        session['next_url'] = next_url
        # Redirect user to Keycloak login
        auth_url = f"{self.KEYCLOAK_SERVER_URL}realms/{self.REALM_NAME}/protocol/openid-connect/auth?client_id={self.CLIENT_ID}&response_type=code&redirect_uri={self.REDIRECT_URI}"
        return redirect(auth_url)

    def on_auth_code(self):
        # Get the authorization code from the URL parameters
        code = request.args.get('code')
        if not code:
            return "Authorization code not provided", 400

        # Make a request to the backend to exchange the authorization code for tokens
        response = requests.post(f"{self.BACKEND_URL}/token", json={'code': code})
        if response.status_code != 200:
            return jsonify(response.json()), response.status_code

        # Redirect to the original requested URL
        next_url = session.get('next_url', url_for('index'))
        session.pop('next_url', None)
        return redirect(next_url)

    def secure_resource(self):
        # Make a request to the backend to access the secure resource
        response = requests.get(f"{self.BACKEND_URL}/secure-resource", cookies=request.cookies)
        if response.status_code == 401:
            return redirect(url_for('login', next=request.url))
        return jsonify(response.json())

    def logout(self):
        # Clear the session
        session.clear()
        # Make a request to the backend to log out
        response = requests.get(f"{self.BACKEND_URL}/logout")
        return redirect(url_for('index'))

if __name__ == '__main__':
    frontend_app = FrontendApp()
    frontend_app.app.run(port=5000, debug=True)
