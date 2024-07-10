## Components

###
- **Kubelet**  

    #####
    -   <i class="fa-brands fa-linux"></i> **`service`** (`linux system`) on every node

        ####
        - glue between Kubernetes and **container runtime** engine, and ensures that containers are running and considered healthy.

        #####
        - <i class="fa-solid fa-network-wired"></i> **communication**: control plane <-> node

        ###
        - The only system component that doesnt run in (dedicated) pod - instead it manages (starts/stops) pods on node.
       Whether independently or externally triggered depending on if pod is part of workload:

            - ##### Workloads

                - _Flow_: **Controller Manager** -> **Scheduler** -> **Kublet**
                (controller manager, delegates to scheduler,  which picks node(s) and delegates to kublet on node in question)

            - ##### Non-Workloads
                - _Flow_:  **Kublet** independently
  
        ###



 
    - 


    
###
- **Kube-Proxy**

    #####
    - <i class='fa fa-ghost' style='color:darkred'></i>**`dameon set`** - dedicated pod on every node 

        #####
        - <i class="fa-solid fa-bell-concierge" style='color:green'></i>  **Service** (web) concept **implementation**

            #####
            - requests to web apps running in cluster are forwarded to pods via service

            #####
            - services exist only as a **logical** concept inside the cluster. There is no physical process that runs inside the cluster for each service that does the proxying. Under the hood, kube-proxy is responsible for managing the virtual IP addresses on the nodes and modifying all forwarding rules.

            #####
            - Even for a ClusterIP service in Kubernetes, kube-proxy on **each node** sets up the necessary network rules to handle traffic to that service, regardless of whether the node currently hosts any of the pods targeted by the service.

            #####
            - Load Balancing and Network Routing for the services 



###
- **Api Server**        
    - exposes the Kubernetes (Rest) API
    -  IP address configured in `controlPlaneEndpoint` of file `kubeadm-init.yaml`
    - only via Api Server can communication take place between: 
        - **outside** <-> **inside** cluster (except app specific - see **kube-proxy**)
        - control <-> worker planes (**kubelet**)

####
- **Controller Manager**
    - watches the state of cluster  and decides
    - **what** needs to be created (so actual state matches desired state, eg num of replicas) 
    - has sub controllers (deployment controller ....) it delegates to  

###
- **Scheduler**
    - **where** (which node) to put new pods that controller manager requires.
        - delegates to kubelet on noe in question.
            
###
- **Etcd**
    - key-value data **persistance**.
    - used by kubernetes itself (which doesnt write to files) for persistance (cluster state, pod definitions, service configurations, secrets, etc.) 
    - not directly accessible by kubectl (admins)  or containerized applications for storing their data. 
    - `etcdctl` can be used by admins to read/write directly (bypassing api server - not recommended) for troubleshooting or diaster recovery
    - regular backup important
    
  


###
- **Workload** (Resource) Components
    - { **Deployment** }
        - { **Replica Set** }  - groups of identical pods (may be spread across multiple nodes)
            - {**Pod**}
                - {**Container**}
        





