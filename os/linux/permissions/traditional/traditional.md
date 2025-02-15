### Traditional File Access (`Permission Bits`)


When a process tries to perform an action (read, write or execute) on  a file or directory,  traditional permission checking is performed as follows (see also [permission bits](permission_bits.md)):

- 1). _which **triad**_ to use - ie who _who should process be interpreted as_ 

    - first wins:
        -  **owner**  - uid of file equals that of process
        -  **group** -  gid of file equals that of _any_ (primary or supplementary) of group of  process 
        -  **other** 

#####
- 2). **use** this triad's **permission bit** for the process action (read, write, execute) in question 


In moderm linux system this permission checking is part of a more elaborate checking - see [permission_checks](../permission_checks.md)


