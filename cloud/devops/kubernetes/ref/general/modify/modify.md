
#### Start pod automatically 
- `apply`, `run`
    - _both_ automatically **start pod** created           


##
#### Resource already exists?
A resource is consisdered to already exist by commands like (`replace`, `create`, `patch`, `delete`....) 
if one can be found with matching
 - `name` and 
 - `namespace` 
 
 ##
#### Immutable Fields

Immutable fields in Kubernetes are special fields that cannot be changed once they're set. A good example is `spec.nodeName` (resources cant move between nodes) or `metadata.namespace` (resources cant move between namespaces)

You cant update an object (after changing immutable field)

- These will all fail:
    - `k` `apply` `-f pod.yaml`   
    - `k` `edit` `pod my-pod`     (won't let you save)
    - `k` `replace` `-f pod.yaml`  

###
- You must (effectively) delete the object and recreate with the new (spec) values:

    - `k` **`replace`** **`--force`** `-f pod.yaml`
    The --force flag works by:

        - Deleting the existing resource (without grace period)
        - Creating a new one with the new configuration
        This effectively the same as :

    - `k` **`delete`** `-f pod.yaml` **`--force --grace-period=0`**
    - `k` `apply` `-f pod.yaml`   