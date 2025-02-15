### Role/ClusterRole
Specify **what** (verb) can be done to **which** resources

###
- **Role**: 
    - **Objects** (resources) in question are limited to **(single) namespace** (namely that of the role, which kubectl implicitly sets to "default" if omitted). Role and as well as resources it describes, must be all in same namespace. 
#####
- **ClusterRole**:
    - .. **not** limited ...namespace 
    - => **easier maintainence** 
         - eg need one clusterrole instead of role per namespace required
---


 - `k` `create` **`role`** `<my-role>` **`--verb=`**`<list,get,watch>` **`--resource=`**`<pods,deployments,services>` `[-n my-ns]` 

    #####
    - `verb` - [possible values](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#request-verb-resource) (mapped from Http verb used in the request) are:
        - `create`, `get`, `list`, `watch`, `update`, `patch`, `delete`, `deletecollection`
    
    ####
    - **role.yaml**
         ```yaml

         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
            name: my-role
            namespace: my-ns
         rules:

            - apiGroups:  [""]    # Pod, Service have "apiVersion: v1" -  "" = core Api group
              resources:  ["pods", "services"]
              verbs:      ["get", "watch", "list", "create"]  # create added manually

            
            - apiGroups:  ["apps"] # Deployment has "apiVersion: apps/v1" -  "apps" Api group
              resources:  ["deployments"]
              verbs:      ["get", "watch", "list"]
         ```

    - `k` **`apply`** `-f role.yaml` **`-n=my-namespace`**

        - Roles (like most resources) exist in a namespace
        - Binding them (see below) to a subject (user or service account) gives the subject permissions for **resources** in **that namespace only**.

    #####
    - `k`  **`get`** **`roles`** `[-A]`
        ```yaml
        NAME        CREATED AT
        my-role   2021-06-23T19:46:48Z
        ```

    - `kubectl` **`describe`** **`role`** `my-role`
        ```yaml
        Name:         my-role
        Labels:       <none>
        Annotations:  <none>
        PolicyRule:
        Resources         Non-Resource URLs  Resource Names  Verbs
        ---------         -----------------  --------------  -----
        pods              []                 []              [get watch list create]
        services          []                 []              [get watch list create]
        deployments.apps  []                 []              [get watch list]
        ```




### Clusterrole
Almost identical to Role except is *non-namespaced*. ie clusterrole object exists outside namespaces.
 -  When bound by `ClusterRoleBinding` (also always non-namespaced) subject is granted permissions on resources in **all namespaces**, *and* on **non-namespaced** resources (persistent volumes, non-resource endpoints etc).
 - When bound by `RoleBinding` (which always exists in a namespace) subject is granted permissions on (namespaced) resources in that **specific namespace**, and ***no* non-namespaced** resources

Kubernetes has many predefined  clusterroles eg

- `cluster-admin`- all permission to everything
- `admin` - all permissions on namespaced resources
- `edit` - Read/write permission to namespaced resources except Roles and RoleBindings
- `view` - Read only ...

------------

