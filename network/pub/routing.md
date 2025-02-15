- **IP Range Manager (Allocation)**
Organizatons are allocated **ip address ranges** (cf [dns domain](domain.md))
   -  they in turn can allocate portion therof to (smaller) organizations (recursively).
  -  *note*: ip ranges are independent of domain (and host) names. ie 2 contiguous ip addresses may have comepletely different domain (and host) names (and vice-versa) 
  
    ###
    - **Internet Routing Registries (IRRs)**
    The organizations must in return **maintain** database (IRR) containing **gateways** (routers that know how to route to these  IP address ranges
        - or if sub allocated - gateway of smaller organization that does  (recursively)

    - ##### vs Routing Domain
    An IP Range Manager can manage multiple routing domains, and a routing domain can span multiple organizations

###
- **Border Gateway Protocol (BGP)**
The means by which routers access (and share with nearby routers) and maintain current, this information. 
  - Key to their performance
  - As otherwise in worst case scenario, router would route packet to its default gateway, the router at which would route to its default getway, ad infinitum - until finally actual destination would be reached (`by chance`)
  - This info (as well as that learned form recent requets) is **cached**