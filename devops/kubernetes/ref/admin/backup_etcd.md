### [etcd Backup/Restore](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/#backing-up-an-etcd-cluster)

- ### etcd

    All Kubernetes objects are stored in etcd
    `etcdctl` is the primary command-line **client** that interacts with `etcd` **server**.
    It is used for day-to-day operations such as managing keys and values, administering the cluster, checking health, and to save/restore contents of etcd store to/from a `snapshot` file. 

    ###
    - etcd runs in a **pod** (like all control plane only components) configured in its manifest:        
        
        ####
        - **`/etc/kubernetes/manifests/etcd.yaml`**

            ```yaml
            ........

            spec:
            containers:
            - command:
                ........

                # options for backup

                # TLS/https security between client and server
                - --cert-file=/etc/kubernetes/pki/etcd/server.crt                           
                - --key-file=/etc/kubernetes/pki/etcd/server.key         
                - --peer-trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt  
                
                # where server is listening
                - --listen-client-urls=https://127.0.0.1:2379,https://192.168.100.31:2379   


                ........
                - hostPath:
                    # where to read/write values
                    path: /var/lib/etcd   # <-- need to set this to location of (extracted) backup
                                          # eg /var/lib/etcd-extracted (see below)
                  name: etcd-data

            ```


- `export ETCDCTL_API=3`
    - should match etcd server (major) version

- ### Backup

                
    - **`etcdctl`**  **`snapshot save`** **`<archive_file_path>`**
        [**`--endpoints`** `$ENDPOINT`] 
        [**`--cacert`** `=<trusted-ca-file>`] [**`--cert`** `=<cert-file>`] [**`--key`** `=<key-file>`]

    ####
    - eg
        ```sh
        etcdctl snapshot save /tmp/etcd-backup.db \
        --endpoints=https://127.0.0.1:2379 \
        --cacert=/etc/kubernetes/pki/etcd/ca.crt \
        --cert=/etc/kubernetes/pki/etcd/server.crt \
        --key=/etc/kubernetes/pki/etcd/server.key
        ```
    - Options:
        
        - `--endpoints` 
            -   where etcd server is listening
                - default: https://localhost:2379

        - `--cacert`, `--cert`, `--key`
            - for securing https connection between client and server

        ####
        - values from `etcd.yaml `manifest (see above)

- ### Restore

- `etcdctl` **`snapshot restore`** `<archive_file_path>` **`--data-dir`** `<extracted_dir_path>` 
        [**`--endpoints`** `$ENDPOINT`] 
        [**`--cacert`** `=<trusted-ca-file>`] [**`--cert`** `=<cert-file>`] [**`--key`** `=<key-file>`]
    ####
    - Extracts snapshot archive to arbitrary location - etcd doesnt use it (yet) though

        - `--extracted_dir_path`
            - dir_path to where archive should be extracted
        - --archive_file_path, --endpoints, --cacert, --cert, --key
            - same as `snapshot save` (see above)
        - eg
            ```sh
            etcdctl snapshot restore /tmp/etcd-archive --data-dir /var/lib/etcd-extracted \
            --endpoints=https://127.0.0.1:2379 \
            --cacert=/etc/kubernetes/pki/etcd/ca.crt \
            --cert=/etc/kubernetes/pki/etcd/server.crt \
            --key=/etc/kubernetes/pki/etcd/server.key
            ```


-  edit etcd manifest so it uses new dir_pat for reading/writing
  
    - **`vim`** `/etc/kubernetes/manifests/etcd.yaml`
        - hostPath.path now points to dir_path of extracted archive
            ```yaml
                ........
                - hostPath:
                    path: /var/lib/etcd-extracted  # <-- location of (extracted) backup

                name: etcd-data
            ```




