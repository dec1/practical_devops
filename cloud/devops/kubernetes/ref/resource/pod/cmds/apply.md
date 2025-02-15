
## `apply`

- `k` **`apply`** `-f pod.yaml` 
    where

####
- `pod.yaml`
    ```yaml
    apiVersion: v1              # the version of the Kubernetes API we are using (possible values defined by Kubernetes)
                                # v1 aka core/v1  ~ Pod, Service, ConfigMap
                                # apps/v1         ~ Deployment, ReplicaSet, StatefulSet

    kind: Pod                   # "Resource"  kind of Object we are creating (Pod, Service, deployment etc)

                                # "Resource" is often used interchangeably with "primitive", though strictly speaking resource is somewhat more general.
                                # "Object" is the more specific term, and is used when referring to a specific instance of a resource.
                                #   -> any entity or object that you can manage or manipulate within kubernetes system

    metadata:
        name: my-pod            # can be used to refer to pod later
        labels:
            myLab:  "some-label-value"              # no spaces -can be used from search/selection (label selectors - service, kubectl -l)
        annotations:
            myAnno: "some long text with spaces"     # cant be used for search/selection

    spec:                           # State desired
        restartPolicy: Never    # pod-wide restartPolicy that applies to all containers
                                # Never, OnFailure, Always
        containers:                 # list of containers to run in this pod
        -   name: my-ctr
            image: nginx:latest
            env:                    # env vars
            - name: key-e
              value: val-e
            ports:
            - containerPort: 80     # ~ doc-only similar to EXPOSE (not "docker run -p 80:80") in Docker.
                                    # Except for its value when referenced from other parts of file (eg "named port" in Probes), 
                                    # where the value does matter, and could otherwise be hard coded there 
                                    # its just doc (non-op)
            
            #----------------------------------------
            # -- adding this overrides default init command of container (nginx serving without terminating) - ie pod completes ()
            # replaces ENTRYPOINT of dockerfile
            #command: ['sh', '-c', 'echo "Hello, Kubernetes!" && touch /my-vol-mnt/healthy' 
            #&& sleep 3600]        # postpone pod completionwit sleep

            #args:    ["arg1", "arg2", ...]                                          # replaces CMD of dockerfile

            #----------------------------------------
            livenessProbe:      # example probes
              exec:
                command:
                - ls
                - /my-vol-mnt/healthy
    
              initialDelaySeconds: 2
              periodSeconds: 3
            # -----
            readinessProbe: # declare the readiness probe
                httpGet: # add this line
                    path: / 
                    port: 80 
                initialDelaySeconds: 1
                periodSeconds: 1
            # --------------------------------------
            volumeMounts:
            - name: my-vol                      # mount shared vol
              mountPath: "/my-vol-mnt"
        
        # check: `k logs my-pod my-init-ctr`
        initContainers:
          - name: my-init-ctr
            image: busybox:1.28
            command: ['sh', '-c', "touch /my-vol-mnt/healthy &&  echo 'init container ran...'  "]
            volumeMounts:
            - name: my-vol                      # mount shared vol
              mountPath: "/my-vol-mnt"

        # --------------------------------------


        volumes:
        - name: my-vol
          emptyDir: {}                    # create a (shared) volume of type empty dir, which any container in pod can mount


    status: {}              # State actual/observed 
                                # {} -> object not yet created 
    ```                     
  