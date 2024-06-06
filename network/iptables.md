### IpTables

- Is used to intercept and process ip packets at the **node** level (for all namespaces and interfaces)
- Intercepts:
    - **Outgoing** packets **after** leaving each interface the node (where ip tables is running), 
         - which allows it to actually **send** it to a different interface than initially intended, and 
    - **Incoming** packets **before** reaching any interface on the node 
        - which allows it to actually **deliver** it to a different interface than initially intended 
    
- It can then drop, modify, or forward the packets as its wishes (based on configurable rules)
    - possible modification includes rewriting src and dst address, to/from that of internal or external interfaces