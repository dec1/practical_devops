## Resource Bounds

###
#### 1. **ResourceQuota** (Namespace total) :
- Limits the **total** resource consumption for _all_ objects in a **namespace**
and additionally allows specifying max number of `pods`

####
- No pods will be started in namespace if their **declared** requests/limits **total** exceed those of ResourceQuota. 



   
   ###
   - `k` **`create`** **`quota`** `rq` **`--hard=`** `pods=2,cpu=1,memory=1Gi,limits.cpu=2,limits.memory=2Gi` 

        ```yaml
        kind: ResourceQuota
        metadata:
            name: rq
        spec:
            hard:
                pods: "2"

                requests.cpu: "1"   // "requests." is optional (doc: "cpu Same as requests.cpu")
                requests.memory: 1G

                limits.cpu: "2"
                limits.memory: 2G
        ```

    ##
    - If `namespace` has a **ResourceQuota**, then it is required for all `resources` (eg pods) in the namespace to either
        - *LimitRange* be be set on namespace, , or 
        -  **explicitly** specify requests/limits (for each individual resource in namespace) - see 3 below
##        
#### 2. LimitRange (Individual default)
- Limits the **individual** resource consumption for _each_ object in the **namespace** that its exists in

    ```yaml
    apiVersion: v1
    kind: LimitRange
    metadata:
      name: my-lr
    spec:
      limits:

      # default for containers that don't explicitly specify
      - default: # this section defines default limits for container that doesn't explicitly specify one
          cpu: 500m
        defaultRequest: 
          cpu: 500m

        # limits anything explicitly set: for container, and defaults above
        max:   
          cpu: "1"
        min:
          cpu: 100m
        type: Container
    ```

#### 3. Requests/Limits  (Individual explicit)
  - explicitly specified for **each container** in Pod.
    - `requests` (min) 
        Kubernetes wont start pods unless it can find nodes that satisfy 
    -  `limits` (max) 
        runtime checks for exceeding **limits** are performed, and violation may result in cpu throttling and termination of the pod.

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
        name: p
    spec:
        containers:
        -   name: my-container
            image: myimage
                resources:
                    requests:
                        cpu: ".5"
                        memory: ".5G"
                    limits:
                        cpu: 1
                        memory: ".5G"
    ```





    
