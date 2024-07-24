## Authentication
- All clients (including kubectl and pods or applications running therein) need to [authenticate](../../../../../../network/web/security/ssl_tls/access_control.md) themselves to api server before they can further access it. Both regular users and service accounts can use any of 3 (**TLS** based) ways

    #####
    ####
    - 1). **Basic Authentciation** - username, password
        -   discouraged - less secure




    ####
    - 2). **Certificate** with **User Name** (and optionally **Group**) 
        - Kubernetes internally identifies (eg when checking permissions for) the user by
            - `name` = `CN` in cert (mandatory)
            - `groups`=  `O`(optional) in cert 

        ####
        -  preferred for regular user accounts due to: 
            - only method that allows client to validate server - mutual TLS, client can validate server (not just vice-versa) nb when since unlike with service accounts communication transcends cluster boundaries, 
            - integration with existing PKI systems, and 
            - ease of use with kubectl

        ####
        - User and group names in **RoleBindings** match these exactly (user names in kubeconfig are **not** used for permission checking - only by kubectl itself, for context switching - specifically  the determining what cert needs to be used for the user in the context)
            - Kubeconfig user names are used only for its own purposes (map: user firiendly name -> cert)

    
       ####
        -  **Certificate**   -  used by **Kubectl**  when `establishing a secure (authenticated) connection` (for **user account**) during context switching. The cert to be used for the (context) user is specified in kubeconfig
            - Each cert used needs to be initially **signed** by kubernetees sever (or CA it trusts). 




    ####
    - 2). **Token** - typical for **Service Account**
        #####
        -  preferred for service accounts due to:
            - simplicity (client doesnt need to validate server)


        ####
        - When you associate a pod with a service account, Kubernetes automatically mounts the associated token into the pod. The token is used to authenticate the (client) pod with the (api) server
    


---
- Note: In principle (though uncommon)  client-server authentication need not use same method as vice-versa eg:
client could validate server using serveer cert, but authenticate itself with server via token




