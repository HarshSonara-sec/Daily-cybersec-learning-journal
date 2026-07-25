# Static Routing & Default Routes
**Source:** Jeremy's IT Lab CCNA – Day 12

**OSI Layer:** Layer 3 (Network Layer)

**Prerequisites:**
- Routing Fundamentals
- IPv4 Addressing
- Routing Tables

---

# Overview

Static routing is the process of **manually configuring routes** on a router to reach remote networks. Unlike **Connected (C)** and **Local (L)** routes, which are created automatically, static routes must be added by the network administrator.

Static routing is commonly used in **small networks**, **stub networks**, and as **backup routes** in larger environments.

---

# Learning Objectives

After completing this topic, you should be able to:

- Understand why static routes are required.
- Configure static routes using Cisco IOS.
- Explain the purpose of a default gateway and default route.
- Differentiate between next-hop IP and exit interface.
- Understand how packets travel across multiple routers.

---

# 1. Why Static Routes?

Connected and Local routes only allow a router to reach:

- Its own interface IP addresses.
- Directly connected networks.

They **cannot** reach remote networks.

To communicate with remote networks, routers require:

- Static Routes
- Dynamic Routing Protocols

---

# 2. Static Route

A **Static Route** is a manually configured route that tells a router where to send packets destined for a specific network.

### Cisco IOS Syntax

```bash
ip route <destination-network> <subnet-mask> <next-hop-IP>
```

Example:

```bash
ip route 192.168.3.0 255.255.255.0 192.168.1.2
```

Meaning:

- Destination Network → `192.168.3.0/24`
- Forward packets to → `192.168.1.2`

---

# 3. Route Planning

Before configuring static routes, identify:

- Source network
- Destination network
- Available path(s)
- Next-hop router

Proper planning ensures packets reach their destination without routing loops.

---

# 4. Two-Way Reachability

Successful communication requires routes in **both directions**.

Example:

```
PC1 ─ R1 ─ R2 ─ PC2
```

Requirements:

- R1 must know how to reach PC2's network.
- R2 must know how to reach PC1's network.

Without return routes, replies cannot reach the sender.

---

# 5. Default Gateway

A **Default Gateway** is the router that an end device uses to send traffic outside its local network.

Every host should be configured with:

- IP Address
- Subnet Mask
- Default Gateway

If the destination is outside the local subnet, the host forwards the packet to its default gateway.

---

# 6. Layer 2 vs Layer 3 Addressing

As packets travel through a network:

### Layer 2 (Data Link)

- Source MAC Address changes at every hop.
- Destination MAC Address changes at every hop.

### Layer 3 (Network)

- Source IP Address remains the same.
- Destination IP Address remains the same.

Only the Ethernet frame changes between routers; the IP packet remains unchanged.

---

# 7. Multiple Paths

A network may have multiple routes to reach the same destination.

Example:

```
R1 → R2 → R4

or

R1 → R3 → R4
```

This provides:

- Redundancy
- Backup paths
- Better network design

Static routing requires the administrator to manually choose which path to use.

---

# 8. Configuring Static Routes

A static route can be configured in three ways.

## Using Next-Hop IP Address

```bash
ip route 10.1.1.0 255.255.255.0 192.168.12.2
```

Recommended for most networks.

---

## Using Exit Interface

```bash
ip route 10.1.1.0 255.255.255.0 GigabitEthernet0/0
```

The router forwards packets through the specified interface.

---

## Using Both

```bash
ip route 10.1.1.0 255.255.255.0 GigabitEthernet0/0 192.168.12.2
```

Provides both the exit interface and the next-hop router.

---

# 9. Proxy ARP

**Proxy ARP (Address Resolution Protocol)** allows a router to respond to an ARP request on behalf of another device.

When only an exit interface is configured in a static route:

- The router may use Proxy ARP to discover the next-hop MAC address.

Although useful, specifying the **next-hop IP address** is generally preferred for clarity.

---

# 10. Default Route

A **Default Route** is a catch-all route used when no more specific route exists.

Network:

```
0.0.0.0/0
```

It is the **least specific route** in the routing table.

---

## Configure Default Route

```bash
ip route 0.0.0.0 0.0.0.0 192.168.1.1
```

Meaning:

"If no matching route exists, forward the packet to `192.168.1.1`."

Default routes are commonly used to forward traffic to:

- Internet Service Providers (ISPs)
- Upstream routers
- Internet gateways

---

# 11. Route Selection

Routers select routes in the following order:

1. Most Specific Match (Longest Prefix Match)
2. Administrative Distance (AD)
3. Metric

The default route (`0.0.0.0/0`) is used **only if no other route matches**.

---

# 12. Administrative Distance (AD)

**Administrative Distance (AD)** measures how trustworthy a routing source is.

- Lower AD = More trusted
- Higher AD = Less trusted

Examples:

| Route Type | Default AD |
|------------|-----------:|
| Connected | 0 |
| Static | 1 |
| OSPF | 110 |
| RIP | 120 |

> **Note:** Administrative Distance is used only when multiple routing sources advertise the same destination.

---

# 13. Metric

A **Metric** represents the cost of reaching a destination.

Different routing protocols calculate metrics differently.

Examples include:

- Hop Count
- Bandwidth
- Delay
- Cost

Routers prefer the route with the **lowest metric** when Administrative Distance is equal.

---

# Useful Cisco IOS Commands

Display routing table:

```bash
show ip route
```

Configure a static route:

```bash
ip route <destination> <subnet-mask> <next-hop>
```

Display interface information:

```bash
show ip interface brief
```

Test connectivity:

```bash
ping <IP-address>
```

Trace packet path:

```bash
traceroute <IP-address>
```

---

# CCNA Exam Tips

- Connected and Local routes only reach directly connected networks.
- Static routes are manually configured.
- End devices use a **Default Gateway** to reach remote networks.
- Source and Destination **IP addresses remain unchanged** during packet forwarding.
- Source and Destination **MAC addresses change at every hop**.
- A Default Route (`0.0.0.0/0`) is used only when no specific route matches.
- Static routes can be configured using a next-hop IP, an exit interface, or both.
- Communication requires routing information in **both directions**.

---

# Key Terms

| Abbreviation | Full Form |
|--------------|-----------|
| IP | Internet Protocol |
| MAC | Media Access Control |
| ARP | Address Resolution Protocol |
| Proxy ARP | Proxy Address Resolution Protocol |
| AD | Administrative Distance |
| ISP | Internet Service Provider |
| CLI | Command-Line Interface |
| IOS | Internetwork Operating System |

---

# Quick Revision

- Static routes are manually configured to reach remote networks.
- Connected and Local routes cannot reach remote destinations.
- End hosts use a Default Gateway for off-network communication.
- MAC addresses change at every router hop, while IP addresses remain the same.
- Static routes can specify a next-hop IP, an exit interface, or both.
- Proxy ARP helps resolve next-hop MAC addresses in certain static route configurations.
- The Default Route (`0.0.0.0/0`) acts as a catch-all route.
- Routers choose the **Longest Prefix Match** first, then consider **Administrative Distance** and **Metric** if needed.
