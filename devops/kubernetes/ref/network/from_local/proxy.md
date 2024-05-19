
### Proxy
Creates a (reverse) proxy server between localhost and the Kubernetes API server. (Kubectl handles locating and authenticating to the apiserver). 

- #### Run
    **`k proxy`** `--port=9999` `[&]`   
    Start reverse proxy to api server on localhost:9999
    - `&` - run in bgd so can use same terminal (below)
        - close:
            - `jobs` - look for job num of prev command
            - `fg %<num>` - bring the command to fgg
            - `CTRL + C` - kill the (proxy) process

- #### Interact
    with api server on localhost. (Useful for debugging/testing)
    
    
     - **api** (top level)
        **`curl`** `[http://]`**`localhost:9999/`** **`api/`**
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

     -  **service**
            send req to (clusterip) **sevice** (which is normally not accessible from external)

        - `curl` **`-L`** `http://` **`localhost:8001/api`** `/v1/` `namespaces/<ns>/` **`services/<service-name>`** **`/proxy/`**
            ####
            - `-L`  follow redirects - needed with proxy
            - `service-name` name of (running) service  
            - `ns` namespace of service   

            ####
            - difficult (format) to remember but cf (output of)
                `k cluster-info` (same pattern)
                - `CoreDNS is running at ...` **`/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy`**

     -  **pod**
            send req to pod directly
           - `curl -L` `http://` `localhost:8001/api/v1/namespaces/<ns>/` **`pods/<pod-name>`** `/proxy`     

