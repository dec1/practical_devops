

##### Container Network Interface (CNI)

Kubernetes mandates the use of a CNI plugin to handle networking for pods. The CNI plugin is responsible for allocating IP addresses to pods and handling the network connectivity. It ensures that all pods can communicate with each other and that services can route traffic to these pods, both within a single node and across multiple nodes.

This can be achieved by a direct physical network (appropriately configured) or a **network overlay** (operates on top of and abstracts from the existing physical network)


When using a container runtime like Docker without a container orchestrator like Kubernetes, a simple [bridge network](../../../docker/main/network.md) can be sufficient to allow containers to communicate with each other when they are all running on the same node.

However, when containers are running across multiple nodes in a distributed environment, more advanced networking capabilities are required to enable effective communication between containers. This is where CNI comes in, providing a standardized way to configure and manage container networking across a cluster.

CNI plugins "plug into" the container runtime, not into Kubernetes directly. When Kubernetes schedules a pod to run on a node, it delegates the responsibility for networking to the container runtime, which then uses the CNI plugin to configure the network interfaces and networking for the containers in the pod.


See also [Life of a Packet](https://youtu.be/cB611FtjHcQ?feature=shared)

