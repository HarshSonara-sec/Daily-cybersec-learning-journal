# Chapter 01 - Ethernet & Layer 2 Fundamentals

> **Course:** Jeremy's IT Lab - CCNA 200-301
> **Related Study Date:** 2026-07-16
> **Category:** Networking Fundamentals
> **Difficulty:** Beginner
> **Prerequisites:** None

---

# Learning Objectives

After completing this chapter, you should be able to:

- Explain what Ethernet is.
- Understand how switches forward frames.
- Identify every field in an Ethernet frame.
- Explain MAC addresses and why they are required.
- Understand decimal and hexadecimal notation.
- Differentiate between unicast and unknown unicast traffic.
- Explain how ARP works.
- Understand ICMP Ping.
- Explain how a switch builds a MAC Address Table.

---

# 1. What is Ethernet?

## Definition

Ethernet is the world's most widely used **Layer 2 (Data Link Layer)** networking technology. It defines how devices communicate over a Local Area Network (LAN).

Simply put,

> Ethernet is the language computers use to communicate inside the same local network.

Examples:

- Home Wi-Fi router
- Office switch
- College computer lab
- Data centers

Nearly all LANs use Ethernet.

---

## Why Do We Need Ethernet?

Imagine everyone in a room shouting at once.

Nobody would understand anyone.

Ethernet defines rules for:

- Sending data
- Receiving data
- Detecting errors
- Identifying devices
- Delivering information correctly

Without Ethernet, computers inside a LAN would not know how to communicate.

---

## Real Life Analogy

Think of a courier company.

Each parcel:

- Has a sender
- Has a receiver
- Contains goods
- Has a label
- Gets checked for damage

Ethernet Frames work exactly the same way.

---

# 2. Ethernet LAN Switching

## Definition

A switch is a Layer 2 device that forwards Ethernet frames using MAC addresses.

Instead of broadcasting everything to every device, a switch learns where devices are connected and forwards traffic intelligently.

---

## Why Switches are Better than Hubs

Hub

- Sends data to everyone.

Switch

- Sends data only to the correct device.

This improves:

- Speed
- Security
- Network efficiency

---

## How a Switch Learns

Whenever a device sends a frame,

the switch records:

```
MAC Address
↓

Incoming Port
```

Example

```
MAC Address              Port

AA:AA:AA:AA:AA:AA  → Fa0/1

BB:BB:BB:BB:BB:BB  → Fa0/5
```

This information is stored inside the **MAC Address Table**.

---

# Easy Memory Trick

Hub = Loud Teacher

Switch = Smart Receptionist

---

# 3. Ethernet Frame

## Definition

An Ethernet Frame is the Layer 2 container used to transport data.

Imagine sending a gift.

Gift

↓

Gift Box

↓

Courier

The Frame is the box.

The Payload is the gift.

---

# Ethernet Frame Structure

```
Preamble
↓

SFD

↓

Destination MAC

↓

Source MAC

↓

Type / Length

↓

Payload

↓

FCS
```

---

## Preamble

### Purpose

Synchronizes sender and receiver.

Allows devices to prepare for incoming data.

Think of it as:

"Hello, I am about to send something."

---

## SFD

### Full Form

Start Frame Delimiter

Marks where the real Ethernet frame begins.

---

## Destination MAC Address

Contains the MAC address of the receiving device.

The switch checks this field before forwarding the frame.

---

## Source MAC Address

Contains the sender's MAC address.

Useful for learning MAC addresses.

---

## Type / Length

Indicates what protocol is inside the payload.

Examples

IPv4

IPv6

ARP

---

## Payload

Contains the actual information being transmitted.

Can include

- Web traffic
- Files
- Emails
- Ping packets

---

## FCS

### Full Form

Frame Check Sequence

Purpose

Detects errors during transmission.

If corruption occurs,

the frame is discarded.

---

# Easy Memory Trick

Imagine mailing a parcel.

Preamble

↓

Knock on the door

Destination

↓

Receiver's address

Source

↓

Sender's address

Payload

↓

Actual parcel

FCS

↓

Quality check

---

# 4. MAC Address

## Full Form

Media Access Control Address

---

## Definition

A unique hardware address assigned to every Network Interface Card (NIC).

Works at Layer 2.

Length

48 bits

Written in hexadecimal.

Example

```
00:1A:2B:3C:4D:5E
```

---

## Why MAC Addresses Exist

IP tells **where** a device is.

MAC tells **who** the device is.

Switches forward frames using MAC addresses.

---

## Easy Memory Trick

IP = House Address

MAC = Person's Name

---

# 5. Decimal vs Hexadecimal

## Decimal

Uses

```
0-9
```

Base 10

Example

```
245
```

---

## Hexadecimal

Uses

```
0-9

A B C D E F
```

Base 16

Example

```
3F

AA

1B
```

---

## Why Networking Uses Hexadecimal

MAC addresses are 48 bits.

Writing them in binary would be very long.

Hexadecimal is shorter and easier to read.

---

# Memory Trick

Every Hex Digit

=

4 Binary Bits

---

# 6. Unicast

## Definition

One sender communicates with one receiver.

Example

Your laptop sends data directly to your router.

```
PC A

↓

PC B
```

Only one destination receives the frame.

---

# 7. Unknown Unicast

Occurs when the switch does not know the destination MAC.

Instead of dropping the frame,

the switch floods it to every port except the incoming port.

Once the destination replies,

the switch learns the MAC address.

Future communication becomes efficient.

---

# Easy Memory Trick

Unknown Person

↓

Ask Everyone

Known Person

↓

Go Directly

---

# 8. ARP

## Full Form

Address Resolution Protocol

---

## Definition

ARP maps an IPv4 address to a MAC address.

Computers know IP addresses,

but Ethernet requires MAC addresses.

ARP connects the two.

---

## Why ARP is Needed

Suppose

```
192.168.1.20
```

is known.

But the sender doesn't know

```
AA:BB:CC:DD:EE:FF
```

ARP finds it.

---

# ARP Process

Step 1

Check ARP Cache.

↓

Step 2

Not Found.

↓

Broadcast

"Who has 192.168.1.20?"

↓

Step 3

Correct PC replies.

↓

Step 4

Store inside ARP Cache.

↓

Step 5

Send frame normally.

---

## ARP Request

Broadcast

Everyone receives it.

---

## ARP Reply

Unicast

Only requester receives it.

---

# Easy Memory Trick

Know IP

↓

Need MAC

↓

Use ARP

---

# Real Life Analogy

You know your friend's house address.

You ask

"Who lives here?"

Someone replies.

Now you know both the address and the person.

That's ARP.

---

# 9. ICMP Ping

## ICMP

Internet Control Message Protocol

Ping uses ICMP.

---

## Purpose

Checks

- Connectivity
- Reachability
- Network delay

---

## Process

Computer A

↓

Echo Request

↓

Computer B

↓

Echo Reply

↓

Success

---

# Easy Memory Trick

Ping

↓

"Are you alive?"

Reply

↓

"Yes."

---

# 10. MAC Address Table

Every switch maintains a table.

Example

| MAC Address | Interface |
|-------------|-----------|
| AA:AA:AA:AA:AA:AA | Fa0/1 |
| BB:BB:BB:BB:BB:BB | Fa0/2 |

Whenever a frame arrives,

the switch learns

```
MAC

↓

Port
```

If destination exists

↓

Forward only to that port.

Otherwise

↓

Flood.

---

# Packet Tracer Practice

Practical topics completed:

- Ethernet Switching
- ARP Request
- ARP Reply
- ICMP Ping
- MAC Learning

Key observation:

As devices communicated,

the MAC Address Table automatically populated with learned MAC addresses.

---

# Common Mistakes

❌ Thinking IP addresses are used by switches.

✔ Switches use MAC addresses.

---

❌ Thinking ARP crosses routers.

✔ ARP only works inside the local LAN.

---

❌ Confusing Broadcast with Unicast.

Broadcast

Everyone receives.

Unicast

Only one device receives.

---

❌ Thinking Ping uses TCP.

Ping uses ICMP.

---

# Interview Questions

### What is Ethernet?

### Why do switches need MAC addresses?

### Difference between IP Address and MAC Address?

### What happens during an ARP Request?

### Why is ARP Request a Broadcast?

### Why is ARP Reply a Unicast?

### What is stored in a MAC Address Table?

### Why are MAC addresses written in hexadecimal?

### What happens when a switch doesn't know the destination MAC?

---

# Quick Revision

✔ Ethernet works at Layer 2.

✔ Switches forward Frames.

✔ Frames contain MAC addresses.

✔ MAC addresses identify devices physically.

✔ ARP converts IPv4 → MAC.

✔ ARP Request = Broadcast.

✔ ARP Reply = Unicast.

✔ Ping uses ICMP.

✔ Switches learn MAC addresses automatically.

✔ FCS detects transmission errors.

---

# Summary

In this chapter, I learned the fundamentals of Layer 2 networking, including how Ethernet communication works, how switches forward frames, the purpose and structure of Ethernet frames, MAC addressing, hexadecimal notation, unicast communication, ARP, ICMP Ping, and MAC address tables. These concepts form the foundation for understanding IPv4 addressing, subnetting, routing, and more advanced networking topics that follow.
