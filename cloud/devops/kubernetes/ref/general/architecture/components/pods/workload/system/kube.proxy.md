### Kube-Proxy
- implements  <i class="fa-solid fa-bell-concierge" style='color:green'></i>  _Kubernetes **Services**_, by 


    - creating network rules (using _iptables_, _IPVS_, or other mechanisms) on **each node** to direct traffic to the _correct pods_ backing a service. 
    
    #####
    - each node (kube-proxy) knows how to direct a request for each service. This information is kept up-to-date by watching the Kubernetes API server.
    
    #####
    - performs _load balancing_ (round-robin on each node by default) across the pods of a service.

####
- relies on a functioning [CNI](cni.md) plugin to be able to do its job
    - CNI makes sure pods can talk to each other on the network.   
    - kube-proxy makes sure traffic sent to a service gets to the right pod(s)

#####
- **proxy-mode** 
    - set on [startup](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/), determines how Kube-Proxy works under the covers.  
        - on Linux this can be **iptables** (default) or **ipvs**. 
        - On Windows the only supported value is **kernelspace**


####
- is a kubernetes <i class='fa fa-ghost' style='color:darkred'></i>**`daemon set`** (ie dedicated pod on every node)

    - `k` **`-n kube-system`** `get` **`ds`**
        ```yaml
        NAME         DESIRED   CURRENT   ...   NODE SELECTOR            AGE
        kube-proxy   3         3         ...   kubernetes.io/os=linux   155m
        weave-net    3         3         ...   <none>                   155m
        ```

