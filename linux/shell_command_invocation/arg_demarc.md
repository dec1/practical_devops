##  Argument Demarcation

### Shell invocation
- In both (script and command) forms, an **outer shell** starts an **inner shell**. 

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

    - Single vs Multiple args (visible to outer shell):
        - `/bin/sh` `-c` `'echo passed p0: $0, p1: $1'` `one two three`
            ```yaml
            passed p0: one, p1: two 
            # outer shell sets 3 cmd line parms for inner shell process
            # inner shell expands $0=one, $1=two 
            ```
            but

        - `/bin/sh` `-c` `'echo passed p0: $0, p1: $1,  one two three'`
            ```yaml
                passed p0: /bin/sh, p1: , one two three 
                # outer shell sets single (implicit) cmd line parm, for inner shell process
                # - the path of  inner shell process itself - just like for script invocation (see above) 
            ```



    - Multiple inner shell commands
        - all of **`other_parms`** is available (to all inner commands) inside script (`$`) or cmd (`\$`) as 
            - `$0`, `$1`, `$2`, ...
                -  `$@` = `$1`, `$2`,...
        ###
        - `/bin/sh -c '` 
        `echo *1* passed p0: $0, p1: $1, p@: $@` `&&`
        `echo *2* passed p0: $0, p1: $1, p@: $@` 
        `' one two three` 


            ```yaml
            *1* passed p0: one, p1: two, p@: two three
            *2* passed p0: one, p1: two, p@: two three
            ```




        ###
        - `/bin/sh -c '` 
        `echo *1* passed p0: $0, p1: $1, p@: $@` `&&`
        `echo *2* passed p0: $0, p1: $1, p@: $@` 
        `' one two three` 
###



- **Double** vs **Single Quotes**
    -  With double quotes (`"cmd"`) the outer shell first processes any (un-escaped)  special chars (eg $) and passes the result (unescaped) to the inner shell. With single quotes it does not (ie exactly same as script form) 
        - This is usual behaviour for single vs double quoted shell commands 

            - `/bin/sh` **`-c`** **`"cmd"`** `[other_params]`
            - `/bin/sh` **`-c`** **`'cmd'`** `[other_params]`

---

####
- **Always use quoted** string 
as otherwise only first word is treated as parm  ie
- `/bin/sh -c word1 word2` is interpreted (by outer shell) as 
    - `/bin/sh -c word1` followed by 
    - `word2`
###
- **Multiple** command args  
    - separate with [eg](multiple_cmds.md) `;` 

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
            