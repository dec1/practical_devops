
## Overlay Networks

- **Encapsulation** of one protocol in another, analogous to the way higher layer packets are encapsulated inside (the payload of) lower layer one in the (osi) layers. Only the motivation is slightly different
- whereas OSI layering is more about the upper layer abstracting away differences in the "underlying" layer, overlay networks are more about 
    - **extending or adding new features** (eg enhancing security, or isolation) to existing ones. 
- Also unlike osi layering, its possible for overlay to be a lower layer protocol than the underlay (as in VXLAN - see below)


- #### L3-over-L3 (IP-over-IP)
    Both underlay and overlay are IP networks.
    - eg 
        - **VPN**
        - **IPv6 over IPv4**
    ###
    - **Nodes** may be:
        
        - **underlay** *only*: node is unaware of overlay - that their packets sometimes are encapsulating another
        
        - **overlay** *only*: e.g., *pods* in Kubernetes [CNI](../../cloud/devops/kubernetes/ref/general/architecture/components/pods/workload/system/cni.md): unaware of underlay

        - _both_ **underlay** _and_ **overlay**: 

            - Nodes in the overlay get a separate (private) **Virtual IP** address (independent of that from underlay)

            #####
            - node is **final destination** (of underlay):
                - Yes
                     - is overlay packet encapsulated?
                        - Yes:
                            - node is also **final destination** of overlay:
                                - yes
                                    - process as overlay destination node
                                - no 
                                    - forward along new underlay path.
                                      **Next hop in overlay is the final destination of (new) underlay message**. 
                                      At the next virtual hop, the overlay node unwraps the virtual payload, figures out the next base "final" destination, and continues the process until the message reaches its final VN destination and forwards to the next hop of the virtual path.
                        - No: 
                            - process as underlay destination node

                - No: 
                    - forward along underlay (as usual underlay node)

    ###

    - Key is encapsulated Packet contains the final virtual address of the node in VN.

    - Payload **may** (e.g., VPN) or may not (just separate management) be **encrypted**.

    - A **tunnel** (terrible name) is simply a connection between 2 nodes of any overlay network.



- #### L2-over-L3 

    -  eg   **VXLAN**
    - encapsulates L2 in L3 packets for transport across ip network. thus 2 L2 networks of a the same "kind" (eg ethernet) can be connected into one, even though separated by a different kind of L2  (eg MLPS). Effectively the ethernet frame is encapsulated in the IP Packet which in turn is encapsulated in the  MLPS frame (during transit across the IP (over MLPS) network

    ###
    - _**L3-on-L2-over-L3**_  
        - often a new L3 network is (layered) on top of this (L2) overlay, inside of which **routing is trivial** since all nodes are in same L2 segment.
    eg **Weave Net** and (optionally configurable) **Calico**, **Flannel**. (see [CNI](../../cloud/devops/kubernetes/ref/general/architecture/components/pods/workload/system/cni.md))
