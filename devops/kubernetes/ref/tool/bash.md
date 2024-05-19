### bash setup

- **~/.bashrc**
    ```bash
    alias k=kubectl
    alias ka="kubectl apply -f"
    alias kd="kubectl --dry-run=client -o yaml"

    export do="--dry-run=client -o yaml"    # k create deploy nginx --image=nginx $do
    export now="--force --grace-period 0"   # k delete pod now   
    ```

- `source ~/.bashrc` 






