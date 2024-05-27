
### Pod


- **Logical application**
    -  All **containers** (co-located and co-scheduled) have **same**:
        - **IP address** and port space as **pod** (individual containers within a pod can be distinguished/addressed via unique port number) - unlike in docker (default)() where container gets its own.
        - **namespaces** (and cgroups)
        - filesystem **volumes**
    - Smallest deployable units of Kubernetes computing



##### 
- **`k run`** `my-pod` `--image=nginx` **`-l key-l=val-l`** **`--env=key-e=val-e`** `-o yaml --dry-run=client` > **[pod_yaml.md](pod_yaml.md)**  
    
    - see also [create_run_apply](../../general/modify/create_run_apply.md)

     

###
- **`k describe`** `pod my-pod`
    - **ip address** 
        ```yaml
        IP:      192.168.1.4           # ---** Pod ip address 
        Node:    node01/10.0.0.11      # ---** Node ip address, where pod is running
        ...
        ```
- ##### Exec

    - **`k exec`** `(POD) [-c CONTAINER] [flags]` **`-- Cmd`** 
    **execute Cmd** in container (default: first) of pod.

        ####
        - `k exec mypod` **`-- env`**
        Get output from running the 'env' (show env vars) command from first container in mypod
        
        ####
        - `k exec my-pod` **`-- /bin/bash -c `** `"env & ls /etc/config && echo"`multiple commands in container.
        
        ####
        - open (and keep open) interactive shell (in container my-ctr) of my-pod 
        `k exec` **`-it`** `my-pod [-c my-ctr]` **`-- /bin/bash`**

    ###
    -  **`k set image`** `pod my-pod` `my-ctr=nginx:alpine`
    set image (trigers update)
        - can be called on deployment too

    ---

    ##### Quickly create multiple pods
    - ``for i in `seq 1 3`; do kubectl run my-pod-$i --image=nginx -l app=v1 ; done``




