- ### Commands
    - Backup/Restore
        - **`iptables-save`**
            - Outputs the current state of the `iptables` rules on the Linux system.
                - more detailed than `iptables -L [-v]` - see below
                - `iptables-save` `| grep`
                    - useful for targeted, detailed search 

        - **`iptables-restore`**
            - Restores `iptables` rules from a file, typically used in conjunction with `iptables-save`.

    ####
    - List
        - **`iptables -L [-v] [-n]`**
            - `-L`: **Lists** all current `iptables` rules in a more human-readable format.

            - `-v`: **Verbose** output, showing more details, such as packet and byte **counters**.
                - Note: even with -v, the output is less **detailed** then that of `iptables-save`
            - `-n`: Numeric output, which displays IP addresses and port numbers **numerically** (without resolving to names ie without reverse DNS lookup).

        ####
        - **`iptables -t nat -L`**
            - Lists rules in the `nat` table, which handles network address translation rules.

        - **`iptables -t filter -L`**
            - Lists rules in the `filter` table, which is the default table and is used for packet filtering.



    ####
    - Modify
        ####
        - **`iptables -A`**
            - Appends a new rule to the end of a specified chain (e.g., INPUT, OUTPUT, FORWARD).

        - **`iptables -I`**
            - Inserts a new rule at the specified position in a chain (e.g., INPUT, OUTPUT, FORWARD).

        - **`iptables -D`**
            - Deletes a rule from a chain by specifying the rule or its position.

        - **`iptables -F`**
            - Deletes (removes) all rules in the specified chain, or all chains if no chain is specified.


