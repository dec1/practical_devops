## Metrics Server


Collects  **CPU** and **memory** from _kubelet_ on each node, and is used by

- [k top](../../../../../query/top.md) 
- Horizontal Pod Autoscaler (HPA) for scaling decisions
- Kubernetes Dashboard
- custom monitoring solutions


The  metrics are collected approx every 15 seconds, and stored in _memory_ (not persisted to disk)



---
##### Installation
If the Metrics Server is not already installed (as is the case with [Killercoda](https://killercoda.com))  you can install it via:

- **install**
    - `kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml`
        deploy metrics server

#####        
- **patch**
    Some clusters (like Killercoda) use self-signed certificates, which cause TLS errors. Fix this by editing the Metrics Server deployment, using [patch](../../../../../modify/commands/patch.md) 
    
    - `kubectl -n kube-system` **`patch`** `deploy metrics-server --type='json' -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'`

        ###
        - this is equivalent to manually:
            - `kubectl -n kube-system edit deploy metrics-server`

                - Add this flag to the Metrics Server container args (under spec.template.spec.containers.args):


                    `- --kubelet-insecure-tls`
                Save and exit. The deployment will automatically restart.

###
- **verify**

    `kubectl -n kube-system get pods | grep metrics-server`
    ```yaml
    metrics-server-587b667b55-rnx9f           1/1     Running   0             10m
    ```
###
- use 
    - wait 1 min or so for metrics to populate, then run `k top pod` and `k top node`, as described above