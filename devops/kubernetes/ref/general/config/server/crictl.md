### crictl

- command-line tool (part of kubernetes) for interacting with and debugging CRI-compatible container runtimes (eg containerd, CRI-O)

[see](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/)

 - `crictl ps` 
    list  containers runnig (inc `api-server`)
-  `watch` `crictl ps`
    watch (follow live) containers including

