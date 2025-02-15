
Multiple commands on same line

- #### Sequential  
    - `cmd1` **`&&`** `cmd2`
     **conditional**: cmd2 after cmd1 _only if_ cmd1 succeeded (exit status 0).
    <br>
    
    - `cmd1` **`;`** `cmd2`
    **unconditional**: cmd2 after cmd1 (even if cmd1 failed)

 

 - #### Concurrent
   - `cmd1` **`&`** `cmd2`
    cmd1 and cmd2 both run at **same time** (cmd1  in the bgd, cmd2 in fgd)

    ###
   - `cmd1` **`|`** `cmd2`
    cmd1 and cmd2 both run at **same time**, with any stdout cmd1 produces becoming (more or less immediately - some buffereing may be involved) available as stdin for cmd2