
### Simple Cluster [setup with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)

Simple ie Single Control Plane Node (ie not HA)


#### 1) install Kubelet, Kubeadm (optionally Kubectl)
- **Kubelet**, **Kubeadm** must be installed (in version matching target kubernetes version - also after [upgrade](../cluster_upgrade/cluster_upgrade.md)) on all nodes
    - `apt-get install` **`kubelet`**`=1.30.2-1.1,` **`kubeadm`**`=1.30.2-1.1`
    - `systemctl daemon-reload`
    - `service kubelet restart`
  

- **Kubectl** only necessary on o you want to run (admin) command from
     - `apt-get install` **`kubectl`**`=1.30.2-1.1`


#### 2) Initialize a Control Plane Node

On the control plane node:

#####
- `kubeadm` **`init`** 
        &nbsp;&nbsp;&nbsp; [**`--kubernetes-version`** `=1.30.0`] 
        &nbsp;&nbsp;&nbsp; [**`--pod-network-cidr`** `192.168.0.0/16`]
    - &nbsp;&nbsp;&nbsp; This option specifies the CIDR block for the pod network. This is the pool of IP addresses from which pod IP addresses will be assigned. Different pod network add-ons (eg Calico) may have different requirements for this value.

    &nbsp;&nbsp;&nbsp; [**`--ignore-preflight-errors`** `=NumCPU`]
        
    #####
    - More [options](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#options)

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
#### 4) Join Worker Node to Cluster

You want to add a node with DNS `node-summer` to the cluster as a worker.

#####
- SSH onto the node
    - `ssh node-summer`

- Install Kubelet and Kubeadm 
    <details>
    <summary>as above </summary>

    - **Kubelet**, **Kubeadm** must be installed (in version matching target kubernetes version - also after [upgrade](../cluster_upgrade/cluster_upgrade.md)) on all nodes
        - `apt-get install` **`kubelet`**`=1.30.2-1.1,` **`kubeadm`**`=1.30.2-1.1`
        - `systemctl daemon-reload`
        - `service kubelet restart`
    </detalis>
         
#####
- Run the command that was output by kubeadm init above

    - `kubeadm` **`join`** `172.30.1.2:6443` **`--token`** `rikaqz.qf5s8mgk6jxjm22k` \
    **`--discovery-token-ca-cert-hash`** `sha256:b7dbee498b70886b8aa2f16ddf50262c78007c2ef1e49d30ff5c7bf0f3a00b17`
    
    ####
    - If you don't have the command anymore, you can (see doc):
        #####
        - **`kubeadm token create --print-join-command`**

            ```yaml
            kubeadm join 172.30.1.2:6443 --token rikaqz.qf5s8mgk6jxjm22k --discovery-token-ca-cert-hash sha256:b7dbee498b70886b8aa2f16ddf50262c78007c2ef1e49d30ff5c7bf0f3a00b17
            ```
            <details>
            <summary>Additionally (get/create just tokens)</summary>

            - as [documented](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#join-nodes)
                ####
                - Get an existing **token** from
                    - `kubeadm token` **`list`**

                ####
                - If none are available (expire after 24 hrs), you can create a new one with
                    - `kubeadm token` ***`create`***

                ####
                - Get an existing **discovery token CA cert hash** from (see doc):

                    - `openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'`
            </details>
            


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
