##  web server - shared volume
simple python web server that serves index.html with content (live) editable on host 

- `docker build -t simple-docker-app --file dockerfile .`
    pass current dir as build context - superfluous




- `docker run -p 8000:8000 -v $(pwd):/app simple-docker-app`
    run the app, adding the current dir as a shared volume  so edits in host are "live" in container

---
Note: since dont need any (copying in) dockerfile (or build context) could simplify the above 2 commands to:
       
- `docker run -p 8000:8000 -v $(pwd):/app python:3.9-slim python3 -m http.server 8000`

--- 
###
-  http://localhost:8000
    Point browser here

#####
- `index.html` 
**edit** and **refresh** browser should reflect edits