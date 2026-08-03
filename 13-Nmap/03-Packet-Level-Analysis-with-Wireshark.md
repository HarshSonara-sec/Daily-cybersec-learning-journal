# Packet-Level Analysis with Wireshark

> **Category:** Network Enumeration
>
> **Difficulty:** Intermediate
>
> **Prerequisites:**
>
> - Nmap Fundamentals
> - TCP SYN vs TCP Connect Scans
> - Wireshark Fundamentals
>
> **Recommended Before:**
>
> - 01-Nmap-Fundamentals.md
> - 02-TCP-SYN-vs-TCP-Connect-Scans.md
>
> **Recommended After:**
>
> - Large PCAP Analysis & Best Practices

---

# Introduction

Nmap tells us **what** is happening on a network.

Wireshark explains **how** it happens.

Using both tools together allows security professionals to understand network communication at the packet level rather than relying solely on scan results.

This workflow was demonstrated throughout the video by running Nmap scans while simultaneously capturing the generated traffic in Wireshark. :contentReference[oaicite:0]{index=0}

---

# Why Capture Nmap Traffic?

Packet captures help us understand:

- TCP handshakes
- Port state determination
- Nmap scanning techniques
- Service responses
- Firewall behavior
- IDS/IPS detection
- Network troubleshooting

Instead of trusting scan results blindly, we verify them using actual packets.

---

# Lab Setup

Example Environment

```
Attacker (Kali Linux)

↓

Nmap Scan

↓

Target Machine

↓

Wireshark Capture
```

The scan is performed from Kali Linux while Wireshark captures every packet exchanged between the attacker and the target.

---

# Capturing the Scan

Start Wireshark before running Nmap.

Choose the correct interface.

Examples:

```
eth0
```

```
wlan0
```

```
tun0
```

(For HTB VPN labs.)

After the capture starts:

Run Nmap.

Observe packets appearing in real time.

---

# Basic Display Filters

Show only TCP packets

```
tcp
```

Show traffic from one host

```
ip.addr == TARGET_IP
```

Show only SYN packets

```
tcp.flags.syn == 1
```

Show reset packets

```
tcp.flags.reset == 1
```

Show DNS traffic

```
dns
```

Display filters reduce noise and make analysis easier.

---

# Analyzing a SYN Scan

Command

```bash
sudo nmap -sS TARGET_IP
```

Expected Packet Flow

```
Attacker

↓

SYN

↓

Target

↓

SYN/ACK

↓

Attacker

↓

RST
```

The missing ACK confirms that Nmap performed a half-open (SYN) scan.

---

# Analyzing a TCP Connect Scan

Command

```bash
nmap -sT TARGET_IP
```

Expected Packet Flow

```
SYN

↓

SYN/ACK

↓

ACK

↓

RST
```

Unlike a SYN scan, the connection is fully established before being closed.

---

# Identifying Open Ports

An open TCP port typically responds with:

```
SYN/ACK
```

This tells Nmap that a service is actively listening.

---

# Identifying Closed Ports

A closed TCP port responds with:

```
RST
```

No application is listening on that port.

---

# Identifying Filtered Ports

Filtered ports often show:

- No response
- ICMP unreachable messages
- Firewall behavior

Nmap reports these as filtered because it cannot determine whether a service exists behind the filtering device.

---

# Following TCP Streams

Right-click a TCP packet.

Select:

```
Follow

↓

TCP Stream
```

Benefits:

- Reconstruct conversations
- Inspect transmitted data
- Verify application behavior
- Understand session flow

Although Nmap scanning itself contains minimal payload data, following streams is valuable when analyzing application traffic after enumeration.

---

# TCP Header Analysis

Inspect each TCP packet for:

- Source Port
- Destination Port
- Sequence Number
- Acknowledgment Number
- Window Size
- Flags
- Header Length

Understanding these fields improves troubleshooting and helps explain Nmap's scanning behavior.

---

# TCP Flags

Important flags include:

| Flag | Meaning |
|-------|----------|
| SYN | Start a connection |
| ACK | Acknowledge received data |
| RST | Reset a connection |
| FIN | Gracefully close a connection |
| PSH | Push buffered data |
| URG | Urgent data |

Nmap primarily relies on SYN and RST during standard TCP scanning.

---

# Window Size

The TCP Window Size controls how much data can be sent before requiring an acknowledgment.

Different operating systems often use different default window sizes.

Although window size alone is not sufficient for fingerprinting, it contributes to operating system detection.

This concept was discussed while examining packet details in Wireshark. :contentReference[oaicite:1]{index=1}

---

# TCP Options

Expand the TCP header.

Common options include:

- MSS (Maximum Segment Size)
- Window Scale
- SACK Permitted
- Timestamps

These values differ between operating systems and are useful during OS fingerprinting.

---

# Packet Timing

Wireshark timestamps reveal:

- Response latency
- Network delays
- Scan speed
- Retransmissions

Slow responses may indicate:

- Congestion
- Firewalls
- Rate limiting
- High network latency

---

# Detecting Nmap Scans

Signs of scanning include:

- Many SYN packets in a short period
- Sequential destination ports
- Numerous failed connection attempts
- Minimal application-layer traffic

Blue Teams and SOC analysts use these indicators to identify reconnaissance activity.

---

# Useful Wireshark Filters

TCP only

```
tcp
```

SYN packets

```
tcp.flags.syn == 1
```

Reset packets

```
tcp.flags.reset == 1
```

Specific host

```
ip.addr == TARGET_IP
```

Specific TCP stream

```
tcp.stream == 0
```

Retransmissions

```
tcp.analysis.retransmission
```

---

# Practical Investigation Workflow

```
Capture Packets
        ↓
Apply Display Filters
        ↓
Identify Scan Type
        ↓
Inspect TCP Flags
        ↓
Determine Port State
        ↓
Follow TCP Stream
        ↓
Document Findings
```

---

# Cybersecurity Use Cases

## Penetration Testing

- Validate scan behavior
- Confirm open ports
- Understand firewall responses

---

## Blue Team

- Detect reconnaissance
- Investigate suspicious traffic
- Verify IDS alerts

---

## SOC

- Correlate packet captures with SIEM events
- Build attack timelines
- Identify scanning hosts

---

## Incident Response

- Confirm attacker activity
- Preserve packet evidence
- Analyze reconnaissance techniques

---

# Best Practices

- Capture traffic before starting scans.
- Filter traffic to reduce noise.
- Compare SYN scans with TCP Connect scans.
- Analyze packet headers instead of relying solely on Nmap output.
- Save PCAP files for future review and reporting.

---

# Common Mistakes

❌ Capturing on the wrong interface.

❌ Forgetting to apply display filters.

❌ Confusing SYN scans with normal TCP connections.

❌ Ignoring TCP flags during analysis.

❌ Assuming Nmap output alone explains every network interaction.

---

# Quick Summary

- Wireshark complements Nmap by exposing the underlying packet exchanges.
- SYN scans terminate before completing the TCP handshake, while TCP Connect scans establish full connections.
- TCP flags, window sizes, options, and timing provide valuable context for understanding scan behavior.
- Packet-level analysis improves troubleshooting, penetration testing, and defensive monitoring.

---

# Key Takeaways

- Nmap answers **what** is exposed; Wireshark explains **how** the communication occurs.
- Combining active scanning with packet captures provides a deeper understanding of network protocols.
- Packet-level analysis is an essential skill for penetration testers, SOC analysts, incident responders, and digital forensics professionals.
- Learning to interpret packet headers and TCP behavior builds a strong foundation for advanced network security analysis.
