# Layer 3

A one kind of [virtual network](../virtual_network.md) which as an abstarction on top of an underlying (eg layer 2) netwok

### Subnet   
- (V)LAN <- 1:1 ->  subnet (almost always)  
    - doesn't require router - for internal (ip based) communication, since nodes are directly connected at layer 2, so can use ARP  to find hardware address for given ip address. Closely connected network nodes are in same LAN (layer2), which is generally mapped 1:1 to a subnet (layer 3)

    see [also](../web/security/subnet/subnet.md)
##
- Each interface within a subnet has a unique IP address, but they all share the same **network prefix**, which identifies the subnet.


### Router  

- connects LANs (usually) via their switches
######
- Required for one LAN (switch) to connect outside world 

######
- Works with IP addresses (and mac addresses)

######
- Forward traffic between IP based networks after examining the Layer-3 header

######
-  Non-router nodes (like hosts or servers) generally only care about packets addressed to their own IP addresses. When a packet arrives, the node checks if the destination IP matches one of its own addresses. If it does, the node processes the packet; if not, it typically ignores the packet.

######
- They require IP addresses in order to operate properly (switches do not)

######
- Use and respond to ARP messages, and listen to (but will not forward) all (ethernet) broadcast frames. 


######
### Routing Tables
- Both routers and hosts (non-router nodes) maintain routing tables (with default gateway/route respt), but those of hosts are much simpler:
- #### Host Routing Table
    -  The routing table on a host generally contains just a few entries:
        - Local Network
            - An entry for the local subnet or network, specifying that packets destined for IP addresses within this subnet should be delivered directly over the local network.           
        - Loopback Interface
            - A loopback address entry (e.g., 127.0.0.1) for local traffic directed to the same host.
        - Default Gateway 
            - Ip address of (default) router for pc/node. Without it, node can only communicate with computers on same LAN. (The routers equivalent is called "default route")


- #### Router Routing Table:


    | Subnet             |  Hop/Gateway  |  (Ext) Interface | Cost|
    | -------           |     ------- | ------- | ------- |
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



### ARP (Address Resolution Protocol):

- "Whats Mac address for this IP address"? 
- Both routers and hosts maintain ARP tables

##
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
- 3+ generally whats means by "web"


##
### Protocol Data Unit (PDU)     

-  L4 (Transport)
    - **Segment**  (Tcp)
    - **Datagram** (Udp)

- L3 (Network)
    - **Packet**   (Ip) - sometimes "packet" used for others pdu's too


- L2 (DataLink)
    - **Frame**      
                 
##
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






---
footnotes/advanced

### IP Masquerading

- Router "hiding" the private Ip addresses of hosts in its network form the outside world eg via:

- #### NAT (Network Address Translation)

    Router changes 
    - a) src IP address of outgoing packets (of some internal/private hosts) to its own, and 
    - b) vice-versa with dst address of incoming packets (that are part of same tcp connection as a) -  ie src and dst ip_address:port match. _"Conntrack"_ is used for this). 


    - ##### Port Mapping (Forwarding)

    - Router additionally assigns a (sender's internal) port to outgoing packets. 
    - This is used to "index" internal (private) host and perform the NAT. 
    - This implementation of NAT is called **PAT** (port address translation).
    - IP **Address _and_ Port** Mapping would be a better name since its actually mapping one pair of ip (address, port) -> another pair

### WAN 

- One or more connected (via router(s)) LANs 
- Pretty arbitrary definition 
    - you could (arbitrarily) divide the internet (the biggest WAN) into any number of different sets of WANs based on various ), but usually they have 
    - But usually all LANs and routers therein managed by the same authority/organization.

