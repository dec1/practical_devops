

## Access Flow

A flow is a way of retrieving an Access Token that allows Application (browser or desktop) to gain access to a (secure) service on behalf of user. A typical (access) flow is:

- ##### User
   - An unidentified user initiates interaction with the application

- ##### Authentication Provider (AuthP)
   - The application directs the user to an Authentication Provider (AuthP) to log in using credentials that may include username, password, and multi-factor authentication

    - ##### Authorization Grant
        - The AuthP provides an authorization grant (e.g. authorization code).
            
            ######
            - The return is actually a **redirect** to a url the scheme of which can be specified by the application. Setting a **custom scheme** is ignored by browsers, but doing so  essential for desktop apps (see below)

    - ##### Token Exchange
        - The application exchanges the authorization grant at the AuthP’s token endpoint for `access tokens` (and possibly also `refresh tokens` which are longer lived than the access tokens and can be used to get a new access token or extend the lifetime of an existing one). 

- ##### Authenticated Session 
    - The application uses the access token to authenticate API requests with the SP on behalf of the uses

- ##### Authorization
     - The service provider decides if the user is authorized to make each request. Typically using  (RBAC) **roles**  and (ABAC) **attributes** (which may include roles, but also information such as location, time..) embedded in tokens, so that a Service Provider (SP) can make authorization decisions independently. This approach streamlines the process and reduces the need for repeated queries back to the IdP or AuthP.

[python example](keycloak/python_keycloak.md)

---- 

#### Extensions
- ##### AuthP -> IdP (Identity Provider)
    - An extension of AuthP, an IdP maintains identity information about registered users (eg email, address, phone number ...), and  in addition to access tokens can provide `identity tokens` with this information embedded. 


    - ###### GitHub 
        - **AuthP** for its **git** users.
            - For its git users, GitHub uses OAuth for authorization.

        - **IdP** for [social logon](federated_identity_sso.md)
    

---

- ### 2-Tier Web Applications 


    - Web applications are often separated into [2-tiers](keycloak/python_keycloak_2-tier/2-tier.md)

- ### Desktop Applications

    - The above flow is not only common in browser based, but also increasingly in Desktop applications. There is a difference in the initiation and final handling however:

        #####
    
        - Initiation (**App -> Browser**)
            - The desktop (requests the os to) opens a browser with the url of the IdP. As a query parm in the url the IdP allows optionally specifying a custom scheme for the redirect, it will return with the Authorization Code. The app uses this and sets a a custom scheme (e.g., `myapp://`) and port? that it has registered with the local os to handle.  Does it have to be running a tcp socket?
        
        #####
        - Handling (**Browser -> App**)
            - The browser is unable (unregistered with local os) to handle the `custom scheme` associated with the redirect, so the os passes it with the App. 



