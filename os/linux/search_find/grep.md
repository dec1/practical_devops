## Search Content



- ### Grep
    - Source file/Dir
        - **`grep`** `"textToFind"`  `[startDir] [-r]` **`file_pattern`**   `[-i]`   `[-Cn|-Bn|-An] [-E]`
    - Pipe 
        - **`some_command | grep`** `"textToFind"` `[-i]` `[-Cn|-Bn|-An]`        
            ###
            
            - `-i` case insensitive 
            #####
            - `startDir` default = curr dir 
            - `-r` recurse (below startDir)

            ####
            - `textToFind` can be a regex (pattern)
            - `file_pattern ` pattern of file names to search (eg *bla.txt myfile.txt)
            #####
            - `-An` show `n` following (**after**) lines in results
            - `-Bn` show `n` preceding (**before**) lines in results
            - `-Cn` show `n` context (before **_and_** after) lines in results

            ####
            - `-E` _extended grep_ (like **`egrep`** - an extension of grep)
                some "special" characteres
                - `+`
                - `?`
                -  `|`
                - `()` 
                no longer need escaping:

                    ####
                    - `ls /` `|`  `grep` **`-E`** `"h`**`|`**`m"` 
                    or
                    - `ls /` `|`  `grep`  `"h`**`\|`**`m"` 
                        ```yaml
                        home
                        media
                        mnt
                        tmp
                        ```                    
    
