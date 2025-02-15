## Helm

- #### Chart 
    A chart is (see [example](example/example.md))
    
    - A collection of Kubernetes **manifests** (yaml) files which may contain **template** placeholders for some values
    - **values** files that can be _injected_ into the templates
    - **Chart.yaml** file containing eg name and version of chart

    A chart can in a (local) directory, or in an archive (local or remote) of such a directory - called a package
    
    The 
    

- #### Chart (Dir)
    - Directory containing chart files, located by a `dir path`


- #### (Chart) Package
    - A chart dir zipped into a **tar.gz** 
    
- #### (Chart) Repository
    - collection of chart packages (online)     
        - eg [bitnami charts](https://charts.bitnami.com/bitnami)

    - add a remote repository to (local) **cache/index** (which can later be referenced via _local_repo_ref_)
        - `helm repo `**`add`** `<`**`local_repo_ref`**`>`      `<remote_repo_url>`
        
 

- #### (Chart)  Repository Cache
    - local snapshot/link to a repository (like local git repo links to remote, on which it can _fetch/pull/push_)
    - see [repo commands](commands/repo.md)

- ##### Chart Location
    A charts location can be specified (necessary for many helm commands) by
    - local:
        - `dir path` (to local chart dir)
        - `file_path` (to local `tar.gz` file)
    - remote (in a repository):
        - `url` (eg https://charts.helm.sh/stable/ingress-nginx )
        - `reference` ie `<local_repo_ref>/<chart_name>`
   
           


- #### Install
    - you can `install` a (local or remote) chart to your kubernetes cluster, which creates a so-called **release** in the cluster.
    - each release has a unique `name` and  `version` which helm stores in _metadata_ in a Kubernetes **secret** in the cluster
    - you pass the install command the chart location (`dir_path`, `file_path` or `url`)

    
    - installing a chart    
        - 1). **renders** manifest files (ie injects values) in-memory
        - 2). calls **`kubectl apply -f`** on these files

    #####
    - you can query installed charts  with `helm ls` and `helm status`

 
---

 - **Package Manager** Helm
    ###
    - **Logical Application**
        - A chart (package) usually corresponds to multiple containers working together as one (logical) application.

    - **Dependency Resolution**
        - Charts can specify dependencies on other charts. Helm can **automatically resolve** and **download** these dependencies from specified repositories (eg bitnami), similar to how package managers work in software development. Helm ensures that dependencies are installed before the chart that depends on them. This is particularly useful for complex applications where the order of deployment and interdependencies between different components (like databases, caching systems, etc.) matter.







---- 

- #### Registry
     - A collection of **repository** metainfo
      in human readable webpages, making them easer to discover and navigate. When you find an interesting repo here in WebBrowser, you can use point helm at the link listed for the repo in question. 
    The Registry doesnt maintain the repo content, just its meta data
    - eg [ArtifactHub](https://artifacthub.io/) or [bitnami](https://bitnami.com)  (ArtifactHub contains bitnami _and_ other providers)




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


