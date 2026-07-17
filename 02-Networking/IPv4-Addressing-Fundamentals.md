# Chapter 02 - IPv4 Addressing Fundamentals

> **Course:** Jeremy's IT Lab - CCNA 200-301
> **Related Study Date:** 2026-07-17
> **Category:** Networking Fundamentals
> **Difficulty:** Beginner
> **Prerequisites:** Ethernet & Layer 2 Fundamentals

---

# Learning Objectives

After completing this chapter, you should be able to:

* Explain what IPv4 is and why it is used.
* Understand binary numbering and octets.
* Convert decimal numbers to binary and binary numbers to decimal.
* Explain the structure of an IPv4 address.
* Understand network and host portions.
* Identify IPv4 address classes (A–E).
* Understand subnet masks and prefix lengths.
* Calculate network addresses and broadcast addresses.
* Identify loopback addresses and their purpose.

---

# 1. What is IPv4?

## Definition

IPv4 stands for **Internet Protocol Version 4**. It is the most widely used protocol for identifying devices on a network and routing packets between networks.

An IPv4 address is a **32-bit logical address** written in decimal format and divided into four octets.

Example:

```text
192.168.1.10
```

Each octet ranges from **0 to 255**.

---

## Why Do We Need IPv4?

In a network, every device must have a unique address so that data can be delivered to the correct destination.

IPv4 provides this addressing system.

Without IP addresses:

* Computers would not know where to send data.
* Routers could not forward packets between networks.
* Internet communication would not be possible.

---

## Real Life Analogy

Think of IPv4 as a **postal address**.

* **House Number / Street** = Host Portion
* **City / Area** = Network Portion

The network portion tells **which network** the device belongs to, while the host portion tells **which device** inside that network.

---

# 2. Binary Basics

## What is Binary?

Binary is a number system that uses only **two digits**:

* 0
* 1

Computers use binary because electronic circuits can represent two states:

* **0** = Off
* **1** = On

---

## What is an Octet?

An IPv4 address is divided into **4 octets**.

Each octet contains **8 bits**.

Example:

```text
11000000 . 10101000 . 00000001 . 00001010
```

This binary address equals:

```text
192 . 168 . 1 . 10
```

---

## Binary Place Values

| Bit Position | 8   | 7  | 6  | 5  | 4 | 3 | 2 | 1 |
| ------------ | --- | -- | -- | -- | - | - | - | - |
| Value        | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

To calculate a binary number, add the values of all **1s**.

Example:

```text
11000000
```

Calculation:

* 128 + 64 = **192**

So:

```text
11000000 = 192
```

---

# Easy Memory Trick

Memorize the binary place values:

**128 - 64 - 32 - 16 - 8 - 4 - 2 - 1**

Say it repeatedly while practicing subnetting.

---

# 3. Decimal to Binary Conversion

## Method

To convert a decimal number to binary:

1. Start with the largest place value.
2. Put **1** if the value can fit into the number.
3. Subtract that value.
4. Continue until the remainder is **0**.

---

## Example: Convert 168 to Binary

| Value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| ----- | --- | -- | -- | -- | - | - | - | - |
| Use?  | 1   | 0  | 1  | 0  | 1 | 0 | 0 | 0 |

Calculation:

* 168 - 128 = 40
* 40 - 32 = 8
* 8 - 8 = 0

Binary result:

```text
10101000
```

So:

```text
168 = 10101000
```

---

# 4. Binary to Decimal Conversion

## Method

To convert binary to decimal:

1. Write the place values.
2. Add the values where the bit is **1**.

---

## Example: Convert 11000000 to Decimal

| Bit   | 1   | 1  | 0  | 0  | 0 | 0 | 0 | 0 |
| ----- | --- | -- | -- | -- | - | - | - | - |
| Value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

Calculation:

* 128 + 64 = **192**

So:

```text
11000000 = 192
```

---

# Easy Practice Trick

Use this shortcut for common values:

| Decimal | Binary   |
| ------- | -------- |
| 0       | 00000000 |
| 1       | 00000001 |
| 2       | 00000010 |
| 4       | 00000100 |
| 8       | 00001000 |
| 16      | 00010000 |
| 32      | 00100000 |
| 64      | 01000000 |
| 128     | 10000000 |
| 255     | 11111111 |

---

# 5. IPv4 Address Structure

An IPv4 address has **32 bits** divided into **4 octets**.

Example:

```text
192.168.1.10
```

Binary form:

```text
11000000.10101000.00000001.00001010
```

---

## Network Portion vs Host Portion

The subnet mask determines which bits belong to the **network** and which belong to the **host**.

Example:

```text
192.168.1.10/24
```

* **Network Portion:** 192.168.1
* **Host Portion:** 10

---

# Easy Memory Trick

* **Network Portion** = Identifies the network.
* **Host Portion** = Identifies the device inside the network.

Think of it as:

**Network = Neighborhood**

**Host = House**

---

# 6. Netmasks

## Definition

A subnet mask is used to separate the network portion from the host portion of an IPv4 address.

It is written in dotted-decimal format.

---

## Common Netmasks

| Prefix | Netmask       | Network Bits | Host Bits |
| ------ | ------------- | ------------ | --------- |
| /8     | 255.0.0.0     | 8            | 24        |
| /16    | 255.255.0.0   | 16           | 16        |
| /24    | 255.255.255.0 | 24           | 8         |

---

## How Netmasks Work

A **1** in the subnet mask means **Network Bit**.

A **0** means **Host Bit**.

Example:

```text
255.255.255.0
```

Binary:

```text
11111111.11111111.11111111.00000000
```

So:

* First 24 bits = Network
* Last 8 bits = Host

---

# Easy Memory Trick

Count the **1s** in the subnet mask.

That number is the **prefix length**.

Example:

```text
255.255.255.0 = /24
```

---

# 7. Prefix Length (CIDR Notation)

## Definition

CIDR (Classless Inter-Domain Routing) notation shows how many bits belong to the network portion.

It is written with a slash.

Example:

```text
192.168.1.10/24
```

This means:

* 24 bits = Network
* 8 bits = Host

---

## Common Prefixes

| Prefix | Binary Mask                         | Usable Hosts |
| ------ | ----------------------------------- | ------------ |
| /8     | 11111111.00000000.00000000.00000000 | 16,777,214   |
| /16    | 11111111.11111111.00000000.00000000 | 65,534       |
| /24    | 11111111.11111111.11111111.00000000 | 254          |
| /30    | 11111111.11111111.11111111.11111100 | 2            |

---

# Easy Memory Trick

* **/8** = 1 full network octet
* **/16** = 2 full network octets
* **/24** = 3 full network octets

---

# 8. IPv4 Address Classes

Originally, IPv4 addresses were divided into **five classes**.

| Class | First Octet Range | Default Prefix | Default Netmask | Purpose         |
| ----- | ----------------- | -------------- | --------------- | --------------- |
| A     | 1–126             | /8             | 255.0.0.0       | Large Networks  |
| B     | 128–191           | /16            | 255.255.0.0     | Medium Networks |
| C     | 192–223           | /24            | 255.255.255.0   | Small Networks  |
| D     | 224–239           | N/A            | N/A             | Multicast       |
| E     | 240–255           | N/A            | N/A             | Experimental    |

---

## Class A

* First octet: **1–126**
* Default prefix: **/8**
* Large number of hosts.

Example:

```text
10.0.0.1
```

---

## Class B

* First octet: **128–191**
* Default prefix: **/16**

Example:

```text
172.16.0.1
```

---

## Class C

* First octet: **192–223**
* Default prefix: **/24**

Example:

```text
192.168.1.1
```

---

## Class D

* First octet: **224–239**
* Used for **multicast**.

---

## Class E

* First octet: **240–255**
* Reserved for **experimental purposes**.

---

# Easy Memory Trick

**ABC = Normal Host Classes**

* **A** = Large
* **B** = Medium
* **C** = Small

**D = Distribution (Multicast)**

**E = Experiment**

---

# 9. Loopback Address

## Definition

The loopback address is used to test the local TCP/IP stack of a device.

The most common loopback address is:

```text
127.0.0.1
```

---

## Why is it Useful?

If you ping **127.0.0.1**, the packet never leaves your computer.

It checks whether the TCP/IP software is working correctly.

Command:

```bash
ping 127.0.0.1
```

---

# Easy Memory Trick

**127 = Me**

Whenever you see **127.x.x.x**, think:

**The computer is talking to itself.**

---

# 10. Network Address

## Definition

The network address identifies the **network itself**.

It cannot be assigned to a host.

---

## Example

IP Address:

```text
192.168.1.10/24
```

Subnet Mask:

```text
255.255.255.0
```

Network Address:

```text
192.168.1.0
```

---

## How to Calculate

Perform a **bitwise AND** between the IP address and subnet mask.

IP:

```text
192.168.1.10
```

Mask:

```text
255.255.255.0
```

Result:

```text
192.168.1.0
```

---

# Easy Memory Trick

For a **/24** network:

* Replace the last octet with **0**.
* That gives the **Network Address**.

---

# 11. Broadcast Address

## Definition

The broadcast address is used to send a packet to **all devices** in a network.

It cannot be assigned to a host.

---

## Example

Network:

```text
192.168.1.0/24
```

Broadcast Address:

```text
192.168.1.255
```

---

## How to Calculate

For a **/24** network:

* Replace the last octet with **255**.

---

# Easy Memory Trick

For **/24**:

* **Network Address** ends with **0**
* **Broadcast Address** ends with **255**

---

# 12. Network Portion and Host Portion

| Part            | Purpose                |
| --------------- | ---------------------- |
| Network Portion | Identifies the network |
| Host Portion    | Identifies the device  |

Example:

```text
192.168.1.10/24
```

* Network Portion: **192.168.1**
* Host Portion: **10**

---

## Why This Matters

Routers use the **network portion** to decide where to send packets.

Devices use the **host portion** to identify the specific destination inside the network.

---

# 13. IPv4 Class Table

| Class | First Octet | Default Mask  | Network Bits | Host Bits |
| ----- | ----------- | ------------- | ------------ | --------- |
| A     | 1–126       | 255.0.0.0     | 8            | 24        |
| B     | 128–191     | 255.255.0.0   | 16           | 16        |
| C     | 192–223     | 255.255.255.0 | 24           | 8         |
| D     | 224–239     | Multicast     | N/A          | N/A       |
| E     | 240–255     | Experimental  | N/A          | N/A       |

---

# 14. Practice Examples

## Example 1: Decimal to Binary

Convert **25** to binary.

| Value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| ----- | --- | -- | -- | -- | - | - | - | - |
| Use?  | 0   | 0  | 0  | 1  | 1 | 0 | 0 | 1 |

Result:

```text
25 = 00011001
```

---

## Example 2: Binary to Decimal

Convert **10101100** to decimal.

Calculation:

* 128 + 32 + 8 + 4 = **172**

Result:

```text
10101100 = 172
```

---

## Example 3: Network and Broadcast Address

IP Address:

```text
192.168.5.34/24
```

Network Address:

```text
192.168.5.0
```

Broadcast Address:

```text
192.168.5.255
```

Usable Host Range:

```text
192.168.5.1 – 192.168.5.254
```

---

# Common Mistakes

❌ Confusing **IP addresses** with **MAC addresses**.

✔ IP addresses are logical; MAC addresses are physical.

---

❌ Forgetting that an IPv4 address has **32 bits**.

✔ IPv4 = 4 octets × 8 bits = 32 bits.

---

❌ Thinking the network address can be assigned to a host.

✔ The network address identifies the network itself.

---

❌ Thinking the broadcast address can be assigned to a host.

✔ The broadcast address is reserved for sending to all hosts.

---

❌ Confusing **/24** with **255 hosts**.

✔ A /24 network has **256 total addresses**, but only **254 usable hosts**.

---

# Interview & CCNA Questions

* What is IPv4?
* How many bits are in an IPv4 address?
* What is an octet?
* How do you convert decimal to binary?
* What is the difference between network and host portions?
* What is a subnet mask?
* What is CIDR notation?
* What is the loopback address?
* What is the network address of 192.168.1.10/24?
* What is the broadcast address of 192.168.1.10/24?
* Why are network and broadcast addresses not assignable to hosts?

---

# Quick Revision Questions

1. How many bits are in an IPv4 address?
2. What is the binary value of 255?
3. Convert **11001000** to decimal.
4. Convert **172** to binary.
5. What is the default subnet mask of Class B?
6. What is the prefix length of **255.255.255.0**?
7. What is the loopback address?
8. What is the network address of **10.0.5.25/8**?
9. What is the broadcast address of **192.168.10.0/24**?
10. How many usable hosts are available in a **/24** network?

---

# Key Takeaways

* IPv4 is a **32-bit logical addressing system**.
* Each IPv4 address has **4 octets**.
* Binary uses only **0 and 1**.
* Decimal ↔ Binary conversion is essential for subnetting.
* A subnet mask separates the **network portion** from the **host portion**.
* **/8, /16, and /24** are the most important beginner prefixes.
* IPv4 classes help identify traditional network sizes.
* **127.0.0.1** is the loopback address.
* The **network address** identifies the network.
* The **broadcast address** sends to all devices in the network.
* Network and broadcast addresses cannot be assigned to hosts.

---

# Summary

In this chapter, I learned the complete fundamentals of IPv4 addressing, including binary numbering, decimal-to-binary conversions, IPv4 address structure, subnet masks, prefix lengths, IPv4 classes, loopback addresses, network and host portions, network addresses, and broadcast addresses. These concepts form the foundation of subnetting, routing, and all future networking studies in CCNA and cybersecurity.
