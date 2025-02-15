

Deploying Nginx with Different Image Versions for **Dev** and **Prod** Environments


```yaml
nginx-kustomize/
├── base/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── kustomization.yaml
└── overlays/
    ├── dev/
    │   ├── deployment-patch.yaml
    │   └── kustomization.yaml
    └── prod/
        ├── deployment-patch.yaml
        └── kustomization.yaml
```

- install (only one) of dev **or** prod
    - Kustomize isnt good at deployment multiple versions of same app 
    - `k apply -k` **`overlays/dev | overlays/prod`**

