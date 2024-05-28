
## Linux Logging Services

### journald 
- most modern and recommended logging service
- part of the **systemd** suite and is included by default, in most modern Linux distributions.
- persists messages in binary format - viewed using **journalctl**

####
- collects messages from various **sources**:
    - #### 1). User space
        - ##### a). Streams
            -  systemd *services* **stdout/stderr** -> **stdin** of _journald_
                - automatically piped by systemd

        - ##### b). API

            - **journal api**:
                - Regular processes not managed by systemd can log messages via the journal API (provided by system libraries). Behind the scenes, UNIX domain sockets (file descriptors) are used for IPC.
                - Journald callbacks get called.
                
            - **syslog api**:
                - Messages from processes using the (superseded by journal API) syslog API to send their log messages. Behind the scenes, the file descriptor `/dev/log` is used.


                
    #### - 2). Kernel space
    - Kernel writes its messages to a ring buffer (file descriptor `/dev/kmsg`)
        - hardware initialization messages, kernel module loading messages, and device driver messages, etc
        - older messages get replaced by newer
        - **dmesg**  can show live snapshot
        - journald logs tracks all messages that got send to ring-buffer





