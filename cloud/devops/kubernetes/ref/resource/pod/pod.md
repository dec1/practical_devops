
### Pod

- A wrapper around a set of closely connected containers
(see also [auxillary containers](../../resource//pod/auxillary_containers.md)) 
    -  All **containers** (co-located and co-scheduled) 
        - sharing
            - do share **same**:
                - **IP address** (which is unique)
                - [namespaces](../../../../docker/tech/process_isolation.md)
                    - **net** (thus localhost and _port space_) 
                    - **mnt** (thus _filesystem volumes_ eg [pod ephemeral volumes](../../resource/storage/volumes/2_pod-ephemeral.md)) 
                    - ipc
                - uts
            - do **not** share 
                - _pid_ namespace 
                - _cgroups_ 
        - are _collocated_ - on a single node (containers never spread across multiple nodes)
 
    
    - contains some _glue_ that help integrate them into rest of kubernetes 
        - metadata (names, labels, annotations, restart policy)


          
---
####
- All pods are ultimately started by **Kubelet** on node in question, but some (staic) it does so independently and directly reading manifests in a pre-defined location, and the rest (workloads) only when/where told to do so by scheduler (and controller manager) we distinguish

```mermaid
flowchart TD
    classDef class_pod fill:goldenrod,stroke-width:2px
    classDef class_sys fill:cyan,stroke-width:2px  
    classDef class_nonsys fill:antiquewhite,stroke-width:2px  
    
    classDef class_stat fill:darkgrey,stroke-width:2px  
    classDef class_nonstat fill:cornsilk,stroke-width:2px    

    A[Pod]:::class_pod
    B[**Workload**]:::class_nonstat
    C[**Static**]:::class_stat

    D[Non-System]:::class_nonsys
    E[**System**]:::class_sys

    F[Non-System]:::class_nonsys
    G[**System**]:::class_sys



    H((in namespace **system**)):::class_sys


    

    A --> B
    A --> |/etc/kubernetes/manifests/| C

    B --> F
    B -->|"CoreDNS, Cni, Metrics Server" | G

    C --> D
    C -->|"on each control plane node" | E

    E <-.- H
    G -.-> H

 
```

##
- #### [Workload](../../general/architecture/components/pods/workload/workload_pods.md) Pods
    Those managed by **controller manager** and **scheduler**, which in turn tell **kubelet** when/where to start/stop them. This includes system workloads like CoreDNS, metrics server, and network (CNI) plugins.

- #### [Static](../../general/architecture/components/pods/static/static_pods.md) Pods
    -  are those which an individual **kubelet** instance, on a given node,
     starts/stops a pod based on presence of a manifest file in  **`/etc/kubernetes/manifests/`**, on said node
        - Critical system components have, by default, a copy of the respective manifest on every control plane node
            - _Api Server, Controller Manager, Scheduler, Etcd_,
            so that each control plane node runs a copy of these system static pods
        - but you can create any  non-system pod static you create by placing a manifest file into
        _/etc/kubernetes/manifests_







