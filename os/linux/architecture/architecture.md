- ### Kernel (Space):

    - The Linux Kernel provides an API (in c libraries) that is the only means of interacting with it (and through it) the hardware.
aka "system calls"

- #### Process and User Space

    - Every process (including the shell) not part of the kernel runs in "user space".
    Strictly speaking, no "process" runs in kernel space (since since its the kernel that makes processes possible).
    All processes are given  a standard in, out, err (which are file descriptors).

- #### Shell

    - The Linux [shell](../startup/shell.md) is just a user space process like any other. Its command-line interface  provides a way for users to interact (indirectly) with the kernel api. 
    Any other user compiled program can do the same by making system calls (through c libraries).


- #### File Descriptor

    - **_Everything is a File_**
    Everything that can be read from or written to (via system calls) is considered a (generalization of an open) file. eg
        - files
        - pipes
        - devices
        -  sockets, etc.

        Each one with a unique (integer) _file descriptor_  that is used to reference it.


            

