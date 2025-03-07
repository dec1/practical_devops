
### Union Filesystem: 
- Efficiently layered filesystems (e.g. OverlayFS) 
    - combines 
        - **multiple read-only** layers, and
        - **single read-write** layer 
      of data to create a single unified view (for processes)

    #####
    - each **layer** in the container image represents a **delta** - modifications or additions to the base file system and only stores the actual differences between layers, not duplicate data.      

    #####
    - versioning -  Layers act as versions, allowing you to easily revert to previous configurations if needed.

    #####
    - **sharing** of  read-only layers, between multiple containers/images 



