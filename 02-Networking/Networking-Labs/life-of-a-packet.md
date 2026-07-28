# ============================================================
# CCNA Lab
# Lab 1 - The Life of a Packet
# Date: 2026-07-28
# Last Updated: 2026-07-28
# Source: Jeremy's IT Lab CCNA - Day 15
# ============================================================

# Lab 1 - The Life of a Packet

## Objective

Observe how an IPv4 packet travels from a source device to a destination device, and understand how switches and routers process traffic at each OSI layer.

---

## Lab Overview

This Packet Tracer lab follows the complete journey of a packet through a network using **Simulation Mode**. It demonstrates how Layer 2 and Layer 3 devices forward traffic and how Ethernet frames are rebuilt at every router hop.

---

## Skills Practised

- Packet flow analysis
- Simulation Mode in Packet Tracer
- ARP process
- Ethernet frame encapsulation
- IP packet forwarding
- MAC address learning
- Router forwarding decisions

---

## Key Observations

### Switch Behaviour

- Learns MAC addresses dynamically.
- Forwards frames based on the destination MAC address.
- Floods unknown unicast frames until the destination MAC is learned.

### Router Behaviour

- Removes the incoming Layer 2 frame.
- Examines the destination IP address.
- Determines the best route.
- Re-encapsulates the packet into a new Ethernet frame.
- Forwards the packet through the correct interface.

### Address Changes

| Address Type | Changes? |
|--------------|----------|
| Source IP | ❌ No |
| Destination IP | ❌ No |
| Source MAC | ✅ Yes |
| Destination MAC | ✅ Yes |

> MAC addresses change at every router hop, while IP addresses remain the same throughout the journey.

---

## Verification

- Entered **Simulation Mode** in Cisco Packet Tracer.
- Tracked the packet hop-by-hop.
- Examined Ethernet and IP headers.
- Verified successful packet delivery to the destination.

---

## Key Learning

- Switches make forwarding decisions using **MAC addresses**.
- Routers make forwarding decisions using **IP addresses**.
- Every router creates a new Layer 2 frame before forwarding the packet.
- Layer 3 addressing remains unchanged from source to destination.

---

## Troubleshooting Notes

- Ensure devices have the correct IP configuration.
- Verify default gateways are configured.
- Check router interfaces are enabled (`no shutdown`).
- Confirm successful ARP resolution before analysing packet flow.

---

## Conclusion

This lab reinforced the interaction between Layer 2 and Layer 3 during packet forwarding. Understanding how Ethernet frames and IP packets behave at each hop is essential for troubleshooting, routing, and packet analysis in real-world networks.
