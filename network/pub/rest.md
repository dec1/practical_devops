
### REST (key principles)


- ##### Client-server architecture: 
    - The system is designed to separate the concerns of the client from those of the server.
    client sends the request

###
- ##### Statelessness: 
    - Each request from the client to the server contains all the information necessary to complete the request. The server does not store any client state between requests.
    - Cookies (and anything that requires authentication) violate this by design 

- ##### Cacheability: 
    - The system must support caching to improve performance, scalability, and reliability.
    - Many typical web requests are not (get current time, value in database that could have changed since last "get" )




- ##### Uniform interface: 
    - The system must use a uniform set of interfaces to enable communication between clients and servers.
    - The uniform interface enables a client to interact with a server in a predictable and consistent way, regardless of the specific implementation details of the server.
    - would expect any good interface to be such - so its hardly a defining characteristic of REST

- ##### Layered system: 
    - The system can be composed of multiple layers, with each layer providing a well-defined interface for the layer above it. 
    - would expect any good system to designed in or viewable as layers - so its hardly a defining characteristic of REST 