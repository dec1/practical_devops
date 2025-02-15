### k config ...
- **View** 
    ###
    - `k` **`config`** ***`view`***
       see  [kubeconfig](kubeconfig.md) 

    ###
    - `k config` **`get-contexts`**  
        - `*` = current

        ```js
        *         kubernetes-admin@kubernetes   kubernetes   kubernetes-admin   
                    purple                        kubernetes   kubernetes-admin   purple
                    yellow                        kubernetes   kubernetes-admin   yellow
        ```

    -  `k config` **`current-context`**
        ```yaml
        kubernetes-admin@kubernetes
        ```       

- **Use** 
    -  `k` `config` **`use-context`**`purple`  
    
        ```yaml
        CURRENT   NAME                          CLUSTER      AUTHINFO           NAMESPACE
                kubernetes-admin@kubernetes   kubernetes   kubernetes-admin   
        *       purple                        kubernetes   kubernetes-admin   purple
                yellow                        kubernetes   kubernetes-admin   yellow 
        ```

- **Edit** 


    ####
    - ###### Context
        `k` `config` **`set-context`** [`<context_name> | --current`] [**`--cluster`**`=<cluster_name>`] [**`--user`**`=<user_name>`] [**`--namespace`**`=<namespace_name>`]

        ####
        - set any of **user**, **cluster**, **namespace** for specified context (name)

        - _create_ a new context with this name (if it doesn't already exist).

   
    ###
    - ###### User 
       (_`config` **`set-user`** would be a more fitting_)
        `k` `config` **`set-credentials`** `my-user` `[--client-certificate=path/to/certfile]` `[--client-key=path/to/keyfile]`
        

        ###

        - `client-certificate`  see set-cluster client-certificate (above)
        - `client-key`              Path to the **file** containing the client's **private key**. 
            - used to sign requests to the API server for authentication purposes


    ###
    - ###### Cluster
        `k` `config` **`set-cluster`** `my-name` [--server=https://1.2.3.4] [--certificate-authority=~/.kube/e2e/kubernetes.ca.crt]
    adds a new cluster entry (my-name) or updates an existing one

        ###
        - `server`        url of cluster **API server**
        - `certificate-authority`**  local file path to the **public cert of CA** (certificate authority) used to verify cert of API server (~ preinstalled root CA certificates in web browser).
        - `tls-server`     server name that should be on server certificate returned by API server.
            -  in case server has multiple, it should return this one. 
            - client verifies this server certificate as part of TLS handshake with the Kubernetes API server 

        - `client-certificate`   - local file path to **file** containing client's certificate (containing **public key**). 
            - used by api sever to verify client messages  






    
----



