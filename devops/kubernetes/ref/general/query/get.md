
- ### get
    Info on resources in current **namespace** (unless overridden with `-n my-ns` or `-A`)
    ####
    
    - `k` **`get`** `[--show-labels]`
        - `show-labels` - shoe labels (in dedicated column)
    #####
    - `k get ...` **`-o wide`** 
        more detail 
    - `k get ...` **`-o yaml`** (also `-o json`)
        much more detail (~  [edit](../modify/edi
        t.md))
    #####
    - `k get` **`-w`**
        **watch**: dont return but keep output updated (like linux `watch` command)

    ###

    #####
    - `k get` **`pods`** [`-n my-ns` | `-A` ]  

        ####
        - **`-n`**  in **namespace** *my-ns*
            
        #####      
        -  **`-A`** in **all** namespaces
                    

        ##       
    - `k` `get` `deployments`
    #####   
    - `k get services `

    #####
    - `k get` **`nodes`** -o wide
        - 2 nodes (1 control, 1 worker)
            ```yaml
            NAME            ROLES           INTERNAL-IP   EXTERNAL-IP   STATUS   VERSION   AGE  OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
            controlplane    control-plane   172.30.1.2    <none>        Ready    v1.29.0   19d  Ubuntu 20.04.5 LTS   5.4.0-131-generic   containerd://1.7.13
            node01          <none>          172.30.2.2    <none>        Ready    v1.29.0   19d  Ubuntu 20.04.5 LTS   5.4.0-131-generic   containerd://1.7.13
            ```

    ###
    - **common** resources (pods, services, deployments...)
        - get most common resources in namespace
            `k get` **`all`** `-n my-ns`
        ###
        - get most common resources all namespaces
            `k get` `all` `-A`

    #
    - **events** 
        `k get` **`events`** `[ | grep "failed liveness probe"]`

        ```yaml
        LAST SEEN           TYPE      REASON                    OBJECT              MESSAGE
        16d                 Normal    Starting                  Node/controlplane   Starting kubelet.
        16d                 Warning   InvalidDiskCapacity       Node/controlplane   invalid capacity 0 on image filesystem
        16d                 Normal    NodeHasSufficientMemory   Node/controlplane   Node controlplane status is now: NodeHasSufficientMemory
        16d                 Normal    NodeHasNoDiskPressure     Node/controlplane   Node controlplane status is now: NodeHasNoDiskPressure
        16d                 Normal    NodeHasSufficientPID      Node/controlplane   Node controlplane status is now: NodeHasSufficientPID
        16d                 Normal    NodeAllocatableEnforced   Node/controlplane   Updated Node Allocatable limit across pods
        16d                 Normal    RegisteredNode            Node/controlplane   Node controlplane event: Registered Node controlplane in Controller
        16d                 Normal    Starting                  Node/controlplane   
        16d                 Normal    NodeReady                 Node/controlplane   Node controlplane status is now: NodeReady
        ....
        ```
    ###
    - ***endpoints*** 
        `k get` **`endpoints`**
        list all (internal) pod ip addresses and ports
        <none> indicates mismatch between label selectors in service and deployment (manifest)      
        ```python
        NAME         ENDPOINTS         AGE
        kubernetes   172.30.1.2:6443   16d    # api-server
        ```

