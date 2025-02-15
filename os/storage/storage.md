### Storage 

After the os [loads](system_boot_and_os_bootloader.md), it makes [disk](disks_and_partitions.md) space available to processes running in the os as [volumes](volumes.md)


<figure>
  <img
  src="img/system_boot.png "
  <figcaption><h6 align="center">Motherboard and Drive  (Disk,  Bootloader and Operating System)</figcaption>
</figure>



### System Startup

The [system firmware](system_firmware.md) on the motherboard  

- initializes system _hardware_   
    - including cpu, memory and peripherals eg (PCI) network cards, and delegates to the

- ##### OS Bootloader
    The system firmware uses the controller on the startup drive to find and execute the os _bootloader_, whose sole job it is to _find and load the os_
    - The bootloader can load an os from (a partition on) the same or a different (connected) disk 
    - The details of the bootloader and how it locates and loads the os depend on the [partitioning scheme](disks_and_partitions.md) used on the disk


### System Running

After the os loads, the system firmware  is no longer in control. Modern versions eg [UEFI](system_firmware.md) often however provide some services to the OS (eg accurtate system time) that it can but need not use. 

- ##### Volumes
    The OS can access data on [partitions](disks_and_partitions.md) of any (connected) disk independently (of system firmware) using the disk controller directly. It makes this data available to processes running in the OS as [volumes](volumes.md)

###
_MS Windows incorrectly refers (eg in windows explorer)  to _volumes_ as [drives](./system_boot_and_os_bootloader.md)_


        



