
### Multiple Values (attributes)

- Getting multiple values in each item (line) of result is trickier.
#### 1) jq
- a).
    - around value list:
        - **`| [ <value1, value2> ] `** 

            - `k get pods -n my-ns -o json` `| jq -r` `'.items[]` **`| [` `.metadata.name` `,` `.metadata.namespace` `]`** `'`
                ```yaml
                [
                "pod1",
                "my-ns"
                ]
                [
                "pod2",
                "my-ns"
                ]
                ```
            - optional
                - **`| join(", ")`**  at end:
                
                    -   `k get pods -n my-ns -o json ` `| jq -r` `'.items[] | [.metadata.name, .metadata.namespace]` **`| join(", ")`**`'`

                        ```yaml
                        pod1, my-ns
                        pod2, my-ns
                        ```
- or b).
    - around each value:
    - **`| \( each value \) `** 
        - `k get pods -n my-ns` `-o json` **`| jq`** `-r `**`'.items[] | "\(.metadata.name) \(.metadata.namespace)"'`**
            

            ```yaml
            pod1 my-ns
            pod2 my-ns
            ```
---

##### 
- #### 2) jsonpath

    is a bit simpler

    ####
    - a). repeat full path 
        - `k <some_cmd> -o jsonpath=` **`"{<exprn_1>}, {<exprn_2>}"`**
        - `k get pods -n my-ns` `-o jsonpath=`**`"{.items[*].metadata.name}, {.items[*].metadata.namespace}"`**
            ```yaml
            pod1 pod2, my-ns my-ns
            ```
    ###
    - or b). **`{range`** `items}` ~_for each_ (item _in_ items)
    
        -  `k get pods -n my-ns` `-o jsonpath="` **`{range .items[*]}`**`{.metadata.name } {.metadata.namespace},`"
            ```yaml
            pod1 my-ns, pod2 my-ns, 
            ```
        

