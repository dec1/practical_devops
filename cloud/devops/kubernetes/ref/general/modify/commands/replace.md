                 

#### Replace
- `k`  **`replace`**  `-f res.yaml` `[--force]`

    ####
    - if resource **does** already exists:
        - _replace_ it 
            - if `--force` passed, deletes the object completely first, allowing changing [immutable fields](../modify.md) 
            - without _--force_, fails on any attempt to change immutable fields 
    - if resource doesnt **not** already exist:
        - create it if `--force` passed
        - fail otherwise



##
_replace_ is bit like the _opposite of apply_  - both try to find an existig resource in order to change it, but whereas

- `apply` (replace **_selectively_**) 
tries hard to selectively modify specific part(s) of the object state, with the config passed (thus maintainng any fields automatically added by kubernetes)

#####
- `replace` (replace **_completely_**) 
unconditionally overwrites all the resource state with the config passed, (intentionally overwriting any fields automatically added by kuberenetes)

        






