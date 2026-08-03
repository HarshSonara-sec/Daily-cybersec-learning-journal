# Wireshark Statistics & Analysis Tools

> **Category:** Network Analysis
>
> **Difficulty:** Beginner → Intermediate
>
> **Prerequisites:**
>
> - Wireshark Fundamentals
> - Display Filters
> - Protocol Analysis
> - TCP Analysis
> - DNS Analysis
> - HTTP/HTTPS Analysis
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
>
> **Recommended After:**
>
> - 09-Wireshark-GeoIP-and-Configuration.md

---

# Introduction

Capturing packets is only the beginning.

Wireshark provides several built-in **statistics and analysis tools** that summarize traffic, identify communication patterns, detect anomalies, and assist with troubleshooting.

These tools save analysts from manually inspecting thousands of packets.

---

# Statistics Menu

Most analysis features are located under:

```
Statistics
```

Common options include:

- Capture File Properties
- Resolved Addresses
- Protocol Hierarchy
- Conversations
- Endpoints
- Packet Lengths
- I/O Graphs
- Flow Graph
- Service Response Time
- DNS Statistics
- HTTP Statistics

These options provide different views of the same packet capture.

---

# Capture File Properties

Navigate to:

```
Statistics

↓

Capture File Properties
```

Displays:

- File Name
- File Size
- Capture Duration
- Start Time
- End Time
- Packet Count
- Average Packet Rate
- Encapsulation Type
- Comments (if any)

Useful for quickly understanding a capture before analysis.

---

# Protocol Hierarchy

Navigate to:

```
Statistics

↓

Protocol Hierarchy
```

Displays:

- Every protocol found
- Packet count
- Percentage of packets
- Percentage of bytes

Example:

```
Ethernet

↓

IPv4

↓

TCP

↓

TLS

↓

HTTP
```

---

## Why It Matters

Protocol Hierarchy helps you answer:

- Which protocols dominate the capture?
- Is there unexpected traffic?
- Are there unnecessary protocols?
- Which application generated most traffic?

---

# Conversations

Navigate to:

```
Statistics

↓

Conversations
```

Displays communication between devices.

Information includes:

- Source
- Destination
- Port Numbers
- Packet Count
- Bytes
- Duration

Supported tabs:

- Ethernet
- IPv4
- IPv6
- TCP
- UDP

---

## Why It Matters

Useful for identifying:

- Top talkers
- Long-lived connections
- Large file transfers
- Suspicious communications

---

# Endpoints

Navigate to:

```
Statistics

↓

Endpoints
```

Displays every unique device in the capture.

Information includes:

- MAC Address
- IP Address
- Packets Sent
- Packets Received
- Total Bytes

---

## Why It Matters

Endpoints help identify:

- Active hosts
- Unknown devices
- High-traffic systems
- Potential attackers

---

# Packet Lengths

Navigate to:

```
Statistics

↓

Packet Lengths
```

Displays the distribution of packet sizes.

Typical packet sizes:

| Length | Common Use |
|---------|------------|
| 64 Bytes | ACK, SYN, ARP |
| 128–512 Bytes | DNS, Small Requests |
| 512–1500 Bytes | Web Traffic, File Transfers |

Large numbers of unusually small or large packets may indicate network issues or attacks.

---

# I/O Graphs

Navigate to:

```
Statistics

↓

I/O Graphs
```

Displays traffic over time.

Useful metrics:

- Packets per Second
- Bytes per Second
- Filtered Traffic

---

## Common Uses

- Detect traffic spikes
- Measure bandwidth usage
- Identify DDoS attacks
- Locate performance issues

Multiple graphs can be displayed simultaneously using different display filters.

Example:

```
Graph 1

tcp

Graph 2

dns

Graph 3

icmp
```

---

# Flow Graph

Navigate to:

```
Statistics

↓

Flow Graph
```

Displays packet exchanges between hosts in chronological order.

Example:

```
Client

↓

DNS Query

↓

DNS Response

↓

TCP SYN

↓

TCP SYN/ACK

↓

TCP ACK

↓

TLS

↓

HTTP GET

↓

HTTP Response
```

---

## Why It Matters

Flow Graph simplifies understanding complex communications without manually following packet numbers.

---

# Expert Information

Navigate to:

```
Analyze

↓

Expert Information
```

One of Wireshark's most valuable troubleshooting features.

Categories include:

- Errors
- Warnings
- Notes
- Chats

---

## Common Issues Detected

- Retransmissions
- Duplicate ACKs
- Out-of-Order Packets
- Malformed Packets
- TCP Resets
- Checksum Errors
- Protocol Violations

Expert Information helps identify problems quickly.

---

# Name Resolution

Navigate to:

```
View

↓

Name Resolution
```

Allows Wireshark to resolve:

- MAC Addresses → Vendor Names
- IP Addresses → Hostnames
- Port Numbers → Service Names

Examples:

Instead of:

```
142.250.183.110
```

You may see:

```
google.com
```

---

# GeoIP

After configuring the GeoLite2 databases:

```
Edit

↓

Preferences

↓

Name Resolution
```

Wireshark can display:

- Country
- City
- ASN (Autonomous System Number)

Useful for:

- Threat Hunting
- Malware Analysis
- Investigating External Connections

---

# Coloring Rules

Navigate to:

```
View

↓

Coloring Rules
```

Coloring Rules visually distinguish packet types.

Typical examples:

| Traffic | Color |
|----------|--------|
| TCP | Blue |
| DNS | Green |
| HTTP | Light Green |
| ICMP | Purple |
| Errors | Red |

You can create custom rules based on display filters.

Example:

```
tcp.analysis.retransmission
```

Highlighting retransmissions makes troubleshooting easier.

---

# Profiles

Profiles save customized Wireshark settings.

Navigate to:

```
Edit

↓

Configuration Profiles
```

A profile stores:

- Layout
- Filters
- Coloring Rules
- Columns
- Preferences

Example Profiles:

- Network Troubleshooting
- Malware Analysis
- HTB Labs
- Incident Response

Using separate profiles keeps your workspace organized.

---

# Find Packet

Navigate to:

```
Edit

↓

Find Packet
```

Search by:

- Packet Number
- String
- Hex Value
- Display Filter
- Protocol Field

Useful when analyzing large captures.

---

# Time Display Formats

Navigate to:

```
View

↓

Time Display Format
```

Available formats:

- Seconds Since Beginning
- Seconds Since Previous Packet
- UTC Date and Time
- Local Date and Time

Changing the time format can simplify performance analysis.

---

# Follow Stream

Available Options:

```
Follow

↓

TCP Stream

UDP Stream

HTTP Stream

TLS Stream
```

Following streams reconstructs entire conversations between hosts.

This is one of Wireshark's most powerful analysis features.

---

# Export Objects

Navigate to:

```
File

↓

Export Objects
```

Supported exports include:

- HTTP
- SMB
- TFTP
- DICOM

Useful for extracting:

- Documents
- Images
- Malware Samples
- Executables

---

# Export Packet Dissections

Navigate to:

```
File

↓

Export Packet Dissections
```

Export formats include:

- Plain Text
- CSV
- JSON
- XML

Useful for:

- Documentation
- Reporting
- Automation
- Further Analysis

---

# Cybersecurity Use Cases

## Blue Team

- Detect abnormal traffic
- Identify malware communication
- Analyze user activity
- Investigate security incidents

---

## Red Team

- Validate payload traffic
- Monitor exploit communication
- Verify C2 connections
- Troubleshoot attacks

---

## Digital Forensics

- Reconstruct timelines
- Recover transferred files
- Analyze attacker behavior
- Preserve packet evidence

---

# Typical Investigation Workflow

```
Open Capture

↓

Protocol Hierarchy

↓

Endpoints

↓

Conversations

↓

Apply Display Filters

↓

Flow Graph

↓

Follow Streams

↓

Expert Information

↓

Export Evidence

↓

Document Findings
```

---

# Best Practices

- Start with Protocol Hierarchy to understand the capture.
- Use Conversations and Endpoints to identify important hosts.
- Monitor I/O Graphs for traffic spikes.
- Review Expert Information early during troubleshooting.
- Create separate profiles for different analysis tasks.
- Export important evidence before modifying the capture.

---

# Common Mistakes

❌ Ignoring the Statistics menu and manually reviewing every packet.

❌ Focusing on packet count without considering byte volume.

❌ Forgetting to use Flow Graph for complex conversations.

❌ Leaving all analysis in the default profile.

❌ Assuming GeoIP always identifies the true physical location of an IP address.

---

# Quick Summary

- Wireshark provides powerful statistical tools for analyzing network captures.
- Protocol Hierarchy summarizes captured protocols.
- Conversations and Endpoints identify communicating hosts.
- I/O Graphs visualize traffic over time.
- Flow Graph reconstructs communication sequences.
- Expert Information highlights potential network issues.
- Profiles and Coloring Rules improve efficiency during repeated analysis.

---

# Key Takeaways

- Wireshark's analysis tools allow analysts to understand large packet captures quickly and efficiently.
- Combining statistical views with protocol analysis provides deeper insight than examining individual packets.
- Features such as Flow Graph, Conversations, Expert Information, and I/O Graphs are essential for network troubleshooting, malware analysis, threat hunting, incident response, and digital forensics.
- Mastering these tools significantly improves the speed and accuracy of packet analysis in both enterprise environments and cybersecurity investigations.
