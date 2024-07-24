## Identity Provider (IdP)

#### Authentication Flow

How an Application (browser or desktop) typically uses an IdP 


- ##### User
   - An unidentified user tries to use the application.

- ##### IdP
   - The application redirects the user to the IdP for authentication.

- ##### Credentials
   - The user logs in with the IdP with their credentials (e.g., username, password, 2FA).
   - This process typically uses protocols like **OpenID Connect** for authentication.

- ### Token Retrieval

    - ##### a) Authorization Code
        - After successful login, the IdP returns a `authorization code`.
        
            - The return is actually a redirect to a url the scheme of which can be specified by the user (application). The custom scheme is ignored by browsers, but essential for desktop apps (see below)

    - ##### b) Token Exchange 
        - The app sends the authorization code to the IdP's token endpoint to exchange it for `access` (and `refresh`) `token`s.

- #####  Authenticated Session:
   - The app uses the access token to authenticate API requests on behalf of the user.

---

- ### 2-Tier Web Applications 


    - Web applications are often separated into a `frontend` (interacted with by the browser)  and a `backend` (interacted with by the frontend).

    ####
    - The splitting of the token retrieval into 2 separate steps facilitates  the browser (frontend) needing to be involved in as little of the process as possible. This is because maintaining [security in browsers](browser_security.md) is difficulty. The frond retrieved the authorization code, which it passes to the backend, which in turn uses it to get the token(s)

- ### Desktop Applications

    - The above flow is not only common in browser based, but also increasingly in Desktop applications. There is a difference in the initiation and final handling however:

        #####
    
        - Initiation (**App -> Browser**)
            - The desktop (requests the os to) opens a browser with the url of the IdP. As a query parm in the url the IdP allows optionally specifying a custom scheme for the redirect, it will return with the Authorization Code. The app uses this and sets a a custom scheme (e.g., `myapp://`) and port? that it has registered with the local os to handle.  Does it have to be running a tcp socket?
        
        #####
        - Handling (**Browser -> App**)
            - The browser is unable (unregistered with local os) to handle the `custom scheme` associated with the redirect, so the os passes it with the App. 



