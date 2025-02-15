
### [Cluster Upgrade](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)

- `kubeadm` **`upgrade plan`**
Check which versions are available to upgrade to and validate whether your current cluster is upgradeable. 

    ```yaml
    Components that must be upgraded manually after you have upgraded the control plane with 'kubeadm upgrade apply':
    COMPONENT   NODE           CURRENT   TARGET
    kubelet     controlplane   v1.30.0   v1.30.2
    kubelet     node01         v1.30.0   v1.30.2

    .....

    You can now apply the upgrade by executing the following command:

        kubeadm upgrade apply v1.30.2
    ```
    ``` 
    Note: Before you can perform this upgrade, you have to update kubeadm to v1.30.2.
    ```
    
- ### Control Plane 
    - #### 1). Before upgrade
        Need to upgrade **kubeadm** 
        
        #### 
        - get installed kubeadm version (1.30.0)

            - **`apt list --installed`** `| grep kubeadm` 

                ```yaml
                WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
                kubeadm/unknown,now 1.30.0-1.1 amd64 [installed,upgradable to: 1.30.2-1.1]
                ```

            - **`dpkg -l`** `| grep kubeadm` 
                ```yaml
                ii  kubeadm                              1.30.0-1.1                        amd64        Command-line utility for administering a Kubernetes cluster
                ```
        ####
        - get all (installable) kubeadm versions
            - **`apt-cache show`** `kubeadm | grep Version` 
                or
            - **`apt-cache madison`** `kubeadm`

        
                ```yaml
                Version: 1.30.2-1.1
                Version: 1.30.1-1.1
                Version: 1.30.0-1.1
                Version: 1.29.6-1.1
                ........
                ```

        - #### **Install** version
            - the prerequisite **kubeadm** version:
                - **`apt-get install`** `kubeadm=1.30.2-1.1` `[ --allow-change-held-packages]`
                Note: you need the trailing `-1.1`
                - `--allow-change-held-packages`
                    - allows upgrading packages otherwsie fixed via `apt-mark hold` 
                    - alternative: explicitly unmark before upgrade via `apt-mark unhold kubeadm`
                - kubeadm version >= target cluster version
                is documented to be _supported_, but its recommended is to use exactly the same.  

    - #### 2). Upgrade 
        - `kubeadm` **`upgrade`** _**`apply v1.30.2`**_ <------------------- 1st control node -------------
            - This command is for the first control plane node. For other control plane nodes and worker nodes, use `kubeadm upgrade node` (see below).
            ```yaml
            .......
            SUCCESS! Your cluster was upgraded to "v1.30.2". Enjoy!
            ```



    - #### 3). After upgrade
        Need to upgrade **kubectl** and **kubelet** 
        - `apt-get install kubectl=1.30.2-1.1 kubelet=1.30.2-1.1`
        - `systemctl daemon-reload`
            - make sure systemd uses new config (unit files) for kublet, instead of any its cached
        - `systemctl restart kubelet`   

            - verify kublet service
                - `systemctl status kubelet` 
                    ```yaml
                    ....
                    Active: active (running)
                    Main PID: 1654 (kubelet)
                    ```

        ####
        - Verify Upgrade to 1.30.2
            - `k version`
                ```yaml
                Client Version: v1.30.2
                Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
                Server Version: v1.30.2
                ```
- ### Worker (or further Control Plane) Node 
    - SSH onto the node
        - `ssh node01`

    ####
    -  1). Before upgrade 
        - upgrade **kubeadm**  (**same** as above - kubeadm is installed on **all nodes**)
            - `apt-get install kubeadm=1.30.2-1.1`

    - #### 2). Upgrade 
    - #### **Install** same 
         - `kubeadm` **`upgrade`** _**`node`**_  <----------------  all other nodes ------------------------------------
            ```yaml
            ........
            [upgrade] The configuration for this node was successfully updated!
            [upgrade] Now you should go ahead and upgrade the kubelet package using your package manager.
            ```
   
    - #### 3) After upgrade
        Need to upgrade **kubelet** on all nodes
        - `apt-get install kubelet=1.30.2-1.1`
        - `systemctl daemon-reload`
        - `systemctl restart kubelet`    

- ### Verify Upgrade
     - to version 1.30.2
        - `k version`
            ```yaml
            Client Version: v1.30.2
            Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
            Server Version: v1.30.2
            ```

        - `k get nodes`
            ```yaml
            NAME           STATUS   ROLES           AGE   VERSION
            controlplane   Ready    control-plane   1h    v1.30.2
            node01         Ready    <none>          1h    v1.30.2
            ```

- ### Draining Nodes
    the [doc](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/) (see [also](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/)) recommends draining nodes before upgrade and uncordoning (ie undrainig) after

    #####
    - `k` **`drain`** `<node> --ignore-daemonsets`
    #####
    - upgrade as above
    #####
    - `k` **`uncordon`** `<node>`


