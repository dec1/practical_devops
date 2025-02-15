#### Wget and Curl
    

- #### wget
    downloads to **file** (by default), and has fewer options
    - follows *redirects* by default (unlike curl)
        - but you can limit number/kind

    ###
    - **`wget` `-O <filename>`**   `<url>`  
        - `filename` 
            - use `-` for **stdout**  
                -  ie `wget -O - <url>` 
        -  `-O ` is an _uppercase_ letter **O**

        ```yaml
        <h1> Welcome to nginx! </h1>
        ...
        ```
    - **`wget --spider`** `url`  
        - verify that download is possible 
        ```yaml
        Connecting to 10.104.86.159:8000 (10.104.86.159:8000)
        remote file exists
        ```
#
- #### curl
    outputs to **terminal** (by default), and has many options and supports more protocols

    - **`curl`** `[-o local_file]` **`[-L]`** `[-k]` `[-m3]`  `[--head]` `url`   
    - `-o` (_lowercase_ letter **o**) to save to file - **cout** is default
    - `-L` - follow redirects (needed eg with proxy)
    - `-k` - insecure (dont care about validating server cert)
    - `--head`  verify (get headers only)
    - `-m3` **max** 3 seconds to wait for response 

    ##### from pod:
    #####
    - ###### ephemeral
        - `k` **`run`** `tmp` **`--restart=Never`** **`--rm`** `-i` `--image=nginx` **`-- curl`**  `[-m3]` `192.168.1.6`
            - `--restart=Never` - **NB** - pod tries to keep restarting container otherwise 
                - not needed if using `-it` (instead of  `-i`) for interactive terminal
            - `--rm` delete pod automatically when it terminates
            - `-i` show output (of curl) on local terminal 
            - `-m3` **max** 3 seconds to wait for response 
            - `tmp` - name of (ephemeral) pod to use
            - `192.168.1.6 `- remote host to download from

    #####
    - ###### existing
        - `k` **`exec`** `my-pod [-c my-ctr] ` **`-- curl`**  `[-m3]` `192.168.1.6`
        execute Cmd in container (default: first) of pod. 

---

###
- **nginx** has *both*
- **alpine** has wget (but not curl)
- **busybox** has curl (but not wget)


   