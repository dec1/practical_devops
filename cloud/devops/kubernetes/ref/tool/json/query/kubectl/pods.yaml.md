- pods.yaml
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
        name: pod1
        namespace: my-ns
    spec:
        containers:
        -   name: container1
            image: nginx
    ---
    apiVersion: v1
    kind: Pod
    metadata:
        name: pod2
        namespace: my-ns
    spec:
        containers:
        -   name: container2
            image: nginx
    ```

- `k create ns my-ns`
- `k apply -f pods.yaml`
