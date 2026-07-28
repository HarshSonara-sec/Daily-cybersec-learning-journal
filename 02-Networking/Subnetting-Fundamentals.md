# ============================================================
# CCNA Notes
# Topic: Subnetting Fundamentals
# Date: 2026-07-28
# Last Updated: 2026-07-28
# Source: Jeremy's IT Lab CCNA - Day 15
# ============================================================

# Subnetting Fundamentals

## Overview

Subnetting is the process of dividing a larger IPv4 network into smaller, more manageable subnetworks. It improves IP address utilisation, reduces broadcast traffic, simplifies network management, and enhances security through network segmentation.

---

## Learning Objectives

By the end of this topic, you should be able to:

- Understand CIDR notation.
- Explain the purpose of subnetting.
- Identify network and host portions of an IPv4 address.
- Calculate the number of subnets and usable hosts.
- Perform subnetting for Class A, B, and C networks.

---

## Prerequisites

- IPv4 Addressing Fundamentals
- Binary Number System
- IPv4 Address Classes
- Subnet Masks

---

## Topics Covered

- CIDR (Classless Inter-Domain Routing)
- Basics of Subnetting
- IPv4 Address Classes
- Dotted Decimal vs CIDR Notation
- Network and Host Bits
- Class C Subnetting (/25–/32)
- Class B Subnetting
- Class A Subnetting
- Host & Subnet Calculations
- Multiple Subnetting Practice Questions

---

# CIDR (Classless Inter-Domain Routing)

CIDR replaces traditional classful addressing by allowing flexible prefix lengths instead of relying solely on default Class A, B, and C subnet masks.

### Example

| CIDR | Subnet Mask |
|------|-------------|
| /24 | 255.255.255.0 |
| /25 | 255.255.255.128 |
| /26 | 255.255.255.192 |
| /27 | 255.255.255.224 |

---

# Why Subnet?

Subnetting provides several advantages:

- Efficient use of IPv4 addresses.
- Smaller broadcast domains.
- Improved network performance.
- Easier network management.
- Better security through network segmentation.

---

# Dotted Decimal vs CIDR Notation

Both represent the same subnet mask in different formats.

| Dotted Decimal | CIDR |
|----------------|------|
| 255.255.255.0 | /24 |
| 255.255.255.128 | /25 |
| 255.255.255.192 | /26 |
| 255.255.255.224 | /27 |

---

# IPv4 Address Classes

| Class | First Octet | Default Prefix |
|-------|-------------|----------------|
| A | 1 – 126 | /8 |
| B | 128 – 191 | /16 |
| C | 192 – 223 | /24 |

> **Note:** Although modern networks use CIDR, understanding IPv4 classes remains important for CCNA and networking fundamentals.

---

# Subnetting Process

For every subnet, determine:

1. Network Address
2. First Usable Host
3. Last Usable Host
4. Broadcast Address
5. Number of Usable Hosts

General steps:

1. Identify the prefix length.
2. Determine the number of network and host bits.
3. Calculate the subnet increment.
4. Find the subnet range.
5. Identify network, usable host, and broadcast addresses.

---

# Host & Subnet Calculations

### Number of Usable Hosts

```
2^(Host Bits) - 2
```

### Number of Subnets

```
2^(Borrowed Bits)
```

---

# Common Class C Prefixes

| Prefix | Usable Hosts | Increment |
|---------|-------------:|----------:|
| /25 | 126 | 128 |
| /26 | 62 | 64 |
| /27 | 30 | 32 |
| /28 | 14 | 16 |
| /29 | 6 | 8 |
| /30 | 2 | 4 |
| /31 | Point-to-Point | 2 |
| /32 | Single Host | N/A |

---

# Class B Subnetting

- Default prefix: **/16**
- Subnetting commonly begins in the **third octet**.
- Frequently used in medium-sized enterprise networks.

---

# Class A Subnetting

- Default prefix: **/8**
- Subnetting commonly begins in the **second octet**.
- Suitable for very large networks requiring many subnets.

---

# Common Mistakes

- Forgetting to subtract **2** when calculating usable hosts.
- Confusing the network and broadcast addresses.
- Using the wrong subnet increment.
- Miscounting borrowed or host bits.

---

# CCNA Exam Tips

- Memorise subnet sizes from **/24 to /30**.
- Learn subnet increments rather than relying on binary every time.
- Practise subnetting without using a calculator.
- Always verify the network and broadcast addresses before selecting the usable host range.

---

# Cybersecurity Relevance

Subnetting is fundamental for:

- VLAN Design
- Network Segmentation
- Access Control Lists (ACLs)
- Firewall Configuration
- Internal Penetration Testing
- Enterprise Network Design

---

# Key Takeaways

- CIDR provides flexible network addressing.
- Subnetting divides larger networks into smaller subnetworks.
- Every subnet contains a Network Address, Usable Host Range, and Broadcast Address.
- Understanding subnetting is essential for CCNA, networking, and cybersecurity.
