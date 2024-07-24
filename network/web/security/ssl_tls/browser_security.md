
### Browser Security 

Browsers are more susceptible to security issues than regular apps, because:

#### 
- Its a single application effectively running multiple _virtual applications_. Furthermore these apps are loaded dynamically from independent sources.

####
- Regular apps are at least to some extent isolated by the os (eg can store separate isolated directories, protected by permissions). 
 Its up to the browser itself however to keep its virtual applications as isolated as necessary  to maintain security without causing excessive **overhead**. (e.g. sandboxing, same-origin policy)

 ####
- Its partly because of this that web applications are often separated into [frontend and backend](identity_provider.md)

---
 **CSRF (Cross-Site Request Forgery)**  
- "__Session (cookie) Riding__"
    - Any request made to domain user is currently logged into (even from different page/tab) will cause submission of all cookies (and thus possible authentication)
    - Requiring (non-cookie) CSRF **token**s for each request mitigate this
    - Such tokens are **not** protection against (malicious) scripts on **same page** (see xss beklow), since such scripts can read all DOM and thus hijack even the (non-cookie) tokens
    
---
 **XSS (Cross-Site Scripting)**  


 Interaction of scripts (on **same page**) from different origins is risky

A web page can load other scripts (from anywhere in principle). This can however be dangerous, if a malicious script gets loaded and later executed. 

####
- **HTTP-only cookies**
    - Cookies that are marked with the "HttpOnly" flag in the response headers when they are set. This flag indicates to the browser that the cookie cannot be accessed via client-side scripts like JavaScript, making it more secure against certain types of attacks like XSS
    -  The browser still automatically includes HTTP-only cookies in HTTP requests sent to the server(just like it does with regular cookies), ensuring that they are available to the server for session management and authentication purposes.

####
-  **SOP (Same Origin Policy)**
    #####
    - allows  script to **read** only **http respons**es from  domain which the scripts in question originate


    #####
    - does **not** prevent scripts **sending** requests to sites other than their origin (eg to fetch remote images to embed). (the script cant read the raw http **response** thereof, just see the new **dom** the browser generates as a result)


        #####
        - default in all browsers -  developers don't need to do anything to enable SOP
        #####
        - eg when the unsanitized sql is link to script on different (malicious) domain, the remote script gets downloaded and embedded, but the origins are different and SOP applies, mitigating xxs risks 



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




