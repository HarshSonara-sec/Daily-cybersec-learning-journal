# Lessons Learned

## July 10, 2026

### Linux & Git

* SSH authentication problems are often caused by using the wrong key or incorrect repository configuration.
* Configure Git (`user.name` and `user.email`) before making commits.
* Work as a regular user instead of `root`; use `sudo` only when necessary.
* Verify changes with `git status` before committing.
* Use meaningful commit messages that describe what changed.

### Linux Administration

* Read the complete error message before troubleshooting.
* Unexpected shutdowns can corrupt the filesystem journal even when the SSD is healthy.
* Always shut down the system properly and avoid forcing power-offs.

### Networking

* Networking fundamentals are the foundation of cybersecurity.
* Understanding IP addressing, DNS, ARP, TCP, and UDP is essential before advanced topics.

### Hack The Box

* Focus on understanding the vulnerability rather than memorizing an exploit.
* Document concepts learned instead of publishing challenge solutions or flags.
* Troubleshooting is part of the learning process, not a distraction.

### General

* Small, consistent study sessions are more valuable than cramming.
* Writing concepts in my own words improves long-term retention.
* Good documentation becomes a personal reference library over time.

---------------------------------------------------------------------------------------

# Linux Troubleshooting – Unsafe Shutdown Investigation

**Date:** July 11, 2026

## Incident

While investigating filesystem and system log warnings, I reviewed the NVMe SSD SMART data to determine whether the issue was caused by failing hardware or an improper shutdown.

## Findings

* SMART overall health: **PASSED**
* Media & Data Integrity Errors: **0**
* Percentage Used: **3%**
* Temperature: **34°C**
* Available Spare: **100%**
* Unsafe Shutdown Count: **19**

The SSD was healthy, indicating that the previous filesystem issues were most likely caused by an unclean shutdown rather than hardware failure.

## Commands Used

```bash
sudo smartctl -a /dev/nvme0n1

dmesg

journalctl -b

sudo poweroff

sudo shutdown -h now
```

## Lessons Learned

* Always read the complete error message before troubleshooting.
* An ext4 journal recovery does **not** necessarily indicate a failing SSD.
* Check SMART data before assuming hardware failure.
* A high unsafe shutdown count usually indicates unexpected power loss rather than SSD damage.
* Always shut down the system properly and avoid forcing power-offs.

## Prevention

* Shut down the system using the operating system instead of holding the power button.
* Wait until the laptop has completely powered off before closing the lid.
* Avoid interrupting package installations or filesystem operations.
* Keep regular backups of important data.

## Key Takeaway

A filesystem error should not immediately be treated as a hardware problem. Verify disk health with SMART data first, then investigate logs and recent shutdown history before drawing conclusions.
