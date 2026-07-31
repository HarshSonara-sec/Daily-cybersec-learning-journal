# Spanning Tree Protocol (STP) - Part 1

## Overview

Spanning Tree Protocol (STP) is a Layer 2 protocol that prevents switching loops in Ethernet networks. It creates a loop-free logical topology by blocking redundant paths while keeping them available as backup links.

---

# Why is STP Needed?

Redundant links improve network reliability, but they also introduce switching loops.

Without STP, loops can cause:

* Broadcast Storms
* Multiple Frame Copies
* MAC Address Table Instability (MAC Flapping)

STP solves these issues by temporarily blocking unnecessary links.

---

# Broadcast Storm

A broadcast frame is forwarded out of every switch port except the one it arrived on.

If a loop exists:

* Broadcast frames circulate forever.
* Network bandwidth becomes saturated.
* CPU usage on switches increases.
* The network may become unusable.

---

# MAC Address Table Instability

Switches learn MAC addresses from incoming frames.

In a switching loop:

* The same MAC address is learned from different ports repeatedly.
* The MAC address table constantly changes.
* Frames may be forwarded incorrectly.

This is called **MAC Flapping**.

---

# How STP Works

Instead of removing redundant links, STP logically blocks some of them.

Result:

* Only one active path exists between switches.
* Backup links remain available.
* If the active path fails, STP can activate a blocked path.

---

# Root Bridge

STP elects one switch as the **Root Bridge**.

The Root Bridge becomes the central reference point for the entire Layer 2 topology.

Every other switch calculates its best path to reach the Root Bridge.

---

# Bridge ID (BID)

Each switch has a unique Bridge ID consisting of:

* Bridge Priority
* MAC Address

The switch with the lowest Bridge ID becomes the Root Bridge.

---

# Port Roles

## Root Port (RP)

* One per non-root switch.
* Best path toward the Root Bridge.
* Always forwards traffic.

---

## Designated Port (DP)

* One Designated Port exists on every network segment.
* Responsible for forwarding traffic toward that segment.
* Always in the Forwarding state.

---

## Non-Designated Port (Blocked Port)

Ports that would create a switching loop are placed into the Blocking state.

Blocked ports:

* Do not forward normal traffic.
* Continue receiving STP messages.
* Can become active if the network topology changes.

---

# STP Election Process

1. Elect the Root Bridge.
2. Each switch selects its Root Port.
3. Each network segment elects a Designated Port.
4. Remaining redundant ports are blocked.

---

# Important Terms

| Term            | Meaning                               |
| --------------- | ------------------------------------- |
| STP             | Prevents Layer 2 loops                |
| Root Bridge     | Central switch in the STP topology    |
| Root Port       | Best path toward the Root Bridge      |
| Designated Port | Forwarding port for a network segment |
| Blocked Port    | Disabled to prevent loops             |
| Bridge ID       | Priority + MAC Address                |

---

# Exam Tips

* STP operates at **Layer 2**.
* STP prevents loops without removing redundancy.
* The switch with the lowest Bridge ID becomes the Root Bridge.
* Every non-root switch has exactly one Root Port.
* Every network segment has one Designated Port.
* Blocked ports still receive STP BPDUs and can become active after a topology change.

---

# Quick Revision

✅ Prevents Layer 2 loops

✅ Prevents Broadcast Storms

✅ Prevents MAC Address Table Instability

✅ Uses a Root Bridge as the reference switch

✅ Blocks redundant paths while keeping them available for failover

✅ Automatically recalculates paths after topology changes

---

# Common Mistakes to Avoid

* ❌ Thinking STP removes redundant links (it only blocks them logically).
* ❌ Assuming blocked ports are permanently disabled.
* ❌ Forgetting that every non-root switch has exactly one Root Port.
* ❌ Confusing a Root Port with a Designated Port.
* ❌ Believing STP is a Layer 3 routing protocol—it operates only at Layer 2.

---

# Cheat Sheet

```
Problem
↓
Layer 2 Loop

↓

Broadcast Storm
MAC Flapping
Duplicate Frames

↓

Enable STP

↓

Elect Root Bridge

↓

Choose Root Ports

↓

Choose Designated Ports

↓

Block Redundant Ports

↓

Loop-Free Network
```
