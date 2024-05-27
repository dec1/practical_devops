### Namespace Types
                    
####
- 1). **pid**  
    - process **identifiers** (of running processes) in any ns are indep of those in any other ns
    - process can be created in specific namespace 


##### 
-  2). ***net***   
    - network **stack** (interfaces, routing table, firewall)
    - only processes in given ns can use network stack of that ns
        - and thus communicate directly with each other via tcp/localhost
    - processes in different network namespaces require additional configuration to communicate
        - e.g. [virtual ethernet devices](../../../network/interafce.md) 
##### 
-  3). **mnt**   
    - processes in the same mount namespace see the same mounted **file systems** at the same mount points

##### 
-  4). **ipc**   
    - only processes in same ns can communicate with each other via ipc (eg shared memory) 


#####             
-  5). **uts**   
    - allow a process in given ns to see
        - **host** - (host name and domain **name**) as different from what processes in other ns do



