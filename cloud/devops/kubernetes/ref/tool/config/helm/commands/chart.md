
- ## Chart
    - ### show values
        - `helm` **`show values `** `my-repo/my-chart`
            <a name="show_values_anchor"></a> 
            show all values in the chart that can be overridden (eg  **controller.adminUser** whose default value is "admin")
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
    - ### install

        - `helm` **`install`**  **`<as_name>`** **`<location>`**   **`-f  <values_file>`** 
        `[-n <some_ns>]` `[--version <some_ver>]`  `--set <some_key>=<some_val>` 
        
            #####
            installs chart at _location_, naming it _as_name_, and injecting values from _values_file_, 
            subsequently overriding those passed with _set_, eg
            
                
            - `helm` **`install`**  **`my-nginx`** **`bitnami/nginx`**  `[-n my-ns]` `[--version 4.6.4]` 
            `  ` `[-f` **`my-vals.yaml`**`]` `[`**`--set`** **`controller.admin.username=my-admin`**`]`

        
            ###
            - name the local installed release **my-nginx** 
            -  **override** default values  in chart,  with *`my-vals.yaml`*
            and *`controller.admin.username`* with  *my-admin*

 

    