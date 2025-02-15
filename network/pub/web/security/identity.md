## Identity

There are two main approaches to verifying "who" the recipient of a matching key is:

- [PKI](ssl_tls/pki.md) 
    - **Chain of Trust** with signed **certificates**
    - used primarily by **TLS/SSL** (esp for **https**)

- [TOFU](ssh/ssh.md) 
    - trust-on-first-use (_known_hosts_)
    - used primarily by **ssh**