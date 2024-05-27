### ssh

- Many applications (eg **git**, scp, rsync) use ssl (protocol and keys) **internally**
    

- TSL (for historic reasons) does not use ssl protocol or keys (and vice versa)




##### Example:
```yaml
> ssh some-user@server.com 
```
or (if config file entry contains _User_)

```yaml
> ssh server.com 
```
    


- The SSH client automatically selects the public key based on
1). or by trying all available keys in 2b).

- ##### 1). Client Config
    - user specific
        - `~/.ssh/config`
    - system wide
        - `/etc/ssh/ssh_config`

            ####

            ``` javascript
            .....
            Host server.com                   // when connecting with this server
                User some-user                // use this username (optional)
                IdentityFile ~/.ssh/id_rsa    // send this cert
            ```

- ##### 2). Standard key locations

    Stored in single file at:

    ####
    - a). **Public** keys (trusted) :

        - **client**

            - user specific
            `~/.ssh/`**`known_hosts`**
            - system wide
            `/etc/ssh/ssh_known_hosts`

                ```yaml
                ...
                # for server.com use public key "AAA...."
                server.com ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEArTzyHrYKK...
                ```
        

        ###
        - **server**
       `/home/some_user/.ssh/`**`authorized_keys`**

            ```yaml
            # list of keys:
            ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEArTzyHrYKK...
            ```

            - prerequisite:  some-user has account on server
            - The server determines the user account from the **username** provided in the SSH connection request.
            - It checks the authorized_keys file in the **home directory** of the specified user to find a matching public key.

    ####
    - b). **Private** keys 
        
        - **`~/.ssh/id_rsa`** (RSA keys)
        - `~/.ssh/id_dsa` (DSA keys)
        - `~/.ssh/id_ecdsa` (ECDSA keys - recommended)
        - `~/.ssh/id_ed25519` (Ed25519 keys)

---
### ssh-keygen:
see also [SSH Academy](https://www.ssh.com/academy/ssh/keygen) 
- **ssh-keygen** [-f ~/file_path] [**-t ecdsa**] [-b 521]
    - **`-t ecdsa`** key format
    - `b 521` key size
    - `f ~/file_path` where to save file pair locally (default: **~/id_rsa.pub** and **~/id_rsa**)


