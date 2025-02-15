

###
- #### Revision
    - `helm` `repo update` - see above

    ####
    - `helm` **`upgrade`** `my-chart my-repo/jenkins`  [--version 5.0.16]
        *upgrade* 5.0.15 -> 5.0.16 (default = latest) in the **cluster**
        ```yaml
        Release "my-chart" has been upgraded. Happy Helming!
        ```
    ####
    - `helm` **`upgrade`** `my-chart my-repo/jenkins`  --version 5.0.14
        *downgrade* 5.0.16 -> 5.0.14 

    ####
    - `helm` **`ls`** `[-A]` `[-a]` 
        -  `-A` all namespaces
        -  `-a` not just `deployed` - also include `failed`, pending-install, , pending-upgrade
        lastest version of each chart **installed chart** in namespace (cf `helm repo ls` above)
        ```yaml
        NAME    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
        my-chart  default         3               2024-02-22 18:38:51.10607678 +0000 UTC  deployed        jenkins-5.0.14  2.440.1   
        ```

    - **history**     
        ###
        - `helm` **`history`** `my-chart `
            all *revisions* of  chart
            ```yaml
            REVISION        UPDATED                         STATUS          CHART           APP VERSION     DESCRIPTION     
            1               Thu Feb 22 18:10:43 2024        superseded      jenkins-5.0.15  2.440.1         Install complete
            2               Thu Feb 22 18:28:03 2024        superseded      jenkins-5.0.16  2.440.1         Upgrade complete
            3               Thu Feb 22 18:38:51 2024        deployed        jenkins-5.0.14  2.440.1         Upgrade complete
            ```

        - `helm` **`rollback`** `my-chart` `2`
        ####
        - `helm` **`history`** `my-chart `
            ```yaml
            REVISION        UPDATED                         STATUS          CHART           APP VERSION     DESCRIPTION     
            1               Thu Feb 22 18:10:43 2024        superseded      jenkins-5.0.15  2.440.1         Install complete
            2               Thu Feb 22 18:28:03 2024        superseded      jenkins-5.0.16  2.440.1         Upgrade complete
            3               Thu Feb 22 18:38:51 2024        superseded      jenkins-5.0.14  2.440.1         Upgrade complete
            4               Thu Feb 22 18:50:28 2024        deployed        jenkins-5.0.16  2.440.1         Rollback to 2   
            ```

        ####
        - `helm` **`uninstall`** `my-chart` `-n my-ns`
         - removes the release from the Kubernetes **cluster**, but it does not affect your local Helm cache or any local chart files you might have.
    





