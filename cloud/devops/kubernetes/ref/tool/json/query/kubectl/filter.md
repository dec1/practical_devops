### kubectl

Both 
 - 1). **`-o json | jq`** `<filter>`, and  
 - 2). **`-o jsonpath`** `=<exprn>`

 can be used to post-process (filter) [kubectl](https://kubernetes.io/docs/reference/kubectl/jsonpath/) output

- jq filter vs jsonpath exprn
    |           | jq filter     | jsonpath exprn | 
    | --------  | --------      | ------- | 
    | begin    | `.`           | `{.`  or `{$.`      (kubectl accepts both)  |
    |end     |             | `}`    |  
    | array     | my_list[] | my_list[`*`] | 

    ie with  `jq`: **omit** the `{}` and `*` in the filter (compared to equavalent jsonpath exprn)
- #### 1) jq
    - jq and its filters (prefer) can be used to post-process JSON output of kubectl 
        - often outputs in color (syntax highlighting)
        - can use [kubernetes jsonpath doc](https://kubernetes.io/docs/reference/kubectl/jsonpath/) as ref for filters - just  omit:
            - **`{}`** enclosing path
            - **`*`** in `[*]` 

    ##
    - **`k -o json`** <some_cmd>  **`| jq`** `[-r]` `<filter>`
        - `k -o json` `get pods -n my-ns` **`| jq` `'.items[].metadata.name'`**
            ```yaml
            "pod1"
            "pod2"
            ```

            - `-r` :  dont enclose output in quotes

                - `k -o json` `get pods -n my-ns` **`| jq -r`** `'.items[].metadata.name'`
                    ```yaml
                    pod1
                    pod2
                    ```


##### 
- #### 2)  jsonpath
    Alternative to jq 
    - `jsonpath=` can added to (implicit) json specified output 
        - `k <some_cmd>` **`-o jsonpath=`**`"{<exprn>}"`
            - `k get pods  -n my-ns -o `**`jsonpath='{.items[*].metadata.name}'`** 
                ```yaml
                pod1 pod2
                ``` 

            - need additional `| tr ' ' '\n'` to get each result of output on separate (line) - another reason to prefer more powerful and flexible  `| jq`

            - note additional enclosing **`{}`** around the actual jsonpath
       
                
            ##
            - `k get pods -n my-ns` -o jsonpath="`{`**`.items[*]`**`.metadata.name}, {`**`.items[*]`**`.metadata.namespace}` "
                ```yaml
                pod1 pod2, my-ns my-ns
                ```
            - `range` (~_for each_)
            -  `k get pods -n my-ns` -o jsonpath="**`{range .items[*]}`**`{.metadata.name } {.metadata.namespace},`"
                ```yaml
                pod1 my-ns, pod2 my-ns, 
                ```
