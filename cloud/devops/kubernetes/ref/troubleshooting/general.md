### log locations

- **`/var/log/`**
  
    -  1). `ls /var/log`**`/pods`**
        
         - dirs 
            ```yaml
            kube-system_kube-apiserver-controlplane_33d556edd3ae8ef21980288cef77ae8b
            kube-system_kube-proxy-6xsx9_81e09ae0-12ec-4ec5-94b8-51cda7906370
            ..........
            ```

            - with sub dirs
            `ls  /var/log/pods/`**`kube-system_kube-apiserver-controlplane_33d556edd3ae8ef21980288cef77ae8b/`**
                ```yaml
                kube-apiserver
                ```

                -  **Aggregate log** file of all containers within _each pod_

                    `ls  /var/log/pods/`*`kube-system_kube-apiserver-controlplane_33d556edd3ae8ef21980288cef77ae8b/`***`kube-apiserver`**
                    ```yaml
                    0.log
                    ```     
                    
    ###
    - `ls /var/log`**`/containers`**
         - **Individual log** file of _each container_

            ```yaml
            kube-apiserver-controlplane_kube-system_kube-apiserver-3959d7abfbd0221e5043fccbcb8040e9a1a4e6518dad483b7a33a131885e0283.log
            kube-proxy-6xsx9_kube-system_kube-proxy-c269a18400e27b14085c57f8e36f5b4d5471c140eb27e8b0f632c056547555de.log
            ..........
            ```        
##
### containers
- **`crictl`** **`ps`** 
    - **list containers** (inc container id)


        ```yaml
        CONTAINER           IMAGE               CREATED             STATE               NAME                      ATTEMPT             POD ID              POD
        35a08c7ab1704       c42f13656d0b2       3 minutes ago       Running             kube-apiserver            0                   adbf955bef189       kube-apiserver-controlplane
        66cdb7529eb29       259c8277fcbbc       3 minutes ago       Running             kube-scheduler            2                   c78bd25c1290d       
        ....
        ```

- **`crictl`** **`logs`** `<container_id>`
    - **show logs** of **container** with id

        - `crictl logs` `35a08c7ab1704`
            ```yaml
            0906 07:17:19.112830       1 options.go:221] external host was not specified, using 172.30.1.2
            I0906 07:17:19.113752       1 server.go:148] Version: v1.30.0
            I0906 07:17:19.113905       1 server.go:150] "Golang settings" GOGC="" GOMAXPROCS="" GOTRACEBACK=""
            ....
        ```

### pods
- **`k get pod`**
    - `k` **`-n kube-system`** **`get pod`** `-o wide`
        - list (system) pods
            ```yaml
            NAME                                       READY   STATUS    RESTARTS      AGE   IP            NODE           NOMINATED NODE   READINESS GATES
            kube-apiserver-controlplane                1/1     Running   0     
            etcd-controlplane                          1/1     Running   1 (61m ago)   35d   172.30.1.2    
            ....
            ```
- **`k`** **`logs`** `<pod_name>` `[<container_name> | --all-containners=true]`
    - show logs of container(s) in pod
        - `<container_name>` optional if only one pod in container
        - `k logs` `-n kube-system` **`kube-apiserver-controlplane`**    
            ```yaml
            0906 07:17:19.112830       1 options.go:221] external host was not specified, using 172.30.1.2
            I0906 07:17:19.113752       1 server.go:148] Version: v1.30.0
            I0906 07:17:19.113905       1 server.go:150] "Golang settings" GOGC="" GOMAXPROCS="" GOTRACEBACK=""
            ....
            ```
###
### services
- **`journalctl`** `| grep kubelet`

    ```yaml
    .....
    Sep 06 07:17:31 controlplane kubelet[1674]: I0906 07:17:31.514221    1674 pod_startup_latency_tracker.go:104] "Observed pod startup duration" pod="kube-system/kube-apiserver-controlplane"
    ```