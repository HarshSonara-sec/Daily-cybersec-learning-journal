# Incident: Kali Linux Root Filesystem Mounted Read-Only After Unsafe Shutdown

**Date:** 2026-07-11
**System:** Kali GNU/Linux Rolling (dual-boot), NVMe SSD (`nvme0n1p6`)

## Symptoms
- Logged in fine, but shell threw errors on every write attempt:
  - `mkdir: cannot create directory '/home/harsh/.cache/oh-my-zsh': Read-only file system`
  - `rm: cannot remove '/home/harsh/.zcompdump-Harsh-5.9': Read-only file system`
  - `zsh: locking failed for /home/harsh/.zsh_history: read-only file system: reading anyway`
- Confirmed root was mounted `ro`:
  ```bash
  mount | grep " / "
  ```

## Root Cause Investigation
Checked kernel log for hardware/filesystem errors:
```bash
dmesg | grep -iE "error|ext4|read-only"
```
Found:
- `pcieport ...: DPC: error containment capabilities ... PoisonedTLP+` — PCIe Downstream Port Containment event
- `mce: [Hardware Error]: Machine check events logged` — CPU-level machine check exception
- `EXT4-fs (nvme0n1p6): orphan cleanup on readonly fs`
- `EXT4-fs (nvme0n1p6): mounted filesystem ... ro with ordered data mode`

**Interpretation:** the kernel detected a PCIe/hardware-level fault and defensively remounted the ext4 root read-only to avoid data corruption, rather than the disk itself failing.

## Diagnosis Steps
1. Since the fs was still readable, backed up critical data to the Windows (NTFS) partition on the same dual-boot disk instead of needing external media:
   ```bash
   lsblk -f                                    # identify NTFS partition
   sudo mkdir -p /mnt/winbackup
   sudo mount /dev/nvme0n1pX /mnt/winbackup     # replace pX with Windows partition
   sudo rsync -avh --progress /home/harsh/ /mnt/winbackup/kali-backup/
   ```
2. Rebooted the system — it came back up clean, mounted `rw`, **no data loss**.
3. Checked NVMe drive health to rule out a failing disk:
   ```bash
   sudo apt install smartmontools nvme-cli -y
   sudo smartctl -a /dev/nvme0
   sudo nvme smart-log /dev/nvme0
   ```

## Key SMART Findings
| Metric | Value | Verdict |
|---|---|---|
| Critical Warning | 0x00 | OK |
| Media and Data Integrity Errors | 0 | OK |
| SMART overall-health | PASSED | OK |
| Percentage Used | 3% | Healthy |
| Temperature | 34°C | Normal |
| Available Spare | 100% | Healthy |
| **Unsafe Shutdowns** | **19** | ⚠️ Elevated |

The high unsafe-shutdown count (relative to 966 power cycles) was the actual smoking gun — pointed to an unclean/forced power-off as the trigger for the ext4 journal issue and the PCIe/MCE noise in dmesg, not a failing drive.

## Resolution
- No hardware replacement needed — drive health confirmed good via SMART.
- Root cause: unclean shutdown corrupting the ext4 journal slightly, which the kernel flagged defensively (DPC + MCE were downstream noise from the same event, not a separate fault).
- Fixed itself on reboot once the journal/orphan-cleanup completed.

## Takeaways / Prevention
- Always shut down cleanly — avoid holding the power button or unplugging without a proper `shutdown`/`reboot`.
- If root ever remounts `ro`, check `dmesg` first before assuming disk failure — DPC/MCE lines can look scary but are often just kernel fault-containment, not permanent damage.
- `sudo nvme smart-log` and `sudo smartctl -a` are the fastest way to rule disk failure in/out.
- Dual-boot systems can double as a backup destination in a pinch — mount the other OS's partition instead of needing a USB drive.
- Consider periodic `rsync` backups of `~/` (especially Obsidian vault + HTB notes) as routine hygiene, not just incident response.

## Commands Reference
```bash
mount | grep " / "
dmesg | grep -iE "error|ext4|read-only"
lsblk -f
sudo mount -o remount,rw /
sudo rsync -avh --progress /home/harsh/ /mnt/winbackup/kali-backup/
sudo apt install smartmontools nvme-cli -y
sudo smartctl -a /dev/nvme0
sudo nvme smart-log /dev/nvme0
```
