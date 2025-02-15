
### get
Info on resources in current **namespace** (unless overridden with `-n my-ns` or `-A`)
####

- `k` **`get`** `<kind> [instance_name]` [`-w`] `[--show-labels]` `[--sort-by=<jq_path>]` [`-l key[=val]`]  `[( -n <namespace> ) | -A ]`  `[--field-selector field_name=val]`
`[-o wide|yaml|json|jsonpath=<pattern>]`

    #####
    - `<kind>` - eg `pods`
    - `instance_name` eg pod name (returns all pods if omitted)

    ####
    - `--show-labels` - show labels (in dedicated column)
    
    ####
    - `-w` - _watch_ (keep output updated (like linux `watch` command), dont return control)

    #####
    -  **`-l`** with specified (selector) labels
        - multiple separated by commas possible
            - in addition to this equality based selection syntax, a 
            - [set based](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#set-based-requirement) syntax is possible (note: quotes required), eg
                - k get pods `-l 'app in (prod, dev)'`

    #### 
    - `-n`  look only in namespace called `<namespace>`
    -  `-A` look in _all_ namespaces    

    #### 
    - `--field-selector` filter results to only show those where field `field_name` has value `val`
        - eg get only pods nodes with name _controlplane_
        `k get pods -A` `--field-selector spec.nodeName=controlplane`
        
            
            
        
    #####
    - `--sort-by` - sort results age using  [jq or jsonpath](../../tool/json/query/jq.md) value 
        - eg sort results by age:
            --sort-by=`{.metadata.creationTimestamp}` # jsonpath 

            --sort-by=`.metadata.creationTimestamp`   # jq (simpler)


            --sort-by=`.spec.nodeName`


    - `-o`
        - `-o wide`  more detail 

        - `-o yaml`  ~similar to manifest that could have been used to create resource 
            - see also [k edit](../modify/commands/edit.md)

        - `-o json` json output which can optionally be filtered by pipe to [jq](../../tool/json/query/jq.md) 
        - `-o jsonpath=<pattern>` json output unconditionally filtered according to <pattern> see [also](https://kubernetes.io/docs/reference/kubectl/jsonpath/)





---

- #### Examples

    #####
    - `k get` **`pods`** 
        ```yaml
        NAME      READY   STATUS    RESTARTS   AGE
        my-pod    1/1     Running   0          18s
        my-pod2   1/1     Running   0          7s
        ```
    - `k get` **`pods`** `-o wide`
        ```yaml
        NAME      READY   STATUS    RESTARTS   AGE   IP            NODE     NOMINATED NODE   READINESS GATES
        my-pod    1/1     Running   0          35s   192.168.1.6   node01   <none>           <none>
        my-pod2   1/1     Running   0          24s   192.168.1.7   node01   <none>           <none>
        ```

    - `k get` **`pods`** my-pod
        ```yaml
        NAME     READY   STATUS    RESTARTS   AGE
        my-pod   1/1     Running   0          79s
        ```


    - `k get pods` `-A` `-o wide` **`--sort-by`**`=.spec.nodeName`  # sort by node name
        ```yaml
        NAMESPACE            NAME                                      READY   STATUS    RESTARTS        AGE     IP            NODE           NOMINATED NODE   READINESS GATES
        kube-system          calico-kube-controllers-94fb6bc47-rxh7x   1/1     Running   2 (7m24s ago)   7d20h   192.168.0.2   controlplane   <none>           <none>
        kube-system          canal-zl4tq                               2/2     Running   2 (7m24s ago)   7d20h   172.30.1.2    controlplane   <none>           <none>
        kube-system          etcd-controlplane                         1/1     Running   2 (7m24s ago)   7d20h   172.30.1.2    controlplane   <none>           <none>
        kube-system          kube-apiserver-controlplane               1/1     Running   2 (7m24s ago)   7d20h   172.30.1.2    controlplane   <none>           <none>
        kube-system          kube-controller-manager-controlplane      1/1     Running   2 (7m24s ago)   7d20h   172.30.1.2    controlplane   <none>           <none>
        kube-system          kube-proxy-2mfwz                          1/1     Running   2 (7m24s ago)   7d20h   172.30.1.2    controlplane   <none>           <none>
        kube-system          kube-scheduler-controlplane               1/1     Running   2 (7m24s ago)   7d20h   172.30.1.2    controlplane   <none>           <none>
        local-path-storage   local-path-provisioner-6c5cff8948-2x89z   1/1     Running   2 (7m24s ago)   7d20h   192.168.0.3   controlplane   <none>           <none>
        kube-system          canal-phldr                               2/2     Running   2 (7m25s ago)   7d20h   172.30.2.2    node01         <none>           <none>
        kube-system          coredns-57888bfdc7-685jj                  1/1     Running   1 (7m25s ago)   7d20h   192.168.1.2   node01         <none>           <none>
        kube-system          coredns-57888bfdc7-bbwzr                  1/1     Running   1 (7m25s ago)   7d20h   192.168.1.3   node01         <none>           <none>
        kube-system          kube-proxy-z2ps8                          1/1     Running   1 (7m25s ago)   7d20h   172.30.2.2    node01         <none>           <none>
        ```

    - `k get pods -A` **`--field-selector`** `spec.nodeName=controlplane` # only pods on with specific value for field  

        ```yaml
        NAMESPACE            NAME                                      READY   STATUS    RESTARTS      AGE
        kube-system          calico-kube-controllers-94fb6bc47-rxh7x   1/1     Running   2 (13m ago)   7d20h
        kube-system          canal-zl4tq                               2/2     Running   2 (13m ago)   7d20h
        kube-system          etcd-controlplane                         1/1     Running   2 (13m ago)   7d20h
        kube-system          kube-apiserver-controlplane               1/1     Running   2 (13m ago)   7d20h
        kube-system          kube-controller-manager-controlplane      1/1     Running   2 (13m ago)   7d20h
        kube-system          kube-proxy-2mfwz                          1/1     Running   2 (13m ago)   7d20h
        kube-system          kube-scheduler-controlplane               1/1     Running   2 (13m ago)   7d20h
        local-path-storage   local-path-provisioner-6c5cff8948-2x89z   1/1     Running   2 (13m ago)   7d20h
        ```
    ---    
    #####       
    - `k` `get` **`deployments`**
    #####   
    - `k get` **`services`**

    #####
    - `k get` **`nodes`** `-o wide`
        - 2 nodes (1 control, 1 worker)
            ```yaml
            NAME            ROLES           INTERNAL-IP   EXTERNAL-IP   STATUS   VERSION   AGE  OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
            controlplane    control-plane   172.30.1.2    <none>        Ready    v1.29.0   19d  Ubuntu 20.04.5 LTS   5.4.0-131-generic   containerd://1.7.13
            node01          <none>          172.30.2.2    <none>        Ready    v1.29.0   19d  Ubuntu 20.04.5 LTS   5.4.0-131-generic   containerd://1.7.13
            ```


 
    ####
    - `k get` **`events`** `[ | grep "failed liveness probe"]`

        ```yaml
        LAST SEEN           TYPE      REASON                    OBJECT              MESSAGE
        16d                 Normal    Starting                  Node/controlplane   Starting kubelet.
        16d                 Warning   InvalidDiskCapacity       Node/controlplane   invalid capacity 0 on image filesystem
        16d                 Normal    NodeHasSufficientMemory   Node/controlplane   Node controlplane status is now: NodeHasSufficientMemory
        16d                 Normal    NodeHasNoDiskPressure     Node/controlplane   Node controlplane status is now: NodeHasNoDiskPressure
        16d                 Normal    NodeHasSufficientPID      Node/controlplane   Node controlplane status is now: NodeHasSufficientPID
        16d                 Normal    NodeAllocatableEnforced   Node/controlplane   Updated Node Allocatable limit across pods
        16d                 Normal    RegisteredNode            Node/controlplane   Node controlplane event: Registered Node controlplane in Controller
        16d                 Normal    Starting                  Node/controlplane   
        16d                 Normal    NodeReady                 Node/controlplane   Node controlplane status is now: NodeReady
        ....
        ```
    ###

     - `k get` **`endpoints`**
        list all (internal) pod ip addresses and ports
        <none> indicates mismatch between label selectors in service and deployment (manifest)      
        ```python
        NAME         ENDPOINTS         AGE
        kubernetes   172.30.1.2:6443   16d    # api-server
        ```

    ###
    - `k get` **`namespaces`**
        ```yaml
        NAME                 STATUS   AGE
        default              Active   25d
        kube-node-lease      Active   25d
        kube-public          Active   25d
        kube-system          Active   25d
        local-path-storage   Active   25d
        ```
    ###
    - `k get` **`all`** 
        - get most common resources of all kinds (pods, services, deployments...) in namespace
        - note the _extra prefix_ **`<kind../...>`** eg `<pod/...>`, `<service/...>` compared to when you specify kind as parameter  to get command
        - _Deployments_, _ReplicaSets_, _StatefulSets_, and _DaemonSets_ belong to the **_apps_** API group, which is why you see `deployment`**`.apps`** below.  _Pods_, _Services_ etc belong to the **_core_** API group (which doesn't have an explicit name)
        ```yaml
        NAME          READY   STATUS    RESTARTS   AGE
        pod/my-pod    1/1     Running   0          2m23s
        pod/my-pod2   1/1     Running   0          2m12s

        NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
        service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   25d

        NAME                     READY   UP-TO-DATE   AVAILABLE   AGE
        deployment.apps/my-dep   0/3     3            0           5s
        ```
    ###
    - `k get` **`all`** `-n kube-system`
        ```yaml
        NAME                                          READY   STATUS    RESTARTS      AGE
        pod/calico-kube-controllers-94fb6bc47-4wx95   1/1     Running   2 (91m ago)   25d
        pod/canal-mfc56                               2/2     Running   2 (91m ago)   25d
        pod/canal-zstf2                               2/2     Running   2 (91m ago)   25d
        pod/coredns-57888bfdc7-6sqfr                  1/1     Running   1 (91m ago)   25d
        pod/coredns-57888bfdc7-jnrx9                  1/1     Running   1 (91m ago)   25d
        pod/etcd-controlplane                         1/1     Running   2 (91m ago)   25d
        pod/kube-apiserver-controlplane               1/1     Running   2 (91m ago)   25d
        pod/kube-controller-manager-controlplane      1/1     Running   2 (91m ago)   25d
        pod/kube-proxy-sqc72                          1/1     Running   2 (91m ago)   25d
        pod/kube-proxy-xknck                          1/1     Running   1 (91m ago)   25d
        pod/kube-scheduler-controlplane               1/1     Running   2 (91m ago)   25d

        NAME               TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
        service/kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   25d

        NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
        daemonset.apps/canal        2         2         2       2            2           kubernetes.io/os=linux   25d
        daemonset.apps/kube-proxy   2         2         2       2            2           kubernetes.io/os=linux   25d

        NAME                                      READY   UP-TO-DATE   AVAILABLE   AGE
        deployment.apps/calico-kube-controllers   1/1     1            1           25d
        deployment.apps/coredns                   2/2     2            2           25d

        NAME                                                DESIRED   CURRENT   READY   AGE
        replicaset.apps/calico-kube-controllers-94fb6bc47   1         1         1       25d
        replicaset.apps/coredns-57888bfdc7                  2         2         2       25d
        replicaset.apps/coredns-6f6b679f8f                  0         0         0       25d
        ```

