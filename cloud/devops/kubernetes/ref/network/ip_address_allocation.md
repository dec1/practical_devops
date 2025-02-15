#### IP Address (Allocation)


- #### Nodes
    Node IP addresses are assigned by the underlying infrastructure or operating system network configuration. For example, in a cloud environment, nodes typically receive their IP addresses via DHCP or from a static configuration provided by the cloud provider. These IPs are **outside the control of Kubernetes** itself.


----

During cluster setup (eg with [with kubeadm](../admin/cluster_setup/cluster_setup_single_control.md)), the admin specifies allowed _(CDIR)_ **IP address ranges** for pods and services


- **`kubeadm`** `init` 
    **`--pod-network-cidr`** `192.168.0.0/16`   # ip range for pods
    **`--service-cidr`** `10.96.0.0/12`         # ip range for services


- #### Pods
  The [Container Network Interface (CNI)](../general/architecture/components/pods/workload/system/cni.md)  assigns each new pod an IP address from pod range.

- #### Services

    The service range gets persisted (re_named) in both 
     - `/etc/kubernetes/manifests/`**`kube-apiserver.yaml`** and **`kube-controller-manager.yaml`** as the field
     _`--service-cluster-ip-range`_

    ####
    The **API Server**’s allocates each new service an IP address from this range

