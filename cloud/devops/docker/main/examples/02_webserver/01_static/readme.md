## web server - static 
simple python web server that serves (snapshot at time of build) dir content

- `docker build -t simple-docker-app  --file dockerfile .`
    pass current dir as build context
    the dockerfile copies this into `/app` dir


- `docker run -p 8000:8000 simple-docker-app`
    run the app

###
-  http://localhost:8000
    Point browser here