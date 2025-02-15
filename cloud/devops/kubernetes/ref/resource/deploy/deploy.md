
### Deployment & ReplicaSet

- ##### ReplicaSet
    - controller deploys and manages (self healing)  a (replica) **set of pods*
    - pods (replicas) are **interchangeable** 

    - actually both of these features come from `ReplicaSet`** which Deployment 
- ##### Deployment
    - extends ReplicaSet with additional  [rollout](rollout.md) features

--- 

- `k` **`create deploy`** `my-dep`  **`--replicas=3`** `--image=httpd:alpine `

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
            template:    # <-- ** "pod" - configure same as standalone (from here down)
                metadata:
                    labels:
                        app: my-app     # must match 
                spec:
                    containers:
                    -   image: httpd:alpine
                        name:  my-ctr
        ```
    - _Note_: that its not possible (without eg `helm`) to have the pod definition in  a **separate** `pod.yaml` file and reference this from `deploy.yaml`. 
    The pod (including containers etc) must be fully defined in the deploy.yaml
    ###

- `k` **`apply -f deploy.yaml`**

- `k` **`get deploy`**

    ```python
    NAME     READY   UP-TO-DATE   AVAILABLE   AGE
    my-dep   3/3     3            3           112s
    ```

- `k` **`describe deploy my-dep`**

    ```yaml
    Name:                   my-dep
    Namespace:              defaul
    Selector:               app=my-app   ## <---Pods- deploy is managing (only way to tell)
    Replicas:               3 desired | 3 updated | 3 total | 0 available | 3 unavailable
    StrategyType:           RollingUpdate  # default update strategy
    ....
    Events:
        Type    Reason             Age   From                   Message
        ----    ------             ----  ----                   -------
        Normal  ScalingReplicaSet  49s   deployment-controller  Scaled up replica set my-dep-d9d5ff94b to 3
    ```

- `k` **`get pods`** **`-l app=my-app`**
    - get pods with same `labels deploy selects`
    ```python
    NAME                      READY   STATUS              RESTARTS   AGE
    my-dep-6888474cc6-d6jj9   0/1     ContainerCreating   0          8s
    my-dep-6888474cc6-sm7wl   1/1     Running             0          8s
    my-dep-6888474cc6-xz9m8   1/1     Running             0          8s
```



