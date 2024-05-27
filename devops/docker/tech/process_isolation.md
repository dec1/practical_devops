
### Process Isolation
**Namespaces** and **Cgroups**, allow you to put a process into different (independent) sets
- A single process can be in at most 1 of each (5) namespace sets, and one (of each of many) cgroup sets
- The sets may coincide, which is  whats done to create the "illusion" of containers




    - #### 1). Namespaces:
        -  **whats visible** to a process 
            - Partitions various system resources (for processes)
                - allowing sets of processes to operate with their own isolated view of the system

            ####
            -  5 linux system **[Namespace Types](./namespace_types.md)** 

            #####
            - Stops one process in one set causing trouble for those in another another by:
                - using too much cpu, memory, storage, network
                - corrupting memory or files of another process
                - sending another process bad data or too many requests




        ####
        - _Note_: while namespaces limit what processes inside ns can see of system, it
        *doesnt stop (any) process outside any ns **looking in*** 
            - eg process running (globally) on host can see pid (entry) of process running inside ns/container (even though actual value may differ) - but not vice versa
        

        - ##### Containers
            - in **Docker** have (by default)  **separate** namespaces 
            -  in (single) **Kubernetes** pod **share** **net** namespace
                - (and sometimes pid, ipc) 
                - allows them to communicate easily using localhost or container names
                  


    - #### 2). Cgroups (Control Groups)
        - **how much** process  **can use**
        - Limits and manages resource usage  of containers.
        - Each process can be assigned a cgroup controller of given type:
            - CPU
            - Memory
            - .....
        - Containers 
            - never share cgroups (neither docker nor kubernetes)


