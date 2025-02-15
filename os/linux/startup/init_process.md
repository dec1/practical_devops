

### init process 



- **process** - One only speaks of processes (or programs) as running in (context of) user space.
In kernel space and before user space starts, cpu runs instructions, but they are not considered programs/processes. 


#####
- init is the first process to starts, and it does so with  `pid = 1` (all other processes are direct or indirect children and get  get pid >1)

####
-   Note: **shell** and system **services** are also just (userspace) processes


####
- **responsible** for [service management](service_man.md)  and other special tasks.
        

    - **container**
        the first process in a container is also a [container init process](../../../cloud/devops/docker/main/container/init/init.md) with pid=1, but it has **no** such special **responsibilities**, and is often 'just' a shell. 
        container init is defined by `ENTRYPOINT/CMD` of dockerfile, or parameters passed to `docker run`. 
        See also [container init](../../../cloud/devops/docker/main/container/init/init.md)


- **systemd** - (most modern) and sysVinit are common implementations of init. 
    - [systemctl](service_man.md) - systemd service management interface eg `sudo systemctl start some-service`
- **booting** - init starting marks the end of booting (technically)

- **root** - is the first user created in userspace and has `uid, gid = 0`

