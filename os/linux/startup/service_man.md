# Service Management 

- ## systemd 
    One of the most common implementaions of [init](init_process.md), which can be interacted with via:
    
    - ### systemctl
        The systemd  interface
        #####
        - sudo **`systemctl`** **`start`** `kubelet`       
        - sudo `systemctl` **`stop`** `kubelet`  
            - ***edit** unit* (config) files requires *daemon-reload* before restart  
            sudo `systemctl` **`daemon-reload`**     
        - sudo `systemctl` **`restart`** `kubelet`    
        - sudo `systemctl` **`status`** `kubelet`    
        - sudo `systemctl` **`enable`** `kubelet`      
        - sudo `systemctl` **`disable`** `kubelet`   

        ###
        list services
        - sudo `systemctl` **`list-units` `--type=service`**


    - ### units

        A **configuration** object that represents a **system resource** or service. Units define how systemd should manage that resource, including its start-up, shut-down, and dependency behavior.

        ###
        - Location:
            #####
            - **`/lib/systemd/system/`** 
            - **`/usr/`** **`lib/systemd/system/`**
                
            ####
            - custom/override: 
                - `/etc/systemd/system/`
            #####
            - user-specific:
                - `~/.config/systemd/user/`


        ###
        - Types
            - **Services**
            - Sockets
            - Mounts
            - Paths
            - Timers
            - Swap Space
            ....


---
Managing services with sysVinit (legacy)
 
 Note: on systemd-based systems, the `service` command is a compatibility wrapper around systemctl, so both "work"
- ####  sysVinit 

    
    - sudo **`service`**  `kubelet` **`start`**      
    - sudo `service` `kubelet`  **`stop`**       
    - sudo `service`  `kubelet` **`restart`** 
    - sudo `service`  `kubelet`    **`status`**

    ###
    list services
    - `ls /etc/init.d/`
