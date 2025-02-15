## Priority Class

###
#### **PriorityClass**
- Determines the **scheduling** _and_ **eviction** _priority_ of Pods within a Kubernetes cluster. 

###
- Pods with higher priority are 
    - more likely to be _scheduled_, and 
    - less likely to be _evicted_ 

than Pods with lower priority, especially when resources are constrained.

   
###
- Define a PriorityClass with a specific priority value and optional description:

    ```yaml
    apiVersion: scheduling.k8s.io/v1
    kind: PriorityClass
    metadata:
        name: high-priority
    value: 1000000
    globalDefault: false
    description: "This priority class is for high-priority workloads."
    ```

##
- Assign a PriorityClass to a Pod by specifying the `priorityClassName` field in the Pod's spec:

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
        name: my-pod
    spec:
        priorityClassName: high-priority
        containers:
        - name: my-container
            image: myimage
    ```




