### Containerized Two-Tier System

- Backend and front end in separate containers
- User on host talks to front end through port 3000
- Front end gets message on port 5000 where its listening
- In turn talks with backend on port (and url) specified in docker compose file - exported to env var - dev setup
    - can use fallback (default) for when env var is not set (eg production)
- clean separation of front end and backend.


---

- build containers (using compose file in current dir)
    - **`docker-compose up --build -d`**

####
- tear down containers
    - `docker-compose down`

####
- show logs from a particular container
    - **`docker-compose logs frontend`**

        ```yaml
        Attaching to my_dev_frontend_1
        frontend_1  |  * Serving Flask app 'app'
        frontend_1  |  * Running on all addresses (0.0.0.0)
        frontend_1  |  * Running on http://127.0.0.1:5000
        frontend_1  |  * Running on http://172.20.0.3:5000
        frontend_1  | Press CTRL+C to quit
        frontend_1  | 172.20.0.1 - - [09/Jul/2024 09:37:03] "GET / HTTP/1.1" 200 -
        ```

####
- call front end from host
    - **`wget http://localhost:3000`**
        ```yaml
        --2024-07-09 10:02:37--  http://localhost:3000/
        Resolving localhost (localhost)... 127.0.0.1
        Connecting to localhost (localhost)|127.0.0.1|:3000... connected.
        HTTP request sent, awaiting response... 200 OK
        Length: 42 [text/html]
        Saving to: 'index.html.1'

        index.html.1                             100%[=================================================================================>]      42  --.-KB/s    in 0s      

        2024-07-09 10:02:37 (83.4 KB/s) - 'index.html.1' saved [42/42]
        ```
