
### Rollout Strategy

 - **In-built**
    Can be set as values in `spec.strategy.type` of deploy.yaml
    ####
    - **Rolling** (defaut)
        - replace each pod individually, so at most one pod is "updating" at a time. 
            - **+** Minimizes downtime. 
            - **-**  Mixed versions pods (during update) 
    - **Recreate**
        - all pods deleted before all are recreated
            - **-** Maximizes downtime. 
            - **+**  No mixed versions pods (during update) 
    ###
- **Custom**
    Manually ([killercoda](https://killercoda.com/killer-shell-ckad)) create     
    - **`2 deployments`**
    - **`1 service`** targeting the pods in 
        - **one** (`blue-green`) or 
        - **both** (`canary`) 
    


    ####
    - **Blue-Green**
        - 1). Service targets the pods of the dep_1
        - 2). Create a new independent dep_2 (with **different labels** on pods)
        - 3). Set service to target pods of dep_2 (eg by changing service selector) when ready 
        - 4). Remove dep_1
        ####

         - *dep_1.yaml*
         ```yaml
         apiVersion: apps/v1
         kind: Deployment
         metadata:
             name: dep-1                          
         spec:
             replicas: 4                          # differ
             selector:
                 matchLabels:
                     my-app: blue                  # 
             template:
                 metadata:
                    labels:
                        my-app: blue                  # ---- 1
                 spec:
                    containers:
                    -   name: my-ctr
                        image: httpd:alpine         # 2
         ```
     - *dep_2.yaml*
         ```yaml
         ....
             name: dep-2                          
                     my-app: green                   # 
                     my-app: green                   # ---- 1
                     image: nginx:alpine             # 2
         ....
         ```
     - *service.yaml*
         ```yaml
         apiVersion: v1
         kind: Service
         metadata:
           name: ser
         spec:
           selector:
             my-app: blue              #  ---> green   (when ready)
           ports:
             - protocol: TCP
               port: 80
               targetPort: 80  
            ```

    #####    
    - **Canary**
        - 1). Create dep_1 and dep_2 (with **same labels** on pods), but
        - 2). replica counts reflecting the desired proportions of each deployment
        - 3). Set service to target pods of both (service selector targets same labels) 
        ####
        - *dep_1.yaml*
            ```yaml
            kind: Deployment
            spec:
                replicas: 4                # differ
                selector:
                    matchLabels:
                        my-app: same-sel   # ----
            ```

        - *dep_2.yaml*
            ```yaml
            ....
            kind: Deployment
            spec:
                replicas: 1                # differ
                selector:
                    matchLabels:
                        my-app: same-sel  # ----
            ....
            ```

        - *ser.yaml*
            ```yaml
            kind: Service
            spec:
              selector:
                my-app: same-sel          # ----
            ....
            ```


