

 
- **base64** command line tool

    ###
    -  **encode**
        - `echo "1" |` **`base64`**
            or
        - **`base64`** `<<< "1"`

            ```yaml
            MQo=
            ```

    - **decode**
        - `echo "MQo=" |` **`base64 -d`**
        or 
        - **`base64 -d`** `<<< "MQo="`

            ```yaml
            1
            ```