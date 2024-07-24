#### YAML vs JSON
- Every JSON can be [transformed](https://jsonformatter.org/) to corresponding YAML. 
    
    Additionally, yaml allows:
    - **Comments**
    - **Date** (and **Time**stamp) values
    - **Multiline** string values (see `Literal Block Scalar` below)
    - **non-string key**s
    - Merging (references) using `&` and `<<`
        ```yaml
        defaults: &defaults
            adapter: postgres
            host: localhost

        development:
            <<: *defaults
            database: dev_db

        # --- equivalent to....
        # development:
        #   adapter: postgres
        #   host: localhost
        #   database: dev_db
        ```


