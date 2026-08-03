# Wireshark Display Filters

> **Category:** Network Analysis
>
> **Difficulty:** Beginner → Intermediate
>
> **Prerequisites:**
>
> - Wireshark Fundamentals
> - Basic Networking Knowledge
>
> **Recommended Before:**
>
> - 01-Wireshark-Fundamentals.md
>
> **Recommended After:**
>
> - 03-Wireshark-Capture-Filters.md

---

# What are Display Filters?

Display filters allow you to **show only the packets you are interested in** without modifying the original packet capture.

Unlike capture filters, display filters work **after packets have already been captured**.

Think of them as a search tool that helps you quickly locate relevant traffic in large packet captures.

---

# Why are Display Filters Important?

Large packet captures can contain thousands or even millions of packets.

Display filters help you:

- Find specific hosts
- Analyze protocols
- Troubleshoot connectivity
- Investigate suspicious traffic
- Reduce analysis time
- Focus on relevant packets

Display filters are one of the most powerful features of Wireshark and are used daily by security analysts and network engineers.

---

# Display Filter Bar

The filter bar is located at the top of the Wireshark window.

```
Display Filter
──────────────────────────────────────
dns
```

### Filter Colors

| Color | Meaning |
|--------|---------|
| Green | Valid filter |
| Red | Invalid filter |
| Yellow | Deprecated or incomplete filter |

Always verify that the filter bar turns **green** before applying a filter.

---

# Display Filter Syntax

Display filters follow this general format:

```
field operator value
```

Example:

```
ip.addr == 192.168.1.10
```

---

# Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal |
| `!=` | Not Equal |
| `>` | Greater Than |
| `<` | Less Than |
| `>=` | Greater Than or Equal |
| `<=` | Less Than or Equal |

Example:

```
tcp.port == 443
```

---

# Logical Operators

| Operator | Purpose |
|----------|----------|
| `and` | Both conditions must be true |
| `or` | Either condition can be true |
| `not` | Negates a condition |

Example:

```
dns and ip.addr == 8.8.8.8
```

Example:

```
http or tls
```

Example:

```
not arp
```

---

# Frequently Used Display Filters

## DNS

```
dns
```

Shows all DNS traffic.

---

## TCP

```
tcp
```

Displays all TCP packets.

---

## UDP

```
udp
```

Displays all UDP packets.

---

## HTTP

```
http
```

Shows unencrypted HTTP traffic.

---

## HTTPS / TLS

```
tls
```

Shows TLS-encrypted traffic.

---

## ICMP

```
icmp
```

Useful for analyzing ping requests and replies.

---

## ARP

```
arp
```

Displays Address Resolution Protocol traffic.

---

## DHCP

```
dhcp
```

Shows DHCP requests and responses.

---

## IPv4

```
ip
```

Displays IPv4 traffic.

---

## IPv6

```
ipv6
```

Displays IPv6 traffic.

---

# Filtering by IP Address

## Specific Host

```
ip.addr == 192.168.1.10
```

Displays packets where the host is either the source or destination.

---

## Source Address

```
ip.src == 192.168.1.10
```

Displays packets sent from the specified host.

---

## Destination Address

```
ip.dst == 192.168.1.10
```

Displays packets sent to the specified host.

---

# Filtering by Port

## TCP Port

```
tcp.port == 80
```

Displays packets using TCP port 80.

---

## Source Port

```
tcp.srcport == 443
```

---

## Destination Port

```
tcp.dstport == 443
```

---

## UDP Port

```
udp.port == 53
```

Displays DNS traffic over UDP.

---

# Filtering by Protocol

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

```
ssh
```

```
ftp
```

```
smtp
```

---

# Multiple Conditions

Example:

```
tcp and ip.addr == 192.168.1.10
```

Displays only TCP traffic involving the specified host.

---

Example:

```
http and tcp.port == 80
```

---

Example:

```
dns or icmp
```

---

# Excluding Traffic

Exclude ARP traffic:

```
not arp
```

Exclude DNS traffic:

```
not dns
```

Exclude one host:

```
ip.addr != 192.168.1.10
```

---

# String Matching

Contains:

```
http contains "login"
```

Contains:

```
frame contains "password"
```

These filters are useful when searching for keywords within packet payloads.

---

# Packet Length

Display packets larger than 1000 bytes:

```
frame.len > 1000
```

Small packets:

```
frame.len < 100
```

---

# TCP Analysis Filters

Retransmissions:

```
tcp.analysis.retransmission
```

Duplicate ACKs:

```
tcp.analysis.duplicate_ack
```

Lost Segments:

```
tcp.analysis.lost_segment
```

Out-of-order packets:

```
tcp.analysis.out_of_order
```

These filters are extremely useful for troubleshooting slow or unreliable network connections.

---

# HTTP Examples

GET Requests:

```
http.request.method == "GET"
```

POST Requests:

```
http.request.method == "POST"
```

Status Code 404:

```
http.response.code == 404
```

Status Code 200:

```
http.response.code == 200
```

---

# DNS Examples

Standard Queries:

```
dns.flags.response == 0
```

Responses:

```
dns.flags.response == 1
```

NXDOMAIN Responses:

```
dns.flags.rcode == 3
```

---

# TLS Examples

TLS Handshake:

```
tls.handshake
```

TLS Certificates:

```
tls.handshake.certificate
```

---

# Conversations

After filtering, use:

```
Statistics
→ Conversations
```

to identify which hosts are communicating.

---

# Follow TCP Stream

Right-click a TCP packet.

```
Follow
→ TCP Stream
```

This reconstructs an entire TCP conversation between two hosts.

---

# Coloring Rules

Coloring rules visually highlight different traffic types.

Examples:

| Protocol | Typical Color |
|----------|---------------|
| TCP | Blue |
| DNS | Light Green |
| HTTP | Green |
| Errors | Red |
| ICMP | Purple |

Custom coloring rules can be created from:

```
View
→ Coloring Rules
```

---

# Best Practices

- Filter before analyzing.
- Combine multiple filters when investigating incidents.
- Save frequently used filters.
- Learn protocol names instead of memorizing port numbers.
- Verify filters are valid before applying them.

---

# Common Mistakes

❌ Confusing display filters with capture filters.

❌ Using a single equals sign (`=`) instead of `==`.

❌ Filtering only by port when protocol filters are more appropriate.

❌ Forgetting that display filters do **not** reduce the capture size.

❌ Ignoring packet details after filtering.

---

# Quick Summary

- Display filters work **after** packet capture.
- They do **not** modify or remove packets.
- Multiple conditions can be combined using logical operators.
- Display filters help isolate protocols, hosts, ports, and application traffic.
- Mastering display filters dramatically improves packet analysis efficiency.

---

# Key Takeaways

- Display filters are the primary method for analyzing packet captures.
- They allow analysts to quickly locate relevant traffic in large captures.
- Combining protocol, IP address, and port filters provides powerful analysis capabilities.
- Understanding display filters is essential for penetration testing, threat hunting, incident response, and network troubleshooting.
