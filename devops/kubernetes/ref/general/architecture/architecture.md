## Architecture

###  Cluster

A single independent Kuberntes "installation"

- [Overview](./architecture_overview.md)
- [Components](./archittecture_details.md)


_Note_: Typically all control nodes are identical, and all worker nodes are identical

---

#### Namespaces

- Allow sharing of single cluster by [dividing](../config/namespace.md) it into multiple (logically separated) virtual clusters.

#### Cluster Federation
- Note: While there are ways to join multiple clusters, this functionality is not part of Kubernetes itself, but added on top (eg Openshift Federation)


