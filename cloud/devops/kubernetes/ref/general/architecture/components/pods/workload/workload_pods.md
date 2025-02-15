### Workload Pods
Workloads are always [pods](../../../../../resource/pod/pod.md) (or groups of pods through higher-level controllers like ([deployments](../../../../../resource/deploy/deploy.md), [stateful sets](../../../../../resource/deploy//stateful_set.md), [daemon sets](../../../../../resource/deploy/daemon_set.md), [jobs](../../../../../resource/job/job.md), and [cron jobs](../../../../../resource/job/job_cron.md)) that are managed by the **[controller manager](../static/system/scheduler.md)**, which delegates to the **[scheduler](../static/system/scheduler.md)**, which delegates to kubelet instances on the nodes the scheduler chooses.

All pods are either workload or [static](../static/static_pods.md) pods



