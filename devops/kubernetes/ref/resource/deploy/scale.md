## Scaling

- ### Horizontal 
    **replica count**  (*number of pods*) of deployment increased/decreased  

    - #### Manual
        - `k apply` after changing **spec.replicas** (or *`k edit` deploy my-dep*)
        
        - *`k` **`scale`** `deploy my-dep` **`--replicas`**`=4`


    - #### Automatic

        - **HorizontalPodAutoScaler** (HPA) can automatically modify the number of replicas in a deployment (or replic set) based on the value of dynamic variables (eg system load etc). 

        - HPA *effectively **adjusts** spec.**replicas*** for pod 
        based on: current cpu usage (averaged over all containers in all pods), as a fraction of that pod requested in, resources.requests.cpu (which *must be specified* for pod  for autoscaling to work)
        
        $$ \frac{CurrentCpusUsedbyPod}{RequestedCpus} $$


        ####
        - Can adjust the number of replicas of a deployment both below and above the number initially specified in the *deployment* **spec.replicas**, as long as the number of replicas remains within the *HPA* **min** and **max** 

        ####
        - Tries to keep pod usage at **80%** of that specified for pod in *resources.**requests.cpu*** 
       
          - `k` **`autoscale`** **`deploy`** `my-dep` **`--min=3 --max=15 --cpu-percent=80`**
        Makes sense if each container has to do more work, when less containers available to share load (eg incoming web requests)

        ####
        - Behind the  scenes this creates a **hpa** object, with same name as deployment
        - `k` **`get`** **`hpa`**
            ```yaml
            NAME     REFERENCE           TARGETS         MINPODS   MAXPODS   REPLICAS   AGE
            my-dep   Deployment/my-dep   <unknown>/80%   10        15        3          18s
            ```
        ####
        - therse ***no** way* to generate **yaml** for HPA (eg with **--dry-run**). 
        hack: create hpa and use `k get hpa my-dep -o yaml > hpa.yaml` ignoring status etc
        
    - **HorizontalPodAutoScaler** (HPA) can automatically modify the number of 

- ### Vertical

    resources.***requests.cpu***  effectively scaled   for pods
    - #### Automatic
        - based on **current time** vs  **historic metrics** 
        - eg fridays cpu usage is usually higher and weekends lower - today is friday so scale up
        - cloud provider support required

