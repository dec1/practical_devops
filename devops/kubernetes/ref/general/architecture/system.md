
# Kubernetes Architecture

- ### Components

    - #### System
        - Those that are needed (internally) by kubernetes itself 
            - ##### Api Server, Controller Manager, Scheduler, Etcd   
                - run on control nodes only
            - ##### _Kubelet_ (linux service), Kube-proxy 
                -   run on all nodes
            - ##### Container Runtime, Networking Plugins, CoreDNS, metrics-server 
                - necessary but not strictly part of kubernetes
                    - CoreDNS, Metrics-Server: non-static pods just like user applications
                    - Container Runtime, Networking Plugins: generally linux services
    - #### Workload (Resource)
        - Those that run client applications
            - deployments, etc
--- 

- #### Pods
    - All components except **kubelet** (linux service), run in a **dedicated pod** on node its deployed on 

    #####
    - Kubelet on the node in manages (starts/stops) the pods

    #####
    - For workload pods, the **scheduler** decides **what node** to run pod on (and delegates starting/stopping kublet on that pod). 
    - The scheduler is not involved in system aka **static pods** - one always runs on each (control) node

    #####
    - The manifest for system pods is at
        -  **`/etc/kubernetes/manifests/`** 
            - each control plane node has a copy
    
----

- ### Nodes
    - #### Control (Plane)
        - each node runs 1 of every system component
        - may also run workload components (not recommended)

    - #### Worker
        - run workload components and
        - 2 system components:
            - kube-proxy
            - kubelet (linux service)




