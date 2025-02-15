### Scheduler

The scheduler decides **which node** each newly created ([workload](../../workload/workload_pods.md)) pod should run on, based on resource requirements, constraints, and cluster state. Its main action is to set `spec.nodeName` in the Pod spec once it chooses a node. Internally it has complex logic (filtering, scoring, etc.), but the final outcome is that single field update.
Delegates to the [Kublet](../../../linux_service/kubelet.md) on the node in question to actually create the pod there.