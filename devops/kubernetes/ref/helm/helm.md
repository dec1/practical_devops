## Helm

-  **Registry** ([artifacthub](https://artifacthub.io),  [bitnami](https://charts.bitnami.com))
    - Local Repository *Alias* [my-bitnami]() -> **Respository** ([bitnami charts](https://charts.bitnami.com/bitnami))
        - Local Chart *Alias* [my-nginx]() -> **Chart** [bitnami/nginx]()
            - Local **Release** my-nginx  [15.14.0]() -  install of _chart_ **version** 15.14.0

--- 
- ### Chart
    Collection of Kubernetes ***template* manifests** combined into a single package. 
    Values can be **injected** for the template variables for customization
    #####
    *Application Stack*: The resources in a chart typically work together to provide a complete application stack (e.g., a WordPress application with a front-end deployment and a MySQL database deployment).

    - ##### Dependency Resolution

        - Charts can specify dependencies on other charts. Helm can **automatically resolve** and **download** these dependencies from specified repositories (eg bitnami), similar to how package managers work in software development. Helm ensures that dependencies are installed before the chart that depends on them. This is particularly useful for complex applications where the order of deployment and interdependencies between different components (like databases, caching systems, etc.) matter.




- ### Repository
    Collection of (possibly multiple versions of) **charts**. 
    - You can **add** (index) a remote repo to your local Helm client.
    - You can install exactly one version (**release**) of one or more of each of these charts, in your cluster
  
    
- ### Registry
     - Collection of **repository** metainfo
      in human readable webpages, making them easer to discover and navigate. When you find an interesting repo here in WebBrowser, you can use point helm at the link listed for the repo in question. 
    The Registry doesnt maintain the repo content, just its meta data
    - eg [ArtifactHub](https://artifacthub.io/) or [bitnami homepage](https://bitnami.com)  (ArtifactHub contains bitnami _and_ other providers)


---
- #### Help
    `helm` **`help`**
    -  get help on a (sub) **command**
    `helm` `help` **`ls`**
        ```yaml
        .....
        Aliases:
            list, ls  
        ```
    ####


