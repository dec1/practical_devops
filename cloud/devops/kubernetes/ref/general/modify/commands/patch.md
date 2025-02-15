# `patch`

Modify Kubernetes resources (or manifests thereof) by _patching_ specific fields.
 Three patch strategies are supported:



| Feature          | 1). Strategic Merge <br> (prefer) | 2). JSON  | 3). JSON Merge  <br> (avoid) |
|-------------------|-----------------------|-------------------|-------------------|
| Default          | Yes   |                | - |
| Complexity       | Medium                  | High               | Low              |
| List Handling    | Merge-by-name <br> (of merge key) <br> with lists | _Index_ -based operations <br> **op**  (`add`,`replace`, `remove`...) <br> **path**,  **value** | Replaces entire list  |




### Example - Update Deployment Replicas

- ##### deploy.yaml
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-dep
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: my-app
      template:
        metadata:
          labels:
            app: my-app
        spec:
          containers:
          - name: my-ctr
            image: nginx
    ```
##
- **Example a)** - change (**scaler**) **`replicas`** (_3_ -> _5_)
    - **Not changing** (item of) **list** - all 3 merge types can be used
    ```yaml
    ....
    spec:
      replicas: 5
    ....
    ```
    -  1). **Strategic Merge** (default)
        - `k patch` `-f deploy.yaml --dry-run=client -o yaml` *`-p '{"spec":{"replicas":5}}'`* [**`--type strategic`**]


    -  2). **Json** (`op`, `path`, `value`)
        - `k patch` `-f deploy.yaml --dry-run=client -o yaml`  `-p '[{"op":"replace","path":"/spec/replicas","value":5}]'` **`--type json`**



    - 3).  **Json Merge**
        - `k patch` `-f deploy.yaml --dry-run=client -o yaml`  `-p   '{"spec":{"replicas":5}}'` **`--type merge`**
###
- **Example b)** - change (**list**) **`image`**  (_nginx_ -> _httpd_)
    - **Changing** item of **list** - 3rd JSON merge **cannot** be used

        - Both of first 2 work (2nd is however not robust since it hardcodes index). 

            ####
            -  1). **Strategic Merge** (prefer)
                uses _merge-by-name_ patch _strategy_  for lists
                -  `k patch` `-f deploy.yaml --dry-run=client -o yaml` `-p '{"spec":{"template":{"spec":{"containers":[{"name":"my-ctr","image":"httpd"}]}}}}'` [**`--type strategic`**]

                ###
                ###### Merge-by-Key patch strategy  (with lists)
                When applying a strategic merge patch (ie `--type strategic`), to resource types that contains **lists**, a *patch strategy* of **merge-by-key** is used. 
                You must specify a value for the merge key(s), with *list* operations, or the patch fails. eg:
                - pod.spec.`containers` uses `name` as merge key
                - pod.spec.`volumes` uses `name` as merge key
                - pod.spec.`tolerations` uses `key` and `effect` as merge keys

                #####
                If an item with matching merge key(s) exists:
                - yes - patch updates only specified fields
                - no - patch adds as new list item
               

            ####
            -  2). **Json** (index-dependent)
                -  `k patch` `-f deploy.yaml  --dry-run=client -o yaml` `-p '[{"op":"replace","path":"/spec/template/spec/containers/0/image","value":"httpd"}]'` **`--type json`**

                ###
                ```
                spec:
                containers:
                - name: my-ctr
                    image: nginx
                ```
        ##
        - avoid- doesnt work   - replaces all lists with this (exact) single list 

            -  3). **JsonMerge**
                - `k patch` `-f deploy.yaml --dry-run=client -o yaml` `-p '{"spec":{"template":{"spec":{"containers":[{"image":"httpd"}]}}}}'` **`--type merge`**
            
                ###
                ```
                spec:
                containers:
                - image: nginx   # ❌ name field removed!, as well as (all  of) any other containers 

                ```




    





