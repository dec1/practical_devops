
## Authentication

Prerequisites:
- `Secure connection` (eg both parties know that they have `constant partner` for whole conversation)
 eg TSL, HTTPS with pub/priv **keys** (partner is holder of private key being used to sign incoming messages)

- `Who` - this constant partner is that they are securely communicating with can be determined in multiple ways:

    - ### 1) Username, Password
        - eg **Basic Authentication**  (username, password) sent (base64 encoded in 
        **Authorization header**) 
            - `Authorization: Basic <base64-encoded username:password>` 
        with **each request**.
        - Username, password must previously have been configured (as valid) on server

    - ### 2) Token

        - Once authenticated by some secure means (eg by Basic Authentication), a client can additionally acquire a (bearer) **token** signed by server.
        - In **each subsequent request**, client can submit this token (instead of username,password) in the Authorization header as 
            - `Authorization : Bearer <token>`
        - Advantages: token may be 
            - **short lived** and **can be revoked** at any time. 
            - restricted in **permissions** or roles it can be used to perform
        - eg JWT (JSON web token), which can additionally include authorization

    - ### 3) Certificate
        - Contain: 
            - *identifying info* fields
                - **Common Name**  (CN)
                - **Organizations** (O) - optional
            - **public key**
        - The info in cert is **correct** according to the 
            - **private key holder**, since a CSR (request to sign the cert) has to be signed by client.
            - *additional **CA** checks* performed - eg government records. 
            Without such checks the CA is redundant, and cert might as well be self-signed by private key holder.

        - Anything owner **signs** with their **private key** can be verified, using public key embedded in the cert, as being _associated_ with **name** etc in cert info.
        - TLS/SSL, HTTPS protocols themselves all (can) use certificates for **establishing secure connections** (during handshake) - but they are generally not exchanged during subsequent requests 

        - Both password and bearer token based authentication, use **https**, which involve certs (or keys) of at least sever.

*Note*: Unlike with ssh keys, there are _no standard locations_ for storing certs or ssl keys
       


