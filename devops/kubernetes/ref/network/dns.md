


## CoreDNS 

Kubernetes registers every Service by its name with the help of its DNS service named CoreDNS. 

So you can access **service** by **name** from
1. **Pod** in
    - same namespace:
        - `my_service`
    ###    
    - different namespace: 
        - **`my_service`** **`.my_ns`** **`[.svc.cluster.local]`** 
            - the pod [usually](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#namespaces-of-services) has its 
            - `/etc/resolv.conf` configured so 
            - `svc.cluster.local` can be dropped 

   #### Api Server
   - **`Api Server`** service is called `kubernetes` and exists in the `default` namespace, so its internally accessible via url :
  `https://` **`kubernetes`** **`.default`** `.svc.cluster.local` **`/api/` `<sub_path>`**
        - **`kubernetes`** name of api server service
        - **`.default`** namespace api server service exists in
        - **`api`** top level path (all paths start with this)
        - **`<sub_path>`** possible values can be found via:
            - `k` **`api-versions`**
                ```yaml
                v1                                  # most common
                apps/v1

                admissionregistration.k8s.io/v1     # less common
                apiextensions.k8s.io/v1
                apiregistration.k8s.io/v1
                authentication.k8s.io/v1
                authorization.k8s.io/v1
                autoscaling/v1
                autoscaling/v2
                batch/v1
                certificates.k8s.io/v1
                coordination.k8s.io/v1
                crd.projectcalico.org/v1
                discovery.k8s.io/v1
                events.k8s.io/v1
                flowcontrol.apiserver.k8s.io/v1
                flowcontrol.apiserver.k8s.io/v1beta3
                networking.k8s.io/v1
                node.k8s.io/v1
                policy/v1
                rbac.authorization.k8s.io/v1
                scheduling.k8s.io/v1
                storage.k8s.io/v1
                ```


