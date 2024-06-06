### Collision Domain
The set of nodes that receive a unicast messages (destined to a specific node). Nodes other than the node dst node is undesirable since, messages from multiple nodes sent simultaneously in this domain collide - all nodes in the domain receive them simultaneously.

### Broadcast Domain
The set of nodes that receive a broadcast message. 

Both **switch** and **bridge** create separate collision domains - **forward** unicast traffic only if appropriate (ie node with specified address is on receiving side), and **broadcast** traffic **unconditionally**. ie  traffic addressed to specific node gets forwarded only to segment containing this dst node (this avoids collisions between segments - but inside any segment there may still be internal collisions). broadcast traffic gets forwarded to all connected segments.

### Subnet (L3)
- IP level (layer 3) network
- **Router** manages (one or more) subnets. nodes (~same nodes as on LAN) connected to its **internal interface**.

- For IP, the **broadcast address** is obtained by setting host (right) part of ip address to all "**1**"s

- **Subnetting** steals bits from the (class based) host portion of the address space and the bits stolen are described by changes in the subnet mask. 
- Routers are tasked with forwarding packets based on the destination **network address**.

- Class based (legacy) vs CIDR ("classless interdomain routing") subnetting: 
  `a.b.c.d/x` where x is the **subnet mask** used to define (sub) network part of address.


### LAN (L2)
####  broadcast domain = (physical) segment

-A group of devices in the same broadcast domain
-Data Link level (layer 2) network
- 1 **Switch** : 1 LAN 

When a switch receives an (ethernet) frame for whose dest MAC address it does not have an entry in its (CAM) table (which is always true for broadcast address ("FF" x6) and unknown (unicast) address ("00" x6), it floods the frame - ie sends the frame out every port within the respective VLAN (ie broadcast domain) except the one through which the frame arrived.


    *Ethernet Broadcast*            (mac) address is "FF:FF:FF:FF:FF:FF"
    *Ethernet Unknown (Unicast)*    (mac) address is "00:00:00:00:00:00"



### VLAN (L2)


generalization of LAN (broadcast domain) beyond single physical segment
Broadcast Domain, where devices are separated **logically** instead of physically. 
Switch-VLAN is not (necessarily) 1:1
    Can have 1 **switch with multiple VLAN**s, or 1 VLAN spanning multiple switches (via trunking), or even a combination of both

- Vlan - Vlan communication
    Separate VLANs (like LANs) must communicate through a layer-3 device (default gateway ~ **router**) ie send layer 2 message (encapsulating layer 3 message) to router, 
    which repackages the layer 3 message as a new layer 2 message on other vlan (segment). 
    [see](https://networkengineering.stackexchange.com/questions/28446/how-can-hosts-on-two-different-vlans-communicate)
   


### WAN (L3)

- One or more LANs connected via **router**(s). 
subnet (layer 3) <-> lan (layer 2) usually (but need not be) 1:1

- Each (layer 3) subnet is identified (by router) by a unique "(sub)network Id" (~subnet mask applied to ip address of any node on the LAN) 

- That router is the "default gateway" for each LAN. 
- The internet is a WAN

`*Ip Broadcast* address is "255.255.255.255"`   



### Network Segment    

1) **Physical** -   Collision domain. Nodes share same physical media. Separated eg hub no (layer 2, address based) processing
2) **Logical**  -   Broadcast Domain. Mac address based communication. Separated eg bridge, switch
                    Logical segment may include multiple physical segments

- **Subnet**   = layer3 segment (doesn't require router - for internal (ip based) communication)

- **LAN/VLAN** = layer2 segment (nodes in same broadcast domain - nodes can be connected by bridge, switch)
- **Link**     = layer1 segment (nodes in same collision domain - nodes can be connected by hub only - not switch, bridge)




### Protocol Data Unit (PDU)     

-  L4 (Transport)
    - **Segment**  (Tcp)
    - **Datagram** (Udp)

- L3 (Network)
    - **Packet**   (Ip) - sometimes "packet" used for others pdu's too


- L2 (DataLink)
    - **Frame**      
                 

### Router  
-   Connects Switch/Router - Switch/Router

- Required for one LAN (switch) to connect outside world (WAN - internet)

- Works with IP addresses (and mac addresses)
-Forward traffic between IP based networks after examining the Layer-3 header

- They require IP addresses in order to operate properly (switches do not)
- Use and respond to ARP messages, and listen to (but will not forward) all (ethernet) broadcast frames. 



- Both routers and hosts maintain routing tables.   
- Default Gateway - Ip address of (default) router for pc/node. Without it, node can only communicate with computers on same LAN


#### Routing Table:


| Subnet             |  Hop/Gateway  |  (Ext) Interface | Cost|
| -------           |     ------- | ------- | ------- |
|            | |  |  |
|            | |  |  |


- **Subnet**:             final - Destination (network) of Ip packet to be routed


- **Gateway/Hop**:        next - ip address of (next) node/router that packet should be sent to
                    (in order to finally reach its destination - subnet)


- **Interface**:          interface (forwarding) host that packet should be sent through
                    (eg  "eth0" - encapsulates mac address and ip address)
            
- **Cost**:               metric    - lower is faster. Router always checks -every- line in table, and chooses cheapest match
<br>
- **Default Route**:      if (Sub)net = all 0, then the (rest of) entry (line) in  routing table where packets should be sent if no over line matches

-  When the router receives a packet, the destination IP address is compared with each entry {subnet, interface} entry in the routing table. This comparison may yield a ** more than one match **entry with the longest matching subnet(mask) wins**     [see](https://www.eventhelix.com/networking/ip-routing)


```
Router (Ip)  manages (one or more) subnets
Switch (Mac) manages (one or more) VLANs  (~ "subnets" of layer 2)
```

### Switch (L2)  
 - Can connect/manage (nodes in) a (V)Lan - broadcast domain
- Works with Mac Addresses
- Ethernet (itself) is a bus topology where all nodes hear all signals. 
Half- duplex: "transmit if quiet - backoff on collision"

- Adding switch or (or directly connecting just 2 nodes) -> full duplex (star topology)
- Switch can ensure only the dest node gets sent appropriate (unicast) signal.


- Switches can operate in full-duplex mode, allowing connected devices to both transmit and receive data simultaneously
- Can also use buffering to avoid multiple simultaneous signals to same dest.


Switching (CAM)  Table:
----------------------
    Mac Address - switch port
    If switch gets mesg for dst address it doesnt (yet) have CAM entry for, 
    if forwards the mesg to * all ports * (except the one the mesg arrived on)



Multilayer Switch -  Can do all a switch can, and also some routing/switching decisions based on deeper (ie layer 3 and 4) PDUs - but only between VLANs connected (directly) to the switch.
                     Generally logic implemented in hardware (ASIC) 
                       -> faster but less flexible (not all routing protocols), more expensive than router (which generally uses software based decisions). 



### Bridge (L2) 

- basically a **simple 2 port switch** (Single In, Single Out (conditional) layer 2 repeater)
- just like switch - conditional forwarding - forwards (eg left to right) unicast messages only if dst node is on (right)  side of bridge and all forward broadcast traffic (ie creates separate collision domains but single broadcast domain)

[see](https://ipwithease.com/difference-between-a-switch-and-a-bridge/)

           
### Hub (L1) 
- (Multiport) repeater. boosts (unconditionally) a signal to increase distance reachable. - - Layer 1. (Effectively longer wire)

- Media Converter - connect one type of medium (wire) to a different one. eg copper <-> fibre (optic)






### OSI Model/Stack  

| Layer             |  Protocols  | Devices | Adressing|
| -------           |     ------- | ------- | ------- | 
| 7 Application     |  |  | 
| (6 Presentation)    |  |  | 
| (5 Session)         |  |  | 
| 4 Transport       | TCP (Segments), UDP (Datagrams) | Multilayer Switch  | port |
| 3 Network (Internet)     | IP, ARP (Packets) | Router  |  IP Address
| 2  Data Link (Network)    |  | Switch | Mac Address |
| 1  Physical      | bits |  Hub |                               
 
Note: in TCP/IP Model:
 - 5-7     are combined as single "Application" Layer, 
- 3       is called "Internet" and 
- 2       called "Network" 

### TCP vs UDP

- Tcp:    
    - connection oriented
    - reliable (guaranteed delivery, error checking)
    - flow control  - receiver informs sender how bit its "receive buffer" is so its not overrun
    - ordered - packets arrive in same order as sent (but not necessarily 1:1 ie one - packet sent might arrive as 2 smaller ones)
    - slower (has to do more)

- Udp:      
    - connectionless
    - unordered
    - unreliable
    - fast        

          
### ARP (Address Resolution Protocol):

- "Whats Mac address for this IP address"? 
- Both routers and hosts maintain ARP tables


### DHCP (Dynamic Host Configuration Protocol):

- DHCP server (often runs in router) dynamically assigns an IP address and other network configuration parameters (IP address of DNS server and default gateway (route))
to each device on a network so they can communicate with other IP networks. Note: Host still doesnt know MAC address of router, 
so it will still have to send ARP request to find it (before sending messages to router).

- Hosts send all all IP packets with destination address outside of its subnet to the default gateway


### Sockets:

- OS generally only exposes Networking to (user space) programs via the Sockets (Api).
- Its basically the way (user space) programs interact with TCP/IP functionality.
- Socket is the interface between the application layer and the transport layer within a host. 
- It is also referred to as the Application Programming Interface (API) between the application and the network, 
since the socket is the programming interface with which network applications are built


### IP Masquerading

- Router "hiding" the private Ip addresses of hosts in its network form the outside world eg via:


### NAT (Network Address Translation)

Router changes 
- a) src IP address of outgoing packets (of some internal/private hosts) to its own, and 
- b) vice-versa with dst address of incoming packets (that are part of same tcp connection as a) -  ie src and dst ip_address:port match. _"Conntrack"_ is used for this). 


- ##### Port Mapping (Forwarding)

- Router additionally assigns a (sender's internal) port to outgoing packets. 
- This is used to "index" internal (private) host and perform the NAT. 
- This implementation of NAT is called **PAT** (port address translation).
- IP **Address _and_ Port** Mapping would be a better name since its actually mapping one pair of ip (address, port) -> another pair


### Circuit vs Packet Switching

- Packet:
     - Internet is packet switched - Ip and Ethernet send "packets" each of which contains all address information necessary for delivery
    
- Circuit: 
    - PSTN (Public Switched Telephone Network) uses circuit switching - a dedicated communication channel (of fixed bandwidth) is created 
    for a conversation during which no (further) address information need be sent.

    - Note: Its possible to packet switch over a circuit switched connection (effectively reserving a fixed bandwidth and unnecessarily 
    sending address info with each packet - worst of both worlds) - this is how internet connection used to work (modem?)    
                    

