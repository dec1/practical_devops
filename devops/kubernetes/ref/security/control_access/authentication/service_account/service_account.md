
### Service Account
-  **Token** - purpose: encode identity of the service account 

    - v.1.24- not only was token mounted into pod 
        -  lifetime was indefinite
        -  persisted in a `secret` (accessible outside pod)
        
    - v.1.24+  [no longer](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#urgent-upgrade-notes) true. Instead:
        - lifetime is limited (kubernetes auto rotates mounted tokens)
        - no storage in secrets
       



#####
- The client/container using the token will have exactly those **permissions** [defined](../../authorization/authorization.md) in the **role** which are **bound** to the `service account` (by default none)



###
    
-  `k` **`get` `serviceaccounts`**
    ```yaml
    NAME      SECRETS   AGE
    default   0         4d
    ```

- `k` **`create` `serviceaccount`** my-sac
    ```yaml
    apiVersion: v1
    kind: ServiceAccount
    metadata:
        name: my-sac
    ```


- `k` **`describe serviceaccount`** `my-sac`
    ```yaml
    Name:                my-sac
    Namespace:           default
    Labels:              <none>
    Annotations:         <none>
    Image pull secrets:  <none>
    Mountable secrets:   my-sac-token-rvjnz
    Tokens:              my-sac-token-rvjnz     # <-- token (<none> in v1.24+)
    Events:              <none>
    ```

- `k` `get secrets`
    ```yaml
    NAME                    TYPE                                  DATA   AGE
    my-sac-token-rvjnz      kubernetes.io/service-account-token   3      20m
    default-token-qgh5n     kubernetes.io/service-account-token   3      93d
    ```
- `k` **`describe secret`** my-sac-token-rvjnz
    get *`contents`* of token, which can be also used for **external clients**

###
- `k` **`create`** **`token`** **`my-sac`** `[--duration 10m]`

    create additional token  manually for existing service account: