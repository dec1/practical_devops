
## Lifecycle

### Pod
###
- **Phase**
      
    - **Terminated** -  **All containers** in the Pod have terminated

        - **Succeeded** - if all in success (`exit` code `0`), and will not be restarted.

        - **Failed** -	if at least one in failure (container either exited with non-0 status or was terminated by the system). 
            - => Pod can be in Failed but still have (other) running containers

    - Not terminated (yet)

        - **Pending**	- The Pod has been accepted by the Kubernetes cluster, but one or more of the containers has not been set up and made ready to run. This includes time a Pod spends waiting to be scheduled as well as the time spent downloading container images over the network.

        - **Running**  -	The Pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting.


        - **Unknown** -	For some reason the state of the Pod could not be obtained. This phase typically occurs due to an error in communicating with the node where the Pod should be running.
###
- **State**
    Not new info - maps directly to one or more phases
    - **Running** - Phase::Running
    - **Terminated** - Phase::Terminated
    - **Waiting** - Phase::Pending
###
- **Condition** 
    - **ContainersReady** 

        - **PodScheduled** - Phase::Pending and the Pod has been scheduled to a node.
        - **PodReadyToStartContainers** - Phase::Pending and Pod sandbox has been successfully created and networking configured.
        - **Initialized**: - all **init containers** have completed successfully
        - **ContainersReady** - **Phase::Running** _and_ all containers have pass [Readiness probe](probes.md) 

        - **Ready** - condition **ContainersReady** _and_ should be added to the load balancing pools of all matching Services.

            - `k` **`wait --for=condition=Ready`** `pod my-pod`
            Wait for my-pod to meet condition "Ready"
                ```yaml
                pod/my-pod condition met
            ```

###
- **RestartPolicy**
    Determines how pod reacts to termination of individual containers.
    - **Always** - keeps restarting any container that terminates (whether successfully or not)
    - **OnFailure** - keeps restarting any container that terminates unsuccessfully 
    - **Never**  - never restarts any container. 
       - **Only**  with this => **can pod fail**  (terminate unsuccessfully, due to container behaviour) 
          - since other 2 (Always, OnFailure) cause indefinite restarts




### Container
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






