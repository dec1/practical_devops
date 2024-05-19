### SecurityContext
- Defines [privilege and access control settings](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-capabilities-for-a-container) for a **Pod or Container**
    - eg uid,gid to run init process as, capabilities, gid of mounted filessystems

#####
- can be applied to:
    #####
    - (i) **whole pod** only (ie all containers)
        - `fsGroup`:  the **GID** to assign to any files/dirs in **mounted volumes**  
            - Mounted  volumes are pod wide (shared by containers)

            - _**Overrides**_ the default behaviour (which is to take primary _group id of user_ - which still happens in ephemeral file system of container)

            - _Note_: logically this might be equally well be applied to an individual container too but, limiting its application to pod as a whole, is a design choice of kubernetes
        
    #####
    - (ii) **single container** 
        - `capabilities` - see egs below
        - `allowPrivilegeEscalation` - child process in a container can gain more privileges than its parent (which means ultimately more than init process of container)
        - `privileged`  - containers have much access to host
        
    ####
    - (iii) either **pod or container** (container settings override any set on pod)
        - `runAsUser `:  **UID** to run the container process as. Overrides any `USER` in dockerfile
        - `runAsGroup`: **GID** .... 
        - `runAsNonRoot`: prevents pod running if USER (or runAsUser) is root

        
    
---
- **pod.yaml**    
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: p
spec:
  #--------------- pod as whole 
  securityContext:
    fsGroup: 2000       # files created by user (uid 1000) have in
                        # (mount) /data/test   :     uid 1000, gid 2000 
                        # (ephemeral fs)       :     uid 1000, gid 3000 (since 3000 is prim gid of user)

    # used by any container that does not explicitly override - see below
    runAsUser:  1001    #  by default 0 (root)
    runAsGroup: 3001    #  by default 0 (gid of root)
  #---------------
 
  containers:
  - name: busybox
    image: busybox:1.28
    command: ["sh", "-c", "sleep 1h"]
    
    volumeMounts:
    - name: vol
      mountPath: /data/test    

    #--------------- (i) container specific --------
    securityContext:
      allowPrivilegeEscalation: false   
      privileged: false  
      runAsUser: 1000     # user gets uid=1000 
      runAsGroup: 3000    # ..... primary gid=3000 (and also belongs to 2000) .......

      capabilities:
        add: ["NET_ADMIN", "SYS_TIME"]   
    #-----------------------------------------------

  volumes:
  - name: vol
    emptyDir: {}
```