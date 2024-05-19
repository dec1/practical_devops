### RoleBinding / ClusterRoleBinding

Ties: 
- **Subjects** 
    - users, groups, service accounts

to 
- **Role/ClusterRole**    
    - verb + objects

-----
- **RoleBinding**: 
    - **Subjects** in question are limited to **namespace** 
        -  **role** used => role (as well as resources it described) must be **all in same namespace**
        - **clusterrole** used => ... need not
- **ClusterRoleBinding**
    - .. subjects **not** limited to any namespace 
        - ~~**role** used =>  Not possible~~
        - **clusterrole** used - subjects and objects can be in any namespace

###

---
- `k` **`create rolebinding`** `my-rb` 
(**`--role`**`=my-role`) | (**`--clusterrole`**`=my-cluster-role`)   # <-- exactly one
[**`--user`**`=my-user`] | [**`--group`**`=my-gp`] | [**`--serviceaccount`**`=ns:my-sac`]     # <-- at least one

    ##
    - `kubectl create rolebinding my-rb --role=my-role --user=bob --group=bob-gp --serviceaccount=default:my-sa`

        ```yaml
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
            name: my-rb
        roleRef:
            apiGroup: rbac.authorization.k8s.io
            kind: Role      #  Role | ClusterRole
            name: my-role   #  my-role | my-cluster-role
        subjects:
            -   kind: User
                name: my-user

            -   kind: Group
                name: my-gp

            -   kind: ServiceAccount
                name: my-sac
                namespace: default
        ```




 




