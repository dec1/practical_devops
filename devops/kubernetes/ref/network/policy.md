
### Network Policy8the 
Restricts communication between pods in a single **namespace**, based on their **labels**.
More, precisely it restricts the **`direction`** of `connection establishment` (once established the traffic can flow freely in either direction) - [online editor](https://editor.networkpolicy.io/)

For all **Pods** (which must reside in `same namespace as policy`) **targeted** ie those matched by 
- **podSelector**

 deny connection requests (if **Ingress/Egress** PolicyType defined) 
 not specifically allowed by subsequent exceptions in
    - `from`  **ingress** (or on same node)
    - `to` **egress**

---- 
- `Default`: **all** *allowed*(ie when neither any policy nor rules defined) - all incoming and outgoing connection requests to/from targetPods allowed
#####
- `Multiple`: union of multiple (`-`) rules (and policies), is whats effectively allowed:
    - `more` `-` ingress/egress  rules 
    -> **more permissive** (see note *** below)
#####
- For a connection from a source pod to a destination pod to be allowed, the connection must be allowed by *both* 
    - **egress** policy on the `source` pod, *and* 
    - **ingress** policy on the `destination` pod


---
##### Example
 - `Allows` incoming connection requests to target pod, port `3306`, _only_,  from pods matching (from) labels or (from) namespace
 - `Denies` all outgoing connection requests from target pod  (to anywhere) 

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: my-policy
  namespace: my-ns
spec:
  # Target Pods - those affected by below
  #-----------
  # podSelector: {}          # targets all pods in __same namespace__ (as policy)
  podSelector:
    matchLabels:            # targets all pods with __labels__ "my-key1=my-val1" and "my-key2=my-val2"
      my-key1: my-val1
      my-key2: my-val2

  # Rules
  #--------
  policyTypes:              # blanket forbids (need explicit exceptions in ingress/egress below).
    - Ingress               
    - Egress                

# egress: {}                # would explicitly alow everything
  ingress:                  # explicit exceptions allowing incoming traffic (__to__ pods matched by __above__ podSelector)
                            # __from__ pods that 1) match on these labels
    - from:
        - podSelector:          # pod in the local Namespace with matching labels matching labels
            matchLabels:
                my-key3: my-val3
                my-key4: my-val4

        - namespaceSelector:    # _OR_ from any Pod in any namespace with matching labels
            matchLabels:
                my-key5: my-val5       
      ports:                # _AND_ are 2) incoming to these ports (default - all ports)
#   - ports:                # _OR_ .....  (- effectively creates new independent rule, and rules are ORed together)
        - protocol: TCP
          port: 3306

    # Notice how items with sub items that are  preceeded with   "-" =>  _OR_  =>  multiple (more permissive) rules ****
    # .....................................NOT ................  "-" => _AND_  =>  single   (less permissive) rule

   
```

