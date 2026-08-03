# TCP SYN Scan vs TCP Connect Scan

> **Category:** Network Enumeration
>
> **Difficulty:** Beginner → Intermediate
>
> **Prerequisites:**
>
> - Nmap Fundamentals
> - TCP/IP Basics
> - Three-Way Handshake
>
> **Recommended Before:**
>
> - 01-Nmap-Fundamentals.md
>
> **Recommended After:**
>
> - Packet-Level Analysis with Wireshark

---

# Introduction

Nmap supports multiple scan techniques, but the two most commonly used are:

- TCP Connect Scan (`-sT`)
- TCP SYN Scan (`-sS`)

Although both identify open ports, they operate differently at the TCP level. Understanding these differences is essential for interpreting scan results and analyzing traffic in Wireshark.

---

# TCP Three-Way Handshake Review

A normal TCP connection follows this sequence:

```
Client
   │
   ├── SYN ─────────────►
   │
   ◄──────────── SYN/ACK
   │
   ├── ACK ─────────────►
   │
Connection Established
```

Every TCP connection begins with this handshake.

---

# What is a TCP Connect Scan?

A TCP Connect Scan uses the operating system's networking stack to establish a **complete TCP connection**.

Nmap completes the full handshake before closing the connection.

Command:

```bash
nmap -sT <target>
```

---

# Packet Flow (TCP Connect Scan)

Open Port

```
Attacker                     Target

SYN ------------------------►

      ◄---------------- SYN/ACK

ACK ------------------------►

Connection Established

RST ------------------------►
```

The operating system completes the connection before terminating it.

---

# Closed Port

```
Attacker                     Target

SYN ------------------------►

      ◄---------------- RST
```

The server immediately refuses the connection because no service is listening.

---

# Characteristics of TCP Connect Scan

Advantages

- Works without raw socket privileges
- Compatible with most operating systems
- Reliable results

Disadvantages

- Slower
- Easily logged
- Completes full TCP connections
- More visible to defenders

---

# What is a TCP SYN Scan?

A TCP SYN Scan is often called a **Half-Open Scan** because it never completes the TCP handshake.

Instead of sending the final ACK, Nmap sends a reset (RST) to terminate the connection.

Command:

```bash
sudo nmap -sS <target>
```

Administrator/root privileges are generally required because raw packets are crafted directly.

---

# Packet Flow (TCP SYN Scan)

Open Port

```
Attacker                     Target

SYN ------------------------►

      ◄---------------- SYN/ACK

RST ------------------------►
```

Notice that the connection is never fully established.

---

# Closed Port

```
Attacker                     Target

SYN ------------------------►

      ◄---------------- RST
```

The response is identical to a normal TCP rejection.

---

# Why is it Called a Half-Open Scan?

The connection is interrupted before the final ACK.

```
SYN
↓

SYN/ACK
↓

RST
```

Because the handshake never completes, the connection remains "half-open."

---

# Why Use SYN Scans?

Benefits include:

- Faster scanning
- Lower resource usage
- Does not establish full TCP sessions
- Preferred scan type for penetration testing

Historically, SYN scans generated fewer application logs because the connection was never fully established.

---

# Stealth Considerations

Older documentation often refers to SYN scans as "stealth scans."

Modern security solutions can still detect SYN scans by monitoring repeated SYN packets, incomplete handshakes, and scanning patterns.

Therefore, SYN scans are **less noisy** than TCP Connect scans but are **not invisible**.

---

# Comparison

| Feature | TCP Connect (`-sT`) | TCP SYN (`-sS`) |
|----------|--------------------|-----------------|
| Completes Handshake | Yes | No |
| Raw Packets | No | Yes |
| Root/Admin Required | No | Usually Yes |
| Speed | Moderate | Fast |
| Logging | More likely | Less likely |
| Common Use | General scanning | Penetration testing |

---

# Packet Analysis in Wireshark

TCP Connect Scan

Look for:

- SYN
- SYN/ACK
- ACK
- RST

This confirms a full connection followed by termination.

TCP SYN Scan

Look for:

- SYN
- SYN/ACK
- RST

The absence of the final ACK indicates a SYN scan.

These packet patterns were demonstrated by capturing Nmap scans in Wireshark. :contentReference[oaicite:0]{index=0}

---

# Cybersecurity Use Cases

## Red Team

- Network reconnaissance
- Service discovery
- Attack surface identification

## Blue Team

- Detect port scans
- Monitor repeated SYN packets
- Identify reconnaissance activity

## SOC

- Correlate Nmap scans with IDS alerts
- Investigate scanning sources
- Build timelines of reconnaissance

---

# Best Practices

- Use SYN scans when you have the required privileges.
- Validate suspicious results with additional scans.
- Analyze packet captures to understand scan behavior.
- Record scan parameters in assessment reports.

---

# Common Mistakes

❌ Assuming SYN scans are undetectable.

❌ Forgetting that `-sS` generally requires administrator/root privileges.

❌ Confusing RST packets from the scanner with RST packets from the target.

❌ Ignoring firewall behavior when interpreting results.

---

# Quick Summary

- TCP Connect scans complete the full TCP handshake.
- TCP SYN scans terminate the connection before completion.
- SYN scans are generally faster and produce less application-level logging.
- Wireshark clearly shows the difference between the two scan types.

---

# Key Takeaways

- Understanding the TCP handshake is essential for interpreting Nmap scans.
- SYN scans are the preferred choice for most penetration testing scenarios.
- Packet captures provide valuable insight into how Nmap interacts with target systems.
