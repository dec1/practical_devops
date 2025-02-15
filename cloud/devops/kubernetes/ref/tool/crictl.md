### crictl

- command-line tool (part of kubernetes) for interacting with and debugging CRI-compatible [container runtimes](../../../../../cloud/devops/docker/tech/tools.md) eg containerd (docker), CRI-O (podman).

It provides a unified way to manage container runtimes that support the CRI, such as containerd and CRI-O, rather than interacting with Docker, Podman, or other specific container tools directly. Many of the commands (`ps`, `run`, `images`, `exec`, `inspect`, `logs`) correspond directly to commands in the native cli of the runtimes, like `docker`

[see](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/) and [github](https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md)

 - `controlplane>` `crictl ps`  
 list  containers running 
    ```yaml
    CONTAINER           IMAGE               CREATED             STATE               NAME                      ATTEMPT             POD ID              POD
    0a24fa2304552       75392e3500e36       3 minutes ago       Running             calico-node               1                   a31fce825e5ce       canal-zl4tq
    6793af3b106f8       ad83b2ca7b09e       3 minutes ago       Running             kube-proxy                2                   27608aec2cc82       kube-proxy-2mfwz
    005d82cfafc5d       045733566833c       3 minutes ago       Running             kube-controller-manager   2                   8a677c1d659e0       kube-controller-manager-controlplane
    4e90cf7a30061       2e96e5913fc06       3 minutes ago       Running             etcd                      2                   37408d4267db4       etcd-controlplane
    3304112146608       1766f54c897f0       3 minutes ago       Running             kube-scheduler            2                   1950c7ae39121       kube-scheduler-controlplane
    0a844734bbe00       604f5db92eaa8       3 minutes ago       Running             kube-apiserver            2                   debf8742ffed2       kube-apiserver-controlplane
    ```
   
-  **`watch` `crictl ps`**
    watch (follow live) containers including

You **ssh** to a **cluster node** to use it:


 - `ssh cluster2-node1`

    ###
    - `crictl ps | grep kube-proxy`
        find the container of the kube-proxy pod 

        ```yaml
        1e020b43c4423   36c4ebbc9d979   About an hour ago   Running   kube-proxy     ...
        ```

    ###
    - `crictl rm 1e020b43c4423`
        delete it
       
    ####
    - `crictl ps | grep kube-proxy`
        a replacement container gets automatically created
        ```yaml
        0ae4245707910   36c4ebbc9d979   17 seconds ago      Running   kube-proxy     ...   
        ```

   