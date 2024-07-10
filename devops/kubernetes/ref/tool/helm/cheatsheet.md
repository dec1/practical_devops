
### Cheatsheet:
###
- `helm` **`repo ls`** `[-A | -n my-ns] ` **`[-a]`**
    - `[-A | -n my-ns]` all or specific namespace
    - `[-a]` all (including failed)
    
    ```yaml
    Error: no repositories to show                             
    ```
###
- `helm` **`ls`**
    ```yaml
    NAME    NAMESPACE       REVISION        UPDATED STATUS  CHART   APP VERSION
    ```

- `helm` **`repo add`** `my-bitnami` `https://charts.bitnami.com/bitnami`
    ```yaml
    "my-bitnami" has been added to your repositories
    ```
###
- `helm` **`repo ls`** 
    ```yaml
    NAME            URL                               
    my-bitnami      https://charts.bitnami.com/bitnami                       
    ```
###
- `helm` **`repo update`**
    ```yaml
    Hang tight while we grab the latest from your chart repositories...
    ...Successfully got an update from the "my-bitnami" chart repository
    Update Complete. ⎈Happy Helming!⎈
    ```
###
- `helm` **`search`** `[repo]`  `[my-bitnami/]` `nginx`
    - Careful: 
        - **not** _repo search_
        - **\<repo-name\>/\<chart-name\>**
    ```yaml
    NAME                                    CHART VERSION   APP VERSION     DESCRIPTION                                       
    my-bitnami/nginx                        15.14.0         1.25.4          NGINX Open Source is a web server that can be a...
    my-bitnami/nginx-ingress-controller     11.0.0          1.10.0          NGINX Ingress Controller is an Ingress controll...
    my-bitnami/nginx-intel                  2.1.15          0.4.9           DEPRECATED NGINX Open Source for Intel is a lig...
    ```

###    
- `helm` **`install`** `my-nginx` `my-bitnami/nginx` `[--set my-key=my-val]`
    - `--set` [values](./commands.md#show_values_anchor) in chart
    ```yaml
    NAME: my-nginx
    LAST DEPLOYED: Tue Mar 19 08:27:34 2024
    NAMESPACE: default
    STATUS: deployed
    REVISION: 1
    TEST SUITE: None
    NOTES:
    CHART NAME: nginx
    CHART VERSION: 15.14.0
    APP VERSION: 1.25.4
    ....
    ```

###
- `helm` **`ls`** 
    ```yaml
    NAME    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
    my-ngnx default         1               2024-03-19 08:38:20.116424964 +0000 UTC deployed        nginx-15.14.0   1.25.4    
    ```

###
- `helm` **`upgrade`** `my-nginx` `my-bitnami/nginx`
    ```yaml
    Release "my-nginx" has been upgraded. Happy Helming!
    ```

###
- `helm` **`uninstall`** my-nginx
    ```yaml
    release "my-nginx" uninstalled
    ```

---