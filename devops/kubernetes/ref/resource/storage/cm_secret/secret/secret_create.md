

#### Create
- **kubectl** Create a secret with kubectl is same as creating configmap, except you additionally specify an option and (in some cases) a `--type`. 

    - The combination you pass determines which of the 6 "Types" of secret (see below) you create. 
    - The only effective difference between the types is where data read from, in which format,  and/or if/how keys get re-named



###
-   `k create secret` (values you pass are all **plaintext**)

    
    ####    
    - 1). generic **Opaque** (arbitrary user-defined data) - most common
    `--from-literal=` `key1=value1` --from-literal=key2=value2
    <br>

        - `k` **`create secret`** `generic my-sec` **`--from-literal=one=1`**

             ```yaml
            apiVersion: v1
            kind: Secret
            metadata:
              name: my-sec

            type: Opaque    # default
            data:
              one: MQ==     # encoded: "1" in base64
             ```
    <details>
       <summary> Other Methods </summary>

      - 2). **Basic Auth**
       `--type=kubernetes.io/` **`basic-auth`**
       `--from-literal=` **`username`** `=myuser` --from-literal= **`password`** `=mypass`
      <br>

          - `k create secret generic sec --type=kubernetes.io/basic-auth  --from-literal=username=myuser --from-literal=password=mypass --dry-run=client -o yaml`

              ```yaml
              apiVersion: v1
              kind: Secret
              metadata:
                name: my-sec

              type: kubernetes.io/basic-auth
              data:
                password: bXlwYXNz
                username: bXl1c2Vy

              ```

      - 3). **SSH Auth** 
      `--type=kubernetes.io/` **`ssh-auth`**
      `--from-file=` **`ssh-privatekey`** `=/path/to/.ssh/id_rsa`
      <br>



    - 4). **Docker (Config Json)** (see _docker-registry_ below)
      `--type=kubernetes.io/`**`dockerconfigjson`** 
      `--from-file=` **`.dockerconfigjson`** `=path/to/.docker/config.json`
      <br>

    - 5). **Docker (Cfg)**  (legacy)
      `--type=kubernetes.io/`**`dockercfg`** 
      `--from-file=` **`.dockercfg`** `=path/to/.dockercfg`
      <br>

      - `docker-registry` (recommended ~ Config Json (above), but reads key/vals **inline**)
        - **Docker Registry**
         `--docker-server=` **`DOCKER_REGISTRY_SERVER`** `--docker-username=` **`DOCKER_USER`**         `--docker-password=` **`DOCKER_PASSWORD`** `--docker-email=` **`DOCKER_EMAIL`**
        <br>
  
            - `k create secret docker-registry sec --docker-server=srv --docker-username=usr        --docker-password=pwd --dry-run=client -o yaml`
  
                ```yaml
                apiVersion: v1
                kind: Secret
                metadata:
                  name: my-sec         
    
                type: kubernetes.io/dockerconfigjson
                data:
                  .dockerconfigjson:            eyJhdXRocyI6eyJzcnYiOnsidXNlcm5hbWUiOiJ1c3IiLCJwYXNzd29yZCI6InB3ZCIsImF1dGgiOiJkW               E55T25CM1pBPT0ifX19
                ```


     - 6). **TLS**
       **`--cert=`** `path/to/cert/file` **`--key=`** `path/to/key/file`  
      <br>
    </details>
----

- Regardless of which parameters above you pass to kubectl to create the secret, the values are all stored  (base64) *automatically* **encoded** similarly in [data](../common.md) section.    
- `k` **`get`** `secret` `my-sec` `-o yaml`v
       
    ```yaml
    apiVersion: v1
    kind: Secret
    type: Opaque
    data:
      one: MQ==         # <-- encoded: ("1" in base64)
    metadata:
      creationTimestamp: "2024-03-25T09:44:19Z"
      name: my-sec
      namespace: default
      resourceVersion: "3707"
      uid: ea4dda28-6111-4ad4-a793-dcf7677da72c

    ```

- When you (`describe` or) **inject** the secret  into a pod (as env vars or vol mounts) secrets are *automatically* **decoded**, so pod doesnt have to

- `k` **`describe`** `secret` `my-sec`
    ```yaml
    Name:         my-sec
    Namespace:    default
    Labels:       <none>
    Annotations:  <none>

    Type:  Opaque

    Data
    ====
    one:  1 bytes       # <-- decoded
    ```




