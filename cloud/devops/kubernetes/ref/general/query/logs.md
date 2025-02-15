

### logs [-f]
cout/cerr of containers


- ### pod
    - `k` **`logs`** **`my-pod`** | **`-l key=val`**      **`[-c my-ctr`**`|` **`--all-containers=true]`** `[-p]` `[-n my-ns]` **`[-f]`** 
        - show logs of container 
            ###
            - `my-pod` pod name
            - **`-l key=val`** labels of pods to log (eps useful for **deployment**)
            

            - `p` show logs from **`previous`** container instance (if pod restarted it)
            - **`-f`** **follow** (live update) 
                - cf `get -w`
            - `-c`  name of container (default:  *first*  ctr in pod) 
            - `--all-containers=true` include all containers
            - `-n` namespace to look in




- ### deployment
    - `k` **`logs`** **` deployment/my-dep`** `[-c my-ctr | --all-containers]` [`-n my-ns`]
    logs of container(s) of deployment my-dep 
        - pods of deployment are called `{deployment_name}_suffix`
            - with this command you **dont have to know suffix**

        ####
        - (the containers of) _which pod_ gets used is _unspecified_

            - if you wish to specfiy which pod to get to get logs of:
                ######
                 - **which pods** are in deployment (only possible via selector labels)
                    - `k describe deploy my-dep`
                        ```yaml
                        .....
                        Selector:               app=my-app
                        .....
                        ```
                - get pods with these labels:
                    - `k get pods` **`-l app=my-app`**

- ### job
    - `k` **`logs`** **`job/my-job`** `[-c my-ctr | --all-containers]` [`-n my-ns`]
    logs of container(s) of job my-job 
        - pods of jobs are called `{job_name}_suffix`
            - with this command you **dont have to know suffix**



   
   