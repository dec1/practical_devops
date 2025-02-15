## Authorization
After the **subject** 
- `user` (and possibly group) from cert,  or
- `service account `

is authenticated, rbac (or some other method) can be used to authorize them to perform certain actions (via api).
Access to the API server is restricted by default - no subjects have any permissions, unless **explicitly** given them

### Role Based Access Control (RBAC)

- `k` **`auth can-i`** **`--list`** [`--as declan`]
    **what can i do?**
    ```yaml
    Resources          Non-Resource URLs   Resource Names   Verbs
    ...
    pods               []                  []               [list get watch]
    services           []                  []               [list get watch]
    deployments.apps   []                  []               [list get watch]
    ```
- `k` `auth can-i` **`get pods`** [`--as kubernetes-admin`]
    - **can i call `k get pods`**?
    ```yaml 
    yes
    ```

- `k`  `auth can-i` **`-n my-ns`** `create secret` `--as` **`system:serviceaccount`:`my-ns`:`my-sa`**
    - can **service account** my-sa, defined in namespace my-ns, create a secret, in namespace my-ns 
    ```yaml
    no
    ```


---

- #### [(Cluster)Role](role.md) 
    - defines a set of **permissions** and where it is **available**, in the whole cluster or just a single namespace.

- #### [(Cluster)RoleBinding](role_binding.md) 
    - connects a set of permissions with an **account** and defines where it is **applied**, in the whole cluster or just a single namespace.

- ####  RBAC Combinations
    Thus  there are 4 different RBAC combinations and 3 valid ones:

    - 1). **Role + RoleBinding** (available in single Namespace, applied in single Namespace)

    - 2). **ClusterRole + ClusterRoleBinding** (available cluster-wide, applied cluster-wide)

    - 3). **ClusterRole + RoleBinding** (available cluster-wide, applied in single Namespace)

    - 4). **~~Role + ClusterRoleBinding~~** (NOT POSSIBLE: available in single Namespace, applied cluster-wide)