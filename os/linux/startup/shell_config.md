#### Shell Configuration:
The [login process](init_process.md)  decides which program to execute as the login shell from last field in user's `/etc/passwd` entry

- ##### Bash initialization order
    - If this is  bash, it reads `/etc/profile` (which typically sources all files found in `/etc/profile.d/`), and also
        (in order,  first found _wins_)             
        - `~/.bash_profile`
        - `~/.bash_login`
        - `~/.profile`


        - the user can subsequently start new (non-login) shells, from their log-in shell. These are configured in `~/.bashrc`
    Some things (such as exported _env vars_) are inherited from login shell, but some (eg _alias_ definitions) not. To be sure everything you need is configured in all shells its generally advised to:

- ##### Recommended Configuration
    - Put all shell config in non-login shell config:
        - `~/.bashrc`  
            ```bash
            # user's custom startup commands
            alias kd="kubectl --dry-run=client -o yaml"
            ```

    ###
    - Source non-login shell config from login-shell config:
        - `~/.bash_profile`  or `/etc/profile`
            ```bash
            # source .bashrc (if it exists)
            if [ -f ~/.bashrc ]; then
                source ~/.bashrc  
            fi      
            ```