
# Kubernetes Architecture

Manages containerized applications at scale

## Cluster 

~ logical App + Infrastructure
         
- **Control** plane (1 - ~3 nodes)
 
    - **Api Server**        
        - exposes the Kubernetes (Rest) API 
        -  IP address configured in `controlPlaneEndpoint` of file `kubeadm-init.yaml`
        - the only way to interact with kubernetes control plane from outside cluster

    - **Controller Manager**
        - watches the state of cluster  and decides
        - **what** pods need to be created (so actual state matches desired state, eg num of replicas) 
        - delegates to Scheduler to create them

    - **Scheduler**
        - **where** (which node) to put new pods that controller manager requires.
                

    - **Etcd**
        - key-value storage, for persistence of all cluster related data
    #####

- **Worker** nodes (1 - n nodes)

     - {**Node**} 
        - **Kubelet**  
            - communication: (control plane <-> node)
            - manages the Pods and the containers running on a machine
            - watches the API Server for new work assignments and maintains a reporting channel back
            - glue between Kubernetes and container runtime engine, and ensures that containers are running and considered healthy.

        - **Container (runtime)** 

        - **Kube-Proxy**
            - **Service** concept **implementation**

            - services exist only as a **logical** concept inside the cluster. There is no physical process that runs inside the cluster for each service that does the proxying. Under the hood, kube-proxy is responsible for managing the virtual IP addresses on the nodes and modifying all forwarding rules.

            - Even for a ClusterIP service in Kubernetes, kube-proxy on **each node** sets up the necessary network rules to handle traffic to that service, regardless of whether the node currently hosts any of the pods targeted by the service.

            - Load Balancing and Network Routing for the services 



    - { **Replica** set }
            groups of identical pods 
            managed by 'deployment'
            (may be spread across multiple nodes)

        - {**pod**}
            - {**container**}


_Note_: Typically all control nodes are identical, and all worker nodes are identical


### Configuration

decouple config from app itself, which can be injected into pod at runtime

- **ConfigMaps** 
    non-sensitive data

- **Secrets**     
    sensitive data (passwords)

- 3rd party tools
    very sensitive

### Namespaces

- Allow sharing of single cluster by dividing it into multiple (logically separated) virtual clusters.
- Most kubernetes objects (eg pods services, deployments) are namespaced (and have "default" namespace if not explicitly set)
- Suitable for sharing cluster among different depts of same company (eg dev, test, qa)
- not suitable for isolating hostile workloads.



