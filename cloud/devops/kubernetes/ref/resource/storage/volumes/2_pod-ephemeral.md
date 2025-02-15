
### emptyDir
- **Ephemeral** - **Pod** lifetime

###
- keeps data as long lived as the pod (which is pretty ephemeral - eg scale down will delete pods) 

- individual volume associated with `single pod` (even in replica set each pod gets its own volume) 

- mount (possibly at different location in each container) the  dir as initially empty. 

- Shared by `all containers` in the Pod can read and write though that volume can be mounted at the same or different paths in each container

###
- **pod.yaml** 



    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-pod
    spec:       
      volumes:                  # volume - for pod
        - name: shared-vol        # containers must use exactly "name"  for volumeMount
          emptyDir: {}            # "{}" is optional
            
      containers:
        -   name: ctr1
            image: busybox
            command: ["/bin/sh", "-c"] 
            args: ["while true; do sleep 600; done"]  
    
            volumeMounts:           # ctr1: mount shared-vol at /etc/a 
            - name: shared-vol      #                               (shared-vol)+++
              mountPath: /etc/a
    
        -   name: ctr2
            image: busybox
            command: ["/bin/sh", "-c"] 
            args: ["while true; do sleep 600; done"]  
    
            volumeMounts:           # ctr2: mount shared-vol at etc/b
            - name: shared-vol
              mountPath: /etc/b
    ```

- `k apply -f pod.yaml`

- `k exec my-pod` **`-c ctr1`** `-- ls /etc`
  or (see [exec](../../pod/cmds/cmds.md) )
  
- `k exec my-pod` `-c ctr2` `--` **`/bin/sh -c`**  `"ls /etc"` 
    ```yaml
    a
    ....
    ```

- `k exec my-pod` **`-c ctr2`** `-- ls /etc`
    ```yaml
    b
    ....
    ```