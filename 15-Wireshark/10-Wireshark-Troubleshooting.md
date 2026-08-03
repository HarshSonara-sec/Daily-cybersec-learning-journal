# Wireshark Troubleshooting Methodology

> **Category:** Network Analysis
>
> **Difficulty:** Intermediate
>
> **Prerequisites:**
>
> - Wireshark Fundamentals
> - Display Filters
> - Capture Filters
> - Protocol Analysis
> - TCP Analysis
> - DNS Analysis
> - HTTP/HTTPS Analysis
> - Statistics & Analysis Tools
> - GeoIP & Configuration
>
> **Recommended Before:**
>
> - 01-Wireshark-Fundamentals.md
> - 02-Wireshark-Display-Filters.md
> - 03-Wireshark-Capture-Filters.md
> - 04-Wireshark-Protocol-Analysis.md
> - 05-Wireshark-TCP-Analysis.md
> - 06-Wireshark-DNS-Analysis.md
> - 07-Wireshark-HTTP-HTTPS.md
> - 08-Wireshark-Statistics-and-Tools.md
> - 09-Wireshark-GeoIP-and-Configuration.md
>
> **Recommended Next:**
>
> - Nmap Fundamentals
> - Packet Analysis Labs
> - Malware Traffic Analysis
> - Active Directory Network Traffic
> - Network Forensics

---

# Introduction

Knowing Wireshark features is only half the skill.

Professional analysts solve problems by following a **structured investigation methodology**, rather than randomly inspecting packets.

This guide brings together everything learned in the previous notes into a practical workflow suitable for:

- SOC Analysts
- Incident Responders
- Network Engineers
- Penetration Testers
- DFIR Analysts

---

# Investigation Workflow

```
Capture Traffic

↓

Understand the Environment

↓

Identify the Devices

↓

Determine the Protocols

↓

Follow the Communication

↓

Locate the Failure

↓

Verify the Root Cause

↓

Document Findings
```

Never jump directly to packet-by-packet analysis.

---

# Step 1 — Verify the Capture

Before analyzing traffic, confirm that the capture itself is valid.

Check:

- Correct network interface
- Capture duration
- Packet count
- Packet timestamps
- File integrity

Navigate to:

```
Statistics
↓

Capture File Properties
```

---

# Step 2 — Identify Active Hosts

Use:

```
Statistics
↓

Endpoints
```

Questions to answer:

- Which devices communicated?
- Which IP addresses appear?
- Are there unknown systems?
- Which host generated the most traffic?

---

# Step 3 — Identify Protocols

Open:

```
Statistics
↓

Protocol Hierarchy
```

Determine:

- TCP vs UDP ratio
- DNS activity
- HTTP/HTTPS usage
- ICMP traffic
- Unexpected protocols

This provides an overview before deep analysis.

---

# Step 4 — Examine Conversations

Navigate to:

```
Statistics
↓

Conversations
```

Identify:

- Long-lived sessions
- Large transfers
- Unusual communication
- High-volume hosts

Focus your investigation on significant conversations first.

---

# Step 5 — Apply Display Filters

Instead of reviewing every packet, isolate relevant traffic.

Common filters:

```
tcp
```

```
dns
```

```
http
```

```
tls
```

```
icmp
```

```
arp
```

Filter combinations:

```
ip.addr == 192.168.1.10
```

```
tcp.port == 443
```

```
dns && ip.addr == 192.168.1.50
```

---

# Step 6 — Follow the Communication

Right-click a packet:

```
Follow

↓

TCP Stream
```

or

```
Follow

↓

HTTP Stream
```

Following streams reconstructs the complete conversation.

This is often more useful than inspecting individual packets.

---

# Step 7 — Look for Errors

Open:

```
Analyze
↓

Expert Information
```

Common warnings include:

- Retransmissions
- Duplicate ACKs
- TCP Resets
- Malformed Packets
- Checksum Errors
- Out-of-Order Packets

Expert Information helps prioritize investigation.

---

# Step 8 — Verify Performance

Use:

```
Statistics
↓

I/O Graphs
```

Look for:

- Traffic spikes
- Bandwidth changes
- Packet bursts
- Periods of inactivity

Performance graphs often reveal issues not obvious in packet details.

---

# Common Troubleshooting Scenarios

---

## Scenario 1 — Website Does Not Load

Workflow:

```
ARP

↓

DNS

↓

TCP Handshake

↓

TLS

↓

HTTP
```

Questions:

- Did ARP resolve the gateway?
- Did DNS return an IP address?
- Was the TCP handshake successful?
- Did TLS complete?
- Was an HTTP response received?

---

## Scenario 2 — Slow Web Browsing

Investigate:

- DNS latency
- TCP retransmissions
- Small TCP window sizes
- High round-trip times
- Excessive redirects

Useful filters:

```
dns
```

```
tcp.analysis.retransmission
```

---

## Scenario 3 — DNS Failure

Check:

```
dns
```

Questions:

- Was a query sent?
- Was a response received?
- Was the response NXDOMAIN?
- Was the correct DNS server contacted?

---

## Scenario 4 — Packet Loss

Indicators:

```
tcp.analysis.retransmission
```

```
tcp.analysis.duplicate_ack
```

```
tcp.analysis.lost_segment
```

Possible causes:

- Congestion
- Poor wireless signal
- Hardware failure
- Network overload

---

## Scenario 5 — Connection Reset

Filter:

```
tcp.flags.reset == 1
```

Possible causes:

- Closed service
- Firewall rejection
- Application crash
- Invalid connection

---

## Scenario 6 — High Bandwidth Usage

Use:

```
Statistics
↓

Conversations
```

and

```
Statistics
↓

Endpoints
```

Identify:

- Largest data transfers
- Top talkers
- Unexpected hosts

---

## Scenario 7 — Malware Investigation

Workflow:

```
Endpoints

↓

DNS

↓

HTTP / HTTPS

↓

TLS

↓

Follow Streams

↓

Export Objects
```

Questions:

- Which domains were contacted?
- Were files downloaded?
- Were unusual User-Agents used?
- Did the host communicate repeatedly?

---

# Building a Timeline

A common investigation technique:

```
ARP

↓

DHCP

↓

DNS

↓

TCP

↓

TLS

↓

HTTP

↓

File Download

↓

Connection Closed
```

Following the chronological order often reveals the attack sequence.

---

# Useful Display Filters

DNS

```
dns
```

TCP

```
tcp
```

UDP

```
udp
```

ICMP

```
icmp
```

ARP

```
arp
```

HTTP

```
http
```

TLS

```
tls
```

Retransmissions

```
tcp.analysis.retransmission
```

Duplicate ACK

```
tcp.analysis.duplicate_ack
```

Reset Packets

```
tcp.flags.reset == 1
```

Destination IP

```
ip.dst == 192.168.1.100
```

Source IP

```
ip.src == 192.168.1.100
```

---

# Common Analyst Questions

Always ask:

- Who initiated the connection?
- What protocol is being used?
- Was the connection successful?
- Was encryption used?
- Was data transferred?
- Did errors occur?
- Is the traffic expected?
- What happened immediately before and after the event?

These questions guide efficient investigations.

---

# Cybersecurity Use Cases

## Blue Team

- Detect suspicious traffic
- Investigate alerts
- Validate IDS events
- Monitor user activity

---

## Red Team

- Verify exploit traffic
- Validate reverse shells
- Confirm payload execution
- Troubleshoot network communication

---

## Incident Response

- Reconstruct attacker activity
- Build timelines
- Recover downloaded files
- Identify command-and-control communication

---

## Digital Forensics

- Preserve packet evidence
- Document findings
- Correlate network activity with host logs
- Produce investigation reports

---

# Best Practices

- Start with the big picture before examining individual packets.
- Use statistics tools to narrow your focus.
- Follow complete streams instead of isolated packets.
- Correlate multiple protocols during analysis.
- Keep detailed notes throughout the investigation.
- Validate assumptions with evidence from the capture.

---

# Common Mistakes

❌ Beginning with packet 1 and reading sequentially.

❌ Ignoring DNS when troubleshooting web applications.

❌ Focusing only on a single protocol.

❌ Assuming encrypted traffic is malicious.

❌ Overlooking retransmissions and TCP resets.

❌ Jumping to conclusions before reviewing the entire conversation.

---

# Quick Summary

- Effective troubleshooting follows a structured methodology.
- Start with statistics and high-level views before examining individual packets.
- Display filters and Follow Stream significantly reduce investigation time.
- Expert Information helps identify common network issues.
- Building a timeline provides valuable context for understanding events.

---

# Analyst Workflow Cheat Sheet

```
Open Capture
      ↓
Capture File Properties
      ↓
Protocol Hierarchy
      ↓
Endpoints
      ↓
Conversations
      ↓
Apply Display Filters
      ↓
Follow Stream
      ↓
Expert Information
      ↓
I/O Graphs
      ↓
Export Evidence
      ↓
Document Findings
```

---

# Key Takeaways

- Wireshark is more than a packet viewer—it is a comprehensive network analysis platform.
- A structured methodology leads to faster and more accurate investigations than manually inspecting packets.
- Combining protocol analysis, statistical tools, timelines, and stream reconstruction enables analysts to solve complex networking and cybersecurity problems efficiently.
- These workflows are directly applicable to enterprise environments, SOC operations, penetration testing, malware analysis, incident response, digital forensics, and certification labs such as HTB CPTS, PNPT, and OSCP.
