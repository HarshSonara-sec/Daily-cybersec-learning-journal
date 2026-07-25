# IPv4 Header
**Source:** Jeremy's IT Lab CCNA – Day 10

**OSI Layer:** Layer 3 (Network Layer)

**Prerequisites:**
- OSI Model
- Ethernet Frames
- IPv4 Addressing Fundamentals

---

# Overview

The **Internet Protocol Version 4 (IPv4)** header is attached to every IPv4 packet and contains the information required for routers to forward packets across different networks.

Unlike an Ethernet frame header, which is only used within a local network, the IPv4 header allows packets to travel between multiple networks until they reach their destination.

Each router examines specific fields within the IPv4 header to determine where the packet should be forwarded next.

---

# Learning Objectives

After completing this topic, you should be able to:

- Explain the purpose of the IPv4 header.
- Identify the important IPv4 header fields.
- Understand fragmentation and reassembly.
- Explain how TTL prevents routing loops.
- Identify common Layer 4 protocol numbers.
- Understand how routers use IPv4 header information.

---

# 1. IPv4 Packet Encapsulation

As data travels down the OSI model, each layer adds its own header.

```
Application Data
        ↓
TCP / UDP Segment
        ↓
IPv4 Packet
        ↓
Ethernet Frame
        ↓
Bits transmitted over the network
```

The IPv4 header encapsulates the Layer 4 segment (TCP or UDP) to create an IP packet.

---

# 2. IPv4 Header Size

The IPv4 header has a **variable length**.

| Header Type | Size |
|-------------|------|
| Minimum | 20 Bytes |
| Maximum | 60 Bytes |

The extra space is used for optional fields that provide additional functionality.

---

# 3. IPv4 Header Fields

The IPv4 header contains several fields, each serving a specific purpose.

---

## Version

The **Version** field identifies the IP version being used.

For IPv4:

```
Version = 4
```

This allows networking devices to distinguish IPv4 packets from IPv6 packets.

---

## IHL (Internet Header Length)

**IHL** specifies the length of the IPv4 header.

- Measured in 4-byte words.
- Minimum value = 20 Bytes.
- Maximum value = 60 Bytes.

Most IPv4 packets use the minimum 20-byte header because optional fields are rarely required.

---

## DSCP (Differentiated Services Code Point)

DSCP is used to classify and prioritise network traffic.

It supports **Quality of Service (QoS)** by allowing important traffic to receive preferential treatment.

Examples:

- Voice over IP (VoIP)
- Video conferencing
- Live streaming

Higher-priority traffic experiences lower delay and reduced packet loss.

---

## ECN (Explicit Congestion Notification)

ECN allows routers experiencing congestion to notify the sender **without immediately dropping packets**.

Benefits include:

- Reduced packet loss
- Better network performance
- Improved handling of congestion

ECN works only when both sender and receiver support it.

---

## Total Length

The **Total Length** field specifies the complete size of the IPv4 packet.

It includes:

- IPv4 Header
- Payload (Data)

```
Total Length = Header + Data
```

---

# 4. Fragmentation

Different networks support different **Maximum Transmission Units (MTUs)**.

When a packet is larger than the outgoing interface's MTU, it may need to be divided into smaller pieces called **fragments**.

Standard Ethernet MTU:

```
1500 Bytes
```

Each fragment travels independently and is reassembled at the destination.

---

# 5. Identification Field

Every fragmented packet receives a unique **Identification** value.

Purpose:

- Groups all fragments belonging to the same original packet.
- Allows the destination device to correctly reassemble the packet.

All fragments from one packet share the same Identification number.

---

# 6. Flags Field

The **Flags** field controls fragmentation behaviour.

Important flags include:

### DF (Don't Fragment)

- Prevents fragmentation.
- If the packet exceeds the MTU, it is discarded.
- The sender receives an ICMP error indicating fragmentation was needed.

### MF (More Fragments)

- Indicates additional fragments follow.
- The final fragment has the MF bit cleared.

---

# 7. Fragment Offset

The **Fragment Offset** indicates the position of each fragment within the original packet.

This ensures fragments can be reassembled in the correct order, even if they arrive out of sequence.

---

# 8. Time To Live (TTL)

**TTL (Time To Live)** limits the number of routers a packet can traverse.

Purpose:

- Prevents packets from circulating endlessly because of routing loops.

Operation:

1. Sender assigns an initial TTL value (commonly 64, 128, or 255).
2. Every router decreases the TTL by 1.
3. When TTL reaches 0:
   - The router discards the packet.
   - An **ICMP Time Exceeded** message is sent back to the sender.

> **Note:** Despite its name, TTL represents **hop count**, not elapsed time.

---

# 9. Protocol Field

The **Protocol** field identifies the Layer 4 protocol carried within the IPv4 packet.

Common protocol numbers:

| Protocol | Number |
|-----------|-------:|
| ICMP (Internet Control Message Protocol) | 1 |
| TCP (Transmission Control Protocol) | 6 |
| UDP (User Datagram Protocol) | 17 |
| OSPF (Open Shortest Path First) | 89 |

This field enables the receiving device to pass the payload to the correct upper-layer protocol.

---

# 10. Header Checksum

The **Header Checksum** verifies the integrity of the IPv4 header during transmission.

Important points:

- Checks only the IPv4 header.
- Does **not** verify the payload.
- Recalculated by every router because fields such as TTL change at each hop.

If the checksum is invalid, the packet is discarded.

---

# 11. Source IP Address

Identifies the IPv4 address of the device that created the packet.

Example:

```
192.168.1.10
```

Routers use this address when sending replies or error messages.

---

# 12. Destination IP Address

Identifies the intended recipient of the packet.

Example:

```
8.8.8.8
```

Routers examine this field to determine the next hop using their routing tables.

---

# 13. IPv4 Options (Optional Field)

The IPv4 Options field is rarely used in modern networks.

Possible uses include:

- Security options
- Timestamp information
- Route recording
- Network diagnostics

Using options increases the header size beyond the standard 20 bytes.

---

# Practical Example

Suppose a PC sends a packet to a web server.

```
PC
 │
 ▼
Switch
 │
 ▼
Router
 │
 ▼
Internet
 │
 ▼
Web Server
```

As the packet travels:

- The Ethernet header changes at every hop.
- The IPv4 Source and Destination addresses remain the same.
- The TTL decreases by one at each router.
- The Header Checksum is recalculated by each router.

---

# Wireshark Observation

When inspecting an IPv4 packet in Wireshark, you will commonly see:

- Version
- Header Length (IHL)
- DSCP
- ECN
- Total Length
- Identification
- Flags
- Fragment Offset
- TTL
- Protocol
- Header Checksum
- Source Address
- Destination Address

Understanding these fields is essential for packet analysis and troubleshooting.

---

# Useful Commands

Although IPv4 headers are commonly examined using packet analysers such as **Wireshark**, the following Cisco IOS commands are useful for verifying Layer 3 connectivity:

Display IP interfaces:

```bash
show ip interface brief
```

Display routing information:

```bash
show ip route
```

Test connectivity:

```bash
ping <IP-address>
```

Trace the packet path:

```bash
traceroute <IP-address>
```

---

# CCNA Exam Tips

- The IPv4 header operates at **OSI Layer 3 (Network Layer)**.
- Minimum header size is **20 Bytes**.
- TTL prevents routing loops by limiting the number of hops.
- Routers decrement TTL and recalculate the Header Checksum at every hop.
- The Protocol field identifies the encapsulated Layer 4 protocol.
- Fragmentation occurs when packets exceed the network MTU.
- The DF flag prevents fragmentation, while the MF flag indicates more fragments follow.
- DSCP supports Quality of Service (QoS) by prioritising traffic.

---

# Key Terms

| Abbreviation | Full Form |
|--------------|-----------|
| IPv4 | Internet Protocol Version 4 |
| IHL | Internet Header Length |
| DSCP | Differentiated Services Code Point |
| ECN | Explicit Congestion Notification |
| QoS | Quality of Service |
| TTL | Time To Live |
| MTU | Maximum Transmission Unit |
| ICMP | Internet Control Message Protocol |
| TCP | Transmission Control Protocol |
| UDP | User Datagram Protocol |
| OSPF | Open Shortest Path First |

---

# Quick Revision

- IPv4 packets operate at **Layer 3**.
- Every packet contains an IPv4 header used for routing.
- Minimum header size is **20 Bytes**.
- IHL specifies the header length.
- DSCP prioritises important traffic, while ECN signals congestion.
- Identification, Flags, and Fragment Offset manage packet fragmentation.
- TTL prevents infinite routing loops.
- The Protocol field identifies the encapsulated Layer 4 protocol.
- The Header Checksum verifies only the IPv4 header.
- Source and Destination IP addresses remain unchanged throughout the packet's journey (unless modified by technologies such as NAT).
