
### PKI
set of roles, policies, hardware, software and procedures needed to create, manage, distribute, use, store and revoke digital certificates and manage public-key encryption.



- ##### SSL (now TLS)
    - authentication and encryption [uses](./tls_ssl.md)
        - **certs** (which include public key along with other information).
        - for each (public) cert is an associated private keys.
        - the additional cert overhead makes TLS more complicated than SSH (which is why applications like git prefer ssh)
        
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















