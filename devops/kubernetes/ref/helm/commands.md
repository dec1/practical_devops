

- #### Dry-Run
 - `heml` **`template`** <other_helm_cmd>
    show the template files for resources that would be created by `helm other_helm_cmd` without actually executing it.
    - helm **template** addtionally has a `--dry-run=` option, but only `server` seems to make sense as a value
    

- #### Repo
    

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


            - ###### App Version
                - software (functional) encapsulated by the chart (eg nginx version)
            - ###### Chart Version 
                - version of wrapper (will have to change when app changes, but also if chart changes).
                - this is what you specify in `helm install` **`--version`**
#####
- #### Chart
   
    - `helm` **`show values `** my-repo/my-chart
        <a name="show_values_anchor"></a> 
        all values in the chart that can be overridden (eg  **controller.adminUser** whose default value is "admin")
        - `helm show values jenkinsci/jenkins`
            ```yaml
            ...
            controller:
                # Used for label app.kubernetes.io/component
                ........
                # you should revert controller.admin.username to your preferred admin user:
                admin:
                    username: "admin"
            ...
            ```
        - **controller.admin.username** has default value of ***admin***
        (which can be overridden)




    #####
    - `helm` **`install`**  **`my-nginx`** **`bitnami/nginx`**  `[-n my-ns]` `[--version 4.6.4]` 
     `  ` `[-f` **`my-vals.yaml`**`]` `[`**`--set`** **`controller.admin.username=my-admin`**`]`

       
         ###
         - name the local installed release **my-nginx** 
         -  **override** default values  in chart,  with *`my-vals.yaml`*
         and *`controller.admin.username`* with  *my-admin*
         #####
         - **my-nginx** 
            - **local** installed release
                - `my-nginx/`
                    - `Chart.yaml`
                    - `values.yaml`
                    #####
                    - `charts/`
                    - `templates/`
                    #####

 

    ###
    - **Revison**  
        - `helm` `repo update` - see above

        ####
        - `helm` **`upgrade`** `my-chart my-repo/jenkins`  [--version 5.0.16]
            *upgrade* 5.0.15 -> 5.0.16 (default = latest)
            ```yaml
            Release "my-chart" has been upgraded. Happy Helming!
            ```
        ####
        - `helm` **`upgrade`** `my-chart my-repo/jenkins`  --version 5.0.14
            *downgrade* 5.0.16 -> 5.0.14 

        ####
        - `helm` **`ls`** `[-A]` `[-a]` 
            -  `-A` all namespaces
            -  `-a` not just `deployed` - also include `failed`, pending-install, , pending-upgrade
            lastest version of each chart **installed chart** in namespace (cf `helm repo ls` above)
            ```yaml
            NAME    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
            my-chart  default         3               2024-02-22 18:38:51.10607678 +0000 UTC  deployed        jenkins-5.0.14  2.440.1   
            ```

        - **history**     
            ###
            - `helm` **`history`** `my-chart `
                all *revisions* of  chart
                ```yaml
                REVISION        UPDATED                         STATUS          CHART           APP VERSION     DESCRIPTION     
                1               Thu Feb 22 18:10:43 2024        superseded      jenkins-5.0.15  2.440.1         Install complete
                2               Thu Feb 22 18:28:03 2024        superseded      jenkins-5.0.16  2.440.1         Upgrade complete
                3               Thu Feb 22 18:38:51 2024        deployed        jenkins-5.0.14  2.440.1         Upgrade complete
                ```

            - `helm` **`rollback`** `my-chart` `2`
            ####
            - `helm` **`history`** `my-chart `
                ```yaml
                REVISION        UPDATED                         STATUS          CHART           APP VERSION     DESCRIPTION     
                1               Thu Feb 22 18:10:43 2024        superseded      jenkins-5.0.15  2.440.1         Install complete
                2               Thu Feb 22 18:28:03 2024        superseded      jenkins-5.0.16  2.440.1         Upgrade complete
                3               Thu Feb 22 18:38:51 2024        superseded      jenkins-5.0.14  2.440.1         Upgrade complete
                4               Thu Feb 22 18:50:28 2024        deployed        jenkins-5.0.16  2.440.1         Rollback to 2   
                ```

            ####
            - `helm` **`uninstall`** `my-chart` `-n my-ns`
        





