### Services

Provide a single virtual ip address (and name) for a group of matching (replica) pods (or nodes), with load balancing (_round-robin_ by default).


- ### [ClusterIP](types/cluster_ip.md)
    Most basic service type which all others extend or encapsulate. Accessible only from inside the cluster.
    
- ### [NodePort](types/node_port.md)
    Makes a ClusterIp accessible from outside the cluster, by exposing a static port (`node port`) on each node of teh cluster (which forwards messages to the internal clusterIP service)

- ### [Ingress](types/ingress/ingress.md)
    Extends ClusterIp Service to provide L7 routing to other (ClusterIp) services, typically via an Ingress Controllers on the pods implementing the ingress service.

---
- ### [Load Balancer](types/load_balancer.md) 
    Provisions an externally accessible cloud load balancer that forwards traffic to nodes implementing a NodePort service in the cluster, automatically updating its target groups as nodes join/leave the cluster. 

- ### [Service Mesh](types/service_mesh.md) 
    Adds advanced traffic management, security (mTLS), and observability to Kubernetes  services (usually ClusterIP, but can be used with others).  It achieves this by deploying a sidecar proxy (additional container) in each  Pod and a control plane component to manage these proxies. 




