### High-Availability (HA) Clusters with kubeadm

The official Kubernetes documentation provides a comprehensive guide on setting up HA clusters with kubeadm. You can find the detailed instructions here:

[Creating Highly Available clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/)

### Key Steps for Setting Up Multiple Control Plane Nodes

#### 1. Set Up the First Control Plane Node

1. Initialize the first control plane node:

    ```sh
    sudo kubeadm init --control-plane-endpoint "<LOAD_BALANCER_DNS>:<LOAD_BALANCER_PORT>" --upload-certs
    ```

    - Replace `<LOAD_BALANCER_DNS>` and `<LOAD_BALANCER_PORT>` with the address and port of your load balancer.

#####
2. Set up `kubectl` for the admin user:

    ```sh
    mkdir -p $HOME/.kube
    sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
    ```
#####
3. Install a pod network add-on, e.g., Calico:

    ```sh
    kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
    ```

4. Save the join command with the certificate key:

    ```sh
    kubeadm token create --print-join-command --certificate-key $(kubeadm init phase upload-certs --upload-certs)
    ```

#### 2. Set Up Additional Control Plane Nodes

1. On each additional control plane node, run the join command saved from the first control plane node:

    ```sh
    sudo kubeadm join <LOAD_BALANCER_DNS>:<LOAD_BALANCER_PORT> --token <TOKEN> \
    --discovery-token-ca-cert-hash sha256:<HASH> --control-plane --certificate-key <CERTIFICATE_KEY>
    ```

    - Replace `<LOAD_BALANCER_DNS>`, `<LOAD_BALANCER_PORT>`, `<TOKEN>`, `<HASH>`, and `<CERTIFICATE_KEY>` with the appropriate values.

####
2. Set up `kubectl` for the admin user on each additional control plane node:

    ```sh
    mkdir -p $HOME/.kube
    sudo cp /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
    ```

#### 3. Set Up Worker Nodes

1. On each worker node, run the join command saved from the first control plane node:

    ```sh
    sudo kubeadm join <LOAD_BALANCER_DNS>:<LOAD_BALANCER_PORT> --token <TOKEN> \
    --discovery-token-ca-cert-hash sha256:<HASH>
    ```

    - Replace `<LOAD_BALANCER_DNS>`, `<LOAD_BALANCER_PORT>`, `<TOKEN>`, and `<HASH>` with the appropriate values.

### Load Balancer Configuration

The load balancer is a crucial component for distributing traffic to multiple control plane nodes. You can use a variety of load balancers such as HAProxy, NGINX, or a cloud provider's load balancer service. Ensure the load balancer forwards traffic to the control plane nodes on port 6443.

### Reference Documentation

- [Creating Highly Available clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/)
- [kubeadm init](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/)
- [kubeadm join](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-join/)

By following these steps and referencing the official documentation, you can set up a Kubernetes cluster with multiple control plane nodes for high availability.
