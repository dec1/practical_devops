### Domain

A domain is a set of nodes on a network that are centrally managed by a **domain controller**. The domain controller, which often functions as a [dns server](dns.md) for the domain, maintains information on **user accounts** and enforces policies governing roles and **access controls** for these accounts within the domain.


####

Examples of domain controller (and [Identity Provider](security/ssl_tls/federated_identity_sso.md)):

- #### Windows

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



- #### Linux
    - Samba
    