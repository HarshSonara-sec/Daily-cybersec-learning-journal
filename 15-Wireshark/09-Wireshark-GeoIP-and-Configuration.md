# Wireshark GeoIP & Configuration

> **Category:** Network Analysis
>
> **Difficulty:** Beginner
>
> **Prerequisites:**
>
> - Wireshark Fundamentals
> - Basic Linux Knowledge
>
> **Recommended Before:**
>
> - 01-Wireshark-Fundamentals.md
> - 08-Wireshark-Statistics-and-Tools.md
>
> **Recommended After:**
>
> - 10-Wireshark-Troubleshooting.md

---

# Introduction

Before using Wireshark professionally, it is important to configure it correctly.

Proper configuration improves:

- Productivity
- Packet visibility
- Analysis speed
- Organization
- Troubleshooting efficiency

This guide covers the most useful configuration options for everyday packet analysis.

---

# Configuration Overview

Most settings are located under:

```
Edit
    ↓
Preferences
```

Configuration categories include:

- Appearance
- Layout
- Name Resolution
- Capture
- Protocols
- Profiles
- Columns
- GeoIP

---

# Configuration Profiles

Profiles allow you to save different Wireshark configurations.

Each profile stores:

- Display filters
- Coloring rules
- Layout
- Toolbar settings
- Packet list columns
- Preferences

Navigate to:

```
Edit

↓

Configuration Profiles
```

---

## Why Use Profiles?

Different investigations require different layouts.

Examples:

| Profile | Purpose |
|----------|----------|
| Default | General Analysis |
| HTB | Hack The Box Labs |
| Malware | Malware Analysis |
| DFIR | Digital Forensics |
| Networking | CCNA / Troubleshooting |

Profiles prevent constant reconfiguration.

---

# Appearance

Navigate to:

```
Edit

↓

Preferences

↓

Appearance
```

Customize:

- Theme
- Fonts
- Colors
- Packet fonts
- Packet list appearance

Choose settings that improve readability during long analysis sessions.

---

# Layout

Navigate to:

```
Edit

↓

Preferences

↓

Layout
```

You can rearrange:

- Packet List
- Packet Details
- Packet Bytes

Common layouts:

```
Packet List

↓

Packet Details

↓

Packet Bytes
```

or

```
Packet List

Packet Details | Packet Bytes
```

Choose the layout that best suits your workflow.

---

# Name Resolution

Navigate to:

```
Edit

↓

Preferences

↓

Name Resolution
```

Available options include:

### MAC Name Resolution

Displays vendor names instead of raw MAC addresses.

Example:

```
Dell_12:34:56
```

instead of

```
00:14:22:12:34:56
```

---

### Network Name Resolution

Attempts to resolve IP addresses into hostnames.

Example:

```
github.com
```

instead of

```
140.82.x.x
```

---

### Transport Name Resolution

Displays service names instead of port numbers.

Example:

```
HTTPS
```

instead of

```
443
```

---

# GeoIP

GeoIP provides geographical information about public IP addresses.

Information may include:

- Country
- City
- ASN (Autonomous System Number)

This feature is especially useful when analyzing connections to external systems.

---

# Installing GeoIP Databases

Wireshark uses **MaxMind GeoLite2** databases.

Required databases:

```
GeoLite2-ASN.mmdb

GeoLite2-City.mmdb

GeoLite2-Country.mmdb
```

---

# Linux Installation

Create the GeoIP directory:

```bash
sudo mkdir -p /usr/share/GeoIP
```

Copy the databases:

```bash
sudo cp *.mmdb /usr/share/GeoIP/
```

Verify installation:

```bash
ls /usr/share/GeoIP
```

Expected output:

```
GeoLite2-ASN.mmdb

GeoLite2-City.mmdb

GeoLite2-Country.mmdb
```

---

# Enabling GeoIP

Navigate to:

```
Edit

↓

Preferences

↓

Name Resolution
```

Verify that:

```
/usr/share/GeoIP
```

is listed under:

```
MaxMind Database Directories
```

Restart Wireshark after making changes.

---

# GeoIP Limitations

GeoIP is useful but not perfect.

Keep in mind:

- Public IPs only
- VPNs can hide the real location
- Proxies affect results
- Cloud providers may appear in different countries
- Databases require regular updates

GeoIP should support investigations—not be treated as definitive evidence of physical location.

---

# Capture Options

Navigate to:

```
Capture

↓

Options
```

Useful settings:

- Capture Interface
- Promiscuous Mode
- Monitor Mode (Wireless)
- Buffer Size
- Capture Filter
- Output File
- Ring Buffer

---

# Promiscuous Mode

Normally, a network interface only receives traffic intended for it.

Promiscuous Mode allows Wireshark to capture all traffic visible on the interface.

Benefits:

- Better troubleshooting
- Observe broadcast traffic
- Analyze switched networks (where applicable)

Note:

On modern switched Ethernet networks, Promiscuous Mode does **not** allow you to see all traffic from other hosts unless additional techniques (such as port mirroring or a network TAP) are used.

---

# Monitor Mode

Available on supported wireless adapters.

Allows capturing raw 802.11 Wi-Fi frames.

Useful for:

- Wireless security testing
- Wi-Fi troubleshooting
- Packet analysis

---

# Ring Buffer

Ring Buffers automatically rotate capture files.

Example:

```
Maximum File Size

↓

100 MB

↓

Maximum Files

↓

10
```

Once the limit is reached, the oldest capture is overwritten.

Useful for:

- Long-term monitoring
- Servers
- Continuous packet capture

---

# Packet List Columns

Customize columns by:

Right-clicking a column header.

Common useful columns:

| Column | Purpose |
|----------|----------|
| Time | Capture time |
| Source | Sender |
| Destination | Receiver |
| Protocol | Network protocol |
| Length | Packet size |
| Info | Packet summary |
| Source Port | Sending port |
| Destination Port | Receiving port |
| TCP Stream | Stream number |

Adding custom columns speeds up packet analysis.

---

# Time Display

Navigate to:

```
View

↓

Time Display Format
```

Options include:

- Seconds Since Beginning
- Seconds Since Previous Packet
- UTC Time
- Local Time

Choose the format that best supports your investigation.

---

# Coloring Rules

Navigate to:

```
View

↓

Coloring Rules
```

Examples:

| Filter | Purpose |
|----------|----------|
| tcp | Highlight TCP |
| dns | Highlight DNS |
| icmp | Highlight ICMP |
| arp | Highlight ARP |
| tcp.analysis.retransmission | Highlight Retransmissions |

Custom coloring makes abnormal traffic easier to spot.

---

# Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl + E | Start / Stop Capture |
| Ctrl + O | Open Capture |
| Ctrl + S | Save Capture |
| Ctrl + F | Find Packet |
| Ctrl + Shift + F | Find Next |
| Ctrl + W | Close Capture |
| Ctrl + R | Reload Capture |

Learning shortcuts improves workflow efficiency.

---

# Updating Wireshark

On Kali Linux:

```bash
sudo apt update

sudo apt install wireshark
```

Verify version:

```bash
wireshark --version
```

Keeping Wireshark updated ensures:

- Bug fixes
- Protocol support
- Security updates
- Performance improvements

---

# Cybersecurity Use Cases

## Blue Team

- Configure investigation profiles
- Enable GeoIP for external IP analysis
- Organize packet captures
- Improve analyst efficiency

---

## Red Team

- Validate attack traffic
- Separate HTB and lab configurations
- Analyze reverse shells
- Capture exploit traffic

---

## Digital Forensics

- Preserve packet evidence
- Maintain organized profiles
- Improve repeatability
- Document configuration settings

---

# Best Practices

- Use separate profiles for different tasks.
- Keep GeoLite2 databases updated.
- Enable only the name resolution features required for your investigation.
- Save important capture files before making changes.
- Use Ring Buffers for long-term packet captures.

---

# Common Mistakes

❌ Assuming GeoIP reveals the exact physical location of an attacker.

❌ Forgetting to restart Wireshark after installing GeoLite2 databases.

❌ Using the default profile for every investigation.

❌ Enabling unnecessary name resolution during forensic analysis.

❌ Ignoring Promiscuous Mode settings before starting a capture.

---

# Quick Summary

- Proper configuration improves efficiency and accuracy.
- Profiles allow different investigation environments.
- GeoIP provides geographical information for public IP addresses.
- Name Resolution converts addresses into more readable names.
- Ring Buffers support continuous packet capture.
- Custom layouts, columns, and coloring rules improve analysis speed.

---

# Key Takeaways

- A well-configured Wireshark environment saves time during investigations.
- Profiles, GeoIP, Name Resolution, and custom columns make packet analysis significantly more efficient.
- Understanding Wireshark configuration is just as important as understanding packet analysis itself.
- These settings form the foundation for professional workflows in network troubleshooting, penetration testing, digital forensics, malware analysis, and incident response.
