# Life of a Packet (CCNA Day 12)

## Overview

The **Life of a Packet** explains how data travels from one device to another across different networks using switches and routers. It combines concepts such as **ARP, Ethernet, IP, Routing, Encapsulation, and Decapsulation.**

---

## Packet Journey

1. **Source device** creates data and encapsulates it into an IP packet and an Ethernet frame.
2. If the destination is on another network, the packet is sent to the **default gateway**.
3. **ARP** is used to learn the gateway's MAC address if it is unknown.
4. The **switch** forwards the frame based on the destination MAC address.
5. The **router** removes the Ethernet frame, checks the destination IP, consults its routing table, and forwards the packet to the next hop.
6. The router creates a **new Ethernet frame** for each hop until the packet reaches the destination network.
7. The destination device decapsulates the packet and delivers the data to the application.

---

## What Changes?

### IP Addresses

* Source IP: **Never changes**
* Destination IP: **Never changes**

### MAC Addresses

* **Change at every router**
* Each router creates a new Ethernet frame using:

  * Source MAC = Router's outgoing interface
  * Destination MAC = Next-hop device's MAC

---

## Device Responsibilities

### Switch (Layer 2)

* Uses **MAC Address Table**
* Forwards frames based on **Destination MAC**
* Does **not** modify the frame

### Router (Layer 3)

* Uses **Routing Table**
* Makes forwarding decisions using **Destination IP**
* Removes the old Ethernet frame and creates a new one for the next hop

---

## ARP (Address Resolution Protocol)

**Purpose:** Resolve an IP address to a MAC address on the local network.

* ARP Request → Broadcast
* ARP Reply → Unicast
* Every router performs ARP independently on its own network segment.

---

## Packet vs Frame

| Packet                | Frame                     |
| --------------------- | ------------------------- |
| Layer 3               | Layer 2                   |
| Contains IP addresses | Contains MAC addresses    |
| Travels end-to-end    | Exists for one hop only   |
| Does not change       | Recreated at every router |

---

## Encapsulation Process

Application Data
↓
Transport Segment
↓
IP Packet
↓
Ethernet Frame
↓
Bits

## Decapsulation Process

Bits
↓
Ethernet Frame
↓
IP Packet
↓
Transport Segment
↓
Application Data

---

## CCNA Exam Points

* IP addresses remain the same throughout the journey.
* MAC addresses change at every router.
* Switches forward using MAC addresses.
* Routers forward using IP addresses.
* ARP resolves IP addresses to MAC addresses.
* Ethernet frames do **not** cross router boundaries.
