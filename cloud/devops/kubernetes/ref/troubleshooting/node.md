# Troubleshooting Kubernetes Nodes

This document provides a comprehensive guide to troubleshooting Kubernetes nodes, including essential commands and a structured approach.

Before _Run on Node_: `ssh <node-name>`
## 1. Gathering Information

*   **Describe Node (Run on Client):**
    ```bash
    kubectl describe node <node-name>
    ```
    (Replace `<node-name>` with the actual name of the node.) This is your *most important* starting point.  Pay close attention to Conditions, Events, and Allocated Resources.

*   **Check Kubelet Status (Run on Node):**
    ```bash
    systemctl status kubelet
    ```
    This will show the current status of the kubelet service, including whether it's running, any recent errors, and the process ID.

*   **Get Kubelet Logs (Run on Node - systemd):**
    ```bash
    journalctl -u kubelet
    # `-u kubelet`  tells journalctl to display only the logs associated with the "kubelet" unit.

    # For more recent logs:
    journalctl -u kubelet -r -n 50  # Shows the last 50 lines in reverse order
    # To follow the logs in real-time:
    journalctl -u kubelet -f
    ```

*   **Get Kubelet Logs (Run on Node - older systems/different distributions):**
    ```bash
    # Check common log locations:
    ls /var/log/kubelet*
    cat /var/log/kubelet.log  # Or the appropriate log file name
    tail -f /var/log/kubelet.log # To follow log in real time
    ```

*   **Check System Logs (Run on Node - systemd):**
    ```bash
    journalctl -u systemd  # General system logs
    journalctl -u <service-name> # Logs for a specific service (e.g., docker, containerd)
    ```

*   **Check System Logs (Run on Node - older systems):**
    ```bash
    cat /var/log/syslog
    cat /var/log/messages
    dmesg  # Kernel messages
    ```

*   **Inspect Running Processes (Run on Node):**
    ```bash
    top      # Interactive process viewer
    htop     # Improved interactive process viewer (if installed)
    ps aux   # List all running processes
    ps -ef | grep <process-name> #Find specific processes
    ```

*   **Network Connectivity (Run on Client or Node):**
    ```bash
    ping <node-ip-or-hostname>  # Test basic connectivity
    traceroute <node-ip-or-hostname> # Trace the network route
    telnet <node-ip> <port>  # Test connectivity to a specific port (e.g., 10250 for kubelet API)
    curl -k https://<node-ip>:10250/healthz #Check the kubelet healthz endpoint (ignores certificate issues)
    nslookup <hostname> # Check DNS resolution
    ```
    (Network connectivity tests can often be run from either the client or the node itself, depending on what you're testing.)

*   **Disk Usage (Run on Node):**
    ```bash
    df -h    # Show disk space usage
    du -sh * # Show directory space usage in current directory
    ```

*   **Memory Usage (Run on Node):**
    ```bash
    free -h  # Show memory usage
    vmstat   # Virtual memory statistics
    ```

## 2. Identifying the Problem

Common problems and their potential causes:

*   **Node Not Ready:** Kubelet issues, network problems, resource exhaustion, OS issues.
*   **Disk Pressure:** Disk is almost full.
*   **Memory Pressure:** Low memory.
*   **PID Pressure:** Too many processes.
*   **Network Unavailable:** Network interface problems.
*   **Container Runtime Issues:** Problems with Docker, containerd, CRI-O.
*   **Hardware Problems:** Failing disks, RAM, etc.

## 3. Taking Corrective Action

*   **Restart Kubelet (Run on Node - systemd):**
    ```bash
    systemctl restart kubelet
    ```

*   **Reboot Node (Run on Node):**
    ```bash
    sudo reboot
    ```

*   **Drain Node (Run on Client):**
    ```bash
    kubectl drain <node-name> --delete-emptydir-data --ignore-daemonsets --force --grace-period=<seconds>
    ```
    (The `--force` option is sometimes necessary. Use with caution!)

*   **Uncordon Node (Run on Client):**
    ```bash
    kubectl uncordon <node-name>
    ```

*   **List Pods on a Node (Run on Client):**
    ```bash
    kubectl get pods -o wide --field-selector spec.nodeName=<node-name>
    ```

*   **Describe a Pod (Run on Client):**
    ```bash
    kubectl describe pod <pod-name> -n <namespace>
    ```

## 4. Prevention and Best Practices

*   **Monitoring:** Implement robust monitoring (Prometheus, Grafana).
*   **Resource Limits and Requests:** Set appropriate limits and requests for pods.
*   **Regular Maintenance:** Perform regular updates and patching.
*   **Node Pools/Machine Sets:** Use node pools for easier management.
*   **Taints and Tolerations:** Control which pods run on specific nodes.

## Example: Troubleshooting "Node Not Ready"

1.  `kubectl describe node <node-name>` (Run on Client): Check Conditions.
2.  `systemctl status kubelet` (Run on Node): Check kubelet status.
3.  `journalctl -u kubelet` (Run on Node): Examine kubelet logs.
4.  `ping <node-ip>` (Run on Client or Node): Test network connectivity.
5.  If the kubelet is crashing, try restarting it: `systemctl restart kubelet`
6.  If resource exhaustion is the cause (`top`, `htop`, `ps aux`), identify and kill resource-intensive processes.

Remember to replace placeholders like `<node-name>`, `<pod-name>`, and `<namespace>` with your actual values. Adapt commands like `journalctl` and log file locations based on your specific Linux distribution.