## Resource Bounds

###
#### 1). **ResourceQuota** (Namespace total) :
- Limits the **total** resource consumption for _all_ objects in a **namespace** (and any specified scope using `scopeSelector`). It also allows specifying the maximum number of `pods`.

###
- No pods will be started in the namespace (and any specified [scope](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-scopes) eg PriorityClass) if their **declared** requests/limits **total** exceed those of ResourceQuota. 

   
   ###
   - `k` **`create`** **`quota`** `rq` **`--hard=`** `pods=2,cpu=1,memory=1Gi,limits.cpu=2,limits.memory=2Gi` 

        ```yaml
        apiVersion: v1
        kind: ResourceQuota
        metadata:
            name: rq
        spec:
            hard:
                pods: "2"
                requests.cpu: "1"
                requests.memory: "1Gi"
                limits.cpu: "2"
                limits.memory: "2Gi"
            scopeSelector:              # Optional - filters which resources the quota applies to based a scope.
                matchExpressions:
                - scopeName: PriorityClass
                  operator: In
                  values:
                  - middle
        ```



    ##
    - If `namespace` has a 1). **ResourceQuota**, then it is required for all `resources` (eg pods) in the namespace for either
        - 2). *LimitRange* to be set on namespace, - see 2 below or 
        - 3). **explicitly** specify requests/limits (for each individual resource in namespace) - see 3 below
##        
#### 2). LimitRange (Individual default)
- Limits the **individual** resource consumption for _each_ object in the **namespace** that the LimitRange exists in

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

#### 3). Requests/Limits  (individual explicit) in Pod
  - explicitly specified for **each container** in Pod.
    - take **precedence** over any **LimitRange** (default) defined on namespace
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
                        cpu: "500m"
                        memory: "0.5Gi"
                    limits:
                        cpu: 1
                        memory: "0.5Gi"
        ```





    
