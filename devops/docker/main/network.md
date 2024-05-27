### Docker (*Bridge*) Network

- Docker containers can be networked together in different ways .
You can specify which (bridge, host, none....) in 
    - `docker run` [command](../main/container/run.md), or
    - docker-compose file


- #### Bridge  Network

    - Default docker network type
    - Docker uses a **`Switch`**  to connect _multiple_ containers on a single host (even though it confusingly calls this a "**bridged**" network - which is technically a 2 port switch).

    #####
    - It operates at the **Layer 2**. (Data Link Layer) and forwards traffic based on MAC addresses, and allows containers to communicate with each other and with the host system, much like devices connected to a physical switch.

    #####
    - By default, each docker **container** gets  its own *separate* container **name** and **IP address** (in fact their own **network namespace** [see also](../../../network/interafce.md))
        - unlike in kubernetes where each shares ip address of pod

    #####
    - containers can communicate with each other (and with the host) over the _bridge_ (using container names or IP addresses)



    ```mermaid

    ---
    &%%title: Docker-like Bridge
    ---
    flowchart LR
        
    subgraph ns_docker-host

        b["Bridge"]

        subgraph ns1_ctr1
        eth-n1
        end

        subgraph ns2_ctr2
        eth-n2
        end

        subgraph ns3_ctr3
        eth-n3
        end


        
        eth-n1 o--o |veth-1| b
        eth-n2 o--o |veth-2| b 
        eth-n3 o--o |veth-3| b 

        Eth-host
        b o-.-o Eth-host
    end    

        Ex["External"]
        Eth-host o--o Ex
    ```

---
- Containers in single Kubernetes **[pod](../../kubernetes/ref/resource/pod/pod.md)**, in contrast, all **share** the **same** network namespace