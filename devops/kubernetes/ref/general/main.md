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

    (for help on resource see [describe/explain](./query/describe_explain.md))
#####
----------
### Version

###
- `k version [--short]`
 
    ```yaml
    Client Version: v1.20.0
    Server Version: v1.20.0
    ```

### Api Server
- `k` **`cluster-info`**
    
    ```javascript
    Kubernetes control plane (Api Server) is running at https://172.30.1.2:6443
    CoreDNS is running at https://172.30.1.2:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

### Resources
- `k api-resources [--sort-by=name|kind]`
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

    - **Namespaced** 
        - `pods, deployments`...  exist in a  namespace. 
    - **Non-Namespaced**  
        - `persistent volumes` ...   do **not**

### cp 
- copy local files to/from pod


    -`k` **`cp`** `local_dir_path` **`my-pod:/pod_dir_path`** 
    -`k` **`cp`** **`my-pod:/pod_dir_path`**  `local_dir_path` 









   
   