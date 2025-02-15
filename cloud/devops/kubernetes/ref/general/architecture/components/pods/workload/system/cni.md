### Container Network Inerface  (CNI) 

These _plugins_ are responsible for the **basic network connectivity** of pods. They:   

- assigns **unique IP** addresses to each _pod_ and 
- they can **route** messages to one another (this often involves setting up _routes between nodes_).

- implements [network policies](../../../../../../network/policy.md) for **pod-to-pod** traffic.   

- challenging as many pods may be coming and going on various nodes often


 ---
Kubernetes network plugins have a **`.conflist`** file in `/etc/cni/net.d/` which in turn references and additional file `calico-kubeconfig`


- cat **`/etc/cni/net.d/`** **`10-canal.conflist`**
    ```yaml
    "cniVersion": "0.3.1",
    "plugins": [
        {
        "type": "calico",
        ........
        "kubernetes": {
            "kubeconfig": "/etc/cni/net.d/calico-kubeconfig"  # <-- more (plugin specific) config here
        ........
    ```


#
#### Implementations
  Calico, Flannel, Cilium, Weave Net


- ##### 1). Flat network
    - plugin allocates/recycles private addresses in address space of existing IP network
    - configures nodes to also route to pods with additional new ip addresses 
    - eg **Cilium**
    - disadvantage: 
        - have to interfere with "underlay" network settings (eg routing)

- ##### 2). [Overlay](../../../../../../../../../../network/pub/overlay_network.md) 
    - _advantage_: 
        - no need to interfere with underlay network settings 

    - ###### L3-on-L2-over-L3
        - routing is trivial
        - **Weave Net**:
        - **Calico**, **Flannel** use this (or optionally flat network)

    - ###### L3-over-L3
        - uncommon 




---
##### Plug into - Container Runtime
- CNI plugins "plug into" the _container runtime_, not into Kubernetes directly. When Kubernetes schedules a pod to run on a node, it delegates the responsibility for networking to the container runtime, which then uses the CNI plugin to configure the network interfaces and networking for the containers in the pod.

####
- (CRI-compliant) Container runtimes (like `containerd` and `CRI-O`) can also use CNI plugins directly for networking, even without Kubernetes.

####
- Docker, on the other hand, is not CNI-compliant, uses its own networking model, and does not natively support CNI plugins directly. Docker's networking is managed through its own drivers and plugins. Its use in Kubernetes was facilitated via "dockershim", and currently, using Docker as a container runtime in Kubernetes is deprecated.
    
    
