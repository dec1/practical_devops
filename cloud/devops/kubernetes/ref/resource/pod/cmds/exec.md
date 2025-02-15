

## Exec

- **`k exec`** `(POD) [-c CONTAINER] [flags]` **`-- Cmd`** 
**execute Cmd** in container (default: first) of pod.

    ####
    - `k exec mypod` **`-- env`**
    Get output from running the 'env' (show env vars) command from first container in mypod
    
    ####
    - `k exec my-pod` `[-c my-ctr]` **`-- /bin/bash -c`** `"env & ls /etc/config && echo"` 
    prefixing with `/bin/bash -c ` allows you to put **multiple commands** (in _"....."_)
    
    ####
    - open (and keep open) interactive shell (in container my-ctr) of my-pod 
    `k exec` **`-it`** `my-pod [-c my-ctr]` **`-- /bin/bash`**

    ####
    compare
    - docker [ shell amd exec forms](../../../../../docker/main/container/init/exec_shell_forms.md) and 
    - linux [shell argument demarcation](../../../../../../../os/linux/shell_command_invocation/arg_demarc.md)










