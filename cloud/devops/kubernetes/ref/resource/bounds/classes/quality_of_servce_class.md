### Quality of Service (QoS) Classes
Kubernetes categorizes pods into three QoS classes based on their individual resource requests and limits defined in each pod. 
Note: These are not calculated from `ResourceQuota` or `LimitRange`, but directly from the pod's own (individual explicit) [resource specifications](../resource_limits.md) (num 3).

- #### 1) Guaranteed

    - Both CPU and memory **requests and limits are set and are equal**.
    - Pods in this class receive the **highest** level of service. They are the last to be evicted under resource pressure.
    - eg
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
                        memory: "500Mi"
                        cpu: "500m"
                    limits:
                        memory: "500Mi"
                        cpu: "500m"
        ```

- #### 2) Burstable

    - Requests and limits are **set, but not equal** (i.e., the requests are less than limits).
    - Pods in this class can burst up to their limits but are more likely to be evicted than Guaranteed pods if the node is under resource pressure.

    - eg
        ```yaml
                ....
                resources:
                    requests:
                        memory: "200Mi"
                        cpu: "200m"
                    limits:
                        memory: "500Mi"
                        cpu: "500m"
        ```
- #### 3) BestEffort

    - **Neither** requests nor limits are **set**
    - Pods in this class receive the **lowest** level of service. They are the first to be evicted under resource pressure.

### Querying 
-    **`status.qosClass`**
     of pods can be used to query qos calculated by kubernetes eg
    - `k get pods -o jsonpath="{range .items[*]}{.metadata.name}` **`{.status.qosClass}`**`{'\n'}"`
        ```yaml
        my-pod-1 Burstable
        my-pod-2 BestEffort
        .......
        ```
