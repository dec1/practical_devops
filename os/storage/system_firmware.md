## System Firmware
System Firmware on the motherboard initializes system _hardware_ including the cpu, memory and peripherals eg (PCI) network cards, and delegates to the Bootloader on the primary disk to locate and load the OS. (see also [overview ](overview.md) overview)


There are 2 main kinds of system firmware:

####
- #### 1)  Unified Extensible Firmware Interface (UEFI)
    A more modern system firmware. A UEFI system can boot from disks partitioned with either MBR (using a Compatibility Support Module (CSM), which emulates BIOS behavior) or GPT (in native UEFI mode). If a UEFI system wants to boot from a [GPT](disks_and_partitions.md) disk, it *must* be in native UEFI mode.

- #### 2) Basic Input/Output System (BIOS)
    An older system firmware. When a computer has a BIOS firmware, the system firmware can only initiate the boot process from a disk that has been partitioned using the Master Boot Record (MBR) [scheme](disks_and_partitions.md).



#####
A computer will have *either* a BIOS (legacy) *or* a UEFI (modern) firmware, but not both.