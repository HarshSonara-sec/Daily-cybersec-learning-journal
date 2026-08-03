# Wireshark Protocol Analysis

> **Category:** Network Analysis
>
> **Difficulty:** Beginner → Intermediate
>
> **Prerequisites:**
>
> - Wireshark Fundamentals
> - Display Filters
> - Capture Filters
> - Basic OSI & TCP/IP Knowledge
>
> **Recommended Before:**
>
> - 01-Wireshark-Fundamentals.md
> - 02-Wireshark-Display-Filters.md
> - 03-Wireshark-Capture-Filters.md
>
> **Recommended After:**
>
> - 05-Wireshark-TCP-Analysis.md

---

# What is Protocol Analysis?

Protocol analysis is the process of examining captured network packets to understand **how devices communicate**.

Instead of simply looking at raw packets, we inspect each protocol layer to answer questions such as:

- Who sent the packet?
- Who received it?
- Which protocol is being used?
- Was the communication successful?
- Is anything abnormal or suspicious?

Protocol analysis is the foundation of:

- Network Troubleshooting
- Penetration Testing
- Threat Hunting
- Malware Analysis
- Incident Response
- Digital Forensics

---

# Understanding Packet Layers

Every packet is made up of multiple protocol layers.

Example:

```
Application Data
        │
HTTP / HTTPS / DNS
        │
TCP / UDP
        │
IPv4 / IPv6
        │
Ethernet II
        │
Physical Network
```

Each layer adds its own header before transmission.

This process is called **Encapsulation**.

---

# Packet Structure in Wireshark

Selecting a packet displays three panes:

## Packet List

Shows a summary of captured packets.

Typical columns:

- Packet Number
- Time
- Source
- Destination
- Protocol
- Length
- Info

---

## Packet Details

Displays every protocol layer contained within the packet.

Example:

```
Frame
Ethernet II
Internet Protocol Version 4
Transmission Control Protocol
Hypertext Transfer Protocol
```

Each section can be expanded for detailed information.

---

## Packet Bytes

Displays raw packet data in:

- Hexadecimal
- ASCII

Useful for:

- Payload inspection
- Malware analysis
- Binary analysis

---

# Ethernet II (Layer 2)

Ethernet is responsible for communication within a Local Area Network (LAN).

### Information Found

- Source MAC Address
- Destination MAC Address
- EtherType

Example:

```
Destination:
00:11:22:33:44:55

Source:
AA:BB:CC:DD:EE:FF

Type:
IPv4
```

### Common EtherTypes

| EtherType | Protocol |
|-----------|----------|
| 0x0800 | IPv4 |
| 0x0806 | ARP |
| 0x86DD | IPv6 |

---

# Address Resolution Protocol (ARP)

ARP maps an IPv4 address to a MAC address.

Without ARP, devices cannot communicate inside a LAN.

### Typical Process

```
Who has 192.168.1.1?

↓

192.168.1.1 is at
00:11:22:33:44:55
```

### Display Filter

```
arp
```

### Important Fields

- Sender MAC
- Sender IP
- Target MAC
- Target IP

---

# Internet Protocol Version 4 (IPv4)

IPv4 provides logical addressing and routing between networks.

### Important Fields

- Source IP
- Destination IP
- Time To Live (TTL)
- Protocol
- Header Length
- Total Length

Example:

```
Source:
192.168.1.10

Destination:
8.8.8.8

TTL:
64
```

### Display Filter

```
ip
```

---

# Internet Protocol Version 6 (IPv6)

IPv6 is the successor to IPv4.

Differences:

- 128-bit addresses
- Larger address space
- Simplified header
- Improved efficiency

Display Filter:

```
ipv6
```

---

# Transmission Control Protocol (TCP)

TCP is a connection-oriented transport protocol.

Provides:

- Reliable delivery
- Ordered packets
- Error checking
- Flow control

### Important Fields

- Source Port
- Destination Port
- Sequence Number
- Acknowledgment Number
- Window Size
- Flags

### Common Flags

| Flag | Purpose |
|------|----------|
| SYN | Start connection |
| ACK | Acknowledge |
| FIN | Close connection |
| RST | Reset connection |
| PSH | Push data |
| URG | Urgent data |

Display Filter:

```
tcp
```

---

# User Datagram Protocol (UDP)

UDP is connectionless.

Characteristics:

- Fast
- Lightweight
- No acknowledgments
- No retransmissions

Common Uses:

- DNS
- DHCP
- VoIP
- Streaming
- Gaming

Display Filter:

```
udp
```

---

# Internet Control Message Protocol (ICMP)

ICMP is used for diagnostics and error reporting.

Examples:

- Ping
- Destination Unreachable
- Time Exceeded

Display Filter:

```
icmp
```

Useful fields:

- Type
- Code
- Checksum

---

# Domain Name System (DNS)

DNS translates domain names into IP addresses.

Example:

```
google.com

↓

142.250.x.x
```

Display Filter:

```
dns
```

Important Fields:

- Transaction ID
- Query
- Response
- Record Type
- TTL

Common Record Types:

| Record | Purpose |
|---------|----------|
| A | IPv4 |
| AAAA | IPv6 |
| MX | Mail Server |
| CNAME | Alias |
| TXT | Text Record |
| NS | Name Server |

---

# Dynamic Host Configuration Protocol (DHCP)

DHCP automatically assigns IP addresses.

The DHCP process:

```
Discover

↓

Offer

↓

Request

↓

Acknowledgment (ACK)
```

Display Filter:

```
dhcp
```

Important Fields:

- Client MAC
- Offered IP
- Lease Time
- DHCP Message Type

---

# Hypertext Transfer Protocol (HTTP)

HTTP transfers web content in plaintext.

Common Methods:

- GET
- POST
- PUT
- DELETE

Common Status Codes:

| Code | Meaning |
|------|----------|
| 200 | OK |
| 301 | Redirect |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

Display Filter:

```
http
```

Useful Fields:

- Host
- URI
- User-Agent
- Cookie
- Response Code

---

# Transport Layer Security (TLS)

TLS encrypts application traffic.

HTTPS is simply:

```
HTTP
+
TLS
```

TLS protects:

- Credentials
- Banking
- Email
- API Communication

Display Filter:

```
tls
```

Useful Fields:

- Client Hello
- Server Hello
- Certificate
- Cipher Suite
- Server Name Indication (SNI)

---

# Following Protocol Flow

Example of visiting a website:

```
ARP
↓

DNS

↓

TCP Handshake

↓

TLS Handshake

↓

HTTP Request

↓

HTTP Response

↓

TCP Connection Close
```

Understanding this sequence makes packet analysis much easier.

---

# Protocol Hierarchy

Navigate to:

```
Statistics
→ Protocol Hierarchy
```

This shows:

- Which protocols appear
- Number of packets
- Percentage of traffic
- Bytes used by each protocol

Useful for quickly understanding a capture.

---

# Expert Information

Navigate to:

```
Analyze
→ Expert Information
```

Highlights:

- Errors
- Warnings
- Retransmissions
- Malformed packets
- Duplicate ACKs

Useful during troubleshooting and incident response.

---

# Cybersecurity Use Cases

## Blue Team

- Detect malware traffic
- Investigate suspicious DNS requests
- Analyze encrypted connections
- Verify authentication traffic

---

## Red Team

- Validate payload communication
- Troubleshoot reverse shells
- Observe exploit traffic
- Analyze C2 communications

---

## Network Engineers

- Troubleshoot routing
- Diagnose DNS failures
- Analyze TCP performance
- Verify DHCP operation

---

# Best Practices

- Read packets from the lowest protocol layer upward.
- Follow complete conversations instead of isolated packets.
- Correlate multiple protocols to understand the full communication.
- Use display filters to reduce noise.
- Learn the purpose of each protocol before memorizing every field.

---

# Common Mistakes

❌ Ignoring Layer 2 information.

❌ Looking only at packet summaries.

❌ Assuming encrypted TLS traffic can always be decrypted.

❌ Forgetting that DNS usually happens before web traffic.

❌ Analyzing packets individually instead of as a conversation.

---

# Quick Summary

- Protocol analysis explains how devices communicate across a network.
- Every packet consists of multiple protocol layers.
- Ethernet provides local delivery.
- ARP resolves MAC addresses.
- IP provides logical addressing.
- TCP offers reliable communication.
- UDP prioritizes speed over reliability.
- ICMP supports diagnostics.
- DNS resolves domain names.
- DHCP assigns IP addresses.
- HTTP transfers web content.
- TLS secures application traffic.

---

# Key Takeaways

- Understanding protocol interactions is more valuable than memorizing packet fields.
- Most network communications follow a predictable sequence (ARP → DNS → TCP → TLS → Application).
- Wireshark allows analysts to inspect each protocol layer independently, making it an essential tool for cybersecurity, network engineering, and digital forensics.
- Strong protocol analysis skills form the foundation for advanced topics such as TCP analysis, malware traffic investigation, Active Directory authentication, and incident response.
