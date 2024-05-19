


##### Build image (from dockerfile)

- `d` **`build`** **`-t`** `my_img[:my_tag]` `[`**`--file`** `<my_dockerfile>]` **`<build-context>`**
    ####
  - `my_tag` default: latest
  - `my_dockerfile`: default `./Dockerfile`
  - **`build-context`** eg
   directory - all files and sub directories (recursive)  are copied as the [build context](https://docs.docker.com/build/building/context/) and made available during build of container
    - `. ` (curr dir)
 my_dockerfile

    - `docker build -t my_img .`
    build an new image "my_img" from 'Dockerfile' in and context being current dir (".")
 
Example:
- alpine.df
    ```yaml
    FROM alpine
    ENTRYPOINT ["bin/echo", "ep..."]
    CMD ["cmd1..."]
    ```
    - `d build -t my_alp --file alpine.df .`

        ```yaml
        Successfully built cb343a9d59ca
        Successfully tagged my_alp:latest
        ```


##### Layers 
FROM, ENTRYPOINT, CMD, RUN etc in Dockerfile instructions define the **layers** of changes from base image             

