## Labels
- **Key-Value** pairs that can be set on objects
- Objects can be **selected** by key [and value]
- key/value fairly limited eg 
    - each max **63** `lowercase [a-z]`, `[0-9]`, `-`, `.`
    - key additionally:
        - may contain single `/`
        - must start and end with lowercase [a-z]

 ###
 -
    ```yaml
    apiVersion: v1              
    kind: Pod                   
    metadata:
        name: my-pod            
        labels:    # <-- **
            myLab:  "some-label-value"              # no spaces -can be used from search/selection (label selectors - service, kubectl -l)
    ``` 

- ### select

    ###
    - `k` **`get`** `pods` [**`--show-labels`**] [**`-l key-01[=val-01]`**`,key-02!=val-02`]  [,**`-l 'key in (val1, val2)'`**]
 
        #####
        - **`-l key[=val]`** only with labels exact match -  has `key` [with value `val`]

            - `-l` ~ `--selector` (equivalent)

        - `-l 'key in (val1, val2)'` only which has label with key, and value that is one of val1, val2
        #####
        - `,` **AND** logical (for combining filters)
        - `=` ~ `==` (equivalent)
        - **`!=`**`val`, **`notin`**`(val1, val2)` also supported
    
        #####
        - **`--show-labels`** show labels (in dedicated column)
            ```yaml
            NAME       READY   STATUS    RESTARTS   AGE     LABELS
            my-pod-1   1/1     Running   0          2m35s   key1=val1,key2=val2
            ```
            - cf `k label --list`

- ### list 
    - `k` **`label`** `pod my-pod` `[my-pod2 my-pod3]` **`--list`**
        ```yaml
        key1=val1
        key2=val2
        ```
        - cf  ` k get --show-labels`

- ### set

    - `k` **`label`** `pod my-pod` `[my-pod2 my-pod3]` **`k1=v1 [k2=v2]`** `[--overwrite]`
        set label `key` of my-pod to `val`
        - `[--overwrite]` -  required if label already exists


- ### combined
    set new label on pods with (existing) label key=val 
    - `k label pod` **`-l key=val`** **`key-new=val-new`** `[--overwrite]` 


- ### remove
    - `k label pod my-pod` `[my-pod2 my-pod3]` **`lab-key-`**
    remove label with key `lab-key-` from pod(s)
    does not require --overwrite