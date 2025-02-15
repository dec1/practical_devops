# DNS

Should be more [accurately](url.md) called 
- **`domain (and host) name`** `resolution`
    - It resolves [host](url.md) (host_name.[domain_name](../domain.md)) as a "dotted string" to an IP address 

Lookup on host:
  - `/etc/hosts`
  - DNS server (configured, e.g., by [DHCP](../layers/network_logical.md))

### DNS Zone

- The DNS is broken up into many different zones. These zones differentiate between distinctly managed (by DNS servers) areas in the DNS namespace.

####
- Zone File    

    - A zone file is a plain text file stored on a DNS server that contains the actual representation of the zone and includes all the records for every domain within the zone. Zone files must always start with a Start of Authority (SOA) record, which contains important information, including contact details for the zone administrator.

###
- [dns-zone](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)
- [dns-zones-explained](http://www.steves-internet-guide.com/dns-zones-explained/)

### DNS Server

- **Resolves** 
  - i.e., returns the IP address for a URL (using the records below)

- Authoritative:

    - Are the source of truth (or a backup copy thereof) for the zone they manage 
    - Primary: Have "live" editable versions of the zone file for the zone they manage - Real source of truth
    - Secondary: Have a (read-only) backup of primary contents

    - **DNS Records** 
        The authoritative DNS server maintains DNS records for hosts in this domain, e.g.:

        - **A** (Address) Record: 
            - Maps a domain to an IPv4 address.
        - **AAAA** (IPv6 Address) Record: 
            - Maps a domain to an IPv6 address.
        - **CNAME** (Canonical Name) Record: 
            - Maps an alias domain to a canonical domain name.
        - MX (Mail Exchange) Record: 
            - Specifies mail servers for a domain.
        - TXT (Text) Record: 
            - Holds arbitrary text, often for verification or configuration (e.g., SPF, DKIM).
        - NS (Name Server) Record: 
            - Specifies the authoritative DNS servers for a domain.
         - PTR (Pointer) Record: 
            - Used for reverse DNS lookups, mapping an IP address to a domain name.
        - SRV (Service) Record: 
            - Defines the location of servers for specific services (e.g., SIP, XMPP).

- Non-Authoritative

    - Doesn't itself know the requested IP address

    - Iterative: Tries to "recommend" another DNS server that would know the IP address.
    - Recursive: Recursively asks other DNS servers for the answer on behalf of the (initial) requester.
