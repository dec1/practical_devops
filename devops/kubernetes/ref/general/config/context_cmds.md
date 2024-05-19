
- **View** 
    ###
    - `k` **`config`** ***`view`***

        ```yaml
       apiVersion: v1
       kind: Config

       clusters:                                       # <--* clusters
       - cluster:
            name: kubernetes
                server: https://172.30.1.2:6443             # # <--* Api Server 
                certificate-authority-data: DATA+OMITTED    # (public) server cert - used by client to authenticate server
 

       users:                                          #  <--* users
       - name: kubernetes-admin
           user:                                       # In general each user has their own cert, and private key
             client-certificate-data: DATA+OMITTED     # (public) client cert - used by server to authenticate user
             client-key-data: DATA+OMITTED             # (private) key to sign with, for user (of context)


       contexts:                                       # <--* contexts
       - context:
            name: kubernetes-admin@kubernetes    
                cluster: kubernetes
                user: kubernetes-admin
                namespace: my-namespace           # Optional: namespace name ("default" if unspecified)
            
       current-context: kubernetes-admin@kubernetes


       preferences: {}
        ```

    - `k config`**`get-contexts`**  
        - `*` = current

        ```js
        *         kubernetes-admin@kubernetes   kubernetes   kubernetes-admin   
                    purple                        kubernetes   kubernetes-admin   purple
                    yellow                        kubernetes   kubernetes-admin   yellow
        ```

    -  `k config`**`current-context`**
        ```yaml
        kubernetes-admin@kubernetes
        ```       
    -  `k config`**`use-context`**`purple`  
    
        ```yaml
        CURRENT   NAME                          CLUSTER      AUTHINFO           NAMESPACE
                kubernetes-admin@kubernetes   kubernetes   kubernetes-admin   
        *       purple                        kubernetes   kubernetes-admin   purple
                yellow                        kubernetes   kubernetes-admin   yellow 
        ```

- **Create/Modify** 
    - **modify** an existing instance (if one with the same name already exists) or
    - **create** a new one (if it doesn't already exist).

    ###
    - `k`  **`config`** **`set-context`** `[ <name> | --current]` `[--cluster=cluster_name]` `[--user=<user_name>]` `[--namespace=ns]`
    Specifying a name that already exists will **merge** new fields on top of existing values for those fields.
    
    ###
    - `k` **`config`** **`set-cluster`** `my-name` [--server=https://1.2.3.4] [--certificate-authority=~/.kube/e2e/kubernetes.ca.crt]
    adds a new cluster entry (my-name) or updates an existing one

        ###
        - --**`server`**        url of cluster **API server**
        - --**`certificate-authority`**  local file path to the **public cert of CA** (certificate authority) used to verify cert of API server (~ preinstalled root CA certificates in web browser).
        - --**`tls-server`**     server name that should be on server certificate returned by API server.
            -  in case server has multiple, it should return this one. 
            - client verifies this server certificate as part of TLS handshake with the Kubernetes API server 

        - --**`client-certificate`**   - local file path to **file** containing client's certificate (containing **public key**). 
            - used by api sever to verify client messages  



    ###
    - `k` **`config`** **`set-credentials`** `my-user` `[--client-certificate=path/to/certfile]` `[--client-key=path/to/keyfile]`
    
        - would be more aptly named '**set-user**'
        ###
  
        - --**`client-certificate`**  see set-cluster --client-certificate (above)
        - --**`client-key`**              Path to the **file** containing the client's **private key**. 
            - used to sign requests to the API server for authentication purposes



    
----



