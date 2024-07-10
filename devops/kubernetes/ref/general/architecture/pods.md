
### Pods
- Wrapper around (one or more) containers that 
- Share common network namespace (and therefore localhost)
- Has unique IP address 
- Are Collocated - on a single node (containers never spread across multiple nodes)
- Also contain some _glue_ that help integrate them into rest of kubernetes 
    - [pod ephemeral volumes](../../resource/storage/volumes/2_pod-ephemeral.md)
    - metadata (names, labels, annotations, restart policy)
    - [init containers](../../resource//pod/lifecycle.md)


- #### Non-Static
    - **controller** - **scheduler** - **kubelet** 
    - Non-Critical system components and user workload pods
        - _CoreDNS, Metrics-Server_
            - **controller** (which one depends on type of resource) watches manifests and always delegates to **scheduler** (to choose node) which delegates to **kublet** (on that node) to stop/start the pod there.
            - some (non-critical) system compo

- #### Static
    -  **kubelet** only
    - Critical system components
        - _Api Server, Controller Manager, Scheduler, Etcd_
            - **kublet** itself watches the manifests 
                - **`/etc/kubernetes/manifests/`** 
                    - each control plane node has a copy





