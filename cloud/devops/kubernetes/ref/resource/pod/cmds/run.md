## `run`
-  **`k run`**  `my-pod ` **`--image=alpine`** **`[--restart=Never]`** **`[--rm]`** **`[-i] [-t]`** **`-l`**`lab-key=lab-val` **`--env`**`env-key=env-val` `[-n ns]` **`[-- command]`** **`[-- <arg_list>...]`** 

    - Where `<arg_list> ` is space separated list of words eg : `<arg1> <arg2>`



    ###

    - `--restart`- **`Always (default) | OnFailure | Never `**
        - sets [restartPolicy](../lifecycle.md) for pod

    #####
    - `--rm`: delete pod automatically after it terminates 
         which is not done by automatically so you can inspect **[logs](../../../general/query/logs.md)**
        - it also effectively makes [restartPolicy](../lifecycle.md)=`Never`

    ####    
    - `-l ` - **labels** to set 
    - `--env ` - **env** vars to set 

    ####
    - `-- command`:   override **ENTRYPOINT** in [dockerfile](../../../../../docker/main/container/init/init.md) with `<arg1>`
        
         - and **remove** `<arg1>` from the trailing `<arg_list>` !! 

    #####
    -  `<arg_list>` overrides **CMD** in dockerfile 
        - if `-- command` was specified then `arg_list` used starts with `<arg2>...`


    ##
    - Note: 
        - most run parameters, have equivalents in [pod manifest](../../../tool/json/query/kubectl/pods.yaml.md)
        - run is effectively the _missing_ [create pod](../../../general/modify/commands/create.md)

---
###
- Examples 
    - ##### One-shot container
        - `k run my-pod` `--image=busybox` **`-it`** `--rm` **`-- /bin/sh -c  "echo hi"`**
            ```yaml
            hi
            pod "my-pod" deleted
            ```

    
    - ##### Keep-alive container
        - `k run my-pod` **`--image=busybox`** `-- /bin/sh -c` **`"while true; do sleep .3; done"`**

            - need to add _while loop_ keeps container alive so you can [exec](exec.md) in:
            `k exec my-pod` **`-it`** `-- /bin/sh`

        ###
        -   `k run my-pod` **--image=nginx**
            - nginx runs its _own event loop_, so will keep alive on its own






    

---
#### 
- Quickly create multiple pods
    - **``for i in `seq 1 3`; do kubectl run my-pod-$i --image=nginx -l app=v1 ; done``**
        ```yaml
        pod/my-pod-1 created
        pod/my-pod-2 created
        pod/my-pod-3 created
        ```