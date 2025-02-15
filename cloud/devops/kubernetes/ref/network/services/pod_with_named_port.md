#### Pod
- `k run my-pod` `--image=nginx` `-l app=my-app` `[--port=<num>]` `-o yaml --dry-run=client > pod.yaml`
    - have to use **label** so service can **target**  (cant target on name)
    


- ##### Port Names
    ```yaml
    .....
    
    # All this is needed to name a port
    # `run --port=80` can create the first 2 lines for you, but you must add the 3rd manually
    
    ports:    # serves  no other purpose other than to allow you to 'name' ports , so they can be referenced elsewhere (eg eg by services) by name instead of number - keeps number (value) closer to source of truth         
    - containerPort: 80   
    name: my-port        
    ..... 
    ```
    Using `--port` in `run`  adds the `ports.containerPort` but unfortunately doesnt provide a way to specify the name - you have to save manifest and add `name: my-port` manually


    #####
    - **pod.yaml**
        ```yaml
        apiVersion: v1
        kind: Pod
        metadata:                   
        labels:                   # service --targets-- based on --labels--
            app: my-app             # <--  this  
        name: my-pod              # cant target based pod name!
        spec:
        containers:
        - image: nginx
            name: my-ctr
            
            # All this is needed (just) to name a port
            ports:                   
            - containerPort: 80   
            name: my-port      #  <-- service can (port) forward to this "name" 
            
            
        ```