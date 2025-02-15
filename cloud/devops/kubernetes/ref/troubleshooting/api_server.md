

- ` k` **`config`** **`view`**
    - [shows](../general/kubeconfig/kubeconfig.md) `IP address` of Api Server

        ```yaml
        ....
        clusters:
        -   cluster:
                certificate-authority-data: DATA+OMITTED
                server: https://172.30.1.2:6443 # <--- *** API Server IP address ***
        ....
        ```

- `k` **`cluster-info`**
    - should [show](../general/main.md) `is running`:

        ```yaml
        .....
        Kubernetes control plane (Api Server) is running at https://172.30.1.2:6443
        .....
        ```
