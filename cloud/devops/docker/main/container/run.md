
### run

- `d` **`run`** **`[--name my_ctr]`** `[-it]` `[-d]` `[-p 8080:80]`  **`[--entrypoint=<ep>]`** **`[--network=<type>]`**  **`my_img`**`[:my_tag]` **`[cmd]`**

    - `--name` - name of container (default: automatically generated)
    - `-i` - see output from container in (host) terminal
    - `-t` - put input to container from host terminal
    - `-d` - run container in background (as a daemon)

    - `-p <host:container>` - map host port (8080) -> container port (80)
    - `my-img` - image to use (eg nginx, alpine, busybox) 
    - `:my-tag` - default: latest

    ###
    - **`cmd`** -  override CMD in dockerfile 
        - `/bin/sh `
        - `/bin/sh echo "hi there"`
        - `env`
    #####
    - **`--entrypoint`** -  override ENTRYPOINT in dockerfile   
        - `--entrypoint='["/bin/echo", "hey.."]']`

    ####
    - **`--network`** -  [network type](../network.md) to (create and) run container in:
        #####
        - `bridge`	**default** network driver.
        - `host`	Remove network isolation between the container and the Docker host.
        - `none`	Completely isolate a container from the host and other containers.
        #####
        - `container:<name|id>`  attach a container to another container's networking stack -
            - both containers then **share a single interface** (and ip address)

        #####
        - .... see  official [docs](https://docs.docker.com/network/#user-defined-networks) 
    
    ###
    (Note: `-i` is needed to see any output from cmd/entrypoint) 

----

###
**run** =  { **pull**, **create**, **start** }, which can be performed individually:

#####
- `d` **`pull`** `alpine`
download an image (without running it) from registry

#####
- `d` **`create`** `--name my_ctr  alpine`
Create a container from image (downloading image first from registry, if necessary), and optionally give it a custom name (Can pass pretty much same parms as 'run' here)

#####
- `d` **`start`** `[-it] myContainer`
start an existing container
    

