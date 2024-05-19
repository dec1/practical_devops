### Operator (Pattern)
The combination of **custom** (user defined):
- #####  1) Schema (Crd)
    - describes structure of custom resource
    - a) `k apply` **schema** (kind: CustomResourceDefinition) 
        - adds a new **resource type** to Kubernetes API
    - b) `k apply` manifest (kind: resource type + any other  **values**)  
        - creates (custom) object 
            - just like built-in
   

- ##### 2) Controller 
   - Polls api for state of (custom) objects, and takes action based on
      - how different this is from desired state (eg as specified in object manifests), and 
      - other arbitrary logic

#### Schema
- crd.yaml
    ```yaml
    apiVersion: apiextensions.k8s.io/v1
    kind: CustomResourceDefinition
    metadata:
      name: smoketests.stable.bmuschko.com      # <plural>.<group>  <--* NB
    spec:
      group:           stable.bmuschko.com      # API Group ~ "core" for built-in resources
      versions:
        - name: v1                              # single version
          served: true
          storage: true
          schema:
            openAPIV3Schema:
              type: object
              properties:                 
                spec:
                  type: object
                  properties:                   #  prop values - specify  when creating objects 
                      service:
                        type: string
                      path:
                        type: string
                      timeout:
                        type: integer
                      retries:
                        type: integer
      scope: Namespaced
      names:                                 
        plural: smoketests                      # -> metadata.name (see above)
        singular: smoketest
        kind: SmokeTest
        shortNames:
        - st
    ```



- `k apply -f crd.yaml`
    - verify 
        - `k api-resources` **`--api-group=stable.bmuschko.com`**
            ```js
            NAME         SHORTNAMES   APIVERSION               NAMESPACED   KIND
            smoketests   st           stable.bmuschko.com/v1   true         SmokeTest
            ```

        - `k get` **`crd`**
            ```js
            smoketests.stable.bmuschko.com                        2024-02-22T11:42:08Z
            ....
            ```

### Values 
- find properties whose values need be specified  when **creating objects** in b). above

    - 1). `k get` **`crd`** `smoketests.stable.bmuschko.com -o yaml`  <sub>(undocumented !) </sub>

        ```yaml
        names:
            kind: SmokeTest
            listKind: SmokeTestList           #    need to specify 
            plural: smoketests
            shortNames:
        .....
        properties:
            spec:
            properties:                     #    need to specify 
                path:
                type: string
                retries:
                type: integer
        .....        
        ```


        - Note:  **without** the **`crd`** you get little!
            `k get  smoketests.stable.bmuschko.com -o yaml`

            ```yaml
            apiVersion: v1
            items: []
            kind: List
            metadata:
            resourceVersion: ""
            ```

    - 2). **`k explain`** `smoketest`.spec

        ```yaml
        GROUP:      stable.bmuschko.com
        KIND:       SmokeTest           #    need to specify 
        VERSION:    v1

        FIELD: spec <Object>
        .....
        DESCRIPTION:
            <empty>
        FIELDS:
            path <string>                   # need to specify 
                <no description>

            retries <integer>
                <no description>
        ....
        ``` 
#### Objects 
- st.yaml 
    sets property values found above

    ```yaml
    apiVersion: stable.bmuschko.com/v1   ## <group>/<version> from crd
    kind: SmokeTest                      # <kind> from crd
    metadata:
      name: my-st
    spec:                                # prop values 
      service: backend                   
      path: /health                      
      timeout: 600                      
      retries: 3                          
    ```
- `k apply -f st.yaml`

    - verify 
        - `k get st [-o yaml]`
            ```yaml
            NAME    AGE
            my-st   3s
            ```
- `k delete -f st.yaml`, or
- **`k delete crd`** `smoketests.stable.bmuschko.com`

    removes resource from api **and** deletes all objects that were created
    #####
    - **`k get crd`** `smoketests.stable.bmuschko.com [-o yaml]`
        ```yaml
        Error ... NotFound
        ```        

    - **`k get st`**
        ```yaml
        Error ... NotFound
        ```