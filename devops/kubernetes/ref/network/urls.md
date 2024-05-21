
-  Services

    - [internally](../network/dns.md) - simply by *dns* **name** (or ip address)
        - **`my_svc`** **`[.ns]`** **`[.svc.cluster.local]`**
            - `k run --image=nginx --restart=Never --rm -i tmp` ***`-- curl -L my-app:80`***
                ```yaml
                <h1>Welcome to nginx!</h1>
                ```

                - `svc.cluster.local` -  default **domain name** for services within a Kubernetes cluster
            (defined as part of Kubernetes' DNS specification)  

                    - `cluster.local`: The default cluster domain. (can be customized during Kubernetes cluster setup) 

                    - `svc`: Indicates that the name is a service within the Kubernetes cluster.


    ##
    - client with kubectl ([proxy](../network/service/cluster_ip.md))
        - **`localhost:8001`** **`/api/v1/namespaces/<ns>/services/<svc>:<port>/proxy`**
            - `ns` - namespace in which service is running
            - `svc` - name of service
            - `port` - port service is listening on
            - **`/proxy`** Api server should **forward** to service in question - not return metadata on this service (default behaviour) 
            ####
            - **`k proxy`** `[--port=8001]` `[&]` 
                    - `--port` - default 8001
                    - `&` move to bdg to free terminal for next command (or just use different terminal)

                ```yaml
                Starting to serve on 127.0.0.1:8001
                ```
            ###
            - `curl -L` `localhost:8001/api/v1/namespaces/default/services/my-ser:80/proxy`
            (see **eselbrücke** in `cluster-info` below for remembering format)
                - `-L` follow redirects          


---
- [Api Server](../security/control_access/authentication/service_account/pod.md) 

    - not especially useful directly 
        - you neeed to set up service account/tokens for authorization, and
        - communicate via http api, not regular kubectlr commands



    -  internally
        - **`https://` `kubernetes.default` `.svc.cluster.local` `/api/v1`**

            - same pattern as other services (see above) when you realize:
                - `kubernetes` - (api server) service name
                - `default` - namespace

            ###
            - ip address
                - `kubectl run dnslookup --image=busybox --restart=Never --rm -it -- nslookup kubernetes.default.svc.cluster.local`

                    ```yaml
                    Name:   kubernetes.default.svc.cluster.local
                    Address: 10.96.0.1   # not same as 'externally' accessible (via cluster-info) - below)
                    ```
        - externally:
            - `k` `cluster-info`
                ```yaml
                Kubernetes control plane is running at https://172.30.1.2:6443
                CoreDNS is running at https://172.30.1.2:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy # <-- ** eselbrücke - helpful for remembering format for internal service access
                ```


      
