### Service Mesh

- Enhances Kubernetes services by providing advanced traffic management, security, and observability.

- It deploys a _**sidecar proxy** (additional container) in each pod_
    - rather than an _additional pod (kube-proxy) on each node_, as Kubernetes services do.

- Can, in principle, be used with virtual machines, but is most commonly used with containers/pods in Kubernetes.

####
- #### Features
  - **Routing**: Provides sophisticated (dynamic) traffic routing (e.g., canary, weighted splits) and load balancing beyond Kubernetes' built-in service capabilities. 
  - **Security**: Implements advanced security features such as mutual TLS (_mTLS_) for encrypted communication between services. zero-trust patterns.
  - **Observability**: Offers detailed metrics, logs, and tracing to monitor and troubleshoot service interactions.

- #### Components

    A combination of a control plane and a data plane component forms a complete service mesh implementation.

    ####
    - **Control Plane**:
      Manages and configures the data plane. It is typically deployed as dedicated pods within the Kubernetes cluster.
        - Examples:
            - **Istio**: Composed of Pilot, Mixer, Citadel.
            - **Linkerd**: Composed of Linkerd Controller, Web Dashboard.
            - **Consul**: Composed of Consul Server and Consul Agent.

    ###
    - **Data Plane**:
      A sidecar **proxy** is deployed as an additional **container** in **each pod**.
      These proxies handle traffic management and enforce policies, analogous to **kube-proxy** on **each node** for built-in service types.
        - Examples:
            - **Envoy**: Default in Istio.
            - **Linkerd Proxy**: Used in Linkerd.
