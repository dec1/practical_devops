### Context 

- ***Kubectl** specific* concept 
- **Api Server** - knows nothing about contexts

###
- Context is a combination of
    - **user**
        - cert send send (api) server
    - **cluster**
        - ip address of (api) server
    - **namespace** (name)
        - required with every call to (api) server

###
- Unlike clusters and users, **namespaces** are Kubernetes **_resources_** managed within the cluster itself, and hence **not** entries in the **kubeconfig**. But once created (as resources) in the cluster  the *namespace **names*** can be used (together with cluster/user name) in defining contexts in kubeconfig, and passed eg to `k set-context`




Contexts are a way (with kubectl) to quickly switch between different **cluster-user-namespace** combinations. 
- This is especially useful when managing multiple clusters or when different roles or permissions are required for different parts of the same cluster.

####

- **namespace** 
    - Kubernetes (Api) server requires an **explcit namespace** speified in every request for a namespaced resource (and will return error otherwise). For convenience kubectl appends what it considers the "current" (context's) namespace if you dont explicitly specify another in a given call.
- **user**
    - Kubernetes (Api) server itself never uses the user specified in the context - **only** that specified in **cert** (for authentication and authorization) presented at establishment of secure connection. Only kubectl itself uses the user name in Kubeconfig, during context switching, in order to determine which cert to present to the api server when reestablishing a secure connection.



Before they can be used in contexts
- **Cluster** and **User** (credentials) must first be created locally (in **kubeconfig**) - see [config](config.md) and 
- **Namespaces** as resources in the **cluster**  



Theres _always_ a **_current context_** in kubectl. 

If you explicitly/individually specify namespace with a kubectl command this value is used. Otherwise the value from the *current context* is used.
**default** is the namespace name used when you create a new context (set-context) without explicitly specifying a different name. Since no context has to have a namespace called "default", this also means - (contrary to popular belief) -  that its not true that kubernetes uses "default" as namespace if you dont specify one explicitly in a kubectl command.








-------------------------------
