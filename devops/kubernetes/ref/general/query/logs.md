

### logs [-f]
cout/cerr of containers


### pod
- `k` **`logs`** `my-pod` | **`-l key=val`**      **`[-c my-ctr`**`|` **`--all-containers]`** `[-p]` `[-n my-ns]` **`[-f]`** 
    show logs of container 
    - `my-pod` pod name
    - **`-l key=val`** labels of pods to log (eps useful for **deployment**)
    - `my-ctr` name of container (default:  *first*  ctr in pod) 

    - `p` show logs from `previous container instance` (if pod restarted it)
    - **`-f`** **follow** (live update) 
        - cf `get -w`


###
- `k` **`logs`** 

### job
- `k` **`logs`** **`job/my-job`** `[-c my-ctr | --all-containers]` [`-n my-ns`]
logs of container of job my-job in namespace my-ns (pod will be called "{job_name}_suffix")
with this command you dont have to know suffix

    - -`my-ctr` container (default: first)


   
   