### Permission Checks - for Process trying to act on File

The logic of the [permission checking](permissions.md)  when a process tries to perform and action on a file:


```mermaid
flowchart TD
    B(Process has Capabilities?)

    C(<b>Capability</b>
    allows Op):::class_cap

    B -->|Yes| C
    
    B -->|No|D("<b>Root</b>   <br> (process uid=0)"):::class_root
    
    C -->|Yes| Allow[Allow Access]
    C -->|No| D
    
    D -->|Yes| Allow
    D -->|No| F(File has 
    ACL Entries)
    
    G(ACL <b>UID</b> Entry  <br> allows op):::class_acl

    F -->|Yes| G
    F -->|No| K(File uid matches <br> process <b>User</b> <br> AND <br> File Owner Triad allows Op):::class_trad
    
    
    G -->|Yes| Allow
    G -->|No| H(ACL <b>Groups</b> Entry <br> allows Op):::class_acl
    
    H -->|Yes| Allow
    H -->|No| I(ACL <b>Other</b> Entry <br> allows Op):::class_acl
    
    I -->|Yes| Allow
    I -->|No| Deny[Deny Access]
    
    K -->|Yes| Allow
    K -->|No| L(File Gid matches any <br> process <b>Group</b>  <br> AND <br> File Group Triad  allows Op):::class_trad
    
    L -->|Yes| Allow
    L -->|No| M(File <b> Other </b> Triad Allows Op):::class_trad
    
    M -->|Yes| Allow:::class_allow
    M -->|No| Deny:::class_deny

    subgraph Legend
        Legend_Cap["Capabilities"]:::class_cap
        Legend_Root["Root"]:::class_root
        Legend_ACL["ACL"]:::class_acl
        Legend_Trad["Traditional <br> (Permission Bits <br> aka File Mode)"]:::class_trad
        
        
    end

    Allow ~~~ Legend
    style Legend fill:none
    %%style J fill:#FFB6C1
    classDef class_cap fill:deepskyblue,stroke-width:2px;
    classDef class_acl fill:lightblue,stroke-width:2px;
    classDef class_trad fill:orange,stroke-width:2px;
    classDef class_root fill:violet,stroke-width:2px;

    classDef class_allow fill:lime,stroke-width:3px;
    classDef class_deny fill:red,stroke-width:3px;
    
```
###
```bash
# Capabilities check
if (process has any (permitted) capabilities set)
    if (one of these capabilities permits the operation on target file)
        allow access;  // using capabilities limits even root access
else if (user is root)
    allow access;

# ACL check
else if (file has ACL entries)
    if (an ACL entry for the effective UID permits the operation)
        allow access;
    else if (an ACL entry for one of the process’s groups permits the operation)
        allow access;
    else if (an ACL “other” entry permits the operation)
        allow access;
    else
        deny access;

# Traditional (permission bits) check:
else if (process’s effective UID matches file’s owner,  AND file owner’s permission allows the operation)
    allow access;
else if (process’s effective GID matches the file’s group OR any of its supplementary groups matches, AND file group’s permission allows the operation)
    allow access;
else if (file’s “other” permission allows the operation)
    allow access;
else
    deny access;
```

