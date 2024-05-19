
# DNS

should be more [accurately](url.md) called 
- **`domain (and host) name`** `resolution`
    -  it resolves host (hostname.domain) as "dotted string" to ip address 

lookup on host:
  - /etc/hosts
  - dns server (configured eg by [DHCP](../network.md))

### DNS Zone

- The DNS is broken up into many different zones. These zones differentiate between distinctly managed (by DNS servers) areas in the DNS namespace.

####
-  Zone File    

    - A zone file is a plain text file stored in a DNS server that contains an actual representation of the zone and contains all the records for every domain within the zone. Zone files must always start with a Start of Authority (SOA) record, which contains important information including contact information for the zone administrator.

###
- [dns-zone](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)
- [dns-zones-explained](http://www.steves-internet-guide.com/dns-zones-explained/)

### DNS server

- **resolves** 
  - ie returns ip address for url

    
- Authoratitive:

    - Are the source of truth (or a backup copy theerof) for the zone the manage 
    - Primary     - Have "live" editable versions of zone file for the zone they manage -  Real source of truth
    - Seconray    - Have (read-only) backup of primary contents


- Non-Authoratitive

    - Doesnt itself know what requested ip address is

    - Iterative - Tries to "recomend" another dns server that would
    Recursive - Recursively asks other dns servers for the answer on behalf of the (initial) requester




