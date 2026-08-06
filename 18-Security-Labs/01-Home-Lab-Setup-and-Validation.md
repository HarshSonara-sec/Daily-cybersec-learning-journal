# 01 - Home Lab Setup and Validation

**Difficulty:** ⭐☆☆☆☆ (Beginner)

**Prerequisites**
- Kali Linux installed
- VMware Workstation Pro installed
- Hardware virtualization (VT-x / AMD-V) enabled

**Estimated Reading Time:** 10–15 minutes

**Last Updated:** 2026-08-06

---

# 🎯 Objective

Build a secure and isolated penetration testing environment using VMware Workstation Pro and Metasploitable 2, verify connectivity, and perform the first reconnaissance and enumeration phase.

---

# 📚 Concepts

## What is a Home Lab?

A home lab is an isolated virtual environment used to safely practice cybersecurity techniques without affecting production systems or external networks.

Benefits include:

- Safe experimentation
- Repeatable practice
- Learning through failure
- Building practical skills
- Testing offensive and defensive techniques

---

## Why Virtual Machines?

Virtual machines allow multiple operating systems to run simultaneously on a single physical computer while remaining isolated from one another.

Advantages:

- Snapshots
- Easy recovery
- Network simulation
- No risk to the host operating system
- Low hardware cost

---

## Why VMware Workstation Pro?

VMware Workstation Pro provides:

- Stable virtualization
- Multiple virtual networks
- Snapshot support
- High compatibility
- Efficient resource management

---

## Lab Environment

### Host Machine

- Kali Linux
- VMware Workstation Pro

### Target Machine

- Metasploitable 2

---

# 🏗️ Lab Architecture

```
+------------------------+
|      Kali Linux        |
|  Attacker Machine      |
|  192.168.89.x          |
+-----------+------------+
            |
      Host-Only Network
            |
+-----------+------------+
|     Metasploitable 2   |
|  Vulnerable Target VM  |
|  192.168.89.x          |
+------------------------+
```

---

# 🛠️ Practical Implementation

## Step 1

Installed VMware Workstation Pro.

Verified:

- VMware launches successfully
- Kernel modules loaded correctly

---

## Step 2

Imported the Metasploitable 2 virtual machine.

---

## Step 3

Configured networking using a Host-Only adapter.

Purpose:

- Allow communication between attacker and target.
- Prevent accidental exposure to external networks.

---

## Step 4

Verified connectivity.

Confirmed:

- Target machine received an IP address.
- Kali Linux successfully reached the target.

---

## Step 5

Performed an initial reconnaissance using Nmap.

Objectives:

- Discover open ports.
- Identify running services.
- Detect software versions.

---

## Step 6

Performed basic enumeration.

Services investigated:

- FTP
- SMB
- HTTP

Enumeration included:

- Anonymous FTP login
- SMB share discovery
- Directory enumeration
- Web technology fingerprinting

---

# 🔍 Troubleshooting

## Slow Metasploitable Download

Several download mirrors were unavailable or extremely slow.

Resolution:

Obtained a working download source before importing the VM.

---

## VMware Verification

Verified:

- Hardware virtualization
- Matching Linux kernel headers
- Successful VMware startup

---

## FTP Behaviour

Anonymous login succeeded.

Directory navigation behaved differently than expected because of server permissions.

---

## SMB Permissions

Anonymous access allowed enumeration.

Access to some resources remained restricted.

This demonstrates that successful authentication does not always imply full authorization.

---

# ⚠️ Common Mistakes

- Using Bridged networking unnecessarily.
- Beginning exploitation before completing enumeration.
- Ignoring software version information.
- Failing to document discoveries.
- Not taking snapshots before experimentation.

---

# ✅ Best Practices

- Keep vulnerable machines isolated.
- Document every finding.
- Verify results using multiple tools.
- Understand why a service is interesting before attempting exploitation.
- Follow a structured penetration testing methodology.

---

# 💻 Commands Reference

```bash
nmap --privileged -sC -sV <target-ip>

ftp <target-ip>

smbclient -L //<target-ip> -N

smbclient //<target-ip>/tmp -N

gobuster dir \
-u http://<target-ip> \
-w /usr/share/wordlists/dirb/common.txt
```

---

# 📖 Lessons Learned

- A well-designed lab is the foundation for practical cybersecurity learning.
- Enumeration provides the information required to make informed decisions during testing.
- Multiple tools should be used to build a complete understanding of the target.

---

# 🎓 Interview Questions

### What is a home lab?

### Why is Host-Only networking recommended for vulnerable virtual machines?

### Why should enumeration always precede exploitation?

### What information can Nmap reveal during reconnaissance?

### What is the difference between authentication and authorization?

---

# 🔗 Related Notes

- Nmap Fundamentals
- Linux System Networking
- Enumeration Workflow Cheatsheet
- Future: Vulnerability Assessment
- Future: Exploitation

---

# 📝 Summary

A secure VMware-based penetration testing lab was successfully created using Kali Linux and Metasploitable 2. Network connectivity was verified, initial reconnaissance was completed, and enumeration identified multiple services for future vulnerability assessment and exploitation. This lab provides a repeatable environment for developing practical penetration testing and security engineering skills.
