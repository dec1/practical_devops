                 
#### Create (Run), Apply


###
- `k`  **`apply`**  - *create* **_or update_** resource 
    - `k create - f res.yaml`  **declarative**, only



---

###
- `k` **`create`** create **only** (throws error if resource already exists).
    - `k create - f res.yaml`  **declarative**, or 
        
    - `k create <Kind> [parms]` **imperative**
        - all `Kind != pod` (see run)

    ##
    - `k` **`run`** = *`k create pod`*
(`create pod` should exist, but doesnt - inconsistent api - _create_ works     with every other resource kind)

---
####
- `create`, (`run`), `apply` 
    - _all_ **start pod** created           


---

####
- if updating (`apply`) - res must initially have been created with 
    - `apply`
    - `run` (doesnt need `--save-config`  - another inconsistency),  or
    - `create` **`--save-config`**

otherwise kubernetes complains about missing '*last-applied-configuration*'

