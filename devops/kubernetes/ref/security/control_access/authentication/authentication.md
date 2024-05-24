## Authentication
- All clients (including kubectl and pods or applications running therein) need to [authenticate](../../../../../../network/web/security/authentication.md) themselves to api server before they can further access it. This can be done in one of 2 (**TLS**) ways (the only difference between them being how server knows identity of client - client **cert**, or bearer **token**)




    ####
    - 1). **User/Group** - and its associated **Certificate**.
        - Kubernetes internally identifies (eg when checking permissions for) the user by
            - `name` = `CN` in cert
            - `groups`=  `O`(optional) in cert 

        ####
        - User and group names in **RoleBindings** match these exactly (user names in kubeconfig are **not** used for permission checking - only by kubectl itself, for context switching - specifically  the determining what cert needs to be used for the user in the context)
            - Kubeconfig user names are used only for its own purposes (map: user firiendly name -> cert)

    
       ####
        -  **Certificate**   -  used by **Kubectl**  when `establishing a secure (authenticated) connection` (for **user account**) during context switching. The cert to be used for the (context) user is specified in kubeconfig
            - Each cert used needs to be initially **signed** by kubernetees sever (or CA it trusts). 


    ####
    - 2). **Service Account**, and its associated **Token**.
    When you associate a pod with a service account, Kubernetes automatically mounts the associated token into the pod. The token is used to authenticate the (client) pod with the (api) server, :
    




---
- In both (1 & 2):
    - both parties know that they are communicating using **encyrpted** messages with **constant** (same) **partner** for duration of session.
    - the client knows the identity of the sever from its ocal copy of server's cert (managed by kubectl in case 1 and  kube-proxy on each worker node in case 2)

    ###
    The difference between 1 and 2 lies only in how server knows identity of (constant) client

    - 1). 
        - symmetric - server also gets copy of client cert (kubectl passes it)

    - 2). 
         - from token created independently of TLS session. passed by client (pod) in http `Authorization` header of `every call` :
            #####
            ```http
            ...
            Authorization: Bearer <service-account-token>
            ...
            ```




