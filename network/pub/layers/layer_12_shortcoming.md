## Layer 2 - Shortcomings

Several shortcomings become apparent when considering scaling LANs to include more interfaces distributed more widely (let alone across the whole planet):

- ##### 1) Hardware Addresses    

    ######
    - Are burned during assembly, before the NICs are even sold (let alone when their usage is determined).
        
    ######
    - **Inflexible**: When you replace an interface (even with an identical copy), the address changes, requiring all other nodes on teh LAN to relearn it.
    
        
    ######
    - "Random" numbers: No inherent way to identify addresses by **role** (e.g., "the printer") or **region** (e.g., "our office"). Any address could belong to any device or location.

- ##### 2) Address Discovery
    - There's no built-in way for an interface to ask "who's there?" (i.e., discover the addresses of other listening interfaces).

- ##### 3) Single Switch/LAN Scaling
    A single LAN can grow with a single switch (or multiple switches, with one necessarily being "in charge").
    
        
    ######
    - Switches handle many (1000+) interfaces well but have limits. Even with multiple switches servicing a single LAN, coordination overhead grows with the number of interfaces.

- ##### 4) Multiple Switches/LANs
    Instead of growing a single LAN, one could try letting separate LANs communicate by enabling switches to send packets to each other. (This would require switches to have interfaces both in their own LAN and in those with other switches - technically forbidden by Layer 2).

    ######
    - A big challenge would then be determining the best **path** for a packet to take across multiple switches.
    
    ######
    - Since MAC addresses are random, a switch would need to store the chosen path (or at least the next hop along that path) for every possible destination, which scales very poorly (linearly with the number of connected interfaces).
    
    ######
    - Packets would need to include a further address (in addition to the ultimate destination) - that of the next switch on the path to this destination
    
    ######
    - Combining LANs with differing Layer 2 standards further complicates things. A single switch would need to be able to process packets in **multiple standards** if it wants to communicate with switches on different protocols (e.g., Ethernet vs. others).

- ##### 5) Security
    Layer 2 traffic is fundamentally insecure:
    
    ######
    - There's no inherent way for interfaces to verify each other. Switches just "learn" which interfaces are connected where by observing the **src** addresses of packets they forward to the intended recipient.
    
    ######
    - Any interface can "pretend" to have any address (**MAC spoofing**) by simply writing a different source address in outgoing packets.
    
    ######
    - An interface could be replaced by a malicious one at any time (without the switch or other interfaces being aware), potentially **intercepting packets** intended for the original device.
    
    ######
    - There is no inherent encryption of Layer 2 packets.
    
    ###
    - **Note**: These vulnerabilities highlight why using public Wi-Fi is fundamentally insecure. On public networks, all devices connected to the same Wi-Fi network can communicate at Layer 2 with your device, exposing it to potential attacks such as MAC spoofing or packet interception.

---

## Solutions – Layer 3

Rather than altering the fundamental workings of Layer 2 to address its shortcomings, it was decided to build on top of it. Switches are excellent at what they do, and communication within a single LAN — **right down to voltages, currents, and bits of information on the physical level** — working reliably as it does, is an amazing feat of engineering. Instead of complicating Layer 2, improvements were engineered as layers (of abstraction) on top of it.

This approach mirrors the Unix philosophy: "Make complicated tools not from scratch, but by combining simple ones, each of which does one simple task well."

#### Virtual (IP) Addresses

- Each interface gets an additional IP address, which is:
    - Independent of its hardware address.
    - Grouped into *ranges* (subnets), reflecting location, role, etc., as needed.
    - Allowed to be changed at a later time eg to facilitate better grouping.
#### Routers

- A new class of device that specializes in determining the best **path** to send a packet along to reach its ultimate destination.

- Can **translate** Layer 2 packets from one standard to another (if necessary) when sending them to the next step (LAN) on the journey.

- Each router manages a subnet, so other routers only need to keep track of the **router managing the IP range**, rather than every individual destination. This division of labor conquers the scaling problem.

#### Packets - Encapsulation

- Layer 3 packets (which include the ultimate destination IP address) are embedded in the payload of Layer 2 packets. These body of these Layer 2 packets are essentially "containers" for the layer 3 packets. They are like russian dolls housing complete (header and payload) of layer 3 packets.

#### Backward Compatibility

######
- It's important to note that a Layer 3 packet travels each step of the way across an underlying Layer 2 network (router). Layer 3 exists only on top of Layer 2, never separate from it.

######
- Using Layer 3 is optional for interfaces on any given LAN. They can still communicate at Layer 2 just as before Layer 3 was introduced. What they put into the payload of the layer2 packets is completely up to them.

######
- However, any interface that wants to benefit from Layer 3 functionality (such as sending/receiving packets beyond its own LAN) must be **Layer 3 aware** and able to pack/unpack Layer 3 packets within Layer 2 packets.

######
- Similarly, routers repackage Layer 3 packets at each hop into new Layer 2 packets, with Layer 2 addresses matching the next router on the path. Typically, routers do this without modifying the Layer 3 packet itself, allowing the Layer 3 information to remain intact throughout the journey.
