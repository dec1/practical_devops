### Container Probes (Observability)

Each container in a pod 

#### Types

- **Startup**
    - Stops after first success. Only then do other 2 begin
    - On **Fail** - container is **killed** and  subjected to its **restart policy**
- **Liveness**
    - Is container in healthy state. 
    - On **Fail** - container is **killed** and  subjected to its **restart policy**
- **Readiness** (Request)
    - Is container able to server http requests. 
    - On **Fail** -  Services **stop** using pod as destination for **requests**
    - Container has **`status Ready`** when this passes (and remains passing)
        - _pod_ has status ready, when all its containers have this status



#### Methods
All 3 types of probes can use any of 4 methods:
 - **exec**         - arbitrary custom shell
 - **tcpSocket**    - container must have app listening for tcp connections on port
 - **httpGet**      - container must have app serving http on port
 - **grpc**         - container should implement gRPC health checks

However not all methods make sense for all probes. eg
exec - most suitable for startup (es if applications not designed for serving requests)



All probes have certain options eg
- `initialDelaySeconds`
- `periodSeconds`
- `timeoutSeconds`

The methods may have further options, meaningful only for that method eg
- path (for httpGet)
