


## CoreDNS 

**Services**  in Kubernetes all have an [FQDN](../../../../../network/pub/web/url.md):


**`<service-name>`**.**`<service-namespace>`** **`[.svc.cluster.local]`** `[/path]`

thanks to CoreDNS (itself also a service). 




- pods [usually](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#namespaces-of-services) have their 
    - `/etc/resolv.conf` configured so 
        - `svc.cluster.local` can be dropped  
        - `service-namespace` can be dropped, if its the same as the pods namespace

        when they are accessing a service
###
-    pods themselves (unlike services),  do *not have FQDN*s.

(see also: [debug service](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service) and [port-forward](from_local/port_forward.md))

---
#### IP Address Resolution
**Manifests**
When you use service FQDN inside a manifest, they are resolved to an IP address dynamically at run time by CoreDns

**Kubectl**
When you use kubectl, you just use the **names** of resources like _services_ (or _pods_), beacuse kubectl communicates with **API Server**, which looks up ip address of services or pods in **etcd**.  (Only system components like API Server can access etcd). 

---

#### Api Server
- **`Api Server`** itself is (also) a kubernetes service is _called_ _**`kubernetes`**_ and exists in the `default` namespace, so its internally accessible via url :
`https://` **`kubernetes`** **`.default`** `.svc.cluster.local` **`/api/[/<sub_path>]`**
    - **`kubernetes`** name of api server service
    - **`.default`** namespace api server service exists in
    - **`/api`** top level path (all paths start with this)
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
    
    - eg: 
        - exec into pod
        `k exec my-pod -it -- /bin/sh`
        ####
        - curl api server (using auth token)
        `curl -k -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)"` **`https://kubernetes.default.svc.cluster.local/api/`**
            ```yaml
            {
            "kind": "APIVersions",
            "versions": [
                "v1"
            ],
            "serverAddressByClientCIDRs": [
                {
                "clientCIDR": "0.0.0.0/0",
                "serverAddress": "172.30.1.2:6443"
                }
            ]
            }
            ```


