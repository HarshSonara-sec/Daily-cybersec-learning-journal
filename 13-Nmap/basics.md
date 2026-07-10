### cheatsheet for Nmap command

```for target scanning ->
nmap –sV –p 80 <target-ip>
-sV enables service version detection
-p 80 specifies that you’re scanning port 80 (HTTP).
<target-ip> should be replaced with the IP address or hostname of the target system.
```
### What is Nmap?
Network Mapper (Nmap) is an open-source network analysis and security auditing tool. It is designed to scan networks and identify which hosts are available on the network using raw packets, services, and applications. 

### How to use Nmap
Nmap can be divided into the following scanning techniques:

Host discovery.

Port scanning.

Service enumeration and detection.

OS detection.

Scriptable interaction with the target service (Nmap Scripting Engine).

### The importance of enumeration: Why learning Nmap is just a starting point
Enumeration is the art of information gathering so that we can identify all of the ways we could attack a target. Nmap is a tool we can use to enumerate this information, but we should always prioritize skills and methodology over tools.

Port 443 is the standard and default TCP port used for HTTPS (Hypertext Transfer Protocol Secure) traffic

In web-application terminology, a folder is commonly known as a directory

The hash character (#) can be used to comment out the rest of a line in MySQL. 

### Important commands
# Nmap Cheat Sheet

## Basic Syntax

```bash
nmap <target>
```

Example:

```bash
nmap 10.129.x.x
```

---

## Commands Practiced

### Scan a Single Host

```bash
nmap <IP>
```

Performs a basic scan of the target.

---

### Service & Version Detection

```bash
nmap -sV <IP>
```

Attempts to identify running services and their versions.

---

### Default Script Scan

```bash
nmap -sC <IP>
```

Runs Nmap's default NSE (Nmap Scripting Engine) scripts.

---

### Aggressive Scan

```bash
nmap -A <IP>
```

Performs OS detection, version detection, script scanning, and traceroute.

---

### Scan Specific Ports

```bash
nmap -p 22,80,443 <IP>
```

Scans only the specified ports.

---

### Scan All TCP Ports

```bash
nmap -p- <IP>
```

Scans all 65,535 TCP ports.

---

### Save Scan Results

```bash
nmap -oN scan.txt <IP>
```

Saves output in a human-readable format.

---

## Important Things to Remember

* Always verify the target IP before scanning.
* Start with a basic scan before using aggressive options.
* Closed ports are normal; focus on **open** ports.
* Service versions help identify potential vulnerabilities.
* Enumeration is more important than rushing to exploitation.
* Save scan results for future reference and documentation.
* Read service banners carefully—they often reveal useful information.
* Scanning large networks or all ports takes significantly longer.

---

## Commonly Encountered Ports

| Port | Service |
| ---: | ------- |
|   21 | FTP     |
|   22 | SSH     |
|   23 | Telnet  |
|   25 | SMTP    |
|   53 | DNS     |
|   80 | HTTP    |
|  110 | POP3    |
|  139 | NetBIOS |
|  143 | IMAP    |
|  443 | HTTPS   |
|  445 | SMB     |
| 3389 | RDP     |

---

## Security Perspective

Nmap is one of the most important reconnaissance tools in cybersecurity. It helps identify live hosts, open ports, running services, and software versions, allowing security professionals to assess attack surfaces before performing further testing.

