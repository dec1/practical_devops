

### Explicit

 
- #### stop
    - `d` **`stop`**  `my_ctr` 
        - or, if you have open terminal:
            - **`CTR+C`**  + `exit` stops container.
            - Note: just closing the terminal window, when logged into a running ctr, does not stop the container.
            -  after container is stopped its **state** is **preserved** - it will restart in same state as it stopped
    
    
- #### start:
    - `d` **`start`** `my_ctr`
    restart a stopped container 
    This causes the main process (ENTRYPOINT) to get rerun.
        - `d` `exec` `-it` `my_ctr` `/bin/sh`
        to get terminal if required

- ##### restart:
    -  **`restart`** = stop +  start

---




 

 ### Implcit (examples)
 If/how containers (self) teminate
- no loop (in shell)
    #####
    -  exit immediately
        `d` `run --name my_ctr` `-d`  `ubuntu /bin/bash` 
        `d` `run --name my_ctr`       `ubuntu /bin/bash`
    #####
    - **keeps running** in fg
    `d` `run --name my_ctr` **`-it`** `ubuntu /bin/bash`  
 #####

- **loop** (in shell)
    #####
    - runs in **background**
 `d` `run --name my_loop -d   ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"`   
    #####
     - runs in **foreground** (CRTL+C kills it (not just to bg), CTRL+Z (pause) has no effect)
    `d` `run --name my_loop      ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"`  
    `d` `run --name my_loop3 -it ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"`  