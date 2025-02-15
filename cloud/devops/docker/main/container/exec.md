
#### exec
- `d` **`exec`** `[-it]` `my_ctr` **`<some_cmd>`**
    - **`<some_cmd>`** - eg
        - `/bin/sh` 
        - `echo 'hi there'`
        - `/bin/sh -c "echo 'hi there' "`
        - `env`
    Run a command in (already) running container

---

- ##### attach

    - `d` **`attach`** `my_ctr`
    attach to my_ctr running in bgd (gets you a terminal prompt)

    - Depending on the container and how it was started, _attach_ [may not work](https://docs.docker.com/engine/reference/commandline/attach/#options)

    - Prefer more general "exec" command instead to execute a (new) command in a running container


