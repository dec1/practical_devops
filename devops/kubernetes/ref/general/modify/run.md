
-  **`k run`**  `my-pod ` **`--image=alpine`** **`[--restart=Never]`** **`[--rm]`** **`[-i] [-t]`** **`-l`**`lab-key=lab-val` **`--env`**`env-key=env-val` `[-n ns]` **`[-- command]`** **`[-- args]`** 


    ####
    - `--rm`: delete pod automatically after it terminates
        (not done by automatically so you can inspect **[logs](../query/logs.md)**)
    - `--restart`- **`Always (default) | OnFailure | Never`**
    - `-l ` - **labels** to set 
    - `--env ` - **env** vars to set 

    ####
    - `-- command`:  `args` should override ENTRYPOINT instead of **CMD** (default) 

    - `-- args`:  
        - override **CMD** (default) or **ENTRYPOINT** (if `--command`) in dockerfile
##
- Examples (see also [docker examples](../../../../docker/main/container/init/exec_shell_forms.md))

    #####
    - dockerfile
        ```yaml
        FROM alpine
        ENTRYPOINT ["bin/echo", "ep..."]
        CMD ["cmd1..."]
        ```
        ###
        - `k` **`run`** `my-pod --image=dec1/my-alp --restart=Never --rm -i`                                  
            ```yaml
            ep... cmd1...
            ```

        - `k` **`run`** `my-pod --image=dec1/my-alp --restart=Never --rm -i`    **`-- echo hi from outside`**
            ```yaml
            ep... echo hi from outside
            ```

        - `k` **`run`** `my-pod --image=dec1/my-alp --restart=Never --rm -i` **`--command`**    **`-- echo hi from outside`**
            ```yaml
            hi from outside
            ```




    

---
#### 
- Quickly create multiple pods
    - **``for i in `seq 1 3`; do kubectl run my-pod-$i --image=nginx -l app=v1 ; done``**
        ```yaml
        pod/my-pod-1 created
        pod/my-pod-2 created
        pod/my-pod-3 created
        ```