# Tunnel

Each of the 2 endpoints of a network tunnel, do exactly one of 2 things with incoming packets, depending on whether they arrive from other end of tunnel or not. packets arriving from:

- everywhere except other end of tunnel: 
    - warp the original  packets as payloads of new "encapsulated" packets, which they then (unconditionally) send to the other end of the tunnel (not the original destination). 

- other end of tunnel: 
    - unwarp the encapsulated packets and send them to original destination

As such the name is somewhat misleading -  it stops incoming traffic going anywhere except through (as opposed to offering a way through an otherwise _impenetrable medium_, as they name might suggest)

- **[IpTables](iptables.md)** on the nodes that form the ends of the tunnel are a common way to  implement tunnels

- **VPN** is a tunnel where the endpoints are  a client (device)  and a (vpn) server

- **Overlay Networks**, add an additional address space in addition to tunneling between nodes