### kube-apiserver

- `/etc/kubernetes/manifests/kube-apiserver.yaml`

    #####
    - configuration for the Kubernetes API server
        - eg enabled/disabled [Admission Controller Plugins](../../../security/control.md):

            ```yaml
            ....
            - --enable-admission-plugins=NodeRestriction,LimitRanger,Priority,MutatingAdmissionWebhook
            - --disable-admission-plugins=NamespaceLifecycle
            ....
            ```

    ####
    - located on ***control plane node*** (not where kubectl client runs)
    ####
    - The kubelet on each **control plane** node    
        - **watches** the `/etc/kubernetes/manifests/` directory and 
        - automatically adapts to changes made there - can seem  affected containers restart [with](./crictl.md)  
            - `watch crictl ps`

