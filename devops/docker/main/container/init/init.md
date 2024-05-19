

### Dockefile USER, and running a container as root

- Container runs (init process - see below) as process with `pid = 1`
- This is analogous to `init` process (initializes user space etc) in standard linux startup, but in container it has no such special tasks - its just the first (userspace) process to run, and like in standard linux init process, all other   processes inherit from it (ie are direct or indirect child processes of it). 
See also [startup_init_process](../../../linux/startup_init_process.md)

- `running a container as root` simply means that the of this initial container `process` is that of root ie `uid, gid = 0` (**inside** the container, which is generally **mapped** from other >0 values on the **host**).
 This is discouraged as it is considered a security risk (since it makes it easier for someone who gets control of running container to also get more control of host os)




### Init Process

Usually a container has an 'init process'. While not strictly necessary, without one, the container would just terminate immediately after starting.

The command for the init process is specified by a [combination](./exec_shell_forms.md) of **`ENTRYPOINT CMD`** in Dockerfile and parameters to `docker`**`run`**, as follows:

- #### `ENTRYPOINT` 
    - **always** gets used as (**start** of) command to execute on container startup
    #####
    - typically: **executable** to run
    #####
    - **named** arg: passing `--entrypoint` to docker run can be used to override for ENTRYPOINT in dockerfile
    #####
    - This is what defines the single "main" process of a container and the only thing that gets re-executed when container restarts

- #### `docker run [COMMAND]`
     - if specified, COMMAND get [appended](./exec_shell_forms.md) to ENTRYPOINT as what to run in  at startup
     #####
     - typically: *options* to pass to the *executable* to be run
     #####
     - **positional** arg - everything directly after image name in docker run command is interpreted as COMMAND (and  **overrides** any **CMD** in dockerfile)
  
    - ####  `CMD`
    - default `COMMAND` (CMD is overridden by any COMMAND specified)

