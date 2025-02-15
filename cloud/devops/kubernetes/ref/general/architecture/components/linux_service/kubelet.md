### Kubelet
Starts/stops all [pods](../../../../resource/pod/pod.md) (ultimately) 

#####
-  Its a  (`linux system`) <i class="fa-brands fa-linux"></i> **`service`**  on every node

    ####
    - glue between Kubernetes and **container runtime** engine, and ensures that containers are running and considered healthy.

    #####
    - <i class="fa-solid fa-network-wired"></i> **communication**: 
        - control plane <-> node

    ###
    - Its the only kubernetes system component that does **not** run in (dedicated) **pod** 
        -  it starts/stops the others.
   

    ####
- ####  Static Pods
    - The kubelet on each **control plane** node    
        - **watches** the  `/etc/kubernetes/manifests/` ([static pods](../pods/static/static_pods.md)) directory and 
        - automatically adapts to changes made there - you can observe the affected containers restart with [crictl](../../../../tool/crictl.md) eg
            - `watch crictl ps`
