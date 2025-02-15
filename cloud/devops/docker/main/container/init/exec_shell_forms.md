
### Shell and exec form

- The `RUN`, `CMD`, and `ENTRYPOINT` instructions all have [two possible forms](https://docs.docker.com/reference/dockerfile/#shell-and-exec-form):

##
- **1) Exec Form** (prefer)
`INSTRUCTION ["executable","param1","param2"] `
####
- **2) Shell Form**
`INSTRUCTION command param1 param2 `            
  
    - Pro: Variable expansion (`sh -c`) automatically prepended 
    - Danger: when used with ENTRYPOINT,  it will ignore any CMD or docker run command line arguments

- Note: `INSTRUCTION "command param1 param2"     `  
    wont work in general as the a command called "command param1 param2"  wil not exist

   
[Understand how CMD and ENTRYPOINT interact](https://docs.docker.com/reference/dockerfile/#understand-how-cmd-and-entrypoint-interact)

#### Recommend:
- Prefer exec form and _manually include shell invocation_ eg:

**`ENTRYPOINT`** **`["/bin/bash", "-c", "echo hello && echo hoo"]`**

see also [argument demarcation](../../../../../../os/linux/shell_command_invocation/arg_demarc.md)

---
Examples:
 - 1). Command 
    -  `/bin/echo`
        ```docker
        FROM alpine
        ENTRYPOINT ["bin/echo", "ep..."]
        CMD ["cmd1..."]
        ```

        - `d rm my-ctr ; d build -t my-img --file df . && d ` **`run`** `-it --name=my-ctr my-img `

            ```yaml
            ep... cmd1...
            ```

        - `d rm my-ctr ; d build -t my-img --file df . && d ` **`run`** `-it --name=my-ctr my-img` **`uno dos tres`**

            ```yaml
            ep... uno dos tres
            ```

        - `d rm my-ctr ; d build -t my-img --file df . && d`  **`run`** ` -it --name=my-ctr` **`--entrypoint='["/bin/echo", "hey.."]'`** `my-img`  `uno dos tres`

            ```yaml
            hey.. uno dos tres
            ```

- 2). Sub shell 
    - `/bin/sh`
        ```docker
        FROM alpine
        ENTRYPOINT ["/bin/sh", "-c", "echo ep ... && echo p0: $0, p1: $1,  pa: $@ "]
        CMD ["one", "two", "three" ]
        ```

        - effectively becomes:
            - `/bin/sh -c` `"echo ep ... && echo p0: \$0, p1: \$1,  pa: \$@\" "` `one two three`
                - Note: docker implicitly adds the [necessary escapes](../../../../../../os/linux/shell_command_invocation/arg_demarc.md)
            ###
            - `d rm my-ctr ; d build -t my-img --file df . && d` **`run`** `-it --name=my-ctr my-img`
                ```yaml
                ep ...
                p0: one, p1: two, pa: two three
                ```

            - `d rm my-ctr ; docker build -t my-img --file df . && d ` **`run`** ` -it --name=my-ctr my-img   uno dos tres `
                ```yaml
                ep ...
                p0: uno, p1: dos, pa: dos tres
                ```

        
