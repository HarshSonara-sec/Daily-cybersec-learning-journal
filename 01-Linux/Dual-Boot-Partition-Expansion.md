# Safely Expanding a Kali Linux Partition in a Dual-Boot Environment (Windows 11 + Kali Linux)

> **Difficulty:** Intermediate  
> **Category:** Linux Administration / Storage Management / System Recovery  
> **Environment:** Windows 11 + Kali Linux Dual Boot (UEFI + GPT)

---

# Objective

Increase the Kali Linux root partition from **37.4 GB** to approximately **118 GB** without:

- Losing Windows data
- Losing Kali data
- Reinstalling either operating system
- Breaking the GRUB bootloader

---

# Why This Was Necessary

Initially, Kali Linux was installed with only **37.4 GB** of storage.

Although this is enough for basic usage, it quickly becomes insufficient for cybersecurity work involving:

- VMware Workstation
- Metasploitable 2
- Multiple Linux VMs
- Windows virtual machines
- Burp Suite
- Docker
- Wordlists (SecLists, RockYou, etc.)
- Wireshark packet captures
- HTB machines
- Metasploit Framework
- Large software updates

A larger root partition provides enough room for future labs while keeping Windows intact.

---

# Initial System Information

## Hardware

- Lenovo IdeaPad Gaming 3 15IHU6
- 512 GB NVMe SSD

---

## Operating Systems

- Windows 11
- Kali Linux 2026.x

---

## Boot Mode

- UEFI

---

## Partition Table

- GPT (GUID Partition Table)

---

# Initial Partition Layout

| Partition | Size | Filesystem | Purpose |
|-----------|------:|-----------|---------|
| nvme0n1p1 | 260 MB | FAT32 | Windows EFI |
| nvme0n1p2 | 16 MB | MSR | Microsoft Reserved |
| nvme0n1p3 | 434.2 GB | NTFS | Windows C: |
| nvme0n1p5 | 977 MB | FAT32 | Kali EFI |
| nvme0n1p6 | 37.4 GB | ext4 | Kali Root (/) |
| nvme0n1p7 | 2.1 GB | swap | Linux Swap |
| nvme0n1p4 | 2 GB | NTFS | Windows Recovery |

---

# Understanding the Partition Layout

The physical disk layout before resizing looked like:

```text
[Windows EFI]
        ↓
[Microsoft Reserved]
        ↓
[Windows (C:)]
        ↓
[Kali EFI]
        ↓
[Kali Root]
        ↓
[Linux Swap]
        ↓
[Windows Recovery]
```

The free space needed for Kali had to be created by shrinking the Windows partition.

---

# Why the Installed Kali System Cannot Resize Itself

The Kali root filesystem (`/`) is mounted while the operating system is running.

A mounted filesystem cannot safely be moved or resized because:

- Active files are in use.
- Filesystem metadata is constantly changing.
- Resizing could corrupt the filesystem.

**Solution:** Boot into **Kali Live** so the installed root partition remains unmounted.

---

# Health Checks Before Partitioning

Before modifying partitions, verify both operating systems are healthy.

## Windows

```cmd
chkdsk
```

Purpose:
- Check filesystem consistency.

---

```cmd
sfc /scannow
```

Purpose:
- Verify Windows system files.

---

```cmd
DISM /Online /Cleanup-Image /CheckHealth
```

Purpose:
- Check Windows component store.

---

```cmd
DISM /Online /Cleanup-Image /ScanHealth
```

Purpose:
- Detect deeper corruption.

---

## Linux

Check mounted filesystems:

```bash
lsblk -f
```

---

View partition table:

```bash
sudo fdisk -l
```

---

Check filesystem usage:

```bash
df -h
```

---

Check free space between partitions:

```bash
sudo parted /dev/nvme0n1 print free
```

---

# Problem Encountered

Windows repeatedly froze while downloading the Kali Live ISO.

Symptoms:

- Mouse frozen
- Keyboard frozen
- Task Manager unresponsive
- Download restarted repeatedly

Root cause was never conclusively identified, but system integrity checks showed no corruption.

Workaround:
- Download the ISO from Kali instead of Windows.

---

# Common Mistake

Initially downloaded:

❌ Kali Installer ISO

The installer ISO is used to install Kali and does **not** provide the live environment required for partition management.

Correct choice:

✅ Kali Live ISO

---

# Creating the Bootable USB

Verify the USB device:

```bash
lsblk
```

Write the ISO:

```bash
sudo dd if=/path/to/kali-linux-live.iso of=/dev/sdX bs=4M status=progress conv=fsync
```

Flush pending writes:

```bash
sync
```

---

# Partitioning Strategy

The safest sequence was:

1. Shrink Windows.
2. Move the Kali EFI partition.
3. Verify Windows boots.
4. Boot Kali Live again.
5. Expand the Kali root partition.
6. Verify both operating systems.

---

# Partition Changes Performed

## Step 1 — Shrink Windows

Windows partition:

```
434.2 GB
```

↓

```
352.2 GB
```

Result:

Approximately **82 GB** unallocated.

---

## Step 2 — Move Kali EFI

The Kali EFI partition was moved left to make the unallocated space contiguous with the Linux root partition.

---

## Step 3 — Verify Windows

Before resizing Linux:

- Windows booted successfully.
- Files were verified.
- GRUB remained functional.

---

## Step 4 — Expand Kali

The root partition (`/dev/nvme0n1p6`) was expanded into the newly created unallocated space.

Final size:

```
118 GB
```

---

# Verification

Check the mounted filesystem:

```bash
df -h /
```

Example output:

```text
Filesystem      Size  Used  Avail  Use%
/dev/nvme0n1p6 118G   28G   84G    25%
```

---

View partitions:

```bash
lsblk -f
```

---

Inspect the partition table:

```bash
sudo fdisk -l
```

---

# Final Partition Layout

| Partition | Size | Purpose |
|-----------|------:|---------|
| Windows EFI | 260 MB | Boot |
| MSR | 16 MB | Microsoft Reserved |
| Windows | 352 GB | Windows 11 |
| Kali EFI | 977 MB | Linux Boot |
| Kali Root | 118 GB | Linux |
| Swap | 2.1 GB | Swap |
| Windows Recovery | 2 GB | Recovery |

---

# Timeshift Snapshot

Immediately after resizing:

- Installed/Opened Timeshift
- Selected RSYNC mode
- Stored snapshots on the root partition
- Created a baseline snapshot

Suggested retention:

- Boot: 1
- Daily: 1
- Weekly: 2
- Monthly: 1

Purpose:

Provides a known-good restore point before future system changes.

---

# Common Mistakes to Avoid

❌ Resizing a mounted root filesystem.

❌ Using the Installer ISO instead of the Live ISO.

❌ Interrupting GParted while operations are running.

❌ Partitioning without checking disk health.

❌ Forgetting to verify Windows before continuing.

❌ Running out of battery during partition operations.

---

# Best Practices

- Always use a Live environment for resizing Linux partitions.
- Keep the laptop connected to AC power.
- Verify Windows health before shrinking NTFS partitions.
- Review all pending operations before clicking **Apply**.
- Create a Timeshift snapshot after successful changes.
- Test both operating systems before considering the task complete.

---

# Lessons Learned

- Live environments are essential for modifying mounted Linux partitions.
- Verifying system health before partitioning significantly reduces risk.
- Incremental validation (checking Windows before expanding Linux) is safer than making all changes at once.
- Good planning is more important than rushing through partition operations.
- A recovery snapshot should be created immediately after major system changes.

---

# Interview Questions

### Why can't you resize the root partition while Kali is running?

Because the root filesystem is mounted and actively in use. Resizing a mounted root partition risks filesystem corruption. A Live environment ensures the partition remains unmounted.

---

### Why is the Kali Live ISO preferred over the Installer ISO for partition management?

The Live ISO boots a temporary operating system into RAM, allowing the installed Linux partitions to remain unmounted and safe to modify.

---

### Why verify Windows before resizing Linux?

Shrinking the Windows partition modifies NTFS metadata. Confirming Windows boots successfully isolates any potential issues before performing additional partition changes.

---

# Summary

Successfully expanded the Kali Linux root partition from **37.4 GB** to **118 GB** without data loss, while preserving a fully functional dual-boot Windows 11 and Kali Linux system. The process included comprehensive health checks, safe partition management using Kali Live and GParted, post-operation verification, and creation of a Timeshift recovery snapshot to protect the newly configured system.
