

##  debug app running in container

- _should work but doesnt (quite) - container cant connect to debug server_

- ### pycharm - create docker run config
    - set `Dockerfile`, `Image Tag`, `Container name` and  `Run options`
    so that run command preview is:
    `docker build -f dockerfile -t my-img-3 . && docker run --name my-ctr-3 my-img-3` 

    - `Path mappings` . `..../03_debug=/my-app`

- ### pycharm - create debug server config
- `IDE host name`  localhost
- `Port` 9000

- ### pydevd_pycharm

- allows app running in container to connect to debug server running on host. needs to be added to pip install and
 the following to app.py>
  `pydevd_pycharm.settrace('host.docker.internal', port=9000, stdoutToServer=True, stderrToServer=True)`

- start 
    - **debug server** (debug) - pycharm debug
    - **container**   - pycharm run







