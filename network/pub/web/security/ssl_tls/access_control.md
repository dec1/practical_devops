

## Access Control


2 fundamental questions to answer when a user tries to access a secure service:

- ### Authentication - Identity
    - client presents **[credentials](credentials.md)** eg username and password
    - service verifies credentials, and (if valid) maps them to a known **identity** (account) 
    - often in combination with token/cert for use in subsequent requests

- ###  Authorization - Permissions
    - service determines what **permissions** this identified user has.
    - often in combination with roles/attributes embedded in the token/cert
