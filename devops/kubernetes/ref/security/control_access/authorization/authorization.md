## Authorization
After the **subject** 
- `user` (and possibly group) from cert,  or
- `service account `

is authenticated, rbac (or some other method) can be used to authorize them to perform certain actions (via api).
Access to the API server is restricted by default - no subjects have any permissions, unless **explicitly** given them

### Role Based Access Control (RBAC)

- `k` **`auth can-i`** ` --list` `--as bmuschko`
    ```yaml
    Resources          Non-Resource URLs   Resource Names   Verbs
    ...
    pods               []                  []               [list get watch]
    services           []                  []               [list get watch]
    deployments.apps   []                  []               [list get watch]
    ```
- `k` **`auth can-i`** ` --list` **`pods`** `--as bmuschko`
    ```yaml
    yes
    ```


