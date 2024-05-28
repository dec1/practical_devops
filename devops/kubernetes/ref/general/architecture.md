
# Kubernetes Architecture

Manages containerized applications at scale

## Cluster 
A single independent Kuberntes "installation"

- **Control** plane (1 - ~3 nodes)
     #####
    - **Api Server**        
        - exposes the Kubernetes (Rest) API
        -  IP address configured in `controlPlaneEndpoint` of file `kubeadm-init.yaml`
        - only via Api Server can communication take place between: 
            - **outside** <-> **inside** cluster (except app specific - see **kube-proxy**)
            - control <-> worker planes (**kubelet**)

    #####
    - **Controller Manager**
        - watches the state of cluster  and decides
        - **what** pods need to be created (so actual state matches desired state, eg num of replicas) 
        - delegates to Scheduler to create them

    #####
    - **Scheduler**
        - **where** (which node) to put new pods that controller manager requires.
                
    #####
    - **Etcd**
        - key-value data **persistance**.
        - used by kubernetes itself (which doesnt write to files) for persistance (cluster state, pod definitions, service configurations, secrets, etc.) 
        - not directly accessible by kubectl (admins)  or containerized applications for storing their data. 
        - `etcdctl` can be used by admins to read/write directly (bypassing api server - not recommended) for troubleshooting or diaster recovery
         
    #####

- **Worker** nodes (1 - many)

     - {**Node**} 
        - **Kubelet**  
            - communication: (control plane <-> node)
            - manages the Pods and the containers running on a machine
            - watches the API Server for new work assignments and maintains a reporting channel back
            - glue between Kubernetes and container runtime engine, and ensures that containers are running and considered healthy.

        #####
        - **Container (runtime)** 

        #####
        - **Kube-Proxy**
            - **Service** concept **implementation**
                - requests to web apps running in cluster are forwarded to pods via service
            #####
            - services exist only as a **logical** concept inside the cluster. There is no physical process that runs inside the cluster for each service that does the proxying. Under the hood, kube-proxy is responsible for managing the virtual IP addresses on the nodes and modifying all forwarding rules.
            #####
            - Even for a ClusterIP service in Kubernetes, kube-proxy on **each node** sets up the necessary network rules to handle traffic to that service, regardless of whether the node currently hosts any of the pods targeted by the service.
            #####
            - Load Balancing and Network Routing for the services 


    #####

    - { **Deployment** }
        - { **Replica Set** }  - groups of identical pods (may be spread across multiple nodes)
            - {**Pod**}
                - {**Container**}
            



_Note_: Typically all control nodes are identical, and all worker nodes are identical



#### Namespaces

- Allow sharing of single cluster by [dividing](../general/config/namespace.md) it into multiple (logically separated) virtual clusters.

#### Cluster Federation
- Note: While there are ways to join multiple clusters, this functionality is not part of Kubernetes itself, but added on top (eg Openshift Federation)



