

#### Expose 

- k create service is most flexible way to create a service
 - "expose" can be used as  convenient alternative that automatically sets the selectors to match the pod labels.

    ###
    - `k` **`expose`** **`pod my-pod`** `--port=80` `[--name=my-svc]` `[--type=ClusterIP]`
        - automatically targets labels of pod 
        ```yaml
        service/my-svc exposed
        ```
        
        
    ###
    -  `k` **`expose`** **`deploy my-dep`** `--port=80 [--target-port=80]` `[--name=my-svc]` `[--type=ClusterIP]`
        - automatically targets same (pod) labels deployment does
        ```yaml
        service/my-dep exposed
        ```
        
    
    ####
    - `k` **`run`** **`--expose`**  **`my-app`** **`--image=nginx`** `--restart=Never` **`--port=80`** `[-n my-ns]` `--dry-run=client -o yaml`
       
       - creates **pod** with labels (key = `run`, value= `<name-of-pod>`) *and* a **service** that targets it in single command (with _same name_ and _port_)
            #####
            - `my-app` - name of bot service and pod
            - `--port=80` - both port (service listens on) and target port (on pod forwarded to) 
       
        ```yaml
        # -------------
        # -- service --
        # -------------
        apiVersion: v1
        kind: Service
        metadata:
          name: my-app
        spec:
          ports:
          - port: 80
            protocol: TCP
            targetPort: 80
          selector:
            run: my-app


        ---  # yaml document separator

        # ---------------
        # ---- pod ------
        # ---------------
        apiVersion: v1
        kind: Pod
        metadata:
          labels:
            run: my-app
          name: my-app
        spec:
          containers:
          - image: nginx
            name: my-app
            ports:
            - containerPort: 80 ## doc only
        ```


