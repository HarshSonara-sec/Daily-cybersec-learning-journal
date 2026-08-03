# Wireshark Fundamentals

> **Category:** Network Analysis
>
> **Difficulty:** Beginner
>
> **Prerequisites:**
>
> - Basic Networking (OSI Model, TCP/IP)
> - IPv4 Addressing
> - Ethernet
> - DNS Basics
>
> **Recommended Before:**
>
> - CCNA Networking Fundamentals
>
> **Recommended After:**
>
> - Display Filters
> - Capture Filters
> - Protocol Analysis

---

# What is Wireshark?

Wireshark is a **free and open-source network protocol analyzer** used to capture, inspect, and analyze packets traveling across a network.

It allows security professionals, network engineers, incident responders, and penetration testers to observe network traffic in real time or analyze previously captured traffic from packet capture (`.pcap`/`.pcapng`) files.

Think of Wireshark as a microscope for network communications.

---

# Why Learn Wireshark?

Wireshark is one of the most important tools in cybersecurity because it helps you:

- Troubleshoot network connectivity issues
- Analyze application traffic
- Understand how protocols work
- Detect suspicious or malicious network activity
- Investigate malware communications
- Validate firewall and router configurations
- Analyze authentication traffic
- Capture evidence during incident response

---

# Common Cybersecurity Use Cases

### Blue Team

- Incident Response
- Malware Analysis
- Threat Hunting
- Network Monitoring
- Detecting Data Exfiltration

### Red Team

- Validate attack traffic
- Troubleshoot payloads
- Observe exploitation attempts
- Verify reverse shells
- Analyze network communications

### Network Engineering

- Diagnose latency
- Troubleshoot DNS
- Verify routing
- Analyze TCP issues
- Inspect VLAN traffic

---

# Installing Wireshark

## Linux (Kali)

```bash
sudo apt update
sudo apt install wireshark
```

Verify installation:

```bash
wireshark --version
```

---

# Wireshark Interface Overview

The Wireshark interface is divided into several important sections.

## 1. Menu Bar

Contains:

- File
- Edit
- View
- Capture
- Analyze
- Statistics
- Telephony
- Wireless
- Tools
- Help

---

## 2. Toolbar

Provides quick access to:

- Start Capture
- Stop Capture
- Restart Capture
- Open Capture
- Save Capture
- Find Packet

---

## 3. Interface List

Displays all available capture interfaces.

Common examples:

- eth0
- wlan0
- lo (Loopback)
- tun0 (VPN)
- Docker Interfaces
- Virtual Machine Interfaces

Always choose the interface carrying the traffic you want to analyze.

---

## 4. Packet List Pane

Displays captured packets.

Each row represents a single packet.

Common columns include:

- No.
- Time
- Source
- Destination
- Protocol
- Length
- Info

This pane provides a quick summary of network traffic.

---

## 5. Packet Details Pane

Displays protocol layers for the selected packet.

Typical layers include:

```
Frame
Ethernet II
Internet Protocol (IPv4 / IPv6)
TCP / UDP
Application Protocol
```

Expand each section to inspect individual fields and values.

---

## 6. Packet Bytes Pane

Displays the raw packet data in hexadecimal and ASCII.

Useful for:

- Binary analysis
- Payload inspection
- Malware analysis
- Reverse engineering

---

## 7. Status Bar

Displays useful capture information including:

- Number of packets captured
- Number of displayed packets
- Current profile
- File information

---

# Starting a Capture

1. Open Wireshark.
2. Select the correct network interface.
3. Double-click the interface or click the blue shark fin icon.
4. Generate network traffic (browse a website, ping a host, etc.).
5. Observe packets appearing in real time.

---

# Stopping a Capture

Click the red square **Stop** button on the toolbar.

Stopping a capture prevents additional packets from being recorded but does not delete captured data.

---

# Saving a Capture

Save captures for future analysis.

Supported formats:

- `.pcapng` (Recommended)
- `.pcap`

Menu:

```
File → Save As
```

---

# Opening Existing Captures

Menu:

```
File → Open
```

Supported formats include:

- .pcap
- .pcapng
- .cap

Analyzing existing captures is common during:

- Capture the Flag (CTF)
- Hack The Box
- Incident Response
- Malware Analysis

---

# Understanding a Packet

Each captured packet contains multiple protocol layers.

Example:

```
Application Data
        ↓
TCP
        ↓
IP
        ↓
Ethernet
        ↓
Physical Network
```

Each layer adds its own header before transmission. This process is known as **encapsulation**.

---

# Encapsulation

When data is sent across a network:

1. Application creates data.
2. TCP/UDP adds a transport header.
3. IP adds a network header.
4. Ethernet adds a frame header.
5. Data is transmitted over the physical medium.

At the receiving device, these headers are removed in reverse order (**decapsulation**).

---

# Packet vs Frame

| Packet | Frame |
|---------|--------|
| Layer 3 (Network Layer) | Layer 2 (Data Link Layer) |
| Contains IP information | Contains MAC information |
| Routed across networks | Delivered within a local network |
| Uses IP addresses | Uses MAC addresses |

A frame encapsulates a packet for transmission over the local network.

---

# Capture Workflow

```
Choose Interface
        ↓
Start Capture
        ↓
Generate Traffic
        ↓
Stop Capture
        ↓
Apply Display Filters
        ↓
Inspect Protocol Layers
        ↓
Analyze Conversations
        ↓
Save Capture
```

---

# Best Practices

- Capture only the traffic you need.
- Save captures before closing Wireshark.
- Use display filters instead of scrolling manually.
- Name capture files descriptively.
- Keep important packet captures for future reference.
- Learn protocol layers before diving into advanced analysis.

---

# Common Mistakes

❌ Capturing on the wrong interface.

❌ Forgetting to stop the capture, resulting in excessively large files.

❌ Confusing capture filters with display filters.

❌ Ignoring protocol layers and focusing only on the packet summary.

❌ Forgetting to save valuable captures.

---

# Quick Summary

- Wireshark is a network protocol analyzer.
- Packets are captured from a selected network interface.
- The interface consists of Packet List, Packet Details, and Packet Bytes panes.
- Packets are organized into protocol layers.
- Data is encapsulated before transmission and decapsulated at the destination.
- Packet captures can be saved as `.pcap` or `.pcapng` files for later analysis.

---

# Key Takeaways

- Wireshark provides deep visibility into network communications.
- Understanding the interface is the foundation for effective packet analysis.
- Packet analysis relies on interpreting protocol layers rather than memorizing every field.
- Mastering Wireshark is an essential skill for network troubleshooting, penetration testing, digital forensics, and incident response.
