note:

when a website receives a request, the standard and reliable way to check what node (originally) made the request is to read the first entry in `X-Forwarded-For` header

`X-Forwarded-Host` is typically a Single Value that of the originally intended final destination, and differs from `Host` which is the _currently intended final destination_, as may have been (re)set by a Proxy on the way. Here Host is not modified so adding _X-Forwarded-Host_ is no advantage, and should not be included.


### Traffic Headers (Ingress)

**0. Client to LoadBalancer:**
* *IP Header*
   * Source IP Address: `client_ip`
   * Destination IP Address: `load_balancer_ip`
* *TCP Header*
   * Source Port: `client_port`
   * Destination Port: `load_balancer_port`
* *HTTP Headers*
   * GET `/my_app1`/some/path HTTP/1.1
   * Host: `service_1_url`
   * X-Forwarded-For: `client_ip`
   * X-Forwarded-Host: `service_1_url`

**1. LoadBalancer to Node (NodePort):**
* *IP Header*
   * Source IP Address: `load_balancer_ip`
   * Destination IP Address: `node_1_ip`
* *TCP Header*
   * Source Port: `load_balancer_ephemeral_port`
   * Destination Port: `node_port`
* *HTTP Headers*
   * GET `/my_app1`/some/path HTTP/1.1
   * Host: `service_1_url`
   * X-Forwarded-For: `client_ip`
   * X-Forwarded-Host: `service_1_url`

**2. Node to Ingress Controller Pod:**
* *IP Header*
   * Source IP Address: `node_1_ip`
   * Destination IP Address: `ingress_pod_1_ip`
* *TCP Header*
   * Source Port: `node_ephemeral_port`
   * Destination Port: `ingress_pod_port`
* *HTTP Headers*
   * GET `/my_app1`/some/path HTTP/1.1
   * Host: `service_1_url`
   * X-Forwarded-For: `client_ip, load_balancer_ip`
   * X-Forwarded-Host: `service_1_url`

**3. Ingress Controller Pod to Service:**
* *IP Header*
   * Source IP Address: `ingress_pod_1_ip`
   * Destination IP Address: `service_1_ip`
* *TCP Header*
   * Source Port: `ingress_ephemeral_port`
   * Destination Port: `service_1_port`
* *HTTP Headers*
   * GET `/my_app1`/some/path HTTP/1.1
   * Host: `service_1_url`
   * X-Forwarded-For: `client_ip, load_balancer_ip, node_ip`
   * X-Forwarded-Host: `service_1_url`

**4. Service to Application Pod:**
* *IP Header*
   * Source IP Address: `node_running_kube_proxy_ip` 
   * Destination IP Address: `app_pod_1_ip`
* *TCP Header*
   * Source Port: `kube_proxy_ephemeral_port`
   * Destination Port: `app_pod_port`
* *HTTP Headers*
   * GET `/my_app1`/some/path HTTP/1.1
   * Host: `service_1_url`
   * X-Forwarded-For: `client_ip, load_balancer_ip, node_ip, ingress_pod_ip`
   * X-Forwarded-Host: `service_1_url`