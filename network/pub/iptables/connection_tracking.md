### Connection

A connection is a series of PDUs that can be considered to be part of a single `conversation` between `2 endpoints`.

- #### Protocol Level
    Some protocols (e.g., TCP) have an explicit and clear definition of what a connection is and how it must be established between two endpoints (e.g., a client and server) before any application data is transmitted. The endpoints are actively involved in establishing and maintaining this connection. The protocol continuously tracks the state (e.g., `SYN_SENT`, `ESTABLISHED`, `FIN_WAIT`) of each connection — i.e., whether it is in the process of being established, actively transmitting data, or being terminated.

- #### OS Level
    - The OS on one or both of the nodes in question (or even any intermediate node) can also perform connection tracking independently of any protocol-inherent tracking. This tracking is done transparently to the endpoints. The OS determines what packets are part of what (if any) connection, unbeknownst to the endpoints, and in addition to any explicit, protocol-level tracking performed by the endpoints.

    #####
    - In Linux, this is performed by the kernel's **`Netfilter`** framework, which can be interfaced with by user-space applications like [`iptables`](iptables.md). Rules (firewall) defined in **`iptables`** are actually implemented by Netfilter. Netfilter supports rules for routing packets between networks, allowing any Linux system to function as a **router**

    #####
    - Netfilter incorporates information from any protocol-level tracking available (e.g., TCP) and monitors how long elapses between packets exchanged between the same two endpoints (short intervals => likely to be considered part of the same connection).
    
    #####
    - **Connection Table**: 
        - *Netfilter* maintains a connection table where it records the state of each active connection, including the endpoints, protocol, and state (e.g., NEW, ESTABLISHED, RELATED, INVALID). This table is used to make decisions about how subsequent packets should be handled.
