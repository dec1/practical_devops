### Api Server
 
Its **REST API** is the primary avenue of interaction with the cluster from outside. Even KubeCtl communictaes (behind the scenes) with the cluster (only) via https with the Api Server



- `/etc/kubernetes/manifests/kube-apiserver.yaml`

    #####
    - configuration for the Kubernetes API server
        - eg 
            - defines IP Range ([CIDR](../../../../../../../../../../network/pub/virtual_network.md)) from new ClusterIp services get their IP Address

            ```yaml
            - --service-cluster-ip-range=10.96.0.0/12 
            ```

            - enabled/disabled [Admission Controller Plugins](../../../../../../security/api_server/api_server.md)
                - these intercept requests to the Kubernetes API server before the persistence of the object, but after the request is authenticated and authorized   

            ```yaml
            - --enable-admission-plugins=NodeRestriction,LimitRanger,Priority,MutatingAdmissionWebhook
            - --disable-admission-plugins=NamespaceLifecycle
            ```
---
##### REST Paths
When using the API Server's you use must paths like:


-  1). for resources in core group eg 
    **`/api/<version>`** **`/namespaces/<namespace>`** **`/<resource-type>/<resource-name>`**

    
    - eg `curl -L` `http://localhost:9999` **`/api/v1`** `/namespaces/default/` **`pods/my-pod`**


#####    
- 2). or for resouces in other groups
    **`/apis/<group>/<version>`** `/namespaces/<namespace>` `/<resource-type>/<resource-name>`

    - eg `curl -L` `http://localhost:9999` **`/apis/apps/v1`** `/namespaces/default/` **`deployments/my-dep`**
/deployments

(see also [main](../../../../../main.md) and [proxy](../../../../../../network/from_local/proxy.md) )

----
#### Groups
Resources are organized in groups as reflected  in the `APIVERSION` column of the output of 
- `k` **`api-resources`** `[--sort-by=name|kind]` `[--namespaced=true|false]`


    ```yaml
    NAME                              SHORTNAMES   APIVERSION                        NAMESPACED   KIND
    pods                              po           v1                                true         Pod
    deployments                       deploy       apps/v1                           true         Deployment
    .......
    ```

and 
- `k` **`api-versions`**
    ```yaml
    v1                                  # core
    apps/v1
    ....
    ```


---

- `k` **`cluster-info`** (follows same pattern)
    ```yaml
    CoreDNS is running at https://172.30.1.2:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
    ```

