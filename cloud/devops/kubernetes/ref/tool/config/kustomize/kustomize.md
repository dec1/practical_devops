### Kustomize: Kubernetes Native Configuration Management

Kustomize is a tool for customizing Kubernetes YAML configurations without modifying the original files. It allows you to manage different environments (e.g., dev, staging, production) by overlaying configurations on a common base.

- 1). **Concept - Bases and Overlays**
    #####
    - **Base**: Common resources (YAML files) shared across environments.
    - **Overlay**: Environment-specific customizations applied on top of the base.

    ### Example Structure:
    ```bash
    ├── base
    │   ├── deployment.yaml
    │   └── service.yaml
    └── overlays
        ├── dev
        │   └── kustomization.yaml
        └── prod
            └── kustomization.yaml
    ```

    ### Example `kustomization.yaml` (Overlay):
    ```yaml
    resources:
      - ../../base
    patchesStrategicMerge:
      - deployment-patch.yaml
    ```

- 2). **Usage with `kubectl`**
    #####
    - Apply configuration:
        ```bash
        kubectl apply -k overlays/dev
        ```
    - Preview configuration:
        ```bash
        kubectl kustomize overlays/dev
        ```

- 3). **Comparison with Helm**
    #####
    - **Kustomize**:
        - Native to Kubernetes, no templating, purely declarative.
        - Simpler, focused on environment-specific overlays.
    - **Helm**:
        - Uses templates for dynamic configuration.
        - More powerful for complex deployments but requires learning Helm syntax.


---

#### vs Helm:
- **Helm** generates different versions of config (yaml files) by injecting values for **template** variables.
- **Kustomize** requires an **overriding** set of yaml files