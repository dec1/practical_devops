### API Gateway

The consolidates everything (cross-cutting) needed for reliable and secure network access (cross-cutting concerns such as load balancing, authentication, rate limiting, request/response transformation, and logging) not specific to any single application (which can then concentrate on implementing the business logic). 

Often a single api gateway sits in front of many (independent) applications. 
Clients can access different, independent APIs as though they were separate, without being aware of the Gateway’s presence.


The API Gateway simplifies backend architecture, offloading network-related responsibilities from individual applications, allowing them to focus solely on implementing business logic.
