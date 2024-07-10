
# Kubernetes Architecture


```mermaid
flowchart LR
    classDef class_KubeProxy fill:#f96,stroke:darkblue,stroke-width:3px
    classDef class_Service fill:lightblue, stroke-dasharray: 1 1, ,stroke-width:2px
    classDef class_Service_Kubernetes fill:lightblue,stroke:darkblue,stroke-width:3px
    classDef class_workloads fill:lightgreen
    classDef class_workloads_sys fill:peachpuff,stroke:darkblue,stroke-width:3px
    classDef class_system stroke:#ff3,stroke-width:4px,color:red
    classDef class_static_pod stroke:darkblue,stroke-width:3px



    %% --------------------- Control -----------

   subgraph Control Node ["`**Control** Node`"]
       direction TB


        subgraph Both_c [" "]
            style Both_c  stroke-width:4px
            direction TB
            subgraph Both_c_service ["`**Services** (linux)`"]
                direction LR
                    ContainerRuntime_c{{Container Runtime  <i class="fa-brands fa-linux"></i>}}:::class_Service 
                    NetworkPlugins_c{{Network Pluginsn  <i class="fa-brands fa-linux">}}:::class_Service

                    Kubelet_c(Kubelet <i class="fa-brands fa-linux">):::class_Service_Kubernetes
            end

            KubeProxy_c(Kube-proxy <i class='fa fa-ghost' style='color:darkred'></i>   <i class="fa-solid fa-network-wired" style='color:green'></i> ):::class_KubeProxy

            %% force specified direction (with invisible link)
            Both_c_service ~~~ KubeProxy_c
       end

       
       

    subgraph static ["`**Static** pods`"]
    direction TB
        Manifest([/etc/kubernetes/manifests/])

        subgraph Static_pods [" " ]
        style Static_pods  stroke-width:4px
        direction TB
            APIServer(Api Server):::class_static_pod
            ControllerManager(Controller Manager):::class_static_pod
            Scheduler(Scheduler):::class_static_pod
            Etcd(Etcd):::class_static_pod
        end


            %% force specified dirn
        Manifest ~~~ ControllerManager  
    end 


    subgraph workloads_sys [" Workloads (system) "]
        direction LR
        subgraph Deployments_sys ["`**Deployments**`"]
        direction TB
            CoreDNS(CoreDNS):::class_workloads_sys
            MetricsServer(metrics-server ):::class_workloads_sys      
        end

        Other_sys(" Other ")
    end

 end
    
    %% --------------------- Worker -----------

    
   subgraph Worker Node ["`**Worker** Node`"]
       direction TB

        subgraph Both_w [" "]
            direction TB
            style Both_w  stroke-width:4px
            subgraph Both_w_service ["`**Services** (linux)`"]
                direction LR
                    ContainerRuntime_w{{Container Runtime <i class="fa-brands fa-linux">}}:::class_Service
                    NetworkPlugins_W{{Network Plugins <i class="fa-brands fa-linux">}}:::class_Service

                    Kubelet_w(Kubelet <i class="fa-brands fa-linux">):::class_Service_Kubernetes
            end

            KubeProxy_w(Kube-proxy <i class='fa fa-ghost' style='color:darkred'></i>   <i class="fa-solid fa-network-wired" style='color:green'></i>  ):::class_KubeProxy
    
            %% force specified dirn
            Both_w_service ~~~ KubeProxy_w 
       end

        subgraph workloads_user [" Workloads (user) "]
            direction LR
            subgraph Deployments_user ["`**Deployments**`"]
            direction TB
                User_App1(User Apps):::class_workloads        
                %% User_App2(User App2):::class_workloads        
            end

            Other_user(" Other ")
            

        end
       
    end
    
    %% force specified dirn
    Both_c ~~~ Both_w  
    Other_sys ~~~ Other_user
    workloads_sys <-. variable .-> workloads_user

    %% Static_pods --> |"Common Label"| Both_c_service
    %% Both_c_service --> |"Common Label"| Both_w 
    %% sBoth_w  --> |"Common Label"| Static_pods

    %% KubeProxy_c --> Static_pods
    %% Both_c <-.-> Both_w 
    %% KubeletC -.- KubeletW
    %% ContainerRuntimeC -.- ContainerRuntimeW
    %% NetworkPluginsC -.- NetworkPluginsW
    %% KubeProxyC <-.-> KubeProxyW

```

- **Dark Borders**:   
    - **Nodes** individual: core kubernetes (system) components
    - **Groups** of Nodes: run only on nodes as shown
        : cf workloads - system and user  (as shown is usual - but may bbe allowed to vary)
- ##### Kublet 
    - starts/stops all pods on node in question



- ##### Workloads
    - usually run on type of nodes shown, but
        - user workloads may (also) run on (some) control nodes, and 
        - CoreDNS and metric server may (also) run on (some) worker nodeS
    - _Pod start/stop_: **Controller Manager** -> **Scheduler** -> **Kublet**
        (controller manager, delegates to scheduler,  which picks node(s) and delegates to kublet on node in question)

- ##### Non-Workloads
    - only run as shown
        - ##### Static Pods
            - only on control plane
    - _Pod start/stop_:  **Kublet**
        (on node in question, acts independently)




