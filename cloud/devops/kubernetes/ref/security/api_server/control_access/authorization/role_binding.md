### RoleBinding / ClusterRoleBinding

Ties: 
- **Subjects** 
    - **Users**
    - **Groups**
    - **Service Accounts**
        - these are the only kind that are namespaced 


to 
- **Role/ClusterRole**    
    - verb + objects

-----
- **RoleBinding**: 
    - _Service Account_ **subjects** mentioned in the RoleBinding are limited to a **single namespace** (namely, that of the RoleBinding, which kubectl implicitly sets to default if omitted).

- **ClusterRoleBinding**
    - _Service Account_ **subjects** **Not** limited to any namespace 
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
        namespace: default # if omitted but kubectl will use "default"
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




 




