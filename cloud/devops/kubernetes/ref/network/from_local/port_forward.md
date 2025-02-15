### Port-Forwarding

Automatically (port) forwards http requests to `localhost`:**`local-port`** to an individual 
**pod/service** (in the cluster) at `pod-port`

(see also [proxy](proxy.md) and [dns](../dns.md))

- `k` **`port-forward`** **`(<pod-name>|svc/<service-name>)`** **`<local-port>`**:**`<pod-port>`**




    - example
        - `k run my-pod --image=nginx:alpine --rm --restart=Never -i`
            - run  pod with web server
        - `k` **`port-forward`** `my-pod 80:80`
            - setup port forwarding to/from (kubectl) client machine
        - **`curl`** `localhost:80`
            - send request to pod through localhost
            ```yaml
            <h1> Welcome to nginx! </h1>
            ```

---

-  ##### Pod
    ###
    -  `k` **`run`** `my-pod --image=nginx`


    ####
    - `k` **`port-forward`** `my-pod` `80:80` [`&`]

        - `&` (optional) -  send to bgd 



    ####
    - **`curl`** `-l localhost:80`
        ```yaml
        <!DOCTYPE html>
        <html>
        <head>
        <title>Welcome to nginx!</title>
        ```

    - cleanup 
        - `jobs` - look for job num of prev command
            ```yaml
            [2]+  Running                 kubectl port-forward my-pod 80:80 &
            ```
            - `kill %2` or
            - `fg` `%2` and `Ctrl+C` 


---
- ##### Service

    ####
    - `k expose --name=my-svc pod my-pod --port=80`
    
    ######
    - `k` **`port-forward`** **`svc/`** `my-svc` `80:80` [`&`]

    ####
    - rest same as for pod

