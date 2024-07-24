

## Access Control


2 fundamental questions to answer when a user tries to access a secure service:

- ### who am i - Authentication
    - client presents **[credentials](credentials.md)** eg username and password
    - service verifies credentials, and (if valid) maps them to a known **identity** (account) 
    - often in combination with token/cert for use in subsequent requests

- ### what may i do - Authorization
    - service determines what **permissions** this identitified user has.
    - often in combination with roles/attributes embedded in the token/cert
