

Kubelet is a linux service and as such is managed by [systemd](../../../../../os/linux/startup/service_man.md)

- 1). Interact - **systemctl**
    #####
    - `[sudo] systemctl` **`status`** `kubelet`    
    - `[sudo] systemctl` **`restart`** `kubelet`       

##
- 2). Configure - **`/usr/lib/systemd/system/`**

    ####
    -  **`kubelet.service`**

        ####
        - Unit file
            - **Configuration Base** (do not edit)
                - Specifies the **executable** (/usr/bin/kubelet), and other essential settings required to run the kubelet process.
                - Includes basic **directives** such as `ExecStart`, `Restart`, `After`, and `Wants`, which define when and how the kubelet service should start and under what conditions.
        

                ###
                - `cat /usr/lib/systemd/system/kubelet.service`
                    ```yaml
                    [Unit]
                    Description=kubelet: The Kubernetes Node Agent
                    Documentation=https://kubernetes.io/docs/
                    Wants=network-online.target
                    After=network-online.target

                    [Service]
                    ExecStart=/usr/bin/kubelet
                    Restart=always
                    StartLimitInterval=0
                    RestartSec=10

                    [Install]
                    WantedBy=multi-user.target
                    ```


    - **`kubelet.service.d/10-kubeadm.conf`**


        - `cat /usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf`
         - **Configuration Extension** (do edit)
            - additional environment variables or configuration parameters

                ```yaml
                # Note: This dropin only works with kubeadm and kubelet v1.11+
                [Service]
                Environment="KUBELET_KUBECONFIG_ARGS=--bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf"
                Environment="KUBELET_CONFIG_ARGS=--config=/var/lib/kubelet/config.yaml"
                # This is a file that "kubeadm init" and "kubeadm join" generates at runtime, populating the KUBELET_KUBEADM_ARGS variable dynamically
                EnvironmentFile=-/var/lib/kubelet/kubeadm-flags.env
                # This is a file that the user can use for overrides of the kubelet args as a last resort. Preferably, the user should use
                # the .NodeRegistration.KubeletExtraArgs object in the configuration files instead. KUBELET_EXTRA_ARGS should be sourced from this file.
                EnvironmentFile=-/etc/default/kubelet
                ExecStart=
                ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_KUBEADM_ARGS $KUBELET_EXTRA_ARGS
                ```
                - **`EnvironmentFile`**
                    - `/var/lib/kubelet/kubeadm-flags.env`
                        - set in extension above an aditional source of environment variables
