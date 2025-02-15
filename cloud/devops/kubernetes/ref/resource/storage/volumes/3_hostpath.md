
#### 3) HostPath

- Directly maps a file or directory from the host node's filesystem into a pod,
- persists beyond the pod's lifecycle but lacks  management and abstraction features of persistent volumes.

###
- **my-host-path.yaml**
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: hostpath-demo
    spec:
    
      volumes:
      - name: host-etc-hostname
        hostPath:
          path: /etc/hostname
          type: File

      containers:
      - name: test-container
        image: nginx

        volumeMounts:
        - name: host-etc-hostname
          mountPath: /host/etc/hostname
          readOnly: true
          

    ```