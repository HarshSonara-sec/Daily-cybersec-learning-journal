# Nmap Scan State Reference

> **Category:** Nmap Reference
>
> **Difficulty:** Beginner
>
> **Prerequisites:**
>
> - Nmap Fundamentals
> - TCP/IP Basics
>
> **Recommended Before:**
>
> - 01-Nmap-Fundamentals.md
> - 02-TCP-SYN-vs-TCP-Connect-Scans.md
>
> **Recommended After:**
>
> - Nmap Commands Cheat Sheet

---

# Introduction

One of the most important skills when using Nmap is understanding **scan states**.

Many beginners immediately focus on whether a port is "open", but Nmap can return several different states depending on how the target responds.

A scan state **does not always indicate the actual condition of the port**. Instead, it describes **how Nmap interpreted the responses (or lack of responses) it received**.

Correct interpretation prevents false assumptions during penetration testing and troubleshooting.

---

# Possible Port States

Nmap may report:

```
open

closed

filtered

unfiltered

open|filtered

closed|filtered
```

Each state has a different meaning.

---

# Open

Example:

```
22/tcp open ssh
```

Meaning:

- An application is actively listening.
- The target accepted the connection.
- Communication is possible.

Packet Flow

```
Scanner
   │
   ├── SYN ─────────────►
   │
   ◄──────────── SYN/ACK
```

Typical Examples

- SSH
- HTTP
- HTTPS
- SMB
- FTP

---

## What Does It Mean?

An open port represents an **available service**.

It does **not** automatically mean:

- Vulnerable
- Misconfigured
- Exploitable

Further enumeration is required.

---

# Closed

Example

```
25/tcp closed smtp
```

Meaning

- The host is reachable.
- No service is listening.
- The operating system rejected the connection.

Packet Flow

```
Scanner
   │
   ├── SYN ─────────────►
   │
   ◄──────────── RST
```

---

## Why Closed Ports Matter

Closed ports confirm:

- The host is online.
- The firewall allowed communication.
- No application is using that port.

Closed ports help verify host availability.

---

# Filtered

Example

```
80/tcp filtered http
```

Meaning

Nmap cannot determine whether the port is open because packets are being filtered.

Possible causes:

- Firewall
- ACL (Access Control List)
- IPS/IDS
- Router filtering
- Packet drops

Packet Flow

```
Scanner
   │
   ├── SYN ─────────────►
   │
      (No Reply)
```

or

```
ICMP Unreachable
```

---

## Important Note

Filtered **does not mean closed**.

It simply means:

```
Nmap could not determine the actual state.
```

---

# Unfiltered

Example

```
80/tcp unfiltered http
```

Meaning

- Packets reached the host.
- Filtering is not preventing communication.
- Nmap still cannot determine whether the port is open or closed with the current scan type.

This state appears mainly with ACK scans (`-sA`).

---

# Open | Filtered

Example

```
161/udp open|filtered
```

Meaning

Nmap cannot distinguish between:

```
Open
```

or

```
Filtered
```

Why?

Many UDP services do not respond unless they receive valid application data.

If no response is received, Nmap cannot tell whether:

- the service ignored the packet, or
- a firewall dropped it.

This state is common during UDP scanning.

---

# Closed | Filtered

Example

```
123/udp closed|filtered
```

Meaning

Nmap cannot determine whether the port is:

- Closed
- Filtered

This state is uncommon and depends on the scan type and target responses.

---

# Quick Comparison

| State | Host Reachable | Service Running | Firewall Possible |
|--------|:--------------:|:---------------:|:-----------------:|
| Open | ✅ | ✅ | Possible |
| Closed | ✅ | ❌ | Usually No |
| Filtered | Unknown | Unknown | ✅ |
| Unfiltered | ✅ | Unknown | ❌ |
| Open\|Filtered | Unknown | Unknown | Possible |
| Closed\|Filtered | Unknown | Unknown | Possible |

---

# Packet-Level View

## Open

```
SYN
↓

SYN/ACK
```

---

## Closed

```
SYN
↓

RST
```

---

## Filtered

```
SYN
↓

No Response
```

or

```
ICMP Unreachable
```

---

# Scan Types and Common States

| Scan Type | Common Results |
|------------|----------------|
| SYN Scan (`-sS`) | Open, Closed, Filtered |
| TCP Connect (`-sT`) | Open, Closed |
| UDP Scan (`-sU`) | Open, Open\|Filtered, Closed |
| ACK Scan (`-sA`) | Filtered, Unfiltered |
| FIN / NULL / Xmas | Open, Closed, Filtered |

---

# Real-World Interpretation

Example

```
PORT     STATE     SERVICE

22/tcp   open      ssh

80/tcp   open      http

135/tcp  filtered  msrpc

139/tcp  closed    netbios

445/tcp  open      microsoft-ds
```

Interpretation

- SSH is available.
- HTTP is available.
- Port 135 is blocked by filtering.
- NetBIOS is not running.
- SMB is available for further enumeration.

---

# HTB Perspective

During Hack The Box machines, you will frequently encounter:

```
22/tcp open ssh

80/tcp open http

445/tcp open smb

53/udp open|filtered
```

Understanding these states determines your next enumeration step.

---

# Cybersecurity Use Cases

## Penetration Testing

- Prioritize open services.
- Investigate filtered ports separately.
- Identify exposed attack surfaces.

---

## Blue Team

- Verify firewall behavior.
- Confirm exposed services.
- Validate security controls.

---

## Incident Response

- Identify unexpected open ports.
- Detect firewall misconfigurations.
- Compare historical scans.

---

# Best Practices

- Do not assume an open port is vulnerable.
- Treat filtered results as inconclusive until verified.
- Use additional scan types when necessary.
- Confirm findings with service enumeration and packet analysis.

---

# Common Mistakes

❌ Assuming "filtered" means the port is closed.

❌ Ignoring closed ports during host discovery.

❌ Believing OS detection is required to interpret port states.

❌ Stopping enumeration after identifying open ports.

❌ Assuming UDP silence always indicates a firewall.

---

# Quick Summary

```
Open
↓

Service is listening

-------------------------

Closed
↓

Host reachable
No service listening

-------------------------

Filtered
↓

Firewall or filtering prevents determination

-------------------------

Unfiltered
↓

Host reachable
Current scan cannot determine state

-------------------------

Open|Filtered
↓

Usually encountered with UDP scans

-------------------------

Closed|Filtered
↓

Rare
Depends on scan type
```

---

# Key Takeaways

- Port states describe **Nmap's interpretation**, not absolute truth.
- Open ports are starting points for further enumeration.
- Filtered states require additional investigation.
- Understanding scan states is fundamental for penetration testing, SOC analysis, and network troubleshooting.
