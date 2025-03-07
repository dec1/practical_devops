#### Container Technology 

- Features of Linux (Kernel) used to implement containers
    - [Process Isolation](./process_isolation.md)
        - Cgroups
        - Namespaces
    - [UnionFS](union_fs.md)

Containers are a Linux (only) feature, made possible by those above. Non-Linux platforms (Windows, MacOS) require a **Linux VM** (behind the scenes) to run containers.

#### Terminology
- _Container_ **Runtime**
    - Low-level component that executes containers and interfaces with kernel features
- _Container_ **Engine**
    -  Higher-level component that provides user-facing functionality, APIs, and commands
- _Container_ **Image**: 
    - Packaged, immutable template containing application code, libraries, and dependencies
 

####
- [Tools](tools.md) that leverage or enhance features  of containers
    - **Image** Manager (building etc)
        - docker, podman, buildah, kaniko 
    - Container **Runtime**
        - docker, podman, container-d, cri-o
    - Container **Orchestrator**
        - kubernetes, openshift, rancher, nomad
    - **Package** Manager
        - helm

    ####
    - *Development Platforms* (for non-Linux systems)
        - **Docker Desktop** _(MacOs and Windows)_
            - bundles a Linux VM, Docker runtime, and UI 
        - **Podman Desktop** _(MacOs and Windows)_
            - bundles a Linux VM, Podman runtime, and UI 
        - **Colima** _(MacOS)_ 
            - bundles Linux VM (through Lima) with a container _runtime_ Docker or Podman - configurable)
            - no GUI (command line only) 
            - Docker/Podman _Desktop_ do _not_ use colima under the hood
            - **Lima** _(MacOS)_
                - provides a lightweight Linux VM; requires you to install a runtime like Docker or Podman separately