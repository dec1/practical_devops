# Virtual Networks:


### Subnet (L3)
- IP level (Layer 3) network.
- **Router** manages (one or more) subnets. Nodes (~same nodes as on LAN) are connected to its **internal interface**.

- Subnet (Layer 3) <-> LAN (Layer 2) is usually (but not necessarily) 1:1.

- Each (Layer 3) subnet is identified (by router) by a unique "(sub)network ID" (e.g., subnet mask applied to IP addresses of nodes on the LAN).

- For IP, the **broadcast address** is obtained by setting the host (right) part of the IP address to all "**1**"s.
    - Example: `*IP Broadcast* address for a /24 subnet is "255.255.255.255"`.

- **Subnetting** involves allocating bits from the host portion of the address space to define the network portion. The number of bits used is specified by the subnet mask.
- Routers forward packets based on the destination **network address**.

- **CIDR** ("Classless Inter-Domain Routing") is the standard for subnetting:
  - Format: `a.b.c.d/x`, where x is the **subnet mask** that defines the network portion of the address.
    - **/x** => **leftmost x bits** are used for the **(sub) network** prefix, and the remaining bits are used for the interface identifier (host) 
    - Supersedes (legacy) _class-based_ addressing with fixed subnet masks:
        ```yaml
        Class A: /8
        Class B: /16
        Class C: /24
        ```
- Subnets are generally managed by a single entity/organization, which may delegate part of it to others.

### VLAN (L2)
- Generalization of LAN (broadcast domain) beyond a single physical segment.
- Broadcast Domain, where devices are separated **logically** instead of physically.
- Switch-VLAN is not (necessarily) 1:1:
    - Can have 1 **switch with multiple VLANs**, or 
    - 1 VLAN spanning multiple switches (via trunking), or a combination of both.

- **VLAN-to-VLAN Communication:**
    - Separate VLANs (like LANs) must communicate through a Layer 3 device (default gateway ~ **router**). Devices send Layer 2 frames (encapsulating Layer 3 packets) to the router, which repackages the Layer 3 packet into a new Layer 2 frame for the other VLAN.
      [see](https://networkengineering.stackexchange.com/questions/28446/how-can-hosts-on-two-different-vlans-communicate)
    

### [Overlay Networks](overlay_network.md)
