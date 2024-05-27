
### PKI
set of roles, policies, hardware, software and procedures needed to create, manage, distribute, use, store and revoke digital certificates and manage public-key encryption.



- ##### SSL (now TLS)
    - authentication and encryption [uses](./tls_ssl.md)
        - **Certs** (which include public key along with other information).
        - for each (public) cert is an associated private keys.
        - the additional cert overhead makes TLS more complicated than SSH (which is why applications like git prefer ssh)

        - **Client verification**
            -  optional. Which makes TSL vulnerable to man-in-middle attacks (see below)
            - using certs for clients is uncommon (troublesome in web browser setting).
                - Alternatives:
                 Passed by client in http `Authorization` header of `every call` :

                    - **Bearer Tokens** (eg **JWT**, **OAuth**). 

                        - from **token** created independently of TLS session :
                            #####
                            ```http
                            ...
                            Authorization: Bearer <service-account-token>
                            ...
                            ```

                    - **Basic Authentication** (username and password) 

                        - **base64** encoded `username:password` 
                            #####
                            ```http
                            ...
                            Authorization: Basic ZGVtbzpwQDU1dzByZA==
                            ...
                            ```
            
- PGP
- S/MIME

---

- ##### SSH
    - authentication and encryption [uses](./ssh.md)
        -  **key pairs** (public and private keys) 
    ####
    - [SSH Academy](https://www.ssh.com/academy/) 

---

### man-in-middle:
- can occur when both parties are not verified.
    - SSH: requires mutual verification, and as such is not very susceptible
    - **TSL**: client verification optional, which makes it more **susceptible**















