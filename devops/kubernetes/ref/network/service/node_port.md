## NodePort 

-  ClusterIP service created (or reused) behind the scenes, which 
can be used directly (just like any ClusterIP service).

#####
- Forwards 
    - `node_ip`  &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  :**`nodePort`** --> 
    - `target_pod_ip`  :**`targetPort`**

####
- **`nodePort`** is of *any* **worker** node in the cluster

#####
- **All** *worker nodes* in the cluster are **identically** configured to **participate** in traffic forwarding,  on the specified nodePort to the associated service. 
####
- **`nodePort`** is *automatically*  allocated, and cluster-wide *unique* 


####
-  **Routing** decisions are based **only** on **port number**
A *single* (worker) *node* can be used by *multiple* NodePort *services*, each with a unique nodePort. The node forwards requests to the ip of ~ service based solely on the port number of the incoming request, URLs (in the request) are not used.





###
---
```mermaid

flowchart TD
    C["Client (ext)" ] 


    subgraph cluster
        Np{{"Service Np"}}
  
        N1[(Node1)]
        N2[(Node2)]

        Cip{{"Service CiP"}}

        Np --o   Cip
        N1 --> Np
        N2 --> Np
    
    end

    C --o   N1
    C --o   N2
```    

---

#### Service
same as  [clusterIP](cluster_ip.md), except:

- `clusterip` -> `nodeport` in *k create*
- **ClusterIP**  -> **NodePort** in *manifest*


#### Pod
- same as  [clusterIP](cluster_ip.md)





---
#### Query

- `k describe service my-ser`
    ```yaml

    # different/new 
    Type:                     NodePort
    NodePort:                 <unset>  31482/TCP        # 31482:            nodePort        <--- *) need this    (automatically allocated)
    ```

#### Connect

- **as before** (access from within cluster) :
     - `k run tst --image=busybox --restart=Never` `--rm` `-it`  `-- /bin/sh` **`-c `** `"wget --spider my-ser:8000"`

        ```yaml
        Connecting to 10.104.86.159:8000 (10.104.86.159:8000)
        remote file exists
        
        pod "tst" deleted  # because of `--rm` 
        ```
##
- **New** - access from **outside** cluster  :
     - `curl` **`172.30.2.2`** **`:31570`**
        - with 
            - **node_ip** &nbsp;&nbsp;(`k` **`describe`** `pod` &nbsp;&nbsp;&nbsp;&nbsp;**`my-pod`**)
            - **nodePort**  (`k describe service` **`my-ser`** )
        ```yaml
        <h1> Welcome to nginx! </h1>
        ...
        ```