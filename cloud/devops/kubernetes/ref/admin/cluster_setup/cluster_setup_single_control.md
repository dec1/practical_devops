
### Simple Cluster [setup with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)

Simple ie Single Control Plane Node (ie not HA)


#### 1) install Kubelet, Kubeadm (optionally Kubectl)
- **Kubelet**, **Kubeadm** must be installed (in version matching target kubernetes version - also after [upgrade](../cluster_upgrade/cluster_upgrade.md)) on all nodes
    - `apt-get install` **`kubelet`**`=1.30.2-1.1,` **`kubeadm`**`=1.30.2-1.1`
    - `systemctl daemon-reload`
    - `systemctl restart kubelet` (see [service managemet](../../../../../../os/linux/startup/service_man.md)
  

- **Kubectl** only necessary on node you want to run (admin) command from
     - `apt-get install` **`kubectl`**`=1.30.2-1.1`


#### 2) *Init*(ialize) a Control Plane Node

On the control plane node:

#####
- `kubeadm` **`init`** 
        &nbsp;&nbsp;&nbsp; [**`--kubernetes-version`**`=1.30.0`] 
        &nbsp;&nbsp;&nbsp; [**`--pod-network-cidr`**`=192.168.0.0/16`]# ip range for **pods**
        &nbsp;&nbsp;&nbsp; [**`--service-cidr`**`=10.96.0.0/12`]  # ip range for (cluster ip) **services**
    - &nbsp;&nbsp;&nbsp; These are 2 pool of IP addresses from which pod and service [IP addresses will be assigned](../../network/ip_address_allocation.md). Different pod network add-ons (eg Calico) may have different requirements for this value.

    &nbsp;&nbsp;&nbsp; [**`--ignore-preflight-errors`** `=NumCPU`]

    ####
    
    - At this point
        - (public) **certs** and (private) **keys** are automatically generated and saved to `/etc/kubernetes/pki`, and a
        - join **token** is output (see below) and saved to `etcd`

            #####
            - more details [here](../../security/api_server/pki.md)
    #####


    -   <details>
        <summary>output</summary>

        ```yaml
        Your Kubernetes control-plane has initialized successfully!

        To start using your cluster, you need to run the following as a regular user:

            mkdir -p $HOME/.kube
            sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
            sudo chown $(id -u):$(id -g) $HOME/.kube/config

        Alternatively, if you are the root user, you can run:

            export KUBECONFIG=/etc/kubernetes/admin.conf

        You should now deploy a pod network to the cluster.
        Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
        https://kubernetes.io/docs/concepts/cluster-administration/addons/

        Then you can join any number of worker nodes by running the following on each as root:

            kubeadm join 172.30.1.2:6443 --token rikaqz.qf5s8mgk6jxjm22k \
                    --discovery-token-ca-cert-hash sha256:b7dbee498b70886b8aa2f16ddf50262c78007c2ef1e49d30ff5c7bf0f3a00b17 
        ```
        </details>
    ######
    - Further options [here](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#options)

####
- Ensure ***kubectl*** can easily find **config** file for specific (non-root) user(on control plane). 
This file is used by kubectl to interact with the Kubernetes cluster. (optional)

    #####
    - `mkdir -p $HOME/.kube`
    - `sudo cp` **`/etc/kubernetes/admin.conf`** **`$HOME/.kube/config`**
    - `sudo chown $(id -u):$(id -g) $HOME/.kube/config`
    
    #####
    - to make kubectl usable on remote machine you need to copy config file to there:
        -  On the control plane node
             - `scp` **`/etc/kubernetes/admin.conf`** `user@remote-machine:`**`~/.kube/config`**

##
#### 3) Install a pod network add-on (e.g. Calico)

`kubectl apply -f https://docs.projectcalico.org/manifests/`**`calico.yaml`**

##
#### 4) *Join* Worker Node to Cluster

You want to add a node with DNS `node-summer` to the cluster as a worker.

#####
- SSH onto the node
    - `ssh node-summer`

- Install **Kubelet** and **Kubeadm** 
    <details>
    <summary>as above </summary>

    - Kubelet, Kubeadm must be installed (in version matching target kubernetes version - also after [upgrade](../cluster_upgrade/cluster_upgrade.md)) on all nodes
        - `apt-get install` **`kubelet`**`=1.30.2-1.1,` **`kubeadm`**`=1.30.2-1.1`
        - `systemctl daemon-reload`
        - `service kubelet restart`
    </detalis>
         
#####
- Run the command that was output by kubeadm init above

    - `kubeadm` **`join`** `172.30.1.2:6443` **`--token`** `rikaqz.qf5s8mgk6jxjm22k` \
    **`--discovery-token-ca-cert-hash`** `sha256:b7dbee498b70886b8aa2f16ddf50262c78007c2ef1e49d30ff5c7bf0f3a00b17`
    - see also [pki](../../security/api_server/pki.md)
    ####
    - If you don't have the command anymore, you can (see doc):
        #####
        - **`kubeadm token create --print-join-command`**

            ```yaml
            kubeadm join 172.30.1.2:6443 --token rikaqz.qf5s8mgk6jxjm22k --discovery-token-ca-cert-hash sha256:b7dbee498b70886b8aa2f16ddf50262c78007c2ef1e49d30ff5c7bf0f3a00b17
           ```


#####
- Return to control plane node
    - `exit`

#####
- Verify 2 nodes as expected
    - `k` **`get nodes`**
    
        ```yaml
        controlplane   Ready    control-plane   38m   v1.30.0
        node-summer    Ready    <none>          17s   v1.30.0
        ```
