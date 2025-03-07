
### Process Isolation
**Namespaces** and **Cgroups**, allow you to put a process into different (independent) sets
- A single process can be in at most 1 of each of the (5) kinds of namespace, and one (of each of many) cgroup sets


- The number (how many containers) and composition (which processes are in each) of the 5 kinds of namespace may coincide,  which is  whats done to create the **_illusion of containers_** 
    - Typically each container has _single namespace of each kind_ and each is _composed of same processes_ as the other kinds. And (as always with namespaces) each  process is in at most one namespace of each kind and therefore in at most a single container.
    - The containers in a single kubernetes [pod](../../kubernetes/ref/resource/pod/pod.md) however share the same single net namespace - ie all the processes in all the containers on a single **pod** are in _single **net**, **mnt**, **ipc**, **uts** namespaces_. ie only pid namespace (and cgroups) dont coincide between containers of a single pod.

But in general, in a linux system, the number and composition of namespaces of any kind is independent of that of any other  (eg how many sets of net namespaces there are, and which processes are in each of them, is independent of the number of pid namespaces and which processes are in each (eg processes in single pid namespace may be in different net namespaces etc)


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


