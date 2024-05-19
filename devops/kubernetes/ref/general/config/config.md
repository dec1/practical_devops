### KubeConfig (Kubectl Configuraution)


- [context](context.md) info
- editable through `k` **`config`** `...`commands
- dynamically calculated **from**     
    - in order (only first found used) contents of :

        - `--kubeconfig` file path 
        - `KUBECONFIG` env var - list of file paths, with contents **merged** 
        (entry in *file later* in list, taking *precedence* if entry in multiple files)
        - **`~/.kube/config`** file 
