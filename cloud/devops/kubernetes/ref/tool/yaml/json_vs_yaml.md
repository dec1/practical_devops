#### YAML vs JSON
- Every JSON can be transformed to corresponding YAML. 
    - [onlineyamltools](https://onlineyamltools.com/convert-yaml-to-json)
    - [jsonformatter](https://jsonformatter.org/)
    
    ###
    Additionally, yaml allows:
    - **Comments**
    - **Date** (and **Time**stamp) values

    - **non-string key**s

    ###
    - **References** using `&` and `<<`
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

    - **Multiline** string values 
        ```yaml
        multi-line-str :                # embedded "\n"
            "This is a multi-line string.\nIt uses inline quoting.\nNewlines are represented by \\n."

        multi-line-str-soft : >         # "Folded Block Scalar"
          This is a multi-line string
          but it will be folded into
          a single line when parsed.


        multi-line-str-hard : |         # "Literal Block Scalar"
          This is a multi-line string.
          Each line break and space
          is preserved exactly as is.

        ```


