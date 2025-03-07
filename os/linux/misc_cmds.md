
#### Os Info
- `cat` **`/etc/os-release`**
    ```bash
    PRETTY_NAME="Ubuntu 24.04.1 LTS"
    NAME="Ubuntu"
    VERSION_ID="24.04"
    VERSION="24.04.1 LTS (Noble Numbat)"
    VERSION_CODENAME=noble
    ID=ubuntu
    ID_LIKE=debian
    HOME_URL="https://www.ubuntu.com/"
    SUPPORT_URL="https://help.ubuntu.com/"
    BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
    PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
    UBUNTU_CODENAME=noble
    LOGO=ubuntu-logo
    ```

#### Size


calculate space used by "path_to_dir"
- **`du`** `-hs` `<path_to_dir>`
    - `h` - human readable (uses kilobytes, megabytes etc)
    - `s` - summarize (otherwise prints val for each sub item)
    

    
####  Symbolic Link
- **`ln`** `-s` <target_file> <source_file>


#### Show ip address
- `ip addr` `show`


---

#### Kill Process (GUI)
- `Alt` + `F2` -> `Run Command`
    - KSysGuard (System Monitor)



#### Open Kde App (eg dolphin) in superuser  mode
- `kdesu dolphin` 




#### Copy output to file (*and* console)

- [redirect](in_out_std_streams.md) all output of <my_cmd> to console and file
`<my_cmd> 2>&1 | tee -a >my_file>`





#### Mount

- mount the (4 TB) sata had disk for everybody, by adding the following line to:
**`/etc/fstab`** 
    ```yaml
    /dev/sdb1 /media/4tb    ext4     auto,exec,rw        0       0
    ...
    ```





#### Dependencies
Find dependencies of binary (locally runnable)
- `ldd <my_executable>`
    - MacOS:
        `otool -L c<my_executable>`   

- Finding the dependencies of ([cross compiled](http://stackoverflow.com/questions/1172649/how-to-know-which-dynamic-libraries-are-needed-by-an-el)) binary
    - `readelf -d libboost_chrono.so | grep 'NEEDED'` 

- read all elf info (eg version info) from a lib
    - `readelf -a libz.so`
        note: needs package _binutils_ installed on opensuse




