
- ### Annotations
- **Key-Value** pairs that can be set on objects
- Like labels except
    - less restriction on size of name and value
    - _can_ **_not_** be **selected** on

    ```yaml
    apiVersion: v1              
    kind: Pod                   
    metadata:
        name: my-pod            
        annotations: # <-- **
            myAnno: "some long text with spaces"     # cant be used for search/selection
    ``` 

- ### list
    - `k` **`annotate`** `pod my-pod` **`--list`**


- ### set
    - `k` **`annotate`** `po my-pod [my-pod2 my-pod3]` **`my-key=' my long value that can have spaces'`**

- ### remove
    - `k` **`annotate`** `pod my-pod` **`my-key-`**