## Node Placement
Settings of Node/Pod  which influence which nodes which pods are placed on.


### Node

#####
 - 1a). **Taint** (needs to be tolerated)
    - Repel  pods that dont have a **Toleration**.
        - **set** 
            `k` **`taint`** `node my-node` `my-key=my-val` `:<Effect>` `[-]`
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
    - Taint/tolerate with _Effect=NoExecute_ is the only way affect _already running_ pods

### Pod 
- 1b). **Tolerate** (a taint)
     - "counteract" nodes with ~ **Taint**

#####
- 2). **nodeSelector**
    - simple **label** (of node) **only** based (_hard_) matching 
    - _node affinity_ (above) is more sophisticated (and complicated)

#####
- 3). **nodeName**
    - exact match on name of node

- 4). Node **Affinity** (attract) 
    - Attract pods to  (either as a preference or a hard requirement).
        -  edit yaml only (cant be set imperatively)
        - more sophisticated (and complex) than _nodeSelector_, _nodeName_ and taint/toleration


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
                                        ## (4) affinity
      affinity:
        nodeAffinity:

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
    ```
    
