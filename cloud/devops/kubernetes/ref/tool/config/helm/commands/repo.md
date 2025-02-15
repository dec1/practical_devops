
## Repo
    

#####
- `helm` **`repo add`** `my-repo` `https://charts.jenkins.io` 
    add to local cache/index as **my-repo** 

#####
-  `helm` **`repo update`**
    update local repo cache (like `apt-get update` ) from remote
    ```yaml
    Hang tight while we grab the latest from your chart repositories...
    ...Successfully got an update from the "my-repo" chart repository
    ```
#####
- `helm` **`repo ls`**
    list repos that have been added (indexed) locally


    ```yaml
    NAME            URL                               
    nginx-stable    https://helm.nginx.com/stable     
    my-repo         https://charts.jenkins.io   
    ```
####
- `helm` **`repo rm`** `my-repo`
    remove from local cache

###
- `helm` **`search`** **`repo`** `my-repo`[/`my-chart`] --versions
    - show repo contents 
    - mathcing `my-chart` if specified , otherwise *all **charts*** 
    - doesnt distinguish installed and uninstalled  
    - `--versions` include all versions of each - not just latest
    
    - cf `helm ls` (below) for showing  installed charts 
    #####
    - `helm search repo bitnami/nginx`
        ```yaml
        NAME                                    CHART VERSION   APP VERSION     DESCRIPTION                                       
        bitnami/nginx                           15.14.0         1.25.4          NGINX Open Source is a web server that can be a...
        bitnami/nginx-ingress-controller        11.0.0          1.10.0          NGINX Ingress Controller is an Ingress controll...
        bitnami/nginx-intel                     2.1.15          0.4.9           DEPRECATED NGINX Open Source for Intel is a lig...`
        ```


        - `APP VERSION`
            - software (functional) encapsulated by the chart (eg nginx version)
        - `CHART VERSION` 
            - version of wrapper (will have to change when app changes, but also if chart changes).
            - this is what you specify in `helm install` **`--version`**
