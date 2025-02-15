

- **my-pod.yaml**

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
    spec:
      volumes:                      # volume (pod) site for: claim 
                                   #    cf "PersistentVolume" in my-volume.yaml
      - name: my-volume
        persistentVolumeClaim:
          claimName: pvc           #  see my-claim.yaml
                                   #       in turn (optionally) specifies storageClassName
      containers:
      - image: nginx
        name: nginx
        volumeMounts:              # volumeMount (container)
        - mountPath: "/var/log/nginx"
          name: my-volume
    ```

- **my-claim.yaml**
    ```yaml
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: pvc
    spec:
                                            # Kubernetes    tries to find  volumes that     matches:
      accessModes:                          # 1) access     --required-- by pod (Kubernetes independently s a   suitable volume)
      - ReadWriteOnce
      resources:
        requests:
          storage: 2Gi                      # 2) size   --required
    # Selectors to match                   
      selector:
        matchLabels:                        
          my-key: my-val                    # 3) label  selector - suitable volumes must have this label
      storageClassName: my-storage-class    # 4)  "my-storage-class.yaml"
    ```

- **my-volume.yaml** (static only)

    ```yaml
    kind: PersistentVolume
    apiVersion: v1
    metadata:
      name: pv
      labels:
        my-key: my-val                      # 3) satisfied
    spec:
      capacity:
        storage: 5Gi                        # 5 Gb # 2)     satisfied
      accessModes:                          # access    --supported-- by volume # 1) satisfied
      - ReadWriteOnce                      # single node (but multiple pods theron) can write to volume - "once" -> "one"
      - ReadOnlyMany                       # multiple nodes (can read volume)
    # - ReadWriteMany                      # multiple nodes (can write to volume)
    # - ReadWriteOncePod                   # single pod can ead and write (v1.29+)

      storageClassName: my-storage-class    #  -**- just a string here -  "my-storage-class.yaml" # 4) satisfied
    # -----
    # 1)
      nfs:
        path: /path/to/nfs                  # NFS server    share path
        server: nfs-server.example.com      # NFS server IP     or hostname
    # -----
    # 2)
    # hostPath:                            # alternative to     nfs # not recommended for production - node-dependent
    #   path: /var/logs
    ```



- **my-storage-class.yaml**  (dynamic only)
    ```yaml
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: my-storage-class                # -**- not just a string here - its the name of an object
    provisioner: example.com/nfs            # what plugin   is used for provisioning PV
    parameters:                             # provisioner   specific
      path: /path/to/nfs
      server: nfs-server.example.com
    reclaimPolicy: Delete                   # delete pv and     storage when pvc deleted (default = Retain)
    volumeBindingMode: Immediate
    ```

### Apply
#### For Static Provisioning:
`kubectl apply -f my-volume.yaml `       -  PV 
`kubectl apply -f my-claim.yaml `        -  PVC to bind to PV
`kubectl apply -f my-pod.yaml `          -  Pod using PVC

#### For Dynamic Provisioning:
`kubectl apply -f my-storage-class.yaml`  -  StorageClass 
`kubectl apply -f my-claim.yaml `         -  PVC (triggers PV creation)
`kubectl apply -f my-pod.yaml `           -  Pod using PVC

##### Verify:
`kubectl get pv`                        - persistentVolumes
`kubectl get pvc`                        - persistentVolumeClaims
`kubectl get pods`                        - pod (status)
`kubectl get sc`                          - storageClasses


