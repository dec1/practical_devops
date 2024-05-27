
## Authentication

Prerequisites:
- 1). **`Secure`** `connection` 
    - both parties know that they have `constant` partner for whole `encrypted` conversation.
 eg SSH, TSL, HTTPS with pub/priv **keys** (partner is holder of private key being used to sign incoming messages)

- 2). `Determine` **`Who`** this constant partner is.  Can be determined in multiple ways:

    - ### 1) Username, Password
        - **Basic Authentication** (username and password) 

            - `Authorization` header of `every call` :
            **base64** encoded `username:password` 
                ####
                ```http
                ...
                Authorization: Basic ZGVtbzpwQDU1dzByZA==
                ...
                ```
        - Username, password must previously have been configured (as valid) on server

    - ### 2) Token

        - **Bearer** Token eg. **JWT**, **OAuth**
        
        -  `Authorization` header of `every call` :
            ####    
            ```http
            ...
            Authorization: Bearer <service-account-token>
            ...
            ```

        - Token must previously be created independently of TLS session       
        - Advantages: token may be 
            - **short lived** and **can be revoked** at any time. 
            - restricted in **permissions** or roles it can be used to perform - 
             token can include authorization information (what token holder is allowed to do)


    - ### 3) Certificate
        - Contain: 
            - *identifying info* fields
                - **Common Name**  (CN)
                - **Organizations** (O) - optional
            - **public key**
        #####    
        - The info in cert is **correct** according to the 
            - **private key holder**, since a CSR (request to sign the cert) has to be signed by client.
            - *additional **CA** checks* performed - eg government records. 
            Without such checks the CA is redundant, and cert might as well be self-signed by private key holder.

        #####
        - Anything owner **signs** with their **private key** can be verified, using public key embedded in the cert, as being _associated_ with **name** etc in cert info.

        #####
        - TLS/SSL, HTTPS protocols themselves all (can) use certificates for **establishing secure connections** (during handshake) - but they are generally not exchanged during subsequent requests 

        - Note: 


_Note_: 
- The Certs (or keys thereof) are also used for 1).
- Its not uncommon for client (eg token) and server (eg cert) to use **different** means to authenticate themselves to the other.


