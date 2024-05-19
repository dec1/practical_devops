### sudo (avoid)
Most docker commands need to be run as sudo. Avoid via:   
```
sudo usermod -g docker declan
```
_adds_ **user** "declan" to **_docker_ group** (in host linux, and *log in* again)


### Docker Engine (Daemon/Server) 
- systemd (eg ubuntu) service
`sudo systemctl     start|stop|restart|status|enable|disable docker`

### storage
host dir which holds images, containers, and container configuration
`/var/lib/docker`