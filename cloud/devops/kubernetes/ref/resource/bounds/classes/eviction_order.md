
### Eviction Order

When resources become scarce, Kubernetes uses decides which pods to evict (in first), as follows:

- Pods are grouped based on values of PriorityClass.

    - **PriorityClass**
        - Groups with lowest value are evicted first. 
            - **QoS Class**  
                - Within each group, QoS class determines eviction order.



