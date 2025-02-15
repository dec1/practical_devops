## Find files/dirs recursively



- **`find`**  `[startDir]` [**`-name|iname pattern`**]   `[-type f|d|l] `      
**recursively** search for matching files/dirs  below  **startdir**   
    - `startDir` root of tree to begin search  (default: `.`)
    - `-name`   filter files/dirs named  (can contains **wildcards**) 
        `-iname`.. case insensitive      
    - `-i` or `-iname`  case insensitive      
    - **`-type`** search for (default= **all**) 
        - `f` files
        - `d` dirs
        - `l` links 

###
- Examples 
    - `find` `/usr/lib/systemd` **`-name kube*`**
        ```yaml
        /usr/lib/systemd/system/kubelet.service
        /usr/lib/systemd/system/kubelet.service.d
        ```

    - `find` `/usr/lib/systemd` **`| grep kube`**
        ```yaml
        /usr/lib/systemd/system/kubelet.service
        /usr/lib/systemd/system/kubelet.service.d
        /usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf
        ```

        see also [grep](grep.md)