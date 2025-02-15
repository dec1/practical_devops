##  Argument Demarcation

### Shell invocation
- In both (script and command) forms, an **outer shell** starts an **inner shell**. 
The inner shell made be started from a script (file) or from a command (-c):

see also docker [ exec_shell_forms](../../../cloud/devops/docker/main/container/init/exec_shell_forms.md) 
- #### Script
    - `[/bin/sh]` `script` `[other_params]`
        
        - tst.sh
            ```yaml
            #!/bin/sh
            echo hi there && echo passed p0: $0, p1: $1, p@: $@  
            ```  
        - `[/bin/sh]` `./tst.sh` `one two three`
            ```yaml
            hi there
            passed p0: /Users/declan/Documents/zone/low/tmp/tst.sh, p1: one, p@: one two three
            ```

            - _Note_: extra `$0` - implicit:  **script path** is **pre**-pended to `other_params` (cf command -c)
- #### Command (-c) 

    - args visible to outer shell:

        ####
        - Multiple:
            - `/bin/sh` `-c` `'echo passed p0: $0, p1: $1'` `one two three`
                ```yaml
                passed p0: one, p1: two 
                # outer shell sets 3 cmd line parms for inner shell process
                # inner shell sees parameters $0=one, $1=two 
                ```
                
        - Single (~> script like):
            - `/bin/sh` `-c` `'echo passed p0: $0, p1: $1,  one two three'`
                ```yaml
                    passed p0: /bin/sh, p1: , one two three 
                    # effectively like as if inner shell were called from script with (textual) content equal to everything after `-c`
                    # - inner shell sees parameters: $0=/bin/sh, $1=
                    # inner shell only gets path to outer shell aas parameter (just like script would)
                ```



    - Multiple inner shell commands
        - all of **`other_parms`** is available (to all inner commands) inside script  as 
            - `$0`, `$1`, `$2`, ...
                -  `$@` = `$1`, `$2`,...
        ###
        - `/bin/sh -c '` 
        `echo *1* passed p0: $0, p1: $1, p@: $@` `&&`
        `echo *2* passed p0: $0, p1: $1, p@: $@` 
        `' one two three` 

            #####
            ```yaml
            *1* passed p0: one, p1: two, p@: two three
            *2* passed p0: one, p1: two, p@: two three
            ```



###



- **Double** vs **Single Quotes**
    -  With double quotes (`"cmd"`) the outer shell first processes any (un-escaped)  special chars (eg $) and passes the result (unescaped) to the inner shell. With single quotes it does not (ie exactly same as script form) 
        - This is usual behaviour for single vs double quoted shell commands 

            - `/bin/sh` **`-c`** **`'cmd'`** `[other_params]`
                - `/bin/sh -c 'echo passed p0: $0, p1: $1' one two three`
                ```yaml
                passed p0: one, p1: two
                ```

            - `/bin/sh` **`-c`** **`"cmd"`** `[other_params]`
                - `/bin/sh -c "echo passed p0: $0, p1: $1" one two three`
                    ```yaml
                    passed p0: bash, p1:
                    ```
                - the outer shell expanded $0 and replaced it with "bash" before calling inner shell, which got no parameters

---

####
- **Always use quoted** string 
    - as otherwise only first word is treated as parm  ie
        - `/bin/sh -c word1 word2` is interpreted (by outer shell) as 
            - `/bin/sh -c word1` followed by 
            - `word2`

###
- **Prefer** `'..$..'` to `"..$.."` for quoted string
    - (or escape:  `$` -> `\$`)
    -  if you want inner shell to see $ 
 
###
- **[Multiple](multiple_cmds.md)** command args  
    - separate with [eg](multiple_cmds.md) `;` or `&&` 

        - `/bin/sh -c 'cmd1; cmd2'`
    or
        - `/bin/sh -c "cmd1; cmd2"`

---


-   **Named** and **Positional** *command-line* arguments" 

    - final `--` is treated as begin of positional arguments
        - `some_cmd` **`p1`**`=12`  **`p2`**`hey` **`-p3`** `you` **`--p4`**`=40` **`-- arg1 arg2`**
            - `arg1`, `arg2 `
                - **positional** arguments
            - `p1`, `p2, `p3, `p4` 
                - **named** arguments
    ###            
    - **Convention** only - every `some_cmd` is free to parse and interpret all arguments (including `--`) as it wishes.
            