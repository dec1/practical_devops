
### Name:Tag
An image can have one or more  `name:tag` combinations 

- #### Add

    -  `d` **`tag`** **`my_img`**`[:my_tag]`  `[my_img_new]` `[:my_tag_new]`
        - create additional `name:tag` combination for image 
            #####
            - `my_img` - existing image name
            - `my_tag` - existing image tag
            ####
            -  `my-img-new` - default:  `my_img` (existing image name)
            - `my_tag`, `my_tag_new` - default: `latest`

            ###
            - _Note_: the "tag" command doesn't just set the tag for an alias, it (can) set the **name** too! 



- #### Remove
- `d` **`rmi`** **`my_img`**`[:my_tag]` 
 
    - remove `name:tag` combination for image 

    - **Also removes image** itself too if this is the **only** name:tag combination referencing it

    - `rmi` = `image rm` (alias)

