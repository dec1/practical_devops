
## Linux Logging Services

### journald 
- most modern and recommended logging service
- part of the **systemd** suite and is included by default, in most modern Linux distributions.
- persists messages in binary format - viewed using      

    #####
    - **journalctl**

        ######
        - examples:

            - **`journalctl`** **`-n 50`**
            show the Most Recent Logs
            #####
            - `journalctl` **`-f`**
                follow New Log Entries in Real-Time
            #####
            - `journalctl` **`-u <service-name>`**
                show Logs for a Specific Service
            #####
            - `journalctl` **`--since "2024-08-15 08:00:00"`**
                show Logs Since a Specific Time
            #####
            - `journalctl` **`-b`**
                show Logs for the Current Boot
            #####
            - `journalctl` **`-p err`**
                filter Logs by Priority (`emerg`, `alert`, `crit`,`err`, `warning`,  `notice`, `info`, `debug`)
            #####
            -  `journalctl` **`-k`**
                show Kernel Messages only



####
- collects messages from various **sources**:
    - #### 1). User space (processes)


        - ##### a). Service 
            -  systemd *services* **stdout/stderr** -> **stdin** of _journald_
                - automatically piped by systemd

        - ##### b). Regular (Non-Service)

            - **journal api**:
                - Regular processes not managed by systemd can log messages via the journal API (provided by system libraries). Behind the scenes, UNIX domain sockets (file descriptors) are used for IPC.
                - Journald callbacks get called.
                
                - **syslog api**:
                    - legacy
                        - Messages from processes using the (superseded by journal API) syslog API to send their log messages. Behind the scenes, the file descriptor `/dev/log` is used.


                
    #### - 2). Kernel space
    - Kernel writes its messages to a ring buffer (file descriptor `/dev/kmsg`)
        - hardware initialization messages, kernel module loading messages, and device driver messages, etc
        - older messages get replaced by newer
        - journald logs tracks all messages that got sent to ring-buffer
            - whereas **dmesg**  can show live snapshot of such





