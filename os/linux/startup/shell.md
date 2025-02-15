## Shell

[init](init_process.md) starts a _login process_ (pid > 1, uid/gid = 0)
if/when user logs on, the login process starts a new process  - the login shell 

#### Login Shell
The user's **login shell** gets uid/gid of this user. Every other shell, and thus every process the user starts (in any shell),  is a (direct or indirect) subprocess of their login shell. (see also [shell config](shell_config.md) and [startup](startup.md))