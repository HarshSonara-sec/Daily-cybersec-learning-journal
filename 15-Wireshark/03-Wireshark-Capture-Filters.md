# Wireshark Capture Filters

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
> - 02-Wireshark-Display-Filters.md
>
> **Recommended After:**
>
> - 04-Wireshark-Protocol-Analysis.md

---

# What are Capture Filters?

Capture filters determine **which packets Wireshark records during a live capture**.

Unlike display filters, capture filters work **before packets are captured**. Any packet that does not match the capture filter is **never recorded**.

This makes capture filters useful for reducing unnecessary traffic, improving performance, and creating smaller capture files.

---

# Display Filters vs Capture Filters

| Feature | Display Filter | Capture Filter |
|----------|----------------|----------------|
| Applied | After Capture | Before Capture |
| Removes Packets | ❌ No | ✅ Yes (not captured) |
| Syntax | Wireshark Display Filter Language | Berkeley Packet Filter (BPF) |
| Performance | No impact on capture | Improves capture performance |
| Flexibility | Very High | Moderate |

**Rule of Thumb:**

- **Capture Filter = What gets recorded**
- **Display Filter = What gets displayed**

---

# Berkeley Packet Filter (BPF)

Wireshark capture filters use **Berkeley Packet Filter (BPF)** syntax.

BPF is also used by:

- tcpdump
- dumpcap
- libpcap
- tshark

Learning BPF makes it easier to use multiple packet capture tools.

---

# Capture Filter Syntax

General format:

```
keyword value
```

Examples:

```
host 192.168.1.10
```

```
port 80
```

```
tcp
```

Unlike display filters, capture filters **do not use `==`**.

---

# Common Keywords

| Keyword | Description |
|----------|-------------|
| host | Match a specific host |
| src | Source address |
| dst | Destination address |
| port | TCP or UDP port |
| portrange | Port range |
| net | Network/Subnet |
| tcp | TCP traffic |
| udp | UDP traffic |
| icmp | ICMP traffic |
| arp | ARP traffic |
| ether | MAC address |
| broadcast | Broadcast traffic |
| multicast | Multicast traffic |

---

# Capturing by Host

Capture traffic to or from a specific host:

```
host 192.168.1.100
```

---

## Source Host

```
src host 192.168.1.100
```

Only captures packets sent **from** the host.

---

## Destination Host

```
dst host 192.168.1.100
```

Only captures packets sent **to** the host.

---

# Capturing by Network

Capture an entire subnet:

```
net 192.168.1.0/24
```

Useful when monitoring all devices within a LAN.

---

# Capturing by Port

Capture HTTP traffic:

```
port 80
```

Capture HTTPS traffic:

```
port 443
```

Capture DNS traffic:

```
port 53
```

Capture SSH traffic:

```
port 22
```

---

# Source and Destination Ports

Source port:

```
src port 443
```

Destination port:

```
dst port 443
```

---

# Port Range

Capture multiple ports:

```
portrange 20-25
```

Useful for FTP, SMTP, SSH, and related services.

---

# Capture by Protocol

TCP:

```
tcp
```

UDP:

```
udp
```

ICMP:

```
icmp
```

ARP:

```
arp
```

IPv6:

```
ip6
```

---

# Capture by MAC Address

Specific Ethernet device:

```
ether host 00:11:22:33:44:55
```

Source MAC:

```
ether src 00:11:22:33:44:55
```

Destination MAC:

```
ether dst 00:11:22:33:44:55
```

Useful when troubleshooting switching or Layer 2 issues.

---

# Broadcast Traffic

Capture only broadcasts:

```
broadcast
```

Examples include:

- ARP Requests
- DHCP Discover
- NetBIOS Broadcasts

---

# Multicast Traffic

```
multicast
```

Useful when analyzing multicast applications such as streaming or routing protocols.

---

# Combining Filters

Use logical operators to build more specific filters.

## AND

Capture HTTP traffic from a host:

```
host 192.168.1.100 and port 80
```

---

## OR

Capture DNS or HTTPS:

```
port 53 or port 443
```

---

## NOT

Exclude SSH:

```
not port 22
```

---

## Complex Example

```
host 192.168.1.100 and tcp and not port 22
```

This captures:

- TCP traffic
- To or from 192.168.1.100
- Excluding SSH

---

# Common Capture Filter Examples

Capture all web traffic:

```
port 80 or port 443
```

Capture DNS:

```
port 53
```

Capture ICMP:

```
icmp
```

Capture local subnet:

```
net 192.168.1.0/24
```

Capture traffic from one device:

```
host 192.168.1.25
```

Capture SSH only:

```
tcp port 22
```

Capture FTP:

```
port 20 or port 21
```

Capture DHCP:

```
port 67 or port 68
```

Capture SMTP:

```
port 25
```

Capture RDP:

```
port 3389
```

---

# Applying a Capture Filter

1. Open Wireshark.
2. Select a network interface.
3. Enter the capture filter in the **Capture Filter** field.
4. Start the capture.
5. Only matching packets will be recorded.

---

# Advantages of Capture Filters

- Smaller capture files
- Reduced CPU and memory usage
- Easier packet analysis
- Faster searches
- Better performance on busy networks

---

# Limitations

Once packets are excluded by a capture filter, **they cannot be recovered**.

If you're unsure what traffic you'll need, it's often better to capture everything and use display filters afterward.

---

# Cybersecurity Use Cases

### Blue Team

- Capture only DNS traffic during malware investigations.
- Monitor authentication traffic.
- Reduce storage requirements on monitoring systems.

### Red Team

- Capture reverse shell traffic.
- Analyze exploit communication.
- Monitor C2 (Command and Control) traffic.

### Network Engineering

- Capture routing protocol traffic.
- Troubleshoot DHCP.
- Monitor VoIP traffic.
- Investigate network latency.

---

# Best Practices

- Keep filters simple whenever possible.
- Test filters before long captures.
- Use capture filters on busy production networks.
- Save complex filters for reuse.
- Capture broadly if forensic completeness is required.

---

# Common Mistakes

❌ Using display filter syntax (`==`) in capture filters.

❌ Forgetting that excluded packets are permanently lost.

❌ Capturing on the wrong interface.

❌ Applying filters that are too restrictive.

❌ Assuming capture filters can be changed after recording starts.

---

# Quick Summary

- Capture filters determine **what Wireshark records**.
- They use **Berkeley Packet Filter (BPF)** syntax.
- Capture filters improve performance by reducing unnecessary traffic.
- They are ideal for live captures on busy networks.
- Excluded packets are never saved and cannot be recovered later.

---

# Key Takeaways

- Capture filters should be used when you know exactly what traffic you need.
- Display filters are better for post-capture analysis.
- Understanding BPF syntax is valuable because it is shared across tools like **tcpdump**, **dumpcap**, and **TShark**.
- Mastering capture filters helps security professionals collect focused, efficient, and relevant packet captures.
