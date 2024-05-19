


[SSH Academy - cryptography explained](https://www.ssh.com/academy/)



### pki
set of roles, policies, hardware, software and procedures needed to create, manage, distribute, use, store and revoke digital certificates and manage public-key encryption.

### man-in-middle:
attacks prevented by (also) authenticating server


### ssl (now tls)
secure communications over a computer network

### ssh
secure commands (tunnel) over a computer network    
- ssh could but doesnt (for historic reasons) use ssl internally 
(but its implementation uses same principles)
    - port 22 : server port (default)
- scp does use ssh



- ##### Standard key locations

    - Trusted public ssh keys often saved locally (in single file on):

        - ssh **client**

            - user specific
            `~/.ssh/known_hosts`
            - system wide
            `/etc/ssh/ssh_known_hosts`
        

        ###
        - ssh **server**
        `/home/some_user/.ssh/authorized_keys`
        (where some-user has account on server)










