
## `ls` 

List details of file or  dir 

- **`ls`** [`-flags`] `some_file_or_dir`  
    - `flags`
        - `a`- all -  including hidden files
        - `i`: show inode number
        - `l` - long -  include additional columns with  detailed information about each file and directory
        .....

    ####
    - `ls -lai beep.mp3`

        ```yaml
        54429604 -rw-r--r--  1 declan  staff  733645 Feb 29  2024 beep.mp3
        ```

##
##### Understanding Output (format)
| inode_num | Type (1) |  Permission Bits <br> (_File Mode_) <br>(9)      | num hardlinks | owner  | group  | size (in bytes) | mtime (last modified) |  name |
|-----------|----------|------------------|---------------|--------|--------|------------------|-----------------------|----|
| 54429604  | -        | -rw-r--r--      | 1  | declan | staff  | 733645 | Feb 29  2024 beep.mp3 | beep.mp3 | 


- ##### inode number
    see [file_system](../../architecture/file_system.md)



##
- ##### Type (1 character)

    - `-` : Regular file  
    - `d` : Directory  
    - `l` : Symbolic link  
    - `c` : Special file - Character (stream of bytes, e.g., terminal)  
    - `b` : Special file - Block (blocks of data, e.g., CD drive)


#
- #### `Permission  Bits` (9 characters)
    Also known as `File Mode`
    see [permission_bits](permission_bits.md)

##    
Examples

 - `touch me.txt`
  - `ls -lai me.txt`
    ```bash
    76360598 -rw-r--r--  1 declan  staff  0 Feb 11 15:26 me.txt
    ```
 - `chmod u+s me.txt` `( - -> S)`
 - `ls -lai me.txt`
    ```bash
    76360598 -rwSr--r--  1 declan  staff  0 Feb 11 15:26 me.txt
    ```

 - `chmod u+x me.txt` `( S -> s)`
 - `ls -lai me.txt`
    ```bash
    76360598 -rwsr--r--  1 declan  staff  0 Feb 11 15:26 me.txt
    ```



- `ls -lai mydir`
    ```bash
    total 0
    76360728 drwxr-xr-x   2 declan  staff    64 Feb 11 15:27 .
    747562 drwxr-xr-x+ 89 declan  staff  2848 Feb 11 15:27 ..
    ```
 
  - `chmod +t mydir`  `( - -> t)`
  - `ls -lai mydir`
    ```bash
    total 0
    76360728 drwxr-xr-t   2 declan  staff    64 Feb 11 15:27 .
    747562 drwxr-xr-x+ 89 declan  staff  2848 Feb 11 15:27 ..
    ```
