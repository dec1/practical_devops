### Context 

- ***Kubectl** specific* concept 
    - **Api Server** - knows nothing about contexts

###
- Context is a combination of

    ######
    - Needed to establish secure connection with correct cluster:
        - **cluster**
            - ip address of api server, and cert of cluster ca (`ca.cert`), used to verify cert `apiserver.crt` presented by api server - [see pki](../../security/api_server/pki.md)
        - **user**
            - client cert, and private key

    #####
    - Needed by the cluster
        - **[namespace](./namespace.md)** (name)
            - required with every call to (api) server

###
- Unlike clusters and users, **namespaces** are Kubernetes **_resources_** managed within the cluster itself, and hence **not** entries in the **kubeconfig**. But once created (as resources) in the cluster  the *namespace **names*** can be used (together with cluster/user name) in defining contexts in kubeconfig, and passed eg to `k conifg set-context`



---


Contexts are a way (with kubectl) to quickly switch between different **cluster-user-namespace** combinations. 
- This is especially useful when managing multiple clusters or when different roles or permissions are required for different parts of the same cluster.

####

- **namespace** 
    - Kubernetes (Api) server requires an **explcit namespace** specified in every request for a namespaced resource (and will return error otherwise). For convenience kubectl appendsthe namespace of _current-context_  if you don't explicitly specify another in a given call. Any context (current or otherwise) that doesnt have an namesapce set, has the implicit value `default` 
- **user**
    - Kubernetes [Api Server](../../security/api_server/api_server.md) requires the client (user) to authenticate and authorized themselves. It uses the user certs presented by kubectl at _connection establishment_ for this. Thereafter it remembers the roles assigned to the current connection. 
    If you switch contexts in kubectl, it must establish a new connection with the cert for the new user.
    



Before they can be used in contexts
- **Cluster** and **User** (credentials) must first be created locally (in **kubeconfig**) - see [kubeconfig](kubeconfig.md) and 
(_Namespaces_ as resources in the cluster, need not - kubeconfig just referrs to them by name)



Theres _always_ a **_current context_** in kubectl. 

- If you explicitly/individually specify **namespace** with a kubectl command, this value is used (overriding any namespace  in the current context). If you do not the value from the *current context* (which has the implicitly `default` is nothing else is explicitly defined in the context) is used.









-------------------------------
