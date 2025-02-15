


### Auxillary Containers
Often one container per pod is sufficient, but 
- #### initContainer
    - **Sequential**
        -   **Each** init container must complete successfully before the next one starts.
        - If an init container fails,  that init container gets (unconditionally) restarted until it succeeds. 
            - unless pod restartPolicy is Never, in which case whole pod fails, as soon as any (init or not) container fails 
        - do not support probes    
    - **Prerequisute**
        - Only when **all** init containers have completed successfully are "regular" containers started

    - **new** 
        - ***sidecar-style** initContainers*
        - Kunbernetes 1.29+ allows for 
            #####
            -  specification of a *dedicated **restartPolicy*** for initContainers (independent of that of (regular) containers).
            #####
            - All started together (No longer have to run and succeed sequentially). 
            Can be started, stopped, or restarted without effecting the main application container and other init containers)
            ##### 
            - They are all started before any of (regular) containers are started
            #####
            - Do support **probes**

- #### Sidecar Container
    - If multiple containers exist in pod one is main and others are called "sidecar".
        - Which is which is very subjective (objectively all are equivalent)
        - independent lifecycles
        - depending on the functional roles, various _patters_ can be implemented:
            - ***Adapter** Pattern* - sidecar adapts disparate interfaces
            - ***Ambassador** Pattern* - sidecar adds extra logic/functionality to main container






