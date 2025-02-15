#### remove 
- **everything** 
`docker stop $(docker ps -a -q); docker system prune -a --volumes --force; docker builder prune -af; docker volume rm $(docker volume ls -qf dangling=true)`
#####

- **specific**
    - Stop all containers:
    `docker stop $(docker ps -a -q)`
    ######

    - Remove all containers:
    `docker rm -vf $(docker ps -a -q)`
    ######
    
    - Remove all images:
    `docker rmi -f $(docker images -a -q)`
    ######

    - Remove all volumes:
    `docker volume rm $(docker volume ls -q)`
    ######

    - Remove all networks not connected to the default networks (bridge, host, none)
    `docker network prune -f`
    ######

    - Clear build cache:
    `docker builder prune -af`
    ######

    - Clear dangling volumes (volumes no longer associated with any containers or services). 
    `docker volume rm $(docker volume ls -qf dangling=true)` 


##### stop/kill containers

    
- stop running container (changes made eg files withing ctr, will be preserved across restarts)
`docker stop my_ctr`   sends SIGTERM  
`docker kill my_ctr`   sends SIGKILL .. process doesnt get chance to clean up
 
 
##### delete container:

- delete container "my_ctr"
 > docker rm my_ctr
 
- remove/delete all local docker containers  (the "-q" causes ps to return only numeric ids)
 > docker rm $(docker ps -a -q)
 
    
##### delete image
 - remove image "my_img"    
 `docker rmi my_img`
 
 - remove all docker images from your local machine
 `docker rmi $(docker images -q) `