## Control (of Api Server requests)

Every request to API server has to pass three stages to succeed.
Request gets drops at fist stage it fails.

- ### 1). [Access Control](./control_access/control_access.md) 
    - **Subject *dependent***
        - [Authentication](../security/control_access/authentication/authentication.md)
        - [Authorization](../security/control_access/authorization/authorization.md)







- ### 2) Admission Control
    - **Subject *in*dependent**
    ###
    - **Admission controllers**  are configured within the api server itself (they are **plugins** but only get loaded at api server start). Each provides a way to approve, deny, or mutate a request. Thus ensuring resources do not exceed specified limits (LimitRanger - enforces limits on the resources that can be requested or used by pods (independent of those in pod manifest), defaulting values, validating resource configurations against policy etc


    