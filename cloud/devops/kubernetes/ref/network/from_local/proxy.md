
### Proxy

Automatically (port) forwards http requests to `localhost`:`port` to the 
**API Server** (in the cluster) 





- _Authentication_:  
uses your existing **kubectl** configuration (which contains your **credentials**) to authenticate with the Kubernetes API server.

#####
- Accessing the API: 
You can then use tools like curl or a web browser to **interact with the  Kubernetes REST API (like kubectl does behind the scenes)


(see also [apiserver](../../general/architecture/components/pods/static/system/apiserver.md))

---

- `k run my-pod --image=nginx`

- **`k proxy`** `--port=9999` `[&]` 
    - `&` (optional) -  send to bgd


##
- get the **pod spec**
    `curl -L` **`http://localhost:9999`** **`/api/v1`** **`/namespaces/default`** **`/pods/my-pod`** 

    ```yaml
    {
    "kind": "Pod",
    "apiVersion": "v1",
    "metadata": {
        "name": "my-pod",
        .....
    ```


###
- **forward** request to the pod (note trailing **`:<port>/proxy`** in url)
    - equivalent to  [port-forward](port_forward.md) (but more complicated url)

    ####
    `curl -L` `http://localhost:9999` `/api/v1` `/namespaces/default` `/pods/my-pod` **`:80`** **`/proxy`**

    ```yaml
    <!DOCTYPE html>
    <html>
    <head>
    <title>Welcome to nginx!</title>
    .....
    ```


- url is difficult (format) to remember but 
    - `k` **`cluster-info`** (follows same pattern)
        ```yaml
        CoreDNS is running at https://172.30.1.2:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
        ```



---
- cleanup 
    - `jobs` - look for job num of prev command
        ```yaml
        [1]+  Running                 kubectl proxy --port=9999 &
        ```
        - `kill %1` or
        - `fg` `%1` and `Ctrl+C` 




