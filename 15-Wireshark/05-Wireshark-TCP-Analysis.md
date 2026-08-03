# Wireshark TCP Analysis

> **Category:** Network Analysis
>
> **Difficulty:** Intermediate
>
> **Prerequisites:**
>
> - Wireshark Fundamentals
> - Display Filters
> - Protocol Analysis
> - Basic TCP/IP Knowledge
>
> **Recommended Before:**
>
> - 01-Wireshark-Fundamentals.md
> - 02-Wireshark-Display-Filters.md
> - 03-Wireshark-Capture-Filters.md
> - 04-Wireshark-Protocol-Analysis.md
>
> **Recommended After:**
>
> - 06-Wireshark-DNS-Analysis.md

---

# What is TCP?

**Transmission Control Protocol (TCP)** is a **connection-oriented** transport layer protocol that provides reliable communication between devices.

Unlike UDP, TCP guarantees:

- Reliable delivery
- Ordered delivery
- Error detection
- Error recovery
- Flow control
- Congestion control

Most modern applications rely on TCP because lost or corrupted data is automatically retransmitted.

---

# Why Analyze TCP?

TCP analysis helps identify:

- Slow network performance
- Packet loss
- Retransmissions
- Connection failures
- Firewall issues
- Server responsiveness
- Application delays

Understanding TCP is one of the most valuable networking and cybersecurity skills.

---

# The TCP Three-Way Handshake

Before any data is exchanged, TCP establishes a connection using a **Three-Way Handshake**.

```
Client                    Server

SYN ---------------------->

<---------------------- SYN, ACK

ACK ---------------------->

Connection Established
```

---

## Step 1 — SYN

The client sends a **SYN (Synchronize)** packet.

Purpose:

- Start a TCP session
- Synchronize sequence numbers

Typical Flags:

```
SYN
```

---

## Step 2 — SYN/ACK

The server replies with:

```
SYN
ACK
```

Purpose:

- Accept connection
- Send its own sequence number

---

## Step 3 — ACK

The client sends:

```
ACK
```

The TCP session is now established.

Application data can begin flowing.

---

# TCP Connection Termination

A normal TCP connection closes using a **Four-Way Handshake**.

```
FIN →

← ACK

← FIN

ACK →
```

This allows both sides to finish transmitting data before disconnecting.

---

# TCP Header Fields

Important fields visible in Wireshark:

| Field | Purpose |
|--------|---------|
| Source Port | Sending application |
| Destination Port | Receiving application |
| Sequence Number | Position of transmitted bytes |
| Acknowledgment Number | Next expected byte |
| Flags | TCP control information |
| Window Size | Flow control |
| Checksum | Error detection |
| Options | Additional TCP features |

---

# TCP Flags

| Flag | Meaning |
|------|----------|
| SYN | Start a connection |
| ACK | Acknowledge received data |
| FIN | Gracefully close a connection |
| RST | Immediately terminate a connection |
| PSH | Deliver buffered data immediately |
| URG | Urgent data present |

Multiple flags may appear in a single packet.

Example:

```
SYN, ACK
```

---

# Sequence Numbers

Every byte transmitted in a TCP connection is assigned a sequence number.

Purpose:

- Maintain correct packet order
- Detect missing packets
- Support retransmissions

Example:

```
Client

Seq = 1000
Length = 500

Next Sequence

1500
```

---

# Acknowledgment Numbers

The acknowledgment number tells the sender:

> "I have successfully received everything up to this point."

Example:

```
Client

Seq = 1000

↓

Server

ACK = 1500
```

Meaning:

"I successfully received bytes 1000–1499."

---

# Window Size

Window Size controls how much data can be transmitted before waiting for an acknowledgment.

Small Window

```
More ACKs
↓

Slower Throughput
```

Large Window

```
Fewer ACKs
↓

Higher Performance
```

---

# TCP Flow Control

Flow control prevents a fast sender from overwhelming a slow receiver.

The receiver advertises its available buffer space using the Window Size field.

---

# TCP Retransmissions

If a sender does not receive an acknowledgment within a certain time, it retransmits the packet.

Display Filter:

```
tcp.analysis.retransmission
```

Common Causes:

- Packet loss
- Congestion
- Poor Wi-Fi
- Network failures
- Firewall issues

Frequent retransmissions usually indicate network problems.

---

# Duplicate ACK

Display Filter:

```
tcp.analysis.duplicate_ack
```

Duplicate ACKs indicate:

- Missing packets
- Out-of-order packets
- Possible congestion

A small number may be normal.

Large numbers often suggest network issues.

---

# Out-of-Order Packets

Display Filter:

```
tcp.analysis.out_of_order
```

Possible Causes:

- Multiple network paths
- Congestion
- Packet reordering
- High-speed networks

---

# Lost Segments

Display Filter:

```
tcp.analysis.lost_segment
```

Indicates Wireshark detected missing TCP segments during analysis.

---

# TCP Reset (RST)

Display Filter:

```
tcp.flags.reset == 1
```

RST immediately terminates a TCP connection.

Possible Reasons:

- Closed port
- Firewall rejection
- Application crash
- Invalid connection

Unlike FIN, RST does **not** gracefully close the session.

---

# TCP Keep Alive

Keep Alive packets ensure an idle connection is still active.

Useful for:

- Long SSH sessions
- VPN connections
- Database connections

---

# Following a TCP Stream

One of Wireshark's most useful features.

Steps:

```
Right-click Packet

↓

Follow

↓

TCP Stream
```

This reconstructs the entire TCP conversation.

Useful for:

- Reading HTTP requests
- Debugging applications
- Malware analysis
- Incident response

---

# TCP Stream Window

The TCP Stream window displays:

- Client requests
- Server responses
- Conversation timeline

This provides a much clearer view than inspecting individual packets.

---

# TCP Conversation Example

Opening a website typically follows this sequence:

```
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

TLS Handshake

↓

HTTP GET

↓

HTTP Response

↓

TCP FIN

↓

Connection Closed
```

---

# Useful Display Filters

All TCP packets

```
tcp
```

TCP Port 80

```
tcp.port == 80
```

TCP Port 443

```
tcp.port == 443
```

SYN Packets

```
tcp.flags.syn == 1
```

SYN packets only (excluding SYN/ACK)

```
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

ACK Packets

```
tcp.flags.ack == 1
```

FIN Packets

```
tcp.flags.fin == 1
```

RST Packets

```
tcp.flags.reset == 1
```

Retransmissions

```
tcp.analysis.retransmission
```

Duplicate ACKs

```
tcp.analysis.duplicate_ack
```

Out-of-Order Packets

```
tcp.analysis.out_of_order
```

Lost Segments

```
tcp.analysis.lost_segment
```

---

# Troubleshooting Workflow

```
Capture Traffic

↓

Apply Display Filters

↓

Locate TCP Handshake

↓

Inspect Sequence Numbers

↓

Verify ACKs

↓

Look for Retransmissions

↓

Check Window Size

↓

Follow TCP Stream

↓

Identify Root Cause
```

---

# Cybersecurity Use Cases

## Blue Team

- Detect failed connections
- Investigate malware communication
- Identify network bottlenecks
- Analyze suspicious sessions

---

## Red Team

- Troubleshoot reverse shells
- Validate exploit traffic
- Confirm successful payload delivery
- Observe encrypted sessions

---

## Incident Response

- Reconstruct attacker communications
- Verify data transfers
- Identify interrupted sessions
- Analyze suspicious outbound traffic

---

# Best Practices

- Always verify the TCP handshake before analyzing application traffic.
- Use **Follow TCP Stream** to understand conversations.
- Investigate retransmissions before assuming an application issue.
- Correlate TCP analysis with DNS and TLS traffic.
- Look at the entire conversation, not isolated packets.

---

# Common Mistakes

❌ Confusing Sequence Numbers with packet numbers.

❌ Assuming every retransmission indicates an attack.

❌ Ignoring Window Size during performance troubleshooting.

❌ Misinterpreting RST packets as malicious activity without additional context.

❌ Forgetting that application problems often originate from TCP issues.

---

# Quick Summary

- TCP provides reliable, connection-oriented communication.
- Every connection begins with a Three-Way Handshake.
- Sequence Numbers and ACKs ensure reliable data transfer.
- Window Size controls flow between sender and receiver.
- Retransmissions, Duplicate ACKs, and Lost Segments help diagnose network problems.
- **Follow TCP Stream** reconstructs an entire conversation and is one of Wireshark's most powerful analysis features.

---

# Key Takeaways

- TCP analysis is essential for understanding network performance and troubleshooting connectivity issues.
- The Three-Way Handshake, Sequence Numbers, and ACKs form the backbone of reliable communication.
- Wireshark's TCP analysis features allow analysts to detect packet loss, latency, and abnormal behavior quickly.
- Strong TCP analysis skills are critical for penetration testing, malware analysis, incident response, digital forensics, and enterprise network troubleshooting.
