Deploying Nginx with Different Image Versions for **Dev** and **Prod** Environments

```yaml
nginx-chart/
│
├── Chart.yaml    
│
├── charts/             # initially empty
│
├── templates/          # Templates
│   ├── deployment.yaml   
│   └── service.yaml

|                       # Values
├── values.yaml             # Base 
├── values-dev.yaml         # Dev 
└── values-prod.yaml        # Prod 
```

- ### Use
    - ##### Release 1 (_my-prod-release_)
        ###
        - `helm` **`install`** **`my-prod-release`** `path_to_dir` `-f` **`values-prod.yaml`**
    
            - `my-prod-release` - unique name for release
            - `_path_to_dir` path to dir containing  _Chart.yaml_
            - `values-prod.yaml` values to inject 

            ###
            This creates a new release in multiple steps:
            - 1). **renders** manifest files (ie creates with values injected)  for kubectl, in-memory
            - 2).calls **`kubectl apply -f`** on these files
            - 3).stores release **metadata** in a Kubernetes **secret** 
                - can subsequently be queried with `helm ls` and `helm status`
        
            ###
            - `helm` **`template`** `my-prod-release.......<same parms as install>`
                only does 1) above - and prints to stdout

                - `> local_file.yaml` 
                    if you want to save manifests aslocal file
    ###
    - ##### Release 2 (_my-dev-release_)
        - `helm` **`install`** **`my-dev-release`** `nginx-chart -f` **`values-dev.yaml`**



