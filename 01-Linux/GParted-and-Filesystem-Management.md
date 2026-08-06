# GParted and Linux Filesystem Management

> **Difficulty:** Intermediate  
> **Category:** Linux Administration / Storage Management

---

# Objective

Understand how Linux partitions, filesystems, and GParted work, and learn how to safely resize, move, and manage partitions in both single-boot and dual-boot environments.

---

# What is GParted?

**GParted (GNOME Partition Editor)** is a graphical partition management tool used to:

- Create partitions
- Delete partitions
- Resize partitions
- Move partitions
- Format partitions
- Check filesystems
- Manage partition flags

It is one of the safest and most widely used partition editors in Linux.

---

# What is a Partition?

A partition is a logical section of a physical storage device.

Instead of treating an entire disk as one large space, it is divided into multiple independent regions.

Example:

```text
512 GB SSD

├── Windows
├── Linux
├── Recovery
└── EFI
```

Each partition behaves like its own storage device.

---

# Why Partition a Disk?

Partitioning provides:

- Better organization
- Multiple operating systems
- Easier recovery
- Different filesystems
- Separate system and user data

---

# GPT vs MBR

## GPT (GUID Partition Table)

Modern partition table format.

Advantages:

- Supports disks larger than 2 TB
- Up to 128 partitions by default
- Better redundancy
- Required for UEFI systems

Used on most modern computers.

---

## MBR (Master Boot Record)

Older partition table.

Limitations:

- Maximum disk size of 2 TB
- Maximum of four primary partitions
- Less fault tolerant

Mostly found on legacy BIOS systems.

---

# BIOS vs UEFI

## BIOS

Legacy firmware.

Characteristics:

- Older systems
- Uses MBR
- Slower boot process

---

## UEFI

Modern firmware replacing BIOS.

Advantages:

- Faster boot
- GPT support
- Secure Boot
- Better hardware compatibility
- Improved recovery features

Modern Windows installations use UEFI.

---

# EFI System Partition (ESP)

The EFI System Partition stores bootloaders for installed operating systems.

Typical size:

- 100 MB–1 GB

Filesystem:

```
FAT32
```

Examples:

Windows EFI

```text
EFI/
 └── Microsoft/
```

Linux EFI

```text
EFI/
 └── kali/
```

Deleting or formatting the EFI partition may make the operating system unbootable.

---

# Linux Root Partition (/)

The root partition contains:

- Linux kernel
- Installed applications
- Libraries
- Configuration files
- System services

Everything except mounted filesystems begins here.

Example:

```text
/
├── bin
├── etc
├── home
├── usr
├── var
└── boot
```

---

# Home Partition (/home)

Some Linux installations separate user data into its own partition.

Advantages:

- Easier OS reinstalls
- User files remain intact
- Better organization

Our setup stores `/home` inside the root partition.

---

# Swap Partition

Swap is disk space used when RAM becomes full.

Purposes:

- Memory overflow
- Hibernation (if configured)

Example:

```
2 GB Swap
```

Commands:

```bash
swapon --show
free -h
```

---

# Common Linux Filesystems

## ext4

Most commonly used Linux filesystem.

Features:

- Journaling
- Stable
- Fast
- Reliable
- Excellent compatibility

Used by Kali Linux.

---

## Btrfs

Modern filesystem supporting:

- Snapshots
- Compression
- Checksums
- Subvolumes

Often paired with Timeshift.

---

## XFS

Designed for:

- Large files
- Enterprise servers
- High performance

Common on Red Hat systems.

---

## FAT32

Typically used for:

- EFI System Partition
- USB drives

Advantages:

- Universal compatibility

Limitation:

Maximum file size:

```
4 GB
```

---

## NTFS

Windows default filesystem.

Supports:

- Large files
- Permissions
- Journaling
- Compression

---

# Mounted vs Unmounted Partitions

A mounted partition is currently in use.

Example:

```bash
mount
```

Mounted partitions appear in the filesystem.

---

Why can't we resize a mounted root partition?

Because:

- Files are actively changing.
- Kernel processes are using it.
- Filesystem metadata is locked.

Always use a Live environment when resizing the root partition.

---

# Live USB

A Live USB boots Linux directly into RAM.

Advantages:

- Installed system remains untouched
- Root partition is unmounted
- Safe partition management
- Useful for system recovery

Common uses:

- Disk repair
- Password reset
- Partition resizing
- Data recovery

---

# Resizing vs Moving a Partition

## Resize

Changes partition size.

Can:

- Increase size
- Decrease size

---

## Move

Changes the partition's physical location.

Data remains intact, but every block is relocated.

Moving partitions generally takes longer than resizing.

---

# Unallocated Space

Unallocated space is disk space that belongs to no partition.

Example:

```text
Windows

↓

Unallocated

↓

Linux
```

Linux can only be expanded into **adjacent** unallocated space.

---

# Why Adjacent Space Matters

Example:

```
Windows

↓

Free Space

↓

Linux
```

Expansion works.

---

Example:

```
Windows

↓

EFI

↓

Free Space

↓

Linux
```

Expansion does **not** work until the EFI partition is moved.

---

# Partition Alignment

Modern SSDs perform best when partitions are properly aligned.

Benefits:

- Better performance
- Reduced write amplification
- Longer SSD lifespan

GParted automatically aligns partitions.

---

# Filesystem Check

Before resizing, verify filesystem integrity.

Examples:

```bash
sudo e2fsck -f /dev/sdXN
```

or

```bash
sudo ntfsfix /dev/sdXN
```

Never resize a corrupted filesystem.

---

# Understanding GParted Warnings

## "Moving a partition might cause your operating system to fail to boot."

Meaning:

Boot files may require updates if the partition's location changes.

It does **not** necessarily indicate an error.

---

## "Editing partitions has the potential to cause data loss."

Meaning:

Power loss, hardware failure, or user interruption during partition operations can corrupt data.

Always ensure:

- Stable power
- Healthy disk
- Verified backups (when available)

---

# Best Practices

- Check filesystem health before partitioning.
- Use a Live USB for root filesystem changes.
- Read every GParted warning carefully.
- Review pending operations before applying.
- Keep the laptop connected to AC power.
- Verify both operating systems after changes.
- Create a Timeshift snapshot after successful partition modifications.

---

# Common Mistakes

❌ Resizing mounted partitions.

❌ Deleting EFI partitions.

❌ Interrupting GParted.

❌ Using the wrong disk.

❌ Forgetting to verify Windows after resizing.

❌ Assuming unallocated space can always be used without checking adjacency.

---

# Interview Questions

### What is the difference between GPT and MBR?

GPT is the modern partition table format supporting larger disks, more partitions, redundancy, and UEFI booting. MBR is the legacy format limited to 2 TB disks and four primary partitions.

---

### Why can't a mounted partition be resized?

Because the operating system is actively using the filesystem, making changes unsafe and risking corruption.

---

### What is the purpose of the EFI System Partition?

It stores bootloaders and firmware boot files required by UEFI systems to start operating systems.

---

### Why is a Live USB recommended for partition management?

It keeps the installed operating system's partitions unmounted, allowing safe resizing, moving, repairing, and recovery operations.

---

# Summary

Understanding partition layouts, filesystems, boot modes, and GParted is an essential Linux administration skill. Safe partition management requires planning, health checks, a Live environment, and careful verification after every change.
