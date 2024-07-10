                 ----------------------------------------------------- 
                  Docker Compose - Building and linking Containers
                ------------------------------------------------------
                
# Docker compose makes it easier to run (one or) several containers (and "link" them together), than running each individually with "docker run"
# Call '> docker-compose' with a 'docker-compose.yml' file, which contains ~ same params you would pass to '> docker run' for each container             
                
 
 # Simple docker compose file:
 
     # docker-compose.yml
     --------------------
        version: '3'
        services:
          redis:
            image: redis


 # A service is (the blueprint for) one or more instances of a given container

 # By default, any service can reach any other service at that service’s name (in network commands where it would otherwise use ip address)
 # "links" item in a service allows you can specify extra aliases  - modifies container's /etc/hosts
 # as an option in docker run its deprecated, but not in docker-compose! 
 # 'depneds_on' ensures containers get started in necessary order
 
 # (If necessary, create and) start services in fgd from the docker-compose.yml file in current directory
 >  docker-compose up
 # CTRL+ C to stop (containers automatically get names like "compose_redis_1" )
  
 # start services in bgd
 >  docker-compose up -d
 
 # stop services
 > docker-compose stop/kill
 
 
 # create 2 of "redis" container and start ( names : "compose_redis_1", "compose_redis_1")
 > docker-compose up --scale redis=2
 

 # stop and delete containers started from this docker-compose.yml
 > docker-compose rm
  
# Analogous to "regular" docker commands (but apply to containers from current docker-compose.yml)
 > docker-compose ps
 > docker-compose logs
 > docker-compose start
 
 