### Domain
Can refer to one of 3 different things:

- #### 1).  Administrative Domain

    A domain is a set of nodes on a network that are centrally managed by a **domain controller**. The domain controller, which often functions as a [dns server](./web/dns.md) for the domain, maintains information on **user accounts** and enforces policies governing roles and **access controls** for these accounts within the domain.


    ####

    Examples of domain controller (and [Identity Provider](web/security/ssl_tls/federated_identity_sso.md)):

    - ##### Windows

        ####
        - **Azure AD (Entra ID)** is a 
        cloud-based version of Active Directory.
            - cloud based
            - any nodes (not just windows)

        ####
        - **Active Directory** 
            - self hosted
            - windows nodes

            - uses **LDAP** (Lightweight Directory Access Protocol)
                - A protocol used to access and manage directory information (eg users, groups, devices) over an IP network



    - ##### Linux
        - Samba
            - Can act as an Active Directory domain controller in Linux environments.
            - Provides interoperability with Windows AD domains.

###
- #### 2). Routing Domain
    -  A collection of IP networks and routers under a common **administration** (eg choice of routing **protocols** and **policies**). This often corresponds to an administrative domain but could span multiple organizations in some cases, such as in a federated network. cf [ip range manager](routing.md) which is about which routers serve which ip ranges.

###
- #### 3). DNS Domain 
    - A [DNS domain](web/url.md), such as _example.com_, is typically managed by a single organization that controls the associated records and servers