
### Reverse Proxy:

- ##### Load Balancing:
    - one primary function of a reverse proxy, but dedicated load balancers may perform better

    

- ##### Caching: 
    - A reverse proxy can cache frequently accessed content, such as images, videos, or static files, to improve performance and reduce server load.


- ##### Security:
    - SSL/TLS Offloading: 
            offload the SSL/TLS encryption and decryption process from the backend servers to improve performance and reduce server load.
    
    - Authentication and Authorization: 
            authenticate and authorize users before forwarding their requests to the backend servers, improving security and access control

- ##### Filtering/Modification/Compression: 
    - filter or modify content in transit, such as removing ads or compressing images, to optimize performance and reduce bandwidth usage.


- ##### Traffic Shaping: 
    - shape traffic by limiting the number of requests per second or per user to prevent overloading of the backend servers.


###  API Gateway

- managing, securing, and optimizing APIs
        versioning 
        aggregation (protocols, use client categ)
        monitoring, and analytics
        protocol translation

- some of general revers proxy functionality (security, traffic shaping)

###  Ingress (Kubernetes specific)

- Routing (only subset of API Gateway functionality) - within a single kubernetes cluster 
  so (multiple) services (of cluster) can be accessed from externally
- the service that gets routed to (can) load balance among the worker pods

         

