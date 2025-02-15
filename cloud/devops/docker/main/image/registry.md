**Registry** (eg Docker Hub)  stores collection of
- **Respository** (eg dec1/my_img) 

    - collection of **images** with same (base) name  and **different tags** (often this is, incorrectly, referred to as an "image")
        
        - images in a repository dont actually have to be based on one another - its just convention as with image names in general
           
---

### Push

- `d` **`tag`** `alpine:local_existing`  **`dec1/my_img:ver2`**
    so pushable to your registry account
        


###
- `d` **`login`** `[registry]`
    - `registry`  -  default hub.docker.com
        - enter  **user name** and **password**

- `d` **`push`** `dec1/my_image:ver2`
- `d` **`logout`**


---
### Search


- `d` **`search`** [registry] `dec1`
search Docker Hub for image
