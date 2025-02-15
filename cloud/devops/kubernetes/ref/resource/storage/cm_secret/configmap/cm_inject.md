
#### Inject 

- 1 **Environment** vars
    - pod.yaml:
        ```yaml
        apiVersion: v1
        kind: Pod
        metadata:
            name: my-pod    
        spec:
            containers:
            -   image: nginx
                name: my-ctr

            ##----------------------------------
            # 1). make -all- values available (cannot rename keys)
                envFrom: 
                - configMapRef:                     
                            name: my-cm            # configMap namename

            ##----------------------------------
            # or 2). make -specific- individual values available
            #           (with possibility to rename keys)
                env: 
                -   name: uno                       # (renamed) local key  
                    valueFrom:
                        configMapKeyRef:            
                            name: my-cm             # configMap name
                            key: one                #  orig key in (configMap) data



        ```
        -  `k apply pod.yaml`
        -  `k` **`exec`** `my-pod` **`-- env`**
            ``` 
            uno=1
            ...
            ``` 
        ####


- 2 **Volume** file/dir  mounts

    - pod-vol.yaml:
        ```yaml
        apiVersion: v1
        kind: Pod
        metadata:
          name: my-pod        
        spec:
          containers:
          - image: nginx
            name: my-ctr
            volumeMounts:                             
            - name: my-vol                            
              mountPath: /etc/config                  
          volumes:
          - name: my-vol                              
            configMap:
              name: my-cm                          
              
              #-------------
              items:                                  # Optional and selective ( cf _valueFrom_ with env above): 
              - key: "one"                            #    map file name/        paths, and if used then _only_ these will be injected
                path: "uno"                        # what local file to save value in
            ##----------------------------------
        ```
        - `k` **`exec`** `my-pod` `-- /bin/bash -c` **`"cat /etc/config/uno"`**
            ```
                1
            ```

 
