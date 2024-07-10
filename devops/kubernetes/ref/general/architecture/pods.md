
### Pods
- Wrapper around (one or more) containers that 
- Share common network namespace (and therefore localhost)
- Has unique IP address 
- Are Collocated - on a single node (containers never spread across multiple nodes)
- Also contain some _glue_ that help integrate them into rest of kubernetes 
    - [pod ephemeral volumes](../../resource/storage/volumes/2_pod-ephemeral.md)
    - metadata (names, labels, annotations, restart policy)
    - [init containers](../../resource//pod/lifecycle.md)



- #### Static
    -  are those which **kubelet** managed independetly (eg of scheduller)
    - Critical system components
        - _Api Server, Controller Manager, Scheduler, Etcd_
            - **kublet** itself watches the manifests 
                - **`/etc/kubernetes/manifests/`** 
                    - each control plane node has a copy





