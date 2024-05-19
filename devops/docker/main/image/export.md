
### Local Image File (tar)

- #### save oci 

    - `skopeo` **`copy`** **`docker-daemon:img-dk`** `:<tag>` **`oci-archive:`**`img-oci.tar`
        - `img-dk`  - docker image 
        - `img-oci.tar` - oci image file
        - `tag` - default: latest

    ##
    - `podman` **`save`** `my-img-pm` **`--format oci-archive`** `-o my-img-oci.tar` 
        save image as tar archive in oci format
        - `img-pm` - image built by podman
            - `podman` `load` `-i img-dk.tar`
                can alternatively be used to load docker image file

        - test:
            - `tar` **`-xvf`** `my-img-oci.tar`
            - `ls`
                ```yaml
                my-img-oci.tar 

                # extracted
                index.json      
                oci-layout  
                blobs   
                ```

##
- #### save docker image 
- `d`**`save`** `img-dk` `-o img-dk.tar`
    - `img-dk` - image built by docker

--- 

- ### save (container as) docker (format) image

    - `d` **`commit`** `[-m "my mesg" -a "authors name"]`  **`my_ctr`** **`my_img`**`[:my_tag]`
    save the current state of a container to an image (so it can be shared)