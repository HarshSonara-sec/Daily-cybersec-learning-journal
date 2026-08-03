# Nmap Fundamentals

> **Category:** Network Enumeration
>
> **Difficulty:** Beginner
>
> **Prerequisites:**
>
> - TCP/IP Basics
> - Ports and Protocols
> - Basic Linux Commands
>
> **Recommended Before:**
>
> - Networking Fundamentals
> - Wireshark Fundamentals
>
> **Recommended After:**
>
> - TCP SYN vs TCP Connect Scans
> - Packet-Level Analysis with Wireshark

---

# Introduction

Nmap (Network Mapper) is one of the most powerful and widely used network discovery and security auditing tools. It enables security professionals, penetration testers, and system administrators to identify live hosts, discover open ports, enumerate running services, detect operating systems, and gather information about networked devices.

Nmap is an essential tool in cybersecurity because almost every engagement begins with **enumeration**—understanding what systems are available and what services they expose.

---

# What is Nmap?

Nmap stands for:

```
Network Mapper
```

It is an open-source utility designed for:

- Host discovery
- Port scanning
- Service enumeration
- Version detection
- Operating system detection
- Network inventory
- Security auditing

---

# Why Use Nmap?

Nmap helps answer critical questions such as:

- Is the target system online?
- Which ports are open?
- Which services are running?
- Which software versions are installed?
- What operating system is being used?
- Are there potential attack surfaces?

Without enumeration, penetration testing becomes guesswork.

---

# Common Cybersecurity Use Cases

## Penetration Testing

- Identify exposed services
- Find attack vectors
- Verify accessible ports

## Blue Team

- Discover unauthorized devices
- Verify firewall rules
- Audit exposed services

## Network Administration

- Inventory devices
- Troubleshoot connectivity
- Validate configurations

## Incident Response

- Identify unexpected services
- Detect rogue hosts
- Investigate suspicious systems

---

# Understanding Ports

A port is a logical communication endpoint used by applications.

Examples:

| Service | Port |
|----------|-----:|
| HTTP | 80 |
| HTTPS | 443 |
| SSH | 22 |
| FTP | 21 |
| DNS | 53 |
| SMTP | 25 |
| SMB | 445 |

Open ports indicate that an application is listening for incoming connections.

---

# Open vs Closed vs Filtered

## Open

```
Client
    ↓
Server accepts connection
```

A service is actively listening.

---

## Closed

```
Client
    ↓
RST returned
```

No application is listening.

---

## Filtered

```
Client
    ↓
Firewall drops packets
```

Nmap cannot determine whether the port is open.

---

# Host Discovery

Before scanning ports, Nmap determines whether a host is online.

Common discovery methods include:

- ICMP Echo Request
- TCP SYN probes
- TCP ACK probes
- ARP requests (local network)

If the host responds, Nmap proceeds with further enumeration.

---

# Port Scanning

After identifying a live host, Nmap checks ports to determine their state.

Possible results include:

- Open
- Closed
- Filtered
- Open|Filtered
- Closed|Filtered

Understanding these states helps assess the target's attack surface.

---

# Service Detection

Knowing that port 80 is open is useful, but identifying the service is even more valuable.

Example:

```
80/tcp open http Apache
```

This reveals:

- Port number
- Protocol
- State
- Service

Service detection assists in vulnerability assessment.

---

# Version Detection

Nmap can determine software versions.

Example:

```
Apache httpd 2.4.58
```

Version information allows analysts to:

- Search for CVEs
- Check vendor advisories
- Assess patch levels

---

# Operating System Detection

Nmap can estimate the target operating system by analyzing responses to crafted packets.

Possible results:

- Linux
- Windows
- FreeBSD
- Cisco IOS
- Network appliances

OS detection is an estimate and may not always be accurate.

---

# Nmap Scripting Engine (NSE)

Nmap includes a powerful scripting engine called **NSE**.

It automates tasks such as:

- Banner grabbing
- Vulnerability detection
- SMB enumeration
- HTTP enumeration
- SSL/TLS checks
- DNS information gathering

Thousands of community scripts are available.

---

# Typical Enumeration Workflow

```
Discover Host
      ↓
Identify Open Ports
      ↓
Identify Services
      ↓
Determine Versions
      ↓
Gather Additional Information
      ↓
Assess Potential Vulnerabilities
```

---

# Nmap and Wireshark Together

The source video demonstrated running Nmap scans while simultaneously capturing the generated traffic with Wireshark. This allows you to observe:

- TCP handshakes
- SYN packets
- RST responses
- Service replies

Capturing scans provides a deeper understanding of how Nmap works at the packet level. :contentReference[oaicite:0]{index=0}

---

# Advantages

- Fast
- Reliable
- Highly customizable
- Supports scripting
- Cross-platform
- Industry standard

---

# Limitations

- Firewalls may block scans.
- IDS/IPS solutions can detect scans.
- UDP scanning is slower than TCP scanning.
- OS detection is not always precise.

---

# Best Practices

- Obtain authorization before scanning.
- Start with basic discovery before advanced scans.
- Save scan results for documentation.
- Correlate Nmap results with packet captures in Wireshark.
- Interpret results carefully rather than relying on assumptions.

---

# Common Mistakes

❌ Assuming an open port is vulnerable.

❌ Ignoring filtered ports.

❌ Forgetting to verify results manually.

❌ Scanning production systems without permission.

❌ Treating OS detection as definitive.

---

# Quick Summary

- Nmap is the industry-standard network enumeration tool.
- It identifies live hosts, open ports, services, versions, and operating systems.
- Enumeration is the foundation of penetration testing.
- Combining Nmap with Wireshark helps visualize scan behavior and understand network communication.
- Accurate interpretation of scan results is just as important as running the scan itself.

---

# Key Takeaways

- Enumeration comes before exploitation.
- Open ports represent potential attack surfaces.
- Service and version detection provide valuable reconnaissance.
- Nmap and Wireshark complement each other, combining active scanning with packet-level analysis.
- Mastering Nmap is a core skill for penetration testers, SOC analysts, incident responders, and network defenders.
