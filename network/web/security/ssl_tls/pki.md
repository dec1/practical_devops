## PKI

One of the distinguishing characteristics of TLS is its ability to use signed certificates (in accordance with PKI principles).


PKI (Public Key Infrastructure) is a set of roles, policies, hardware, software, and procedures needed to create, manage, distribute, use, store, and revoke digital **certificates** and manage public and private keys for public-key encryption. Commonly associated with TLS/SSL.

- **Client Verification**
    - Optional in TLS; not using it makes TLS vulnerable to man-in-the-middle attacks.
    - Using certificates for clients is less common, especially in web browsers due to management challenges.
        - Alternatives:
            - Pass client credentials in the HTTP `Authorization` header for each request:

                - **Bearer Tokens** (e.g., **JWT**, **OAuth**):
                    - Composed of **header**, **payload**, **signature**.
                    - Created and signed with a key independently of the TLS session.
                        ```
                        ...
                        Authorization: Bearer <service-account-token>
                        ...
                        ```

                - **Basic Authentication** (username and password):
                    - **Base64** encoded `username:password`.
                        ```
                        ...
                        Authorization: Basic ZGVtbzpwQDU1dzByZA==
                        ...
                        ```
    - Always use TLS to secure the transmission of these credentials.

###
- Other Protocols that use PKI:
    - **PGP (Pretty Good Privacy)**: Used primarily for securing emails through encryption and digital signatures. Each user has a public/private key pair, and users can exchange encrypted messages that only the intended recipient can decrypt.
    - **S/MIME (Secure/Multipurpose Internet Mail Extensions)**: Also used for email security, enabling encryption and digital signatures. Unlike PGP, which can be more peer-to-peer, S/MIME often relies on certificates issued by a trusted authority, integrating seamlessly with corporate email systems.

---

### Man-in-the-middle Attacks:
- Occur when both parties are not verified.
    - SSH: Requires mutual verification and is less susceptible.
    - **TLS**: Client verification is optional, which increases susceptibility to attacks.