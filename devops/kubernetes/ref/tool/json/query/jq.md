- ## [jq](https://github.com/jqlang/jq)

    - A tool for processing JSON input 
        - Similar to `awk` and `sed` for text input.

    ### 
    - can search (and optionally modify) json input (source), based on a 
        - **filter** (filename or stdin data)
            - (almost) identical to  [jsonpath](https://en.wikipedia.org/wiki/JSONPath) expressions:

            |           | jq filter     | jsonpath | |
            | --------  | --------      | ------- | -------|
            | start     | .             | $.       | Kubernetes (kubectl) accepts both  |
            | array     | **my_list[]** | **my_list[*]** | |

    - #### Usage  
        - [example.json](../example.json)

            - as filename:
                - **`jq`** \<**`filter`**\> \<`source_file`\>,

            - source as data on stdin 
                - cat \<`source_file`\> | **`jq`** \<**`filter`**\>
                
                ####
                
                - 
                    -  **`jq` `'.kind'`** *`example.json`*, 
                    or 
                    - `cat example.json |` **`jq` `'.kind'`**
                    
                        ```json
                        "List"
                        ```
        - [kubectl output](https://kubernetes.io/docs/reference/kubectl/jsonpath/)        
        
            - jq and its filters (prefer) can be used to post-process JSON output of kubectl 
                - **`kubectl -o json`** <some_cmd>  **`| jq`** \<`filter`\> 
                    - **`kubectl -o json` `get pods` `| jq` `'.items[].metadata.name'`**
                        - often outputs in color (syntax highlighting)
                        - can use [kubernetes jsonpath doc](https://kubernetes.io/docs/reference/kubectl/jsonpath/) as ref for filters - just  omit:
                            - **`{}`** enclosing path
                            - **`*`** in `[*]` 
            ##### 
            - jsonpath= can added to (implicit) json specified output 
                - **`kubectl -o jsonpath={<some_path>}`** <some_cmd>
                    - `kubectl get pods -o jsonpath='{.items[*].metadata.name}'` 

                        - need additional `| tr ' ' '\n'` to get each result of output on separate (line) - another reason to prefer more powerful and flexible  `| jq`

                        - note additional enclosing **`{}`** around the actual jsonpath

