- #### Examples

    ####
    - 1). **Create** Rules:
        ######
        -  DoS Prevention
            - Limit the number of connections from a single IP address to prevent a Denial of Service (DoS) attack.
            
                - **`iptables` `-A INPUT`** `-p tcp --dport 80 -m connlimit --connlimit-above 10 -j DROP`
                    -  This rule drops incoming TCP packets on port 80 (HTTP) if more than 10 simultaneous connections are attempted from a single source IP address.

        ####
        - Block Outgoing on Port 25 (SMTP)
            - Block outgoing TCP packets on port 25 (standard for email via SMTP)  to prevent the server from being used to send spam email.
                - **`iptables` `-A OUTPUT`** `-p tcp --dport 25 -j REJECT`
                
    ##
    - 2). **Query** Rules:

        ####
        - **`iptables`** **`-L -v -n`**
        
            ######
            ```yaml
            Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
            pkts bytes target     prot opt in     out     source               destination         
                0     0 DROP       tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:80 flags:0x17/0x02

            Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
            pkts bytes target     prot opt in     out     source               destination         

            Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
            pkts bytes target     prot opt in     out     source               destination         
                0     0 REJECT     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:25 reject-with icmp-port-unreachable
            ```

        ##
        - **`iptables-save`** `| grep -- "--connlimit"`
            - `connlimit` doesnt get output by `iptables -L -v` 
            ```yaml
            -A INPUT -p tcp -m connlimit --connlimit-above 10 --connlimit-mask 32 --connlimit-saddr --dport 80 -j DROP
            ```


   