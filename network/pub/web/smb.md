### SMB and Samba

**SMB** is the protocol of choice on all platforms for file and printer sharing. 
On windows and mac smb support is built into the os
On linux  its implemented by **samba** which can be (un)installed separately from the os. 


#### Printer Sharing

The following need to be layered on top of TCP

- ##### Queue Management
    SMB manages multiple print jobs, queues them, and handles priorities. Without SMB, you'd need to create a custom queuing system.

- ##### Error Handling
    SMB handles job retries and errors (e.g., printer offline). TCP alone doesn't manage these retries or status updates.

- ##### Printer Status
    SMB has built-in ways to check if a printer is available (e.g., out of paper, offline). You’d need a custom solution over TCP to do this.

- ###### Printer search (discovery) 

- #####  Cross-Platform Compatibility
    SMB provides a standardized way to share printers between Windows, Linux, and macOS. TCP alone wouldn't ensure this interoperability.


#### File Sharing


The following need to be layered on top of TCP

- ##### File Access and Management
    SMB provides operations to open, read, write, and close files on a remote server. Without SMB, you'd need to implement your own methods to manage file access (like locking, reading, or writing to files) over TCP.

- ##### File Permissions and Security 
    SMB handles access control (who can read/write/execute files) through authentication and permissions. TCP alone doesn't provide a way to enforce these security rules for file access.

- ##### File Locking
    SMB allows for file locking to ensure that only one process can modify a file at a time, preventing data corruption. Without SMB, you would need to create a custom file locking mechanism on top of TCP.


- ##### Directory Traversal
    SMB provides operations to list the contents of directories (e.g., files and subdirectories). Without SMB, you would need to manually implement directory traversal logic and ensure it works across different filesystems over TCP.

- ##### Directory Permissions 
    SMB respects and enforces permissions on directories (e.g., who can list, read, or write to directories). TCP alone doesn't provide access control for listing directory contents.


- ##### Cross-Platform Compatibility
    SMB standardizes the way files are shared across different operating systems (Windows, Linux, macOS). Without it, you'd have to create custom protocols to ensure interoperability across these platforms.