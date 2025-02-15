

### Namespaces



####
- Most kubernetes objects (eg pods services, deployments) are namespaced
    - ie are associated with exactly one namespace

####
- Kubernetes (Api) server requires an **explicit namespace** specified in every request for a namespaced resource (and will return error otherwise)

####
- The scope of the command is limited to the resources in the namespace specified

####
- kubectl [contexts](./context.md) make switching more convenient and **seem** like theres a `default` namespace

####
- namespaces _themselves_ are Kubernetes **_resources_** managed within the cluster

[see also](../main.md) `k api-resources [--namespaced]`

---
- Allow sharing of single cluster by dividing it into multiple (logically separated) virtual clusters.


- Suitable for sharing cluster among different depts of same company (eg dev, test, qa)

- not suitable for isolating hostile workloads.

