### 1)  Container Runtime (Engine)

- Handles everything after image creation

    - **[Docker](https://www.docker.com/)** Engine 
        - uses containerd under the hood 

    - **[Podman](https://podman.io/)**
        - uses CRI-O under the hood  
        - rootless, deamonless, pod concept (similar to kubernetes)

    ####
    - **[_Containerd_](https://containerd.io/)**
        - simplicity, performance, secutity. default in kubernetes

    - **[_CRI-O_](https://cri-o.io/)**         
        - used by podman, openshift


### 2) Image Management (bulding etc)

- building, pushing/pulling from repos
    - **[Docker](https://www.docker.com/)**
    - **[Podman](https://podman.io/)**
        
        
    #####
    - **[_Buildah_](https://buildah.io/)**
    - **[_Kaniko_](https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md)**
    

      

### 3) Container Orchestrator

- uses a container runtime engine to instantiate a container while adding sophisticated features like **scalability**, **networking**

    #####
    - **[Kubernetes](https://kubernetes.io/)**
    - **[OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift)** 
    - **[Nomad](https://www.nomadproject.io/)**   
    - **[Rancher](https://www.rancher.com/)**

### 4) Package Manager
- **Application** (containerized)
    - multiple containers working together as one (logical) application
 - **Package Manager** simplifies/automates the packaging/configuration of containerized _applications_ (as a single unit) within a container orchestration platform
    - **[Helm](../../kubernetes/ref/helm/helm.md)**
            


