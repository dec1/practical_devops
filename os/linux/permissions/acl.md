### Access Control Lists (ACLs)


_Extends permission modes_ of file/dir (which allow setting access permissions on file/dir for owner, group and other of the file/dir) to allow setting (individual) _access_ **permissions** to **arbitrary users and groups**.




```mermaid
---
title: Example ACL in File
---
graph LR

    subgraph users[Users]
        bob[bob] --> bobp["rwx<br/>(read, write, execute)"]
        kate[kate] --> katep["r--<br/>(read)"]
        alice[alice] --> alicep["rw-<br/>(read, write)"]
    end

    subgraph groups[Groups]
        dev[developers] --> devp["rwx<br/>(read, write, execute)"]

    end

    subgraph others[Others]
        other[other] --> otherp["r--<br/>(read)"]
    end

    style users fill:#e6ffe6,stroke:#333
    style groups fill:#ffe6e6,stroke:#333
    style others fill:#e6e6ff,stroke:#333
    style bob fill:PaleGreen 
    style kate fill:PaleGreen 
    style alice fill:PaleGreen  
    style dev fill:#FFB6C1
    style other fill:#B0C4DE
    %% style bobp,katep,alicep,devp,qap,otherp fill:#f9f9f9

    users ~~~ groups ~~~ others
```
- The effective permissions a process gets, are the most restrictive set of permissions derived from (combining) both the ACL entries and the traditional Unix permissions.

---

### ACL Commands

`setfacl` and `getfacl` commands are used to set/get acls on specific files/dirs

- Set ACLs
    - **`setfacl`** **`flags`** **`entry`** `<file_or_dir_path>`

        - `flags`:
            - **`-m`**: modify/add entry
            - **`-x`**: remove entry
            - **`-b`**: remove all entries
            
            ######   
            - **`-d`**: set default (directory only)
            - **`k`**:  remove-default

        #####
        - `entry`:
            - `(`**`u`**`|`**`d`**`)` `:<(username|groupname)>:` **`[r][w][x]`**

###
- Get ACLs
    - **`getfacl`** [`flags`] **`entry`** `<file_or_dir_path>`



##
##### Examples
```bash
# Give user bob read & execute permissions on file
setfacl -m u:bob:rx file.txt

# Set default ACL on directory - all new files inside will inherit:
# group 'devs' gets read & write
setfacl -d -m g:devs:rw dir/

# Multiple ACLs in one command:
# - user bob gets read & execute
# - group devs gets read & write
setfacl -m u:bob:rx,g:devs:rw file.txt

# Show all ACLs on file
getfacl file.txt

# Remove just bob's ACL entry
setfacl -x u:bob file.txt

# Remove all ACL entries (back to basic unix permissions)
setfacl -b file.txt

# Remove all default ACLs
setfacl -k dir/
```