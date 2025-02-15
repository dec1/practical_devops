
### Pod

#####
-  Each **pod** is associated with a *single* **service account**, and a token which identifies it and contains roles, which are used to detremine its access rights to Api Server (ie what functions it can call)
    - `default` service account allows very little), 
    -  Kubernetes **automatically mounts** a service account (jwt) token into running pods  at
        - **/var/run/secrets/kubernetes.io/serviceaccount/token**
        -  so `containers` within it can read/use it eg (see also below):
            - `k exec -it  my-pod -- curl -s -k -m5
-H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" https://kubernetes.default.svc.cluster.local/api/v1/namespaces/my-ns/pods `



#####
- **Containers** within pod all share same filesystem volumes, and 
     - can read the token here, and append it to http headers when communicating with the 
     
`Api Server` `service` internally [accessible at](../../../../../network/dns.md):
 **`https://kubernetes.default.svc.cluster.local/api/v1`**
#####
- Service account 
    - does not (cf [network policy](../../../../../network/policy.md)) control ability of (containers within) pods to communicate with (containers within) other pods and services 
    - only their ability to communicate with **Api Server**
#####
- The service account token can also be (manually) used by any **external** clients (eg CI pipeline) to authenticate with the API server.


####
- **pod.yaml** (declarative)
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
        name: my-pod
    spec:
        serviceAccountName: my-sac  # <-- assign service account to pod - so that the
                                    # token will be mounted at:
                                    # /var/run/secrets/kubernetes.io/serviceaccount/token

                                    # superfluous if you create and mount token manually via `k create token`
        containers:
        - name: my-container
          image: nginx
          ports:
          - containerPort: 80
    ```

###
- `k` `describe pod` my-pod
    ```yaml
        Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5q8hw 
        .....
    ```
- `k exec -it my-pod -- ls` **`/var/run/secrets/kubernetes.io/serviceaccount`**
    ```yaml
    ca.crt  namespace  token
    ```
    - **`token`**: The service account **(jwt) token** - used by API server to **verify pod**/container connecting
        - `ca.crt`: The certificate of the CA that signed the API server's certificate, use by pod to **verify** the **API server**'s certificate when making HTTPS calls.
        - `namespace`: namespace of the pod.
    ###
    - `k exec -it my-pod -- cat ` **`/var/run/secrets/kubernetes.io/serviceaccount/`** **`token`**
        ```yaml
        eyJhbGciOiJSUzI1NiIsImtpZCI6IlpveEpuU1h6aElpODVRcDJoQWZ0OGxkaW5KcjVEZlRiSXhwYkRYWm1XR0UifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzQxNjgwODY3LCJpYXQiOjE3MTAxNDQ4NjcsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJteS1wb2QiLCJ1aWQiOiJhOGNkZGE3Zi0zNzY5LTRmY2YtYTMyMy01OTlkNWMxY2FmMWQifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6Im15LXNhYyIsInVpZCI6IjQwODNiMzcxLWUwZmItNDE1NC1hNmQwLWE3ODhmOTcyNTJkZCJ9LCJ3YXJuYWZ0ZXIiOjE3MTAxNDg0NzR9LCJuYmYiOjE3MTAxNDQ4NjcsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0Om15LXNhYyJ9.qLvVjF-_IjtXHhn7GshmCTsARTIO9BvNTKfQDgVwlKUmgw-xGIoPDXpTzAy-t6GY3DIiHmPgTg7J6X7lh9fid0yAEER8M-IE12gGvzKWE7g23vF6aeFncNpHc_7LhPp-VJ_bij27n6KaOaRHgsIvLHxkUm3_6siXfSgSnEpGVX-nmSJy0N4xDG0nGPGYnrfbfUQIyK8KiHeP1qR3L8JabcvwgkZBBqrloUuVlYs_89iYjQchW8cGkiRPyzZq8Cede1UkjKE4WutB5w_9rALxx-oQsjT8s4maSRPZHqjIEJ7yefcAxIDdwHU2CFm-TM-1ne9JnXCMeJjASXKvcwzElwcontrolplane 
        ```


   
    #####
    - `k` **`exec`** `-it my-pod` **`-- curl`** `-s -k -m5` 
    **`-H "Authorization: Bearer`** `$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" 
    https://kubernetes.default.svc.cluster.local/api/v1/namespaces/my-ns/pods`

        - query api server from inside pod (conainer) 
        eg for list of pods in namespace my-ns using token
        ###
        - `-s`: Silent mode. It prevents curl from showing progress or error messages.
        - `-k`: Allows connections to SSL sites without cert signed by CA curl trusts (often api server's cert is self-signed)
        - `-m5`: Wait max 5 secs
        