## Cryptography Keys

Play a crucial role in ensuring that both parties in a conversation (or a recipient of data/token encoded by someone else) are confident that they are communicating with the holder of a matching key.

##
- ### Symmetric
    - the same key is used for both encryption and decryption
    - typical algorithms:
        - AES 
        - Blowfish
        - Twofish

- ### Asymmetric
    - involves a pair of keys (public and private)
    - each key can encrypt anything, but can only decrypt what the other key has encrypted
    - **hash**: to verify integrity (i.e., payload not tampered with after encryption), a hash of the contents is often included. The recipient can verify this hash matches the one it can independently calculate from the decrypted content.
    - typical algorithms:
        - RSA
        - ECDSA

##
- ##### Handshake
    - During the handshake phase of establishing a secure connection (such as with SSH or TLS), asymmetric keys are used primarily to agree upon symmetric keys for the rest of the conversation for performance reasons, as symmetric encryption is faster.

- ##### [Identity](identity.md)
    - Knowing who the holder of a key is requires more than just the key itself
    -  this is where certificates in PKI or TOFU in SSH come in.
