
#####  volumes
   
- Share dir with host ( -v hostDir:containerDir)
` docker run -it -v /home/declan/tmp/my_docker_vol:/home/tmp alpine /bin/sh`
     - note that this works fine if dir path already exists on host. Otherwise docker creates path necessary and only root has access in host. any contents in the docker dir before the mounting will be lost - ie mounting is from host to container (prev contents of host dir still there, but those of container dir overwritten)
 
 - run a container from image and share a host volume
` docker run  -v /home/zodmoran/Dokumente/zone/low/docker-share/:/home/docker-share -it --entrypoint=/bin/bash --name my_ctr_zemu3d_18 dec1/zemu3d_u18:ver1` 

 
- run a container from image and share a host volume
` docker run  -v /home/declan/Documents/zone/low/tmp/qt/tst/:/home/docker-share -it --entrypoint=/bin/bash --name my_ctr stateoftheartio/qt6:6.4-gcc-aqt`

#####  copying (cp)

- copy a file (tmp/wee.txt) from a docker container my_ctr to host  (or vice-versa)
 `docker cp my_ctr:/tmp/wee.txt /home/tmp/wee.txt`
    - works with stopped containers too


