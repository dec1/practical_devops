                 

#### Apply
- `k`  **`apply`**  `-f res.yaml`
    - _create new_ resource (if doesnt exist), or
    - _update existing_ resource (if it does exist, and contains _last-applied-configuration_)

        ###
        
        - ###### `last-applied-configuration` and 3-way Merge 
            Kubernetes adds a lot of fields to a resources (eg yaml) state, automatically at runtime to the state of a resouce, if you dont specify them explicitly. Since you are not (necessarily) providing the new values of all fields when updaing, Kubernetes needs a way to figure out what to do with those you don't explicitly set. In particualar it needs to distinguish, which fields (you dont now explcitly set) you _mean to remove_ from those which you _dont care_ to explicity set. It does this by comapring the current manifest you are applying with the last one applied (the so-called _last-applied-configuration_):

            ####
            - _remove_: fields in _last-applied-configuration_, but not in _current configuration_
            - _keep_: fields not in either (presume kubernetes added them automatically)

            ###
            So to modfiy an existing resource with _apply_, Kubernetes needs a copy of **`last-applied-configuration`** which it saves in the state metadata, if you create the resource with

            - `apply` 

            #####

            - `create`|`run`|`replace` **`--save-config`**

##
compare [_replace_](replace.md)      
which is a bit like the (opposite intent) of apply





