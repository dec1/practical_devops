
### emptyDir
- **Ephemeral** - **pod** lifetime

- keeps data as long lived as the pod (which still pretty ephemeral - eg scale down) 

- individual volume associated with individual pod (even in replica set each pods gets individual volume) 

- mount (possibly at different location in each container) initially empty dir. 

- All containers in the Pod can read and write though that volume can be mounted at the same or different paths in each container

###
- **my-empty-dir.yaml** 
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: alpine
    spec:       
                                #                       names:  (shared-vol)+++ must match exactly   
      volumes:                  # volume - for pod
      - name: shared-vol        # nameVol                       (shared-vol)+++
        emptyDir: {}            # "{}" is option
        
      containers:
      - name: ctr1             
        image: alpine:3.12

        volumeMounts:           # ctr1: mount shared-vol at /etc/a 
        - name: shared-vol      #                               (shared-vol)+++
          mountPath: /etc

      - name: ctr2                        
        image: alpine:3.12

        volumeMounts:           # ctr2: mount shared-vol at etc/b
        - name: shared-vol
          mountPath: /etc
    ```
