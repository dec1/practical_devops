## Configuration Management

Helm and Kustomize are tools designed to manage Kubernetes configurations, but they approach the task differently.

Helm generates different versions of config (yaml files) by injecting values for template variables.
whereas kustomize requires an overriding set of base yaml files.

Example:
- Deploying Nginx with Different Image Versions for Dev and Prod environments  using:
    - [Helm](helm/example/example.md)
    - [Kustomize](kustomize/example/example.md) 


--- 
###
- **Helm**
    - **Templating**: Helm uses a templating system to generate Kubernetes manifests. It allows for dynamic configuration by injecting values into templates.
    - **Charts**: Helm packages configuration as "charts," which are collections of templates and values files. These charts can be reused across different environments.
    - **Release Management**: Helm manages deployments as "releases," enabling versioned and rollback-capable deployments.

    - **Example**: Install a chart with environment-specific values:
        - `helm install` **`my-release`** `my-chart -f` **`values.yaml`**
        
###
- **Kustomize**
    - **Overlay System**: Kustomize uses a declarative approach with overlays to modify base configurations. No templating is involved, making it simpler but less dynamic.
    - **Bases and Overlays**: Kustomize organizes configurations into "bases" (common resources) and "overlays" (environment-specific customizations).
    - **No Release Management**: Kustomize doesn't track deployments as releases, and there’s no built-in versioning or rollback.

    - **Example**: Apply an overlay for a specific environment:
        - `kubectl apply -k` **`overlays/dev`**

####
- **Key Differences**
    - **Dynamic Configuration**: Helm’s templating allows for more dynamic, flexible configurations, while Kustomize focuses on straightforward, static customizations.
    - **Release Tracking**: Helm offers built-in release management, making it suitable for more complex deployment scenarios. Kustomize doesn’t track deployments.
    - **Complexity**: Helm is more powerful but requires learning its templating syntax. Kustomize is easier to use for simpler, environment-specific modifications without the need for templating.
