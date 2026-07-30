# ============================================================
# CCNA Notes
# Topic: VLANs and Inter-VLAN Routing
# Date: 2026-07-30
# Last Updated: 2026-07-30
# Source: Jeremy's IT Lab CCNA - Days 17, 18 & 19
# ============================================================

# VLANs and Inter-VLAN Routing

## Overview

Virtual LANs (VLANs) logically divide a physical network into multiple broadcast domains. They improve network performance, security, and manageability by separating devices into different logical groups while using the same physical switching infrastructure.

---

## Learning Objectives

By the end of this topic, you should be able to:

- Explain the purpose of VLANs.
- Understand broadcast domains.
- Configure VLANs on Cisco switches.
- Configure trunk ports using IEEE 802.1Q.
- Explain Router-on-a-Stick (ROAS).
- Configure native VLANs.
- Understand Layer 3 Switching.
- Analyze VLAN traffic using Wireshark.

---

## Prerequisites

- Ethernet Switching
- MAC Address Tables
- Basic Switch Configuration
- IPv4 Addressing

---

# LAN (Local Area Network)

A **LAN** is a group of devices connected within a limited geographical area such as a home, office, or campus.

Characteristics:

- High-speed communication
- Local connectivity
- Uses switches to forward frames
- Devices communicate within the same network

---

# Broadcast Domains

A **broadcast domain** is the set of devices that receive a broadcast frame.

Without VLANs:

- Every device belongs to the same broadcast domain.
- Broadcast traffic reaches every connected device.

Problems:

- Increased unnecessary traffic.
- Reduced network performance.
- Lower security.

---

# VLAN (Virtual Local Area Network)

A **VLAN** logically separates devices into different networks, regardless of their physical location.

Each VLAN creates its own broadcast domain.

Example:

- VLAN 10 – Sales
- VLAN 20 – HR
- VLAN 30 – IT

Devices in different VLANs cannot communicate without a Layer 3 device.

---

# Purpose of VLANs

- Reduce broadcast traffic.
- Improve security.
- Organize departments logically.
- Simplify network management.
- Improve overall network performance.

---

# Configuring VLANs

Basic steps:

1. Create the VLAN.
2. Assign a name.
3. Assign switch ports to the VLAN.
4. Verify the configuration.

Common verification command:

```bash
show vlan brief
```

---

# Access Ports

An **access port** belongs to a single VLAN and connects end devices such as:

- PCs
- Printers
- IP Phones

Access ports carry **untagged Ethernet frames**.

---

# Trunk Ports

A **trunk port** carries traffic for multiple VLANs over a single physical link.

Commonly used between:

- Switch ↔ Switch
- Switch ↔ Router
- Switch ↔ Multilayer Switch

Benefits:

- Reduces cabling.
- Allows multiple VLANs across one connection.
- Required for inter-VLAN communication.

---

# IEEE 802.1Q Encapsulation

IEEE **802.1Q** is the standard used to identify VLAN traffic across trunk links.

It inserts a **4-byte VLAN tag** into Ethernet frames.

The tag contains:

- VLAN ID
- Priority Information
- Other control information

Frames on access ports remain untagged.

---

# Native VLAN

The **Native VLAN** carries **untagged traffic** on a trunk link.

Key points:

- Default Native VLAN is VLAN 1.
- Both ends of a trunk should use the same Native VLAN.
- Native VLAN mismatches can cause connectivity issues.

---

# Router-on-a-Stick (ROAS)

ROAS enables communication between multiple VLANs using a single router interface.

How it works:

- A trunk link connects the router and switch.
- Multiple router subinterfaces are created.
- Each subinterface is assigned a VLAN.
- Each VLAN uses its own default gateway.

Advantages:

- Cost-effective.
- Easy to implement.
- Suitable for small to medium-sized networks.

Limitations:

- All VLAN traffic shares one physical interface.
- Performance is lower than Layer 3 switching.

---

# Layer 3 Switching (Multilayer Switching)

A **Layer 3 switch** performs both switching and routing.

Instead of using a separate router, it routes traffic directly between VLANs.

Advantages:

- Faster inter-VLAN routing.
- Better scalability.
- Reduced network bottlenecks.
- Common in enterprise environments.

---

# Wireshark Analysis

Wireshark can be used to inspect VLAN traffic.

Observed concepts:

- IEEE 802.1Q VLAN tags
- Tagged vs Untagged frames
- VLAN ID inside Ethernet frames
- Encapsulation changes across trunk links

---

# CCNA Exam Tips

- Every VLAN is a separate broadcast domain.
- Access ports belong to one VLAN.
- Trunk ports carry multiple VLANs.
- IEEE 802.1Q provides VLAN tagging.
- Native VLAN carries untagged traffic.
- ROAS uses router subinterfaces.
- Layer 3 switches perform inter-VLAN routing without an external router.

---

# Cybersecurity Relevance

VLANs are widely used to improve security through network segmentation.

Common examples:

- Separate employee and guest networks.
- Isolate servers from user devices.
- Restrict broadcast traffic.
- Reduce the attack surface.
- Improve access control using ACLs and firewalls.

---

# Key Takeaways

- VLANs logically divide a physical network.
- Every VLAN creates its own broadcast domain.
- Access ports carry traffic for a single VLAN.
- Trunk ports carry traffic for multiple VLANs using IEEE 802.1Q.
- Native VLAN handles untagged frames on trunk links.
- ROAS enables inter-VLAN routing using router subinterfaces.
- Layer 3 switches provide faster and more scalable inter-VLAN routing.
- VLAN segmentation improves both network performance and security.
