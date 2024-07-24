from flask import Flask, request, jsonify, make_response, redirect, url_for, session
from keycloak import KeycloakOpenID

class BackendApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'supersecretkey'  # Used to sign session cookies for security
        self.KEYCLOAK_SERVER_URL = "http://localhost:8080/auth/"
        self.CLIENT_ID = "myapp"
        self.CLIENT_SECRET = "your-client-secret"
        self.REALM_NAME = "mycompany"
        self.REDIRECT_URI = "http://localhost:5000/on_auth_code"
        self.FRONTEND_URL = "http://localhost:5000"

        self.keycloak_openid = KeycloakOpenID(server_url=self.KEYCLOAK_SERVER_URL,
                                              client_id=self.CLIENT_ID,
                                              realm_name=self.REALM_NAME)

        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule('/token', 'token', self.token, methods=['POST'])
        self.app.add_url_rule('/secure-resource', 'secure_resource', self.secure_resource)
        self.app.add_url_rule('/logout', 'logout', self.logout)

    def token(self):
        data = request.get_json()
        code = data.get('code')
        if not code:
            return jsonify({"error": "Authorization code not provided"}), 400

        # Exchange authorization code for token
        token_response = self.keycloak_openid.token(data=code, client_secret=self.CLIENT_SECRET, redirect_uri=self.REDIRECT_URI)
        access_token = token_response['access_token']

        # Store the access token in an HTTP-only cookie
        resp = make_response(jsonify({"message": "Token received"}))
        resp.set_cookie('access_token', access_token, httponly=True, secure=True)
        print(f"Token set in cookie: {access_token}")  # Debugging statement
        return resp

    def secure_resource(self):
        # Retrieve access token from cookie
        access_token = request.cookies.get('access_token')
        print(f"Access token from cookie: {access_token}")  # Debugging statement
        if not access_token:
            return redirect(self.FRONTEND_URL + url_for('login', next=request.url))

        # Decode token to get user roles and resource access
        try:
            decoded_token = self.keycloak_openid.decode_token(access_token, key={"alg": "RS256"})
            user_roles = decoded_token.get('realm_access', {}).get('roles', [])
        except Exception as e:
            print(f"Token decode error: {e}")
            return redirect(self.FRONTEND_URL + url_for('login', next=request.url))

        # Check user roles to determine access
        if "admin" in user_roles:
            return jsonify({"message": "Admin access: You can access sensitive data."})
        elif "user" in user_roles:
            return jsonify({"message": "User access: You have standard access."})
        elif "editor" in decoded_token.get('resource_access', {}).get('myapp', {}).get('roles', []):
            return jsonify({"message": "Editor access: You can edit content."})
        elif "viewer" in decoded_token.get('resource_access', {}).get('myapp', {}).get('roles', []):
            return jsonify({"message": "Viewer access: You can view content."})
        else:
            return jsonify({"error": "Access denied: You do not have the necessary roles."}), 403

    def logout(self):
        # Clear the session and cookies
        session.clear()
        resp = make_response(jsonify({"message": "Logged out"}))
        resp.set_cookie('access_token', '', expires=0, httponly=True, secure=True)
        return resp

if __name__ == '__main__':
    backend_app = BackendApp()
    backend_app.app.run(port=5001, debug=True)
