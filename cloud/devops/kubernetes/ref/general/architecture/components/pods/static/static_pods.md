### Static Pods

Static [pods](../../../../../resource/pod/pod.md) are started unconditionally by a particular [kubelet](../../linux_service/kubelet.md) instance 

###
- #### Configuration

    - `find` **`/etc/kubernetes/manifests/`**

        
    - ### System Static Pods 
        identical configuration  on each and every control plane node

        - `/etc/kubernetes/manifests/` **`kube-apiserver.yaml`**
            `/etc/kubernetes/manifests/` **`kube-controller-manager.yaml`**
            `/etc/kubernetes/manifests/` **`kube-scheduler.yaml`**
            `/etc/kubernetes/manifests/` **`etcd.yaml`**
            
        ###
        - **Api Server**        
            - exposes the Kubernetes (Rest) API
            -  IP address configured in `controlPlaneEndpoint` of file `kubeadm-init.yaml`
            - only via Api Server can communication take place between: 
                - **outside** <-> **inside** cluster (except app specific - see **kube-proxy**)
                - control <-> worker planes (**kubelet**)

        ####
        - **Controller Manager**
            - watches the state of cluster  and decides
            - **what** needs to be created (so actual state matches desired state, eg num of replicas) 
            - has sub controllers (deployment controller ....) it delegates to  

        ###
        - **Scheduler**
            - **where** (which node) to put new pods that controller manager requires.
                - delegates to kubelet on node in question.

        ###
        - **Etcd**
            - key-value data **persistance**.
            - used by kubernetes itself (which doesnt write to files) for persistance (cluster state, pod definitions, service configurations, secrets, etc.) 
            - not directly accessible by kubectl (admins)  or containerized applications for storing their data. 
            - `etcdctl` can be used by admins to read/write directly (bypassing api server - not recommended) for troubleshooting or diaster recovery
            - regular backup important
        
- ### Non-System Static Pods
    - Simply putting a custom resource manifiest (yaml) file into `/etc/kubernetes/manifests/` will cause the automatic creation of a (static) pod from it. eg:
        - `k` **`run` `my-static-pod`** `--image=nginx:1.16-alpine -o yaml --dry-run=client >`  **`/etc/kubernetes/manifests/my-static-pod.yaml`**
        - `k get pod -A `
            ```yaml
            NAMESPACE            NAME                                       READY   STATUS              RESTARTS        AGE
            default              my-static-pod-controlplane                 0/1     ContainerCreating   0 
            3s 
            ```   