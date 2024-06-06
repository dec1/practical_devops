

### top [-f]
    - Requires `metrics server` to be installed
     

 ###
 - `top`
    ```yaml
    top - 08:46:05 up 52 min,  0 users,  load average: 0.17, 0.20, 0.26
    Tasks: 201 total,   1 running, 200 sleeping,   0 stopped,   0 zombie
    %Cpu(s):  4.8 us,  2.7 sy,  5.8 ni, 86.0 id,  0.3 wa,  0.0 hi,  0.0 si,  0.3 st
    MiB Mem :   1983.3 total,     83.8 free,    994.6 used,    905.0 buff/cache
    MiB Swap:      0.0 total,      0.0 free,      0.0 used.    794.4 avail Mem 

        PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                                                                                 
    1947 root      20   0 1541180 248828  35960 S   3.3  12.3   1:59.54 kube-apiserver                                                                                                                          
    1579 root      20   0 1935904  63300  27748 S   1.3   3.1   0:38.89 kubelet                                                                                                                                 
    1933 root      20   0   10.7g  63436  19532 S   1.0   3.1   0:39.76 etcd                                                                                                                                    
    2007 root      20   0 1334184  60376  17336 S   1.0   3.0   0:29.15 kube-controller                                                                                                                         
    32690 root      20   0    6668   3720   2936 R   0.7   0.2   0:00.02 top 
    ```               

