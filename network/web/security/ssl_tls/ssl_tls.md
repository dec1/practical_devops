- ##### TLS 
    - Replaces **SSL**.

    ####
    - Authentication and encryption use public/private key pairs alone or 
        - **Certificates** (X.509) - which include key pairs along with other information.
            - Relies on a **chain of trust** established by Certificate Authorities (CAs).

    #####
    - **HTTPS** and all token-based [access control](access_control.md) use TLS/SSL.
        - Many other applications (e.g., git, scp, rsync) use **SSH** (not TLS/SSL).
        - **TLS** (for historic reasons) does not use SSL protocol or keys (and vice versa).

- ##### Standard Key Locations

    - Public (certs):
      - `/etc/ssl/certs/`
    
    - Private (keys):
      - `/etc/ssl/private/`

---

### TLS key and cert generation 

- 1). Generate the Private Key:

    - **`openssl`** **`genpkey`** `-algorithm EC` `-pkeyopt ec_paramgen_curve:P-521` `-out` **`tls_private_key.pem`**

        #####
        - `algorithm EC`:
            -  the algorithm (ECC in this case).
        - `pkeyopt ec_paramgen_curve:P-521`: 
            -  the curve (P-521, analogous to -b 521 in ssh-keygen for ECDSA).
        - `out tls_private_key.pem`: 
            - the output filename for the private key.

###
- 2). Generate the (self-signed) cert with embedded public key

    - **`openssl`** `req` **`-new`** `-x509` `-key` **`tls_private_key.pem`** `-out` **`tls_certificate.pem`** `-days 365`

        #####

        - `x509`    
            - Specifies that this is a self-signed certificate.
        - `tls_private_key.pem`
            -  private key file to use.
        -  `tls_certificate.pem`
            - output filename for the certificate.
        - `days 365`
            - Sets the validity of the certificate to 365 days.
        - `new` 
            - Indicates that a certificate request is also being generated (not passed _info file_ - see below - so will prompt for this interactively)

            #####
            - alternatively you can create  _info file_  in separate step, eg
                - `openssl req -new -key tls_private_key.pem` **`-out`** **`csr.pem`** `-subj "/C=US/ST=California/L=San Francisco/O=Your Organization/OU=Your Department/CN=www.example.com"`

                ####
                - and pass this to cert generation
                    - `openssl req -x509 -key tls_private_key.pem` **`-in`** **`csr.pem`** `-out tls_certificate.pem -days 365`


###
- 3). Optionally Generate a separate public key
    - `openssl pkey -in tls_private_key.pem -pubout -out tls_public_key.pem`

        - optional, since TLS typically uses certificates which include the public key