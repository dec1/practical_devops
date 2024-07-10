## Sockets 

The OS offers to access network protocols only via the (["Berkley Bsd" or "Posix"](https://en.wikipedia.org/wiki/Berkeley_sockets)) Socket Api
               



### 1) Network
- #### a)  TCP/IP Sockets
    - Layer 4
    - **AF_INET**
    - The most common and widely used, fundamental for network communication.
    - These sockets provide (indirect) access to the TCP and UDP protocols, which are used for most internet communication.
    - Common Use Cases: HTTP frameworks, web servers, and other networked applications.
    - Examples: Web servers (e.g., Apache, Nginx), network clients and servers, HTTP frameworks.

###
- #### b) Raw Sockets
    -  Layer 2 (Ethernet Frames) and Layer 3 (IP Packets)
    - **SOCK_RAW**
    - These sockets allow access to raw network frames at the data link layer, or raw IP packets, bypassing the TCP/IP stack.
    - Privileges: Requires elevated privileges (e.g., sudo) due to potential security risks.
    - Common Use Cases: Network diagnostic tools, custom protocol implementations.
    Examples: Wireshark, tcpdump, custom packet generation tools.

----
_Aditionally the Api offers a form of IPC_
### 2) Local 
- #### IPC Sockets (Inter-process Communication IPC)  
    - **AF_UNIX**
    - These sockets provide a mechanism for communication between processes on the same machine, using Unix domain sockets.
    - Common Use Cases: Local inter-process communication, where performance and efficiency are important.
    - Comparison: While useful, they are not as commonly used as pipes for simple IPC tasks.
    - Examples: Local services communicating with each other, certain database systems (e.g., PostgreSQL).
---
### Examples:
- **Tcp**
    ```python
    import socket

    # Create a TCP/IP socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address
    server_address = ('localhost', 10000)
    tcp_socket.connect(server_address)

    try:
        # Send data
        message = 'This is a message.'
        tcp_socket.sendall(message.encode())

        # Receive response
        data = tcp_socket.recv(1024)
        print('Received:', data.decode())

    finally:
        # Close the socket
    tcp_socket.close()
    ```

- **Raw**
    ```python
    import socket

    # Create a raw socket
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    # Enable the socket to include IP headers
    raw_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    try:
        # Example: sending a simple ICMP packet (not a full example, just for demonstration)
        # ICMP packet must be crafted with appropriate headers and data
        icmp_packet = b'\x08\x00'  # ICMP echo request, type 8, code 0
        raw_socket.sendto(icmp_packet, ('8.8.8.8', 0))

        # Receive a response
        data, addr = raw_socket.recvfrom(65535)
        print('Received from', addr, data)

    finally:
        # Close the socket
        raw_socket.close()
    ```

- **IPC**
    ```python
    import socket
    import os

    # Create a Unix domain socket
    ipc_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # The file path for the socket
    socket_path = '/tmp/ipc_socket'

    # Make sure the socket does not already exist
    try:
        os.unlink(socket_path)
    except OSError:
        if os.path.exists(socket_path):
            raise

    # Bind the socket to the file path
    ipc_socket.bind(socket_path)

    # Listen for incoming connections
    ipc_socket.listen(1)

    try:
        # Accept a connection
        connection, client_address = ipc_socket.accept()
        try:
            print('Connection from', client_address)

            # Receive the data
            data = connection.recv(1024)
            print('Received:', data.decode())

            # Send a response
            connection.sendall(b'This is a response.')

        finally:
            # Clean up the connection
            connection.close()

    finally:
        # Clean up the socket
        ipc_socket.close()
        os.unlink(socket_path)
    ```  

----
Api:
     
    creation:
    ---------
        socket(domain, type, protocol) 
            domain:    
                        AF_INET(6) for network sockets
                        AF_UNIX for IPC sockets

            type:       SOCK_STREAM (reliable stream-oriented service or Stream Sockets) - connection stays open till explicit close()
                        SOCK_DGRAM (datagram service or Datagram Sockets) - connection only open while data is being sent or received (typically through sendto() and recvfrom()).  It's closed at all other times
                                                                                    
                        SOCK_SEQPACKET (reliable sequenced packet service)
                        SOCK_RAW (raw protocols atop the network layer)

            protocol:   IPPROTO_TCP
                        IPPROTO_SCTP
                        IPPROTO_UDP
                        IPPROTO_DCCP

    usage:
    -----
        server:    
            * bind()    
            * listen()
            * accept() 

        client:    
            * connect()

        * send()
        * recv()   
        * close()