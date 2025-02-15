## Pod Placement
Settings of Node/Pod  which influence which nodes which (workload) pods are (scheduled) placed on.


### Node

#####
 - 1a). **Taint** (needs to be tolerated)
    - Repel  pods that dont have a **Toleration**.
        - **set** 
            `k` **`taint`** `node my-node` `my-key[=my-val]` `:<Effect>` `[-]`
            - `my-key`: The key for the taint. 
            - `[=my-val]`: Optional. The value associated with the key. If omitted, the taint still applies but without a value.

            - `<Effect>`:   
                - **PreferNoSchedule** - try to avoid scheduling (new) pods on node (not guaranteed)
                - **NoSchedule** -  avoid scheduling (new) pods on node
                - **NoExecute** - avoid scheduling (new) pods on node,  _and_ evict any running (after [_tolerationSeconds_)
            
            - `-`:  remove the taint
        ###    
        - **show** 
        `k` **`describe`** node my-node | **`grep "taint"`** -iC3
            
            ```yaml
            Taints:             my-key=my-val:PreferNoSchedule
            ```
        ###    
    - Taint/tolerate with _Effect=NoExecute_ is the only way to affect _already running_ pods
    - **`node-role.kubernetes.io/control-plane`** is a _standard_ [label](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-role-kubernetes-io-control-plane) and [taint](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-role-kubernetes-io-control-plane-taint)



### Pod 
- 1b). **Tolerate** (a taint)
     - allow match on nodes with ~ **Taint**
        - Toleration must match `Effect`, `key` and (if exists) `value` in order to ~ Taint

#####
- 2). **nodeSelector**
    - match nodes with  **label**(s) 
    - _node affinity_ (below) is more sophisticated (and complicated)

#####
- 3). **nodeName**
    - exact match on name of node

#####
- 4). Node **Affinity** (attract) 
    - Prefer (`preferredDuring...`) or require (`requiredDuring...`) nodes matching conditions in `affinity.nodeAffinity`

        - more sophisticated (and complex) than _nodeSelector_, _nodeName_ and taint/toleration

#####
- 5a). Pod **AntiAffinity**
    - pods repel each other - ~ 5b

#####
- 5b). Pod **Spread**
    - Spread pods (across nodes) - ~alternative to~ 5a

###
- pod.yaml
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-pod
    spec:
      containers:
      - name: my-ctr
        image: nginx
   
      # ------------------------------------------------------------
      topologySpreadConstraints:  # (5b) spread pods (equivalent to 5a below) 

      - maxSkew: 1                # allow no more than 1 pod difference to exist between
                                  #  the nodes with the highest and lowest number of pods for the specified label.               
        topologyKey: kubernetes.io/hostname      # across hosts with unique hostnames
        whenUnsatisfiable: DoNotSchedule         
        labelSelector:           # for pods matching these labels               
            matchLabels:                           
                id: "key-4"                   
                  
     # -------------------------------------------------------------
      tolerations:                      # (1) Toleration

      - key: "taint-key1"
        operator: "Equal"                   # Equal -  requires
        value: "value1"                     #            value
        effect: "NoSchedule"                #  NoSchedule | PreferNoSchedule | NoExecute

      - key: "taint-key2"
        operator: "Exists"                  # Exists - no value
        effect: "NoSchedule" 

                                        # (2) Node Selector
      nodeSelector:           
        my-sel-key: "my-sel-value"          # only schedule on nodes with matching label

                                        # (3) nodeName
      nodeName: my-node-name                # ** only schedule on nodes with name

      ## ----------------------------------
                                        
      affinity:
        nodeAffinity:                   ## (4) node affinity

          requiredDuringSchedulingIgnoredDuringExecution:     
            nodeSelectorTerms:
            - matchExpressions:
              - key: "key1"
                operator: "In"
                values:
                - "value1"

          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 1
            preference:
              matchExpressions:
              - key: "key2"
                operator: "In"
                values:
                - "value2"

        podAntiAffinity:              # (5a) pod anti-affinity (equivalent to 5b above)                 
            # dont schedule more than one pod with the label key: "key3" and value: "value3"  on each node with a unique hostname.    
          requiredDuringSchedulingIgnoredDuringExecution:   
          - labelSelector:                                  
              matchExpressions:                             
              - key: "key3"                                     
                operator: In                                
                values:                                     
                - "value3"                            

            topologyKey: kubernetes.io/hostname                                        
    ```
    
