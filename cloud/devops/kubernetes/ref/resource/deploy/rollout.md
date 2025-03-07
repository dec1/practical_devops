## Rollout
**replace** existing/running **pods** of deployment - in response to change in **spec.template**   
 **revision** - new
- cf scaling which adds more (same) pods or removes (leaving some same) - all same revision.
- **rollout strategy** - [how/when](rollout_strategy.md) this replacement happens 
  

 A Deployment's rollout is triggered if and only if the Deployment's Pod template (that is, .spec.template) is changed, for example if the labels or container images of the template are updated. Other updates, such as scaling the Deployment, do not trigger a rollout.

####
- deploy.yaml
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
        name: my-dep
    spec:
        replicas: 3                 # replica set with 3 pods
        selector:
            matchLabels:
                app: my-app         # must match 
        template:
            metadata:
                labels:
                    app: my-app     # must match 
            spec:
                containers:
                -   image: httpd:alpine
                    name:  my-ctr

    ## --------------------------
        strategy:
            type: RollingUpdate     # default

            rollingUpdate:          # options (specific to strategy type)
                
                # during the update process:
                maxUnavailable: 1   # (optional) max num pods that can be *unavailable* 
                maxSurge: 2         # (optional) max num pods that can be created *above replicas*
     ## --------------------------          
    ```



------
-  `k` **`rollout status`** `deploy my-dep`
    ```yaml
    deployment "my-dep" successfully rolled out
    ```

- `k` **`rollout history`** deploy my-dep
    ```yaml
    deployment.apps/my-dep 
    REVISION  CHANGE-CAUSE
    1         <none>  
    ```

- `k` **`set image`** `deploy my-dep` `my-ctr=nginx:alpine`
   (trigers update)
    ```yaml
    deployment.apps/my-dep image updated
    ```

- `k` **`rollout history`** `deploy my-dep`  **`[--revision=<num>]`**
    `--revision`- details on revision num (or list of all revisions if omitted)
    ```yaml
    REVISION  CHANGE-CAUSE
    1         <none>
    2         <none>        # new revision 2
    ```
    - trigger update
        **Manual** edit spec.template 
        `k  apply -f deploy.yaml` 

    #####
    - `k rollout history deploy my-dep`
        ```yaml
        REVISION  CHANGE-CAUSE
        1         <none>
        2         <none>
        3         <none>    # new revision 3
        ```



- **`k rollout undo deployment my-dep --to-revision=2`** 
    - `--to-revision`default = 0 (last revision).

    - `k rollout history deploy my-dep`
        ```yaml 
        REVISION  CHANGE-CAUSE
        1         <none>
        3         <none>
        4         <none>        # "2" -> "4" and moved to top of stack
        ```
