<style>
b { color: Blue }
g { color: Green }
o { color: Brown }
</style>


## Lifecycle


### Container 
- **State**

    - **<o>Terminated</o>** - ran
        -  to completion, ie returned    
            - exit code `0` : success
            - exit code `non-0` : failure
        -  was _prematurely_ terminated _by the system_

    - **<b>Running</b>**  - container running (without issues)

    - **<g>Waiting</g>** - neither running nor terminated. (It may be performing operations required for startup, such as pulling images).



### Pod 

###
- #### RestartPolicy
    Determines how pod reacts to termination of individual containers.
    - **Always** (default) - keeps restarting any container that terminates (whether successfully or not)
    - **OnFailure** - keeps restarting any container that terminates unsuccessfully 
    - **Never**  - never restarts any container. 
       - **Only**  with this => **can pod fail**  (terminate unsuccessfully, due to container behaviour) 
          - since other 2 (Always, OnFailure) cause indefinite restarts

- #### Status

    - **Phase**

        - _Terminated_ 
    **All** containers in the Pod have **<o>Terminated</o>** (returning an `exit code`) and will _not be restarted_

            - **Succeeded** -  **all** containers returned exit code `0`

            - **Failed** -  _not_ succeeded. At least one container didn't return exit code 0, or was terminated by the system. 


        - Not terminated (yet)

            - **<b>Running</b>**  -   At least **one** (non-init) container is **running** (or ready to run).
            The Pod has been bound to a node, and all of the containers have been created. 


            - **<g>Pending</g>**   - At least **one** container is **waiting**
            The Pod has been accepted by the Kubernetes cluster.

        - Unknown

            - **Unknown** - For some reason the state of the Pod could not be obtained. This phase typically occurs due to an error in communicating with the node where the Pod should be running.




    ###
    - **Condition** 
        Can be seen as a sub categorization of pod phases (running or pending) as well as a transition between them

        ###
        - part of _Pending_ phase:
            - **PodScheduled**: the Pod has been scheduled to a node.
            - **PodReadyToStartContainers**: (beta feature; enabled by default) the Pod sandbox has been successfully created and networking configured.

        ###
        - during transition _Pending -> Running_ phase
            - **ContainersReady**: all containers in the Pod are ready.
            - **Initialized**: all _init containers_ have completed successfully.

        ###
        - late _Running_ phase
            - **Ready**:  the Pod is able to serve http requests  - ie _all containers_ have pass [Readiness probe](probes.md)
                - note: _all_ containers must be running - not just _any_ container - which is requirement for pod to _enter_ running _phase_ 

    ----
   

- #### `k wait`
    Kubectl has an (experimental) function, that waits for a specific condition or phase on one or many resources. eg

    - `k` **`wait --for=condition=Ready`** `pod my-pod`
    Waits for my-pod to meet condition "Ready"
        ```yaml
        pod/my-pod condition met
        ```





