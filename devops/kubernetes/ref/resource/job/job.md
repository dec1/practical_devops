
### Job
Creates one or more Pods and will continue to restart (can only happend due to container with according to them until success or failure.
- **RestartPolicy**:
    - Coincides (replaces) with position of  RestartPolicy of Pod (in spec) but interpretation is slightly different (cf: [pod restartPolicy](../pod/lifecycle.md))
        - ~~Always~~-  not allowed
        - Never 
            -  (as for individual pod)  **Only**  with this => **can pod fail**
            - but now additionally:
                - pod gets restarted  (max `backoffLimit` times)
           
        - OnFailure - same as  as for individual pod    
            - container gets restarted     
    
##### Cleanup  
-  When a Job completes, no more Pods are created. Deletion of existing:

    - **Manual** - deletes _job_ **and** _pods_ 
    `k delete -f job.yaml`  
    `k delete job my-job`
    - **Automatic**
    `ttlSecondsAfterFinished` see below (Kubernetes **1.24**+ only. Earlier versions dont support automatic deletion)

        - CronJobs clean up automatically (see successfulJobsHistoryLimit, failedJobsHistoryLimit)

<br>

- **Success** 
    - `spec.completions` pods have succeeded (all containers exit `code 0`  see [Pod](pod.md))

- **Failure**
    - `backoffLimit` -  total Pod failure count exceeds
    - `activeDeadlineSeconds`  - total execution time of all pods 

###

<br> 

---

 - `k` **`create job`** `my-job` `--image=busybox` **`-- /bin/sh -c "echo  hello job"`**

 - `k` **`describe job`** `my-job` `| grep` **`pod`** `-iC2`

    ```yaml
    Created pod: my-job-vdsc5
   ```
- **logs**   
    - `k` `logs` **`job/my-job`**   #  job (first pod) 
or
    - `k logs` **`my-job-vdsc5`**   # specific pod 

    ```yaml
    hello job
    ```

- job.yaml
    ```yaml
    apiVersion: batch/v1
    kind: Job
    metadata:
        name: my-job
    spec:
        ttlSecondsAfterFinished: 200    # cleanup job (and pods) automatically after 200s. (Kubernetes 1.24 + only)
        backoffLimit:           4       # number of pod fails before job fails.
        activeDeadlineSeconds:  100     # if job is not completed within this time, it is considered failed. Prevents further Pods being started


        parallelism: 1                   # how many pods can run in parallel
        completions: 1                   # how many total pods need succeeded before job succeeds.


      # completionMode:                 # NonIndexed: (default) - all pods are "equal", or 
                                        # Indexed:  Each pods gets an index, and a job is only complete when a pod with each index has succeeded

     # only for completionMode: Indexed
        # backoffLimitPerIndex:
        # maxFailedIndices:


        template:
            spec:
                containers:
                    - name: my-ctr
                      image: busybox
                      command: ["/bin/sh", "-c", "echo hello job"]

                                        # ------------------------------------------------------------------------
                                        # Careful- "overrides" semantics RestrtPolicy (individual) Pod (would have)
   ------------------------------------------------------------------------
                restartPolicy: Never    # | OnFailure: 
    ```


