### Computer Startup

After power on
- **cpu** loads instructions (via memory and registers) from (BIOS/UEFI) **firmware** , which 
- initializes (essential) **hardware**, and 
- loads the **bootloader**. (See also [storage](../../storage/overview.md)).  The bootloader 

###
- loads the os **kernel**. When the kernel is finished initializing (_kernel space_), it 
- loads **user space** and starts first process (init) 

###
- **[init process](init_process.md)**  starts with `pid = 1`, and has `uid/gid = 0` (ie is process associated with user **root**) 
    - its the first process, and parent (direct/indirect) of all others (which all get pid >1) 
    - Note: **shell** and system **services** are also just (userspace)  processes

####
- init starts a _login process_ (pid > 1, uid/gid = 0)
    - if/when user logs on the login process starts a new process:
        - the user's **login shell** (which gets uid/gid of this user)  
        every other shell, and thus every process the user starts (in any shell),  is a (direct or indirect) subprocess of the login shell. (see also [shell config](shell_config.md))



