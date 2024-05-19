
### Browser Security 


---
 **CSRF (Cross-Site Request Forgery)**  
- "__Session Riding__"
- Any request made to domain user is currently logged into (even from different page/tab) will cause submission of all cookies (and thus possible authentication)
- Requiring **CSRF token**s for each (trusted) request (form) mitigate this (as would using non-cookie token?!)
- Such tokens are **not** protection against (malicious) scripts on **same page**, since such scripts can read all DOM and thus hijack the tokens
---
 **XSS (Cross-Site Scripting)**  


 Interaction of scripts (on **same page**) from different origins is risky

A web page can load other scripts (from anywhere in principle). This can however be dangerous, if a malicious script gets loaded and later executed. 


- eg unsanitized (link in) sql  
    - browser user is tricked into loading an executing script from a malicious site (different to the one they think theyre visiting) eg from rendering of   
    

####
-  **SOP (Same Origin Policy)**
    #####
    - allows  script to **read** only **http respons**es from  domain which the scripts in question originate


    #####
    - does **not** prevent scripts **sending** requests to sites other than their origin (eg to fetch remote images to embed). (the script cant read the raw http response therof, just see the new do the browser generates as a result)


    #####
    - default in all browsers -  developers don't need to do anything to enable SOP
    #####
    - mitigates XXS eg when the unsanitized sql was link to script on different (malicious) domain, the remote script gets downloaded and embedded, but the origins are different and SOP applies



    ####
    - **CORS (Cross-Origin Resource Sharing)**
        - Relaxes SOP restrictions 
        - increases origins a scripts (from different origin) can read responses from.
        - Requires developers to add specific HTTP headers.

        #####
    -  **CSP (Content Security Policy)** 
        - Increases SOP restrictions
        - limits origins scripts (from different origin) can make requests to
        - Requires developers to add specific HTTP headers.




