


     
##### Identification

- **id**
    - ` docker images my_image --format "{{.ID}}"`    show id of my_image 
    - ` docker images          --format "{{.ID}}"`    show ids of all images
    
    Uniquely identifies a **single** image

### 
- **Name:Tag**

    All images also have at least one combination **{name, tag}** 
    - each *combination* is **unique** and **arbitrary**
    #####
    - `latest`-  **default** tag  
  
    ####
    - The combination of name and tag is completely **arbitrary**, but its convention to include a **version** number in the tag, and to only give same name to images which are based on one another.







