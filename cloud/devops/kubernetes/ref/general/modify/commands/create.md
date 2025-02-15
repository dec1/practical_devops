                 
#### Create 

Can be used to create instance of all resource types **_except Pod_**

There are 2 forms of the command, one of which takes a manifest file patrameter, and the other a resource _Kind_ parameter

- `k create` `-f res.yaml`  _declarative_, or 
    
- `k create` `<type> [parms]` _imperative_
    - where `type`can be _anything **except pod**_
        - inconsistent api - you can use any other resource _type_ 
        - Use **[run](../../kubeconfig/cmds.md)** instead, which is basically and _alias_ for (non-existing) (imperative) _create pod_ 
     


both forms:
- _create new_ resource (if doesnt exist), or
- _fail_  (if resoucre already exists)







