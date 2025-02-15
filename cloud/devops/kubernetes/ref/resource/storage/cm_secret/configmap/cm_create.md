#### Create 
 There are 4 ways (from literal, file, env...) to provide the values for a configmap, but the resulting configmap is **independent of method**  chosen
<br>

1 **Literal** value(s)

- `k` **`create configmap`** `my-cm` **`--from-literal=one=1 --from-literal=two=2`** 
    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
        name: my-cm

    data:       ## <-- same regardless of how configmap create
        one: "1"
        two: "2"

    ```
    - `k` **`describe`** `configmap  cm`
        ```yaml
        Name:         cm
        Namespace:    default
        Labels:       <none>
        Annotations:  <none>

        Data
        ====
        one:
        ----
        1
        two:
        ----
        2
        ```
<details>
  <summary> Other Methods </summary>

2 **File**  

- **my-file**

    ```python
    # contents are valid `env file` 
    # but can be equally be read as multiline (non-env) file
    one=1
    two=2
    ```


- 1. **env-file**  - interpreted with _each_ **line**  as  `key=value` 
        - `k create cm my-cm` **`--from-env-file`**`=my-file-path --dry-run=client -o yaml`

            ```yaml
            apiVersion: v1
            kind: ConfigMap
            metadata:
                name: my-cm

            data:           # no mention of (env) file name (myfile) 
                one: "1"            # (one, 1)
                two: "2"            # (two, 2)    
            ```

- 2. **file** interpreted as _single_ (key = file name, value = *complete* **contents** ) 

        - `k create cm my-cm` **`--from-file`**`=[my-key=]my-file-path --dry-run=client -o yaml`

            ```yaml
            apiVersion: v1
            kind: ConfigMap
            metadata:
                name: my-cm

            data:
                my-key: |          # my-key (basename of file-path used if omitted)
                    one=1           #  ->  single (multi-line value) (my-file contents: one=1 \n two=2)
                    two=2
            ```

    3. **Directory** 
        -   **list** of (*single*) file name -> file lines
        <br>
            ``` python
            my-dir          
                /my-file        # (my-file  contents: one=1 \n two=2 )
                /my-file1       # (my-file1 contents: one1=11 \n two1=22)
            ```

        - `k create cm my-cm` **`--from-file=my-dir`** ` --dry-run=client -o yaml`

            ```yaml
            apiVersion: v1
            kind: ConfigMap
            metadata:
                name: my-cm
                                # each file name of dir used as key with single (multi-line value)
            data:                       
                myfile: |                  
                    one=1                   
                    two=2
                myfile1: |                  
                    one1=11
                    two1=22
            ```

        -  cant use "from-env-file" with dir 
        `k create cm my-cm` **`--from-env-file=my-dir`** `--dry-run=client -o yaml`
            "Error..."
</details>