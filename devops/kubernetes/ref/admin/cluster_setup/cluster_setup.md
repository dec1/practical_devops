## Setup Cluster 
- ####  Simple
    - [Single Control Plane node](./cluster_setup_single_control.md)
- #### High Availability (HA)
    - [Multiple Control Plane nodes](./cluster_setup_single_control.md)

Note: 
- One of the significant advantages of using a **managed Kubernetes** service from a **cloud provider** (like Google Kubernetes Engine, Amazon EKS, or Azure AKS) is that it simplifies the setup and management of HA clusters. The cloud provider handles the complexity of setting up and managing multiple control plane nodes, load balancers, and etcd clusters, allowing you to focus on deploying and managing your applications