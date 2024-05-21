### Computer Startup

After power on
- **cpu** loads instructions (via memory and registers) from **firmware** (eg bios/uefi), which 
- initializes (essential) **hardware**, and 
- loads the **bootloader**. The bootloader 
- loads the os **kernel**. When the kernel is finished initializing (_kernel space_), it 
- loads **user space** and the first process is 
- **init** process starts with `pid = 1` (as first and process in suer space, and parent (direct/indirect of all others including any shell, and get pid >1).

### init process 
- **process** - One only speaks of processes (or programs) as running in (context of) user space.
In kernel space and before user space starts, cpu runs instructions, but they are not considered programs/processes). 

- **responsible** for `service` management and other special tasks.
        

    - **container**
        the first process in a container is also init process with pid=1, but it has **no** such special **responsibilities**, and is often 'just' a shell. 
        container init is defined by `ENTRYPOINT/CMD` of dockerfile, or parameters passed to `docker run`. 
        See also [container init](../devops/docker/main/container/init/init.md)


- **systemd** - (most modern) and sysVinit are common implementations of init. 
    - **systemctl** - systemd service management interface eg `sudo systemctl start some-service`
- **booting** - init starting marks the end of booting (technically)

- **root** - is the first user created in userspace and has `uid, gid = 0`

- **container** there is also an init process, which is that 
