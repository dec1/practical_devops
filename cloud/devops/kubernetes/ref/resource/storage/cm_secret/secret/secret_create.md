

#### Create
- **kubectl** Create a secret with kubectl is same as creating configmap, except you additionally specify _kind_ (usually `generic`, other possibilities being: `docker-registry` and `tls`). 

    - The only effective difference between the kinds is where data is read from, in which format,  and/or if/how keys get re-named



###
- `k create` **`secret`** **`generic`** `my-secrets-name` 
     [**`--from-literal=key1=value1`**] [`--from-literal=key2=value2`] 
    [`--from-file=[key=]file_path`] 
    [`--from-env-file=file_path`]
    [`--type=type`]  
    -  _type_ only affects metadata in the secret - the key names and data stored (as [base64](../../../../tool/base64.md)) renamin unchanged



  
  ---

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

- Regardless of which parameters above you pass to kubectl to create the secret, the values   are all  *automatically*  [base64](../../../../tool/base64.md) **encoded**  before being stored in [data](../cm_secrets.md) section.    
- `k` **`get`** `secret` `my-sec` `-o yaml`
       
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

- When you (`describe` or) **inject** the secret  into a pod (as env vars or vol mounts) secrets are *automatically* [base64 -d](../../../../tool/base64.md) **decoded**, so pod doesnt have to

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




