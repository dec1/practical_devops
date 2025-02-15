### SSH

- Many applications (e.g., **git**, **scp**, **rsync**) use SSH **internally**. 

    Typically this involves use of library functions that are part of os ssh implementation (eg libssh2):

    ```c
    ssh_connect()
    ssh_auth_pubkey_file()
    ssh_channel_open_session()
    ssh_send() / ssh_recv() (for data transfer)
    ssh_disconnect()
    ```
Unlike SSL (which also plays a role in authorization eg by allowing roles to be embeded in tokens), SSH is concerned with **authentication only**

##### Example:

- **`ssh` `[<some-user>@]` `<server>`** [`<remote_commnd>`] [`&> local_file`]
    - `ssh some-user@server.com `

        or simply (if config file entry contains _User_ - see below)

    - `ssh server.com`

    ###
    - `ssh server.com` **`'ls /home/declan'`** **`&> local_file`**
        executes command `ls` on `server.com` and saves output (redirects both stdout and stderr) to `local_file` (on the ssh _client_)

It is possible(depending on server configuration) to authenticate via 
- **username/password**, or 
- **multi-factor** authentication.
- **ssh keys** (most common). 

#### SSH Keys
SSH client selects the private key to use based on the config in 1), or if no entry is found, it tries all keys in standard locations.
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

    Stored in single files, with locations depending on the whether node is client or sever. 


    #####
    - a) **Incoming** connections from **users** of (ssh **server**) node:
      `/home/some_user/.ssh/`**`authorized_keys`**

        ```yaml
        # list of keys:
        ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEArTzyHrYKK...
        ```

        - Prerequisite: some-user has an account on this node.

        - The server determines the user account from the **username** provided in the incoming SSH connection request _(which includes a copy of the public key_ the client intends to use)

        - It checks the authorized_keys file in the **home directory** of the specified user to find a matching public key.

        ####
        - note: *git* (server) uses single user account with username "git" for all client users.  The git user’s ~/.ssh/authorized_keys file contains an entry for each individual Git user, each mapped to their unique public SSH key - for performance purposes server  looks in database (using a fingerprint of key send by client in connection request) - rather than iterating through all entries in _authorized_keys_ file
    #####
    - b) **Outgoing** connections (from ssh **client**) to **remote hosts**:
        
        - User specific:
          `~/.ssh/`**`known_hosts`**
        - System wide:
          `/etc/ssh/ssh_known_hosts`

            ```yaml
            ...
            # for server.com use public key "AAA...."
            server.com ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEArTzyHrYKK...
            ```
        - is `TOFU` (trust on first use) - ensures the server’s identity is trusted based on previous connections

---
### ssh key generation

- **`ssh-keygen`** [-f ~/file_path] [**-t ecdsa**] [-b 521]
    - **`-t ecdsa`** specifies the key format
    - **`-b 521`** specifies the key size
    - **`-f ~/file_path`** specifies where to save the key pair locally (default: **~/id_rsa.pub** and **~/id_rsa**)

###
- See also [SSH Academy](https://www.ssh.com/academy/ssh/keygen) 
