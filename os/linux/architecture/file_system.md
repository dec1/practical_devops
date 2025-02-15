#### File (System)

- ##### inode 
    - _metadata_ about the file (permissions, owner, size, etc)
    _where_ `data blocks` are

    - ##### data (blocks)
        - the actual data

##
- ##### dir (entries) 
    - maps: 
        `filepath` (key)  -> `inode` (val)
    
##
- ##### links

    - **sym** (new: key, val)
        a new file, the data blocks of which contains file system path (dir entry) of original.
        new key and value in file system map
    
    ####
    - **hard** (new: key)
        a new entry in the file system map - new key with same value (inode)
        (inode stores how many hard links point to it, so os knows can deleted when count == 0)


