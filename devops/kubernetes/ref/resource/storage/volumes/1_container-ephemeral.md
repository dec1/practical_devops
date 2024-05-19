- ###  Container ephemeral 
    - Lifetime (inc restarts but not deletes)  of container 
        - Container restarted -> data (in container file system maintained)
        - Container deleted -> ... NOT
            Under the following conditions container may be deleted (without deleting pod). 
            If/when a pod restarts such containers depends on the pod's "restartPolicy"
            - Container process crashes.
            - Liveness Probe failure.
            - Manual container termination from within.
            - Resource limit violation.