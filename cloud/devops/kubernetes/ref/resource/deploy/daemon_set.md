### [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)

Ensures that 
- _**all (or some)** Nodes run a copy of a **Pod**_

- it dynamically creates/removes the pods in question when nodes are added/removed to/from cluster

- Deleting a DaemonSet will clean up the Pods it created.