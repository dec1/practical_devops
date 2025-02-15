

### top 

Show  **memory** and **cpu** *usage* in pod(s) or node(s)
- `k top` **`node`** [**`node-name`**]


    ```yaml
    NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
    node-1         500m         25%    3400Mi          45%       
    node-2         1200m        60%    5800Mi          78%       
    master-node    200m         10%    1200Mi          16%
    ``` 
    - **`node-name`** just for specific pod with this name



####
- `k top` **`pod`** [**`pod-name`**] [**`--containers`**]   `[--sort-by=cpu|memory]` `[-l name=myLabel]` `[-A | -n ns-name]`

    ```yaml
    NAME              CPU(cores)   MEMORY(bytes)   
    web-app-abc123    5m           100Mi           
    db-backend-xyz    10m          250Mi           
    cache-redis-123   2m           50Mi
    ``` 
    - **`pod-name`** just for specific pod with this name
    - **`--containers`** include containers in output
    - `--sort-by` sort output by `cpu` or `memory`
    - `-l` only pods with matching labels
    - `-n` only pods in given namespace 
    - like most kubectl commands current namespace is used if none specified

###
- Units:

    - `m` = `millicores` (1/1000 of a CPU core).
    - `Mi` = `mebibytes` (= 2^20 = 1,048,576 bytes), 
    ####
    - Similar to: 
        -  `kubectl exec` into a container, followed by `top` (in the container)

-----
#### metrics server
Note that k top requires the  [metrics server](../architecture/components/pods/workload/system/metrics_server.md) to be installed. 