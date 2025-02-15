## Control (of Api Server requests)

Every request to API server has to pass three stages to succeed.
Request gets drops at fist stage it fails.

- ### 1). [Access Control](./control_access/control_access.md) 
    - **Subject *dependent***
        - [Authentication](../../security/api_server/control_access/authentication/authentication.md)
        - [Authorization](../../security/api_server/control_access/authorization/authorization.md)







- ### 2) Admission Control
    - **Subject *in*dependent**
    ###
    - **Admission Controller Plugins** 
        These intercept requests to the Kubernetes API server before the persistence of the object, but after the request is authenticated and authorized.

        Each provides a way to approve, deny, or mutate a request. Thus ensuring resources do not exceed specified limits. eg
        
        - [LimitRanger](../../resource/bounds/resource_limits.md) - enforces resource limits on Pods and Containers in a namespace.  

        - [Priority](../../resource/bounds/classes/priority_class.md): This plugin allows you to define a priority class for Pods, which can be used to prioritize critical workloads.


    