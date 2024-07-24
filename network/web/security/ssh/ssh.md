### SSH

- Many applications (e.g., **git**, **scp**, **rsync**) use SSH (protocol) **internally**.

##### Example:
```yaml
> ssh some-user@server.com 
```
or simply (if config file entry contains _User_ - see below)

```yaml
> ssh server.com 
```

- The SSH client selects the private key to use based on the config in 1), or if no entry is found, it tries all keys in standard locations.

- ##### 1). Private keys
    The private key to use when communicating with a host can be configured in a file:
    - User specific:
        - `~/.ssh/config`
    - System wide:
        - `/etc/ssh/ssh_config`

    #### Example Configuration:
    ```javascript
    .....
    Host server.com                   // when connecting with this server
        User some-user                // use this username (optional)
        IdentityFile ~/.ssh/id_rsa    // use this private key
    ```

    ####
    - If no entry is found for the host being connected to, SSH tries all keys in standard locations:

        - `~/.ssh/id_rsa` (RSA keys)
        - `~/.ssh/id_dsa` (DSA keys)
        - `~/.ssh/id_ecdsa` (ECDSA keys - recommended)
        - `~/.ssh/id_ed25519` (Ed25519 keys)

- ##### 2). Public keys

    Stored in single files, with locations depending on the purpose. 
    - `TOFU` (trust on first use esp `known_hosts`)

    #####
    - a) **Incoming** connections from **users** of node:
      `/home/some_user/.ssh/authorized_keys`

        ```yaml
        # list of keys:
        ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEArTzyHrYKK...
        ```

        - Prerequisite: some-user has an account on this node.

        - The server determines the user account from the **username** provided in the incoming SSH connection request.

        - It checks the authorized_keys file in the **home directory** of the specified user to find a matching public key.

    #####
    - b) **Outgoing** connections to **remote hosts**:
        
        - User specific:
          `~/.ssh/known_hosts`
        - System wide:
          `/etc/ssh/ssh_known_hosts`

            ```yaml
            ...
            # for server.com use public key "AAA...."
            server.com ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEArTzyHrYKK...
            ```

---
### ssh key generation

- **`ssh-keygen`** [-f ~/file_path] [**-t ecdsa**] [-b 521]
    - **`-t ecdsa`** specifies the key format
    - **`-b 521`** specifies the key size
    - **`-f ~/file_path`** specifies where to save the key pair locally (default: **~/id_rsa.pub** and **~/id_rsa**)

###
- See also [SSH Academy](https://www.ssh.com/academy/ssh/keygen) 
