 
### 2-Tier Web Application

Server often split into [2-tiers](../../access_flow.md)

- [frontend](frontend.md)
    - browser interacts with this
    - retrieves authorization code, which it passed too backend

####
- [backend](backend.md)
    - frontend interacts with this
    - uses authorization coe from frontend to get token 

####
- The splitting of the token retrieval into 2 separate steps facilitates.

    #####    
    - the browser (which interacts with frontend) needing to be involved in as little of the process as possible. Good because maintaining [security in browsers](../../browser_security.md) is difficulty. 

    #####
    - backend which maintains the credentials the longest, need never know the username and password (which is generally valid much longer), but only ever has a token of limited lifetime (which needs regular refreshing - something which can be refused if secutity breach suspected)



