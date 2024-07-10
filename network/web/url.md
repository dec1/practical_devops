### Url Anatomy

URLs always contain:

- **Protocol (Scheme)**
- **Host** (defined as a **FQDN**, or an **IP address**)
- **Port** (implicit default for the protocol, if not explicitly written)

DNS is used to resolve the hostname and domain name into an IP address.
They may optionally include:

- Path
- Query String
- Fragment
- User Info (username and password for authentication)


`https://` `[user[:password]@]` `www.sdom.dom.com` `[:443]` /`some/path` `[?key=val1&key2=val2]` `[#question13]`

`scheme://` `authority` /`path` `[?queryString]` `[#fragment]`
###
- `scheme` - https
- `authority` - user:password@**Host**:port
    
###
- **`FQDN` (~Host)**   =      **`hostname`**.**`domainname`**
    - `hostname` -    `www`
    - `domainname`  - `sdom.dom.com`  

    ####
    - Note:
        - DNS is used to resolve the *entire **FQDN*** (not hostname, hostname individually)
        - confusing terminology:
            - **domain** is sometime confusingly used for domainname eg in "_domain name resolution_" - which is incorrect.
            -  (FQDN itself has a confusing "domain name" at end of acronym)

    ### 
    - `top level`    -     com
    - `sub`      -  dom
    - `subsub`   -  sdom


    ###
    - `port` - 443
- `path`:       -    some/path
- `queryString` key val pairs separated by `&` or `;`
    - key=val1
    - key2=val2 


##
- `fragment`:  -       question13       

---

 - [what-every-developer-should-know-about-urls](https://skorks.com/2010/05/what-every-developer-should-know-about-urls/)
 - [qt -  url](https://doc.qt.io/qt-6/qurl.htm)