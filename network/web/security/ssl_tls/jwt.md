### JWT

 - A **standard** for creating tokens with a specific structure and content. 
 - Libraries exist in various programming languages, to create, sign, read, and validate these tokens.

##
 - Analogous to the zip standard for fie (de)compression, and the library functions for creating/reading them

 ##
- #### Structure:
    - **Header**
        - contains metadata about the token, such as the type of token and the hashing algorithm used, as json

    - **Payload**
        - contains the claims, which are statements about an entity (typically, the user) and additional data, as json

    - **Signature**
         - ensures that the token hasn’t been altered after it was signed. It’s created using the header, payload, and a secret key or a public/private key pair.

- #### Semantics:
    - jwt has no notion of the semantics of the token content (payload).
    thats left to the application/framework using the token (~ zip archives)
    - **OAuth** is framework  that (can) uses jwt for its tokens. It defines specific semantics for the content of the JWT payload.

---
- Example

    - **Input**:
        - header
            ```yaml
            {
            "alg": "HS256",
            "typ": "JWT"
            }
            ```

        - payload
            ```yaml
            {
            "any": "stuff",
            "you": "want",
            "here": true 
            }
            ```
        - your_secret
            - "any string you want" used by hashing algorithm to create signature

    #### 
   - **Output** (encoded Jwt):

        - **`base64UrlEncode(header).base64UrlEncode(payload).signature`**
            where 
            -  `signature = HS256_hash (base64UrlEncode(header) + "." +  base64UrlEncode(payload), your_secret)`
##
- **Verification** by recipient
    - the secret may  (depending on the chosen algorithm) be:

        - a symmetric key, in which case the recipient must (and no untrusted parties transmitting the token may) also possess it, or

        - a private key, and the recipient must (and anybody else may) have the ~public key
---

- [jwt.io](https://jwt.io/) allows you to interactively create, and encode jwts