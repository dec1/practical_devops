# kubectl

[command line tool](https://kubernetes.io/docs/reference/kubectl/cheatsheet) for communicating  with Kubernetes API Server
 
#####
### help (commands)
- `k`**`help`**`[command] [flags] [options]`, or
- `k  [command] [flags] [options]`**`--help`**
    - `k help`
    - `k help service`
    - `k help service clusterip`
    - `k help service clusterip`

    (for help on resource see [describe](./query/describe.md), [explain](./query/explain.md))
#####
----------
### Version

###
- `k version`
 
    ```yaml
    Client Version: v1.30.0
    Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
    Server Version: v1.30.0
    ```

### Api Server
- `k` **`cluster-info`** [ **`dump`** [`--output_dir=`dir_path]
    
    ```javascript
    Kubernetes control plane (Api Server) is running at https://172.30.1.2:6443
    CoreDNS is running at https://172.30.1.2:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
    ```

    - **`dump`**
        write info for debugging and diagnosing cluster problems to stdout 
        -  `--output_dir` 
            write to files in (existing) dir_path

### Nodes
- `k` `get` **`nodes`**
    ```yaml
    NAME           STATUS   ROLES           AGE   VERSION
    controlplane   Ready    control-plane   18d   v1.31.0
    node01         Ready    <none>          18d   v1.31.0
    ```

### Resources
- `k` **`api-resources`** `[--sort-by=name|kind]` `[--namespaced=true|false]`
        **Resources** (aka primitives) that can be instantiated as kubernetes objects, together (inc ~ `Kind` and `apiVersion` you should use in manifest) 

        NAME                              SHORTNAMES   APIVERSION                        NAMESPACED   KIND
        pods                              po           v1                                true         Pod
        deployments                       deploy       apps/v1                           true         Deployment
        configmaps                        cm           v1                                true         ConfigMap
        jobs                                           batch/v1                          true         Job
        cronjobs                          cj           batch/v1                          true         CronJob
        networkpolicies                   netpol       networking.k8s.io/v1              true         NetworkPolicy
        persistentvolumes                 pv           v1                                false        PersistentVolume
        persistentvolumeclaims            pvc          v1                                true         PersistentVolumeClaim
        resourcequotas                    quota        v1                                true         ResourceQuota secrets                                        v1                                true         Secret
        services                          svc          v1                                true         Service
        serviceaccounts                   sa           v1                                true         ServiceAccount
        .....


    - `--namespaced` 
        - if specified, limits results to (non) namespaced. 

            - **Namespaced** 
                - `pods, deployments`...  exist in a  namespace. 
            - **Non-Namespaced**  
                - `persistent volumes`, `nodes` ...   do **not**
    - #### API Groups
        (see also [apiserver](architecture/components/pods/static/system/apiserver.md))
        Groups of resources based on type (not groups of API functions or operations (like GET, POST, PUT, DELETE) as the name might suggest). They are subdivided into versions. 
        The APIVERSION column in output of `k api-resources`  above lists `<GroupName>/<version>` eg `apps/v1`

        -  **core** (No `<GroupName>`): Resources like Pods, Services, Namespaces, Nodes, etc., belong to the core API group, which `doesn't have an explicit name`. They are often referred to as the "core" group.  

        - **apps**: For application workloads like `Deployments`, `ReplicaSets`, `StatefulSets`, `DaemonSets`.
        - **batch**: For batch `jobs` and Cro``nJobs.
        - **autoscaling**: For Horizontal Pod Autoscaler (HPA) resources.
        - **networking.k8s.io**: For networking resources like Ingresses, NetworkPolicies, etc.   
        - **rbac.authorization.k8s.io**: For Role-Based Access Control (RBAC) resources.   
        - **storage.k8s.io**: For storage resources like PersistentVolumes and PersistentVolumeClaims.
        - **apiextensions.k8s.io**: For Custom Resource Definitions (CRDs).



### cp 
- copy local files to/from pod


    -`k` **`cp`** `local_dir_path` **`my-pod:/pod_dir_path`** 
    -`k` **`cp`** **`my-pod:/pod_dir_path`**  `local_dir_path` 









   
   