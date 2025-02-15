### Url Anatomy

- URLs always contain:

    ######
    - **Protocol (Scheme)**

    ###
    - **Host** can be either:

        #####
        - 1). A combination of    **host name** (eg `www`), and  (dns) **domain name** (eg `example.com`)
            - confusingly often just referred to as just a (_fully qualified_) _domain name_, and abbreviated to **_FQDN_**
                - even more confusingly _domain name_ itself is often abbreviated to just _domain_, which has  [multiple different meainings](../domain.md)  
            
            ####
            - eg `www.example.com` or `www.sdom.dom.com`  
            DNS is used to resolve the host into one or more 
            IP addresses.

        or 
            
        #####    
        - 2). A single  **IP address**
            - each IP address correspods to exactly 1 (layer 2) **Interface**
    
            ##
            A web browser sets the  Http `Host Header` to the _Host_ used in the URL,
            and sends the request (with this header) to whatever IP address it (or its DNS server) resolves _Host_ to.             
            And a load balancer can forward requests with the same `Host` header, to one of possibly multiple IP addresses its _balancing_

    ######
    - _Confusing Terminology_: that _Host_ is sometimes confusingly also used to mean _Node_, even though a node can have multiple interfeces, each with (one or more)  ip address, and thus multiple hosts

    ###
    - **Port** (implicit default for the protocol, if not explicitly written)

###
- URLs may optionally include:

    #####
    - Path
    - Query String
    - Fragment
    - User Info (username and password for authentication)

####
- The general form of a URL is
    - `https://` `[user[:password]@]` `www.sdom.dom.com` `[:443]` /`some/path` `[?key=val1&key2=val2]` `[#question13]`

    eg
    ###
    - `scheme` - https
    - `authority` - user:password@**Host**:port
        
        ###
        - **Host**   =      **`host_name`**.**`domain_name`** 
            - `host name` -    `www`
            - `domain name`  - `sdom.dom.com`  

            ####
            - Note:
                - DNS is used to resolve the **entire** _host_name.domain_name_ combination (not _host name_, and _domain name_ individually)


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
 - [qt -  url](https://doc.qt.io/qt-6/qurl.html)
