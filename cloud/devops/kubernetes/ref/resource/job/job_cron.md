
### CronJob

##### Schedule syntax
        ┌───────────── minute (0 - 59)
        │ ┌───────────── hour (0 - 23)
        │ │ ┌───────────── day of the month (1 - 31)
        │ │ │ ┌───────────── month (1 - 12)
        │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday)
        │ │ │ │ │                                   OR sun, mon, tue, wed, thu, fri, sat
        │ │ │ │ │ 
        │ │ │ │ │
        * * * * *

<br>

##### Cleanup  

- CronJobs (unlike regular [Jobs](job.md)) clean up **automatic except** for 
    - **successfulJobsHistoryLimit** (default 3)
    - **failedJobsHistoryLimit**     (default 1)

    _Manual cleanup_ of these (default 3+1) jobs still necessary -  just as for regular [Jobs](job.md)
<br>

- job.yaml
    ```yaml
    apiVersion: batch/v1
    kind: CronJob
    metadata:
        name: my-cron-job
    spec:
        successfulJobsHistoryLimit: 5           # keep 5 (default 3) -successful-   jobs
        failedJobsHistoryLimit: 3               # keep 3 (default 1) -failed-       jobs

        startingDeadlineSeconds:    20          # max secs (default: infinite) the CronJob can take to start if it misses its scheduled time for any reason 
        concurrencyPolicy:          Allow       # whether to allow jobs to run concurrently: # {Allow (default), Forbid, Replace}
                                                # cf Job: parallelism which governs concurrency of pods *within* the job


        schedule: "* * * * *"                   # when to run job - see (syntax) above
        jobTemplate:
            spec:
            template:
                spec:
                containers:
                - name: my-ctr
                    image: busybox:1.28
                    imagePullPolicy: IfNotPresent
                    command:
                    - /bin/sh
                    - -c
                    - date; echo "Hello from My Cron Job"
                restartPolicy: OnFailure
    ```
        


