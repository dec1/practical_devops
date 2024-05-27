
## Authentication

Can be see seen as combination of both:
- a). **`Secure`** the `connection` 
    - so both parties know that they have `constant` partner for whole `encrypted` conversation.
 eg SSH, TSL, HTTPS with pub/priv **keys** (partner is holder of private key being used to sign incoming messages)

- b). `Determine` **`Who`** this constant partner is.  Can be achieved in multiple ways:

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



    - ### 3) Certificate
        - Contain: 
            - *public key* -  for a).  
            - **identifying info** fields -  for b).  
                - **Common Name**  (CN)
                - **Organizations** (O) - optional

        #####    
        - The info in cert is **correct** according to the 
            - **private key holder**, since a CSR (request to sign the cert) has to be signed by holder.
            - *additional **CA** checks* performed - eg government records. 
            Without such checks the CA is redundant, and cert might as well be self-signed by private key holder.

        #####
        - Anything owner **signs** with their **private key** can be verified, using public key embedded in the cert, as being _associated_ with **name** etc in cert info.

        #####
        - TLS/SSL, HTTPS protocols themselves all (can) use certificates for **establishing secure connections** (during handshake) - but they are generally (unlike 1,2) not exchanged during subsequent requests 




_Note_: 
- **Asymmetric**: Its not uncommon for client (eg token) and server (eg cert) to use **different** means to authenticate themselves to the other.
- **Token** can be used not just for authentication but also **authorizaion** - contain **permissions** or roles for holder


