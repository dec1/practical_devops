## delete

- `k` **`delete`** `-f res.yml`
undo apply - deletes any resources created by `apply -f res.yml`  to same file
does **NOT** delete the file itself
#####

- `k delete` `pod` **`nginx`** 
delete pod _by name_ and wait for confirmation from cluster

#####
- `k` `delete` **`pods[,services]`** **`-l myKey=myVal`**
delete pods and services _with label_ name=myLabel


_Note_: Pods are **not** deleted **automatically** (after termination) so you can eg inspect **[logs](../query/logs.md)**

#### force,  grace-period


- `k delete pod nginx` **`--force`** `[--now | --grace-period=-1]`
  delete pod **without** waiting for confirmation from cluster

gives pod (grace period) to terminate, kills thereafter.
the grace period is that explicitly (>=0) specified - otherwise that of pod itself

Note: `--now` alias for `grace-period=1` 




    


Only force delete pods when you are sure the pod is terminated, or if your application can tolerate multiple (different) copies of the same pod running at once.