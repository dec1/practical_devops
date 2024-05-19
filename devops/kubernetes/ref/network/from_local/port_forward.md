### Port-Forwarding

- `k` **`port-forward`** **`<pod-name>`** **`<local-port>`**:**`<pod-port>`**
Allows you to access pod by name and port as through localhost:local-port on your local machine (where kubectl is running

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
