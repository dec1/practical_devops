## Authentication
- All clients (including kubectl and pods or applications running therein) need to [authenticate](../../../../../../network/web/security/authentication.md) themselves to api server before they can further access it. This can be done in one of 2 ways:


    ####
    - **Service Account**, and its associated with a **Token**.
    When you associate a pod with a service account, Kubernetes automatically mounts the associated token into the pod. The token is used to authenticate the pod to the api server. The token is automatically rotated by the api server.After the subject

        user (and possibly group) from cert, or
        service account 
    , passed (in http `Authorization` header) of `every call`. 

    

    ####
    - **User/Group** - and its associated **Certificate**.
        - Kubernetes internally identifies (eg when checking permissions for) the user by
            - `name` = `CN` in cert
            - `groups`=  `O`(optional) in cert 

    -

    -  **Certificate**   -  used by **Kubectl**  when `establishing a secure (authenticated) connection` (for **user account**) during context switching. The cert to used for the (context) user is specified in kubeconfig
        - Each cert used needs to be initially **signed** by kubernetees sever (or CA it trusts). 
    


    ####
    - User and group names in **RoleBindings** match these exactly (user names in kubeconfig are **not** used for permission checking - only by kubectl itself, for context switching - specifically  the determining what cert needs to be used for the user in the context)

    ####
    - Kubeconfig user names are used only for its own purposes (map: user firiendly name -> cert)
        


