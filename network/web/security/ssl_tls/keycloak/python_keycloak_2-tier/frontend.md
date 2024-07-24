


- `my_frontend.py`

```python
from flask import Flask, redirect, request, session, url_for, jsonify
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Used to sign session cookies for security

# Configuration
KEYCLOAK_SERVER_URL = "http://localhost:8080/auth/"
CLIENT_ID = "myapp"
REALM_NAME = "mycompany"
REDIRECT_URI = "http://localhost:5000/callback"
BACKEND_URL = "http://localhost:5001"

@app.route('/')
def index():
    return 'Welcome to the Frontend of the Flask + Keycloak integration example.'

@app.route('/login')
def login():
    # Store the original requested URL to redirect after login
    next_url = request.args.get('next', url_for('index'))
    session['next_url'] = next_url
    # Redirect user to Keycloak login
    auth_url = f"{KEYCLOAK_SERVER_URL}realms/{REALM_NAME}/protocol/openid-connect/auth?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Get the authorization code from the URL parameters
    code = request.args.get('code')
    if not code:
        return "Authorization code not provided", 400

    # Store the authorization code in the session and pass it to the backend
    session['authorization_code'] = code
    return redirect(url_for('get_auth_code'))

@app.route('/get_auth_code')
def get_auth_code():
    # Pass the authorization code to the backend
    code = session.get('authorization_code')
    if not code:
        return "No authorization code in session", 400

    # Make a request to the backend to exchange the authorization code for tokens
    response = requests.post(f"{BACKEND_URL}/token", json={'code': code})
    if response.status_code != 200:
        return jsonify(response.json()), response.status_code

    # Redirect to the original requested URL
    next_url = session.get('next_url', url_for('index'))
    session.pop('next_url', None)
    return redirect(next_url)

@app.route('/secure-resource')
def secure_resource():
    # Make a request to the backend to access the secure resource
    response = requests.get(f"{BACKEND_URL}/secure-resource", cookies=request.cookies)
    if response.status_code == 401:
        return redirect(url_for('login', next=request.url))
    return jsonify(response.json())

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    # Make a request to the backend to log out
    response = requests.get(f"{BACKEND_URL}/logout")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)

```
