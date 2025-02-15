- ## [jq](https://github.com/jqlang/jq)

    - A tool for processing JSON input 
        - Similar to `awk` and `sed` for text input.

    ### 
    - can search (and optionally modify) json input (source), based on a 
        - **filter** (filename or stdin data)
            -  [almost](kubectl/filter.md) identical to  [jsonpath](https://en.wikipedia.org/wiki/JSONPath) expressions
            -  includes functions like [select()](https://jqlang.org/manual/#select), [test()](https://jqlang.org/manual/#test) for further filtering results - see examples below 

    - #### Usage  
        - [example.json](example.json)

            ###
            - as _filename_:
                - **`jq`** \<**`filter`**\> \<`source_file`\> 
                    -  **`jq` `'.kind'`** *`example.json`*
            
                ####
                or, alternatively:
            ####
            - source  as data (piped) on _stdin_ 
                - cat \<`source_file`\> | **`jq`** \<**`filter`**\>
                    - `cat` [example.json](example.json) `|` **`jq` `'.kind'`**
                ####
                
          
            ##    
            - both commands above output:             
                ```json
                "List"
                ```
            
        - ##### Furter filtering results - with `select()` (and `test()`)
            ##
            - `jq` `'.items[].metadata'` [example.json](example.json)
                - gets all `'.items[].metadata'`, and
            
            #####
            - `jq` `'.items[].metadata | select(.name` **`| test("0.0")`** `)'`  [example.json](example.json)
                - gets all `'.items[].metadata'` _where_ `metadata.name` **contains** `"0.0"`
                #####
                both producing (with this _example.json_):

                ```yaml
                {
                    "name": "127.0.0.1",
                    "labels": {
                        "kubernetes.io/hostname": "127.0.0.1"
                    }
                }
                {
                    "name": "127.0.0.2"
                }
                ```


            ##
            - `jq` `'.items[] | select(.metadata.name | test("0.0"))` **`.metadata.name`**`'`  [example.json](example.json)
                - for  all `'.items[]'` whose `.metadata.name` _contain_ `"0.0"` get the  _metadata.name_
                ```yaml
                "127.0.0.1"
                "127.0.0.2"
                ```
                see  final exmample of [jsonpath support ](https://kubernetes.io/docs/reference/kubectl/jsonpath/)

            
            #
            -  `jq` `'.items[].metadata | select(.name` **`== "127.0.0.1")'`** [example.json](example.json)
                - gets all `'.items[].metadata'` _where_ `metadata.name` is **exactly** `"127.0.0.1"`
                ```yaml
                {
                  "name": "127.0.0.1",
                  "labels": {
                    "kubernetes.io/hostname": "127.0.0.1"
                  }
                }
                ```






