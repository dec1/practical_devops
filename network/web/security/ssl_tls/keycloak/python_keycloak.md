### Access Flow Example

- Python and Keycloak

This example shows how a Flask web application can use Keycloak to authenticate a user, retrieve their roles from the access token, and conditionally serve resources based on those roles. This leverages Keycloak's ability to manage user identities and roles, demonstrating a practical integration for access control in web applications.

#### Explanation of `app.secret_key`

The `app.secret_key` is used by Flask to sign the session cookie, which ensures the integrity and security of the session data. This prevents attackers from tampering with the session data on the client side.

- Pre-requisites:
    - A Keycloak server setup with realms, users, and roles configured.
    - `python-keycloak` library installed:
        - `pip install python-keycloak`

- `my_server.py`

    ```python
    from flask import Flask, request, jsonify, redirect, url_for, session, make_response
    from keycloak import KeycloakOpenID

    app = Flask(__name__)
    app.secret_key = 'supersecretkey'  # Used to sign session cookies for security

    # Configuration
    KEYCLOAK_SERVER_URL = "http://localhost:8080/auth/"
    CLIENT_ID = "myapp"
    CLIENT_SECRET = "your-client-secret"
    REALM_NAME = "mycompany"
    REDIRECT_URI = "http://localhost:5000/token"

    # Configure Keycloak client
    keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_SERVER_URL,
                                    client_id=CLIENT_ID,
                                    client_secret=CLIENT_SECRET,
                                    realm_name=REALM_NAME)

    @app.route('/')
    def index():
        return 'Welcome to the Flask + Keycloak integration example.'

    @app.route('/login')
    def login():
        # Redirect user to Keycloak login
        auth_url = keycloak_openid.auth_url(redirect_uri=REDIRECT_URI)
        return redirect(auth_url)

    @app.route('/token')
    def token():
        # Get the authorization code from the URL parameters
        code = request.args.get('code')
        if not code:
            return "Authorization code not provided", 400

        # Exchange authorization code for token
        token_response = keycloak_openid.token(code, redirect_uri=REDIRECT_URI)
        access_token = token_response['access_token']

        # Store the access token in an HTTP-only cookie
        resp = make_response(redirect(url_for('secure_resource')))
        resp.set_cookie('access_token', access_token, httponly=True, secure=True)
        return resp

    @app.route('/secure-resource')
    def secure_resource():
        # Retrieve access token from cookie
        access_token = request.cookies.get('access_token')
        if not access_token:
            return redirect(url_for('login'))
        
        # Decode token to get user roles and resource access
        decoded_token = keycloak_openid.decode_token(access_token, key={"alg": "RS256"})
        user_roles = decoded_token.get('realm_access', {}).get('roles', [])
        
        # Check user roles to determine access
        if "admin" in user_roles:
            return "Admin access: You can access sensitive data."
        elif "user" in user_roles:
            return "User access: You have standard access."
        elif "editor" in decoded_token.get('resource_access', {}).get('myapp', {}).get('roles', []):
            return "Editor access: You can edit content."
        elif "viewer" in decoded_token.get('resource_access', {}).get('myapp', {}).get('roles', []):
            return "Viewer access: You can view content."
        else:
            return "Access denied: You do not have the necessary roles."

    @app.route('/logout')
    def logout():
        # Clear the session and cookies
        session.clear()
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('access_token', '', expires=0, httponly=True, secure=True)
        return resp

    if __name__ == '__main__':
        app.run(debug=True)
    ```

- Keycloak (JWT) Token
    - The JWT token includes various claims.
    - Among these claims, there are typically fields for `roles`, which might be listed under a claim like `realm_access` or `resource_access` depending on whether they are realm roles (independent of the client being used by the user) or client-specific (dependent on which client the user is using to access the resource) roles.
    - **Example Token content**:
        ```yaml
        {
            "exp": 1300819380,
            "user_name": "Alice",
            "realm_access": {
                "roles": ["admin"]
            },
            "resource_access": {
                "myapp": {
                    "roles": ["editor"]
                },
                "mobileapp": {
                    "roles": ["mobile-user"]
                }
            },
            "iss": "http://localhost:8080/auth/realms/mycompany",
            "aud": "myapp"
        }
        ```
        ```yaml
        {
            "exp": 1300819380,
            "user_name": "Bob",
            "realm_access": {
                "roles": ["user"]
            },
            "resource_access": {
                "myapp": {
                    "roles": ["viewer"]
                }
            },
            "iss": "http://localhost:8080/auth/realms/mycompany",
            "aud": "myapp"
        }
        ```

    - **Benefits of Embedding Roles in Tokens**:
        - **Simpler**: The application can itself determine the user’s permissions without needing to make an additional request to Keycloak or another service to fetch this information.
        - **Reduced Latency**: Access control decisions can be made quickly, reducing the latency in serving protected resources.
