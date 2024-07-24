

- `my_backend.py`

```python
from flask import Flask, request, jsonify, make_response, redirect, url_for
from keycloak import KeycloakOpenID

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Used to sign session cookies for security

# Configuration
KEYCLOAK_SERVER_URL = "http://localhost:8080/auth/"
CLIENT_ID = "myapp"
CLIENT_SECRET = "your-client-secret"
REALM_NAME = "mycompany"
REDIRECT_URI = "http://localhost:5000/callback"
FRONTEND_URL = "http://localhost:5000"

# Configure Keycloak client
keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_SERVER_URL,
                                client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                realm_name=REALM_NAME)

@app.route('/token', methods=['POST'])
def token():
    data = request.get_json()
    code = data.get('code')
    if not code:
        return jsonify({"error": "Authorization code not provided"}), 400

    # Exchange authorization code for token
    token_response = keycloak_openid.token(code, redirect_uri=REDIRECT_URI)
    access_token = token_response['access_token']

    # Store the access token in an HTTP-only cookie
    resp = make_response(jsonify({"message": "Token received"}))
    resp.set_cookie('access_token', access_token, httponly=True, secure=True)
    return resp

@app.route('/secure-resource')
def secure_resource():
    # Retrieve access token from cookie
    access_token = request.cookies.get('access_token')
    if not access_token:
        return redirect(FRONTEND_URL + url_for('login', next=request.url))

    # Decode token to get user roles and resource access
    decoded_token = keycloak_openid.decode_token(access_token, key={"alg": "RS256"})
    user_roles = decoded_token.get('realm_access', {}).get('roles', [])
    
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

@app.route('/logout')
def logout():
    # Clear the session and cookies
    session.clear()
    resp = make_response(jsonify({"message": "Logged out"}))
    resp.set_cookie('access_token', '', expires=0, httponly=True, secure=True)
    return resp

if __name__ == '__main__':
    app.run(port=5001, debug=True)

```
