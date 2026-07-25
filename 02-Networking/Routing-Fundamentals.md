# Routing Fundamentals
**Source:** Jeremy's IT Lab CCNA – Day 11

**OSI Layer:** Layer 3 (Network Layer)

**Prerequisites:**
- IPv4 Addressing Fundamentals
- IPv4 Header
- Binary & Subnetting Basics

---

# Overview

**Routing** is the process of forwarding IP packets from one network to another. Unlike switches, which forward Ethernet frames using MAC addresses, routers forward packets using **IP addresses** and make forwarding decisions based on a **routing table**.

Every router maintains a routing table that contains information about reachable networks and the best paths to those networks.

Understanding routing is one of the most fundamental concepts in networking and is essential for the CCNA certification.

---

# Learning Objectives

After completing this topic, you should be able to:

- Explain what routing is.
- Differentiate routing from switching.
- Understand the purpose of a routing table.
- Identify Connected and Local routes.
- Explain Static and Dynamic routing.
- Understand Longest Prefix Match (Most Specific Match).
- Understand what happens when no matching route exists.

---

# 1. What is Routing?

Routing is the process of selecting the best path to deliver an IP packet from its source network to its destination network.

A **router** examines the **Destination IP Address** in the packet and consults its routing table to determine where to forward the packet.

Example:

```
PC1
192.168.1.10
      │
      ▼
 Router
      │
      ▼
192.168.2.10
PC2
```

Since PC1 and PC2 belong to different networks, the router forwards packets between them.

---

# 2. Switching vs Routing

Although both switches and routers forward traffic, they operate differently.

| Switch | Router |
|---------|---------|
| Operates at Layer 2 | Operates at Layer 3 |
| Uses MAC addresses | Uses IP addresses |
| Uses a MAC Address Table | Uses a Routing Table |
| Forwards Ethernet frames | Forwards IP packets |
| Connects devices within a LAN | Connects different networks |

---

# 3. Routing Table

A **Routing Table** is a database that stores information about reachable networks.

Each entry tells the router:

- Which destination network can be reached.
- Which interface should be used.
- Whether a next-hop router is required.
- How the route was learned.

Useful command:

```bash
show ip route
```

Example:

```
C 192.168.1.0/24 is directly connected, GigabitEthernet0/0

L 192.168.1.1/32 is directly connected, GigabitEthernet0/0
```

---

# 4. Components of a Route

Every routing table entry contains important information.

| Component | Description |
|-----------|-------------|
| Destination Network | Network being reached |
| Prefix Length | Defines the network size |
| Exit Interface | Interface used to forward packets |
| Next Hop | Next router (if required) |
| Route Source | How the route was learned |

---

# 5. Connected Routes (C)

A **Connected Route** is automatically created when:

- An interface is configured with an IP address.
- The interface is in an **Up/Up** state.

Example:

```
Interface:
192.168.1.1/24
```

Automatically creates:

```
C 192.168.1.0/24
```

This route represents the entire directly connected network.

### Characteristics

- Automatically generated.
- No manual configuration required.
- Removed if the interface goes down.

---

# 6. Local Routes (L)

A **Local Route** represents the router's own interface IP address.

Example:

Router interface:

```
192.168.1.1/24
```

Automatically creates:

```
L 192.168.1.1/32
```

Notice the **/32 prefix**, which represents a single host.

### Purpose

Allows the router to recognise packets addressed to itself.

---

# Connected Route vs Local Route

| Connected Route | Local Route |
|-----------------|-------------|
| Entire subnet | Single IP address |
| Example: 192.168.1.0/24 | Example: 192.168.1.1/32 |
| Used to forward packets | Used for packets destined for the router |

---

# 7. Route Matching

Whenever a router receives a packet, it compares the destination IP address against every route in its routing table.

The router asks:

> "Which route contains this destination IP address?"

Example:

Destination:

```
192.168.1.50
```

Route:

```
192.168.1.0/24
```

Since the destination belongs to that network, the route matches.

---

# 8. Most Specific Match (Longest Prefix Match)

Often, multiple routes match the same destination.

The router always selects the route with the **longest prefix length**, also known as the **Most Specific Match**.

Example routing table:

```
192.168.0.0/16

192.168.1.0/24

192.168.1.50/32
```

Destination:

```
192.168.1.50
```

The router chooses:

```
192.168.1.50/32
```

because **/32** is more specific than **/24**, and **/24** is more specific than **/16**.

---

# Prefix Length Priority

| Prefix | Specificity |
|---------|-------------|
| /32 | Highest |
| /30 | Very High |
| /24 | Medium |
| /16 | Low |
| /8 | Very Low |
| /0 | Lowest (Default Route) |

The longest prefix always wins.

---

# 9. Variably Subnetted Networks

Sometimes a routing table contains multiple subnet masks within the same major network.

Example:

```
192.168.1.0/24

192.168.1.128/25

192.168.1.64/26
```

This is called **Variable Length Subnet Masking (VLSM)**.

Routers can store and use multiple subnet sizes simultaneously.

---

# 10. Static Routing

A **Static Route** is manually configured by the network administrator.

Example:

```bash
ip route 10.1.1.0 255.255.255.0 192.168.1.2
```

### Advantages

- Simple
- Predictable
- Secure
- Uses very little CPU and memory

### Disadvantages

- Manual configuration
- Difficult to manage in large networks
- No automatic updates

Static routing is commonly used in:

- Small networks
- Stub networks
- Backup routes

---

# 11. Dynamic Routing

Dynamic routing allows routers to automatically learn and update routes.

Instead of manually configuring every network, routers exchange routing information with neighbouring routers.

Common routing protocols:

| Protocol | Full Form |
|----------|-----------|
| RIP | Routing Information Protocol |
| OSPF | Open Shortest Path First |
| EIGRP | Enhanced Interior Gateway Routing Protocol |
| IS-IS | Intermediate System to Intermediate System |
| BGP | Border Gateway Protocol |

### Advantages

- Automatically learns routes.
- Adapts to network changes.
- Suitable for large networks.
- Requires less manual administration.

### Disadvantages

- Uses CPU and memory.
- Slightly more complex to configure.

---

# 12. What Happens if No Route Exists?

If the destination IP does not match any entry in the routing table:

- The router **drops the packet**.
- An ICMP Destination Unreachable message may be generated.

Unlike switches, routers **do not flood unknown traffic**.

---

# 13. Router vs Switch Behaviour

### Switch

When the destination MAC address is unknown:

- Floods the frame out all ports except the incoming port.
- Learns the destination later when a response is received.

### Router

When the destination IP has no matching route:

- Drops the packet.
- Does not flood traffic.

This behaviour improves both efficiency and security.

---

# Packet Forwarding Process

Whenever a router receives a packet:

1. Receive the packet.
2. Read the Destination IP Address.
3. Search the routing table.
4. Find all matching routes.
5. Select the **Longest Prefix Match**.
6. Forward the packet through the correct exit interface.
7. If no route exists, discard the packet.

---

# Useful Cisco IOS Commands

Display the routing table:

```bash
show ip route
```

Display interface information:

```bash
show ip interface brief
```

Test connectivity:

```bash
ping <IP-address>
```

Trace the packet path:

```bash
traceroute <IP-address>
```

---

# CCNA Exam Tips

- Routers forward **IP packets**, while switches forward **Ethernet frames**.
- Routing decisions are made using the **Routing Table**.
- **Connected (C)** and **Local (L)** routes are created automatically when an interface is configured and active.
- A Local Route always uses a **/32** prefix.
- Routers always select the **Longest Prefix Match** when multiple routes exist.
- Static routes are manually configured; Dynamic routes are learned automatically through routing protocols.
- Routers **never flood** packets with unknown destinations—they simply drop them if no matching route is found.

---

# Key Terms

| Abbreviation | Full Form |
|--------------|-----------|
| IP | Internet Protocol |
| LAN | Local Area Network |
| WAN | Wide Area Network |
| VLSM | Variable Length Subnet Masking |
| RIP | Routing Information Protocol |
| OSPF | Open Shortest Path First |
| EIGRP | Enhanced Interior Gateway Routing Protocol |
| IS-IS | Intermediate System to Intermediate System |
| BGP | Border Gateway Protocol |
| ICMP | Internet Control Message Protocol |
| CPU | Central Processing Unit |

---

# Quick Revision

- Routing forwards packets **between different networks**.
- Routers operate at **OSI Layer 3** and use **IP addresses**.
- The routing table stores information about reachable networks.
- **Connected (C)** routes represent directly connected networks.
- **Local (L)** routes represent the router's own interface IP address and always use a **/32** prefix.
- Routers compare the destination IP against all routes and choose the **Longest Prefix Match**.
- Static routes are manually configured, while Dynamic routes are learned using routing protocols.
- If no route matches the destination IP, the router drops the packet instead of flooding it.
