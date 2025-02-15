
### Pod Comnands


#### Creation 

- [run](run.md)
- [apply](../../../general/modify/commands/apply.md) 


    
##
#### Describe

- **`k describe`** `pod my-pod`
    - **ip address** 
        ```yaml
        IP:      192.168.1.4           # ---** Pod ip address 
        Node:    node01/10.0.0.11      # ---** Node ip address, where pod is running
        ...
        ```


##
#### Set Image

-  **`k set image`** `pod my-pod` `my-ctr=nginx:alpine`
set image (trigers update)
    - can be called on deployment too








