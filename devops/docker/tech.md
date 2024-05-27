1)  Container Runtime (Engine)
    -------------------------
    Handles everything after image creation

    - **_Containerd_**
            simplicity, performance, secutity. default in kubernetes

    - **_CRI-O_**         
            used by OpenShift

    ####
    - **Docker (Engine)** 
            uses containerd under the hood 

    - **Podman**
            uses CRI-O under the hood  

2)  Image Management (bulding etc)
    --------------
    - **_Buildah_**
    - **_Kaniko_**
    #####
    - **Docker**
    - **Podman**
        - rootless, deamonless, pod concept (similar to kubernetes)
      

3)  Container Orchestrator
    -------------------- 
    uses a container runtime engine to instantiate a container while adding sophisticated features like **scalability**, **networking**

    #####
    - **Kubernetes**
    - **Nomad**           


