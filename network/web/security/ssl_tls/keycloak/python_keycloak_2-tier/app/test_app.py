import pytest
import requests_mock
import subprocess
import time
from frontend import FrontendApp
from backend import BackendApp

# Create instances of the frontend and backend applications
frontend_app = FrontendApp().app
backend_app = BackendApp().app

# Configure the frontend and backend applications for testing
frontend_app.config['TESTING'] = True
backend_app.config['TESTING'] = True

# Define constants for URLs
KEYCLOAK_SERVER_URL = 'http://localhost:8080/auth/realms/mycompany/protocol/openid-connect'
KEYCLOAK_AUTH_URL = f'{KEYCLOAK_SERVER_URL}/auth'
KEYCLOAK_TOKEN_URL = f'{KEYCLOAK_SERVER_URL}/token'
KEYCLOAK_INTROSPECT_URL = f'{KEYCLOAK_SERVER_URL}/token/introspect'
BACKEND_SERVER_CMD = ['flask', 'run', '--port', '5001']

@pytest.fixture(scope='module')
def backend_server():
    # Run the backend server in a separate process
    process = subprocess.Popen(BACKEND_SERVER_CMD, env={"FLASK_APP": "backend.py"})
    time.sleep(2)  # Give the server time to start
    yield
    process.terminate()
    process.wait()

@pytest.fixture
def client(backend_server):
    with frontend_app.test_client() as client:
        yield client

def mock_keycloak(requests_mock):
    # Mock Keycloak's token endpoint
    requests_mock.post(KEYCLOAK_TOKEN_URL, json={
        'access_token': 'mock-access-token'
    })

    # Mock Keycloak's introspection endpoint
    requests_mock.post(KEYCLOAK_INTROSPECT_URL, json={
        'active': True,
        'username': 'Alice',
        'realm_access': {
            'roles': ['admin']
        },
        'resource_access': {
            'myapp': {
                'roles': ['editor']
            },
            'mobileapp': {
                'roles': ['mobile-user']
            }
        }
    })

def test_secure_resource_flow(client):
    with requests_mock.Mocker() as m:
        mock_keycloak(m)

        # Step 1: User requests secure resource
        response = client.get('/secure-resource')
        print(f"Step 1: status code = {response.status_code}, location = {response.location}")
        assert response.status_code == 302  # Redirect to login
        assert '/login' in response.location

        # Step 2: User is redirected to Keycloak login
        keycloak_auth_url = response.location
        response = client.get(keycloak_auth_url)
        print(f"Step 2: status code = {response.status_code}, location = {response.location}")
        assert response.status_code == 302  # Redirect to Keycloak login page

        # Simulate Keycloak login and redirection back to frontend with authorization code
        keycloak_callback_url = '/on_auth_code?code=mock-auth-code'
        response = client.get(keycloak_callback_url)
        print(f"Step 3: status code = {response.status_code}, location = {response.location}")
        assert response.status_code == 302  # Redirect to get_auth_code

        # Step 3: Frontend exchanges authorization code for tokens
        response = client.get(response.location)
        print(f"Step 4: status code = {response.status_code}, location = {response.location}")
        assert response.status_code == 302  # Redirect to original secure resource

        # Step 4: User requests secure resource again with token
        response = client.get('/secure-resource', headers={'Cookie': 'access_token=mock-access-token'})
        print(f"Step 5: status code = {response.status_code}, response = {response.get_json()}")
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == 'Viewer access: You can view content.'

if __name__ == '__main__':
    pytest.main()
