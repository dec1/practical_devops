
### Persistent Volumes

-  Outlives pod (like hostpath, but is more flexible)

- **PersistentVolumeClaim** (storage requirement), specified by pod, for which Kubernetes finds  a suitable:

    ###
    - **PersistentVolume** (_static_ provisioning), which it mounts into a Pod at given specified mount path. 
    ###
    or
    ###
    - **StorageClass** (_dynamic_ provisioning) - Which in turn for creates PersistentVolumes (PVs). It abstracts the details of how storage is provided. Cluster admin creates these freely. Used for dynamic provisioning (see below)

#### Volume Provisioning
- **Static** 
    - You (manually) create volume object (using manifests). These may contain a storageClass**Name** - if so they are used to match volumes that have ~ storageClass**Name**. ***No** StorageClass **Objects** created*

- **Dynamic** 
    -  You do ***not** create volumes directly*. Existing StorageClass object is matched to the claim and this automatically creates a PV. 


#### Matching (Binding)
 Kubernetes first tries **static** provisioning first, then if unsuccessful dynamic matching on
- **Access mode**s (see below)  
- **Selector** - in claim to match **labels** in Volume
-  **storageClassName** 
    - **static**: should match in both pvc and pv 
        - `my-storage-class.yaml` **not** used  (and no object thereof created)
        - (one would think just using labels might be more appropriate here)
    - **dynamic**: storageclass **object** (`my-storage-class.yaml` ) with matching name should exist
        - `my-volume.yaml` **not** used  (and no object thereof created)
    


###
----

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
            claimName: pvc          #  see my-claim.yaml
                                    #       in turn (optionally) specifies storageClass

      containers:
      - image: nginx
        name: nginx

        volumeMounts:                      # volumeMount (container)
          - mountPath: "/var/log/nginx"
            name: logs-volume
    ```

- **my-claim.yaml**
    ```yaml
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: pvc
    spec:
                                            # Kubernetes tries to find volumes that matches:
      accessModes:                          # 1) access --required-- by pod (Kubernetes     independently picks a suitable volume))
        - ReadWriteOnce

      resources:
        requests:
          storage: 2Gi                      # 2) size --required

    # Selector to match labels              # 3) label selector
      selector:
        matchLabels:
        my-key: my-val


      storageClassName: my-storage-class    # 4)  "my-storage-class.yaml"  
    ```

- **my-volume.yaml**

    ```yaml
    kind: PersistentVolume
    apiVersion: v1
    metadata:
      name: pv
      labels:
        my-key: my-val                      # 3) satisfied
    spec:

      capacity:
        storage: 5Gi        # 5 Gb          # 2) satisfied 

    
      accessModes:          # access --supported-- by volume     # 1) satisfied 

        - ReadWriteOnce     # single node (multiple pods theron)  - "once"  -> "one"
        - ReadOnlyMany      # multiple nodes (can read)

      # - ReadWriteMany       # multiple nodes (can write )
      # - ReadWriteOncePod    # single pod (v1.29+)

      storageClassName: my-storage-class  # "my-storage-class.yaml"   # 4) satisfied 
    # -----
    # 1) 
        nfs:
            path: /path/to/nfs  # NFS server share path
            server: nfs-server.example.com  # NFS server IP or hostname
        
    # -----
    # 2)
      # hostPath: # alternative to nfs
      #     path: /var/logs

    ```



- **my-storage-class.yaml**
    ```yaml
    apiVersion: storage.k8s.io/v1
    Kind: StorageClass
    metadata:
        name: my-storage-class
    provisioner: example.com/nfs    # what plugin is used for provisioning PV
    parameters:                     # provisioner specific
        path: /path/to/nfs
        server: nfs-server.example.com
    reclaimPolicy: Delete           # (|Retain) default - delete pv and storage when pvc deleted ()
    volumeBindingMode: Immediate
    ```



