# Lab 09 - Configuring Static Routes
**Source:** Jeremy's IT Lab CCNA - Static Routing Lab

**Lab Type:** Cisco Packet Tracer

**Difficulty:** Beginner–Intermediate

**Related Theory:**
- Routing Fundamentals
- Static Routing
- Connected & Local Routes
- Default Gateway
- Routing Tables

---

# Objective

Configure static routes on three Cisco routers to allow communication between two different LANs.

By the end of this lab you should be able to:

- Configure router interfaces.
- Configure end-device IP addressing.
- Plan static routes.
- Configure static routes using the next-hop IP address.
- Configure static routes using the exit interface.
- Verify routing tables.
- Test end-to-end connectivity.

---

# Network Topology

```
        LAN 1
     192.168.1.0/24

      PC1
       |
      SW1
       |
      R1
       |
192.168.12.0/24
       |
      R2
       |
192.168.13.0/24
       |
      R3
       |
      SW2
       |
      PC2

       LAN 2
    192.168.3.0/24
```

---

# Network Addressing

## PC Configuration

| Device | IP Address | Subnet Mask | Default Gateway |
|---------|------------|-------------|-----------------|
| PC1 | 192.168.1.1 | 255.255.255.0 | 192.168.1.254 |
| PC2 | 192.168.3.1 | 255.255.255.0 | 192.168.3.254 |

---

## Router Interfaces

| Router | Interface | IP Address |
|---------|-----------|------------|
| R1 | G0/1 | 192.168.1.254/24 |
| R1 | G0/0 | 192.168.12.1/24 |
| R2 | G0/0 | 192.168.12.2/24 |
| R2 | G0/1 | 192.168.13.2/24 |
| R3 | G0/0 | 192.168.13.3/24 |
| R3 | G0/1 | 192.168.3.254/24 |

---

# Step 1 - Configure Router Interfaces

Assign the correct IP addresses to each router interface.

Enable every interface.

```bash
no shutdown
```

Add meaningful interface descriptions.

Example:

```bash
description ## to R2 ##
```

Verify:

```bash
show ip interface brief
```

Expected output:

```
Interface Status : Up/Up
```

---

# Step 2 - Configure End Devices

Configure PC1

```
IP Address:
192.168.1.1

Subnet Mask:
255.255.255.0

Default Gateway:
192.168.1.254
```

Configure PC2

```
IP Address:
192.168.3.1

Subnet Mask:
255.255.255.0

Default Gateway:
192.168.3.254
```

---

# Step 3 - Plan Static Routes

Before configuring routes, determine how packets will travel.

Desired path

```
PC1

↓

R1

↓

R2

↓

R3

↓

PC2
```

Remember:

Communication must work **both ways**.

Every router needs to know how to reach remote networks.

---

# Step 4 - Configure Static Routes

## Router R1

R1 needs a route to LAN 2.

```
Destination Network

192.168.3.0/24
```

Configuration

```bash
ip route 192.168.3.0 255.255.255.0 192.168.12.2
```

Meaning

```
To reach 192.168.3.0/24

Send packets to R2

192.168.12.2
```

---

## Router R2

R2 requires two static routes.

### Route to LAN 1

Configured using the exit interface.

```bash
ip route 192.168.1.0 255.255.255.0 g0/0
```

---

### Route to LAN 2

Configured using the next-hop IP.

```bash
ip route 192.168.3.0 255.255.255.0 192.168.13.3
```

---

## Router R3

Configure a route back to LAN 1.

```bash
ip route 192.168.1.0 255.255.255.0 192.168.13.2
```

---

# Static Route Summary

| Router | Destination | Method |
|---------|-------------|---------|
| R1 | 192.168.3.0/24 | Next-Hop IP |
| R2 | 192.168.1.0/24 | Exit Interface |
| R2 | 192.168.3.0/24 | Next-Hop IP |
| R3 | 192.168.1.0/24 | Next-Hop IP |

Total Static Routes

```
4
```

---

# Step 5 - Verify Routing Table

Display the routing table.

```bash
show ip route
```

Expected entries

```
C

Connected Route
```

```
L

Local Route
```

```
S

Static Route
```

Example

```
S 192.168.3.0/24

via 192.168.13.3
```

---

# Step 6 - Test Connectivity

Ping from PC1

```bash
ping 192.168.3.1
```

The first ping may fail because of **ARP (Address Resolution Protocol)** resolution.

Subsequent replies should succeed.

Example

```
!!!!!

Success
```

---

# Route Configuration Methods

Cisco allows three ways to configure a static route.

## Method 1 - Next-Hop IP (Recommended)

```bash
ip route 192.168.3.0 255.255.255.0 192.168.13.3
```

Advantages

- Most common
- Easy to troubleshoot
- Preferred for Ethernet networks

---

## Method 2 - Exit Interface

```bash
ip route 192.168.1.0 255.255.255.0 g0/0
```

Advantages

- Simple on point-to-point links

Disadvantages

- May trigger Proxy ARP on Ethernet networks.
- Less preferred on multi-access networks.

---

## Method 3 - Next-Hop + Exit Interface

```bash
ip route 192.168.3.0 255.255.255.0 g0/1 192.168.13.3
```

Provides both forwarding information and next-hop information.

---

# Verification Commands

Check interface status

```bash
show ip interface brief
```

View routing table

```bash
show ip route
```

View running configuration

```bash
show running-config
```

Test connectivity

```bash
ping <IP-address>
```

Trace packet path

```bash
traceroute <IP-address>
```

---

# Common Mistakes

❌ Forgetting to configure return routes.

❌ Incorrect next-hop IP address.

❌ Wrong subnet mask.

❌ Interfaces left in shutdown state.

❌ Missing default gateway on PCs.

❌ Not verifying the routing table after configuration.

---

# Best Practices

- Configure interface IP addresses before routing.
- Verify interfaces are **Up/Up**.
- Plan routes before entering commands.
- Prefer the **next-hop IP** method on Ethernet networks.
- Use descriptive interface descriptions.
- Always verify using `show ip route`.
- Test with `ping` after every major configuration.

---

# Important Commands Learned

```bash
hostname

interface

ip address

description

no shutdown

ip route

show ip interface brief

show ip route

show running-config

ping

traceroute
```

---

# Key Terms

| Abbreviation | Full Form |
|--------------|-----------|
| IP | Internet Protocol |
| LAN | Local Area Network |
| ARP | Address Resolution Protocol |
| CLI | Command-Line Interface |
| IOS | Internetwork Operating System |

---

# Key Takeaways

- Static routes enable communication with remote networks.
- Every router must know how to reach every remote destination.
- Bidirectional routing is essential for successful communication.
- Cisco routers support static routes using a next-hop IP, an exit interface, or both.
- `show ip route` is the primary command for verifying routing.
- The first ping may fail due to ARP resolution, but subsequent pings should succeed.
- Careful planning and verification are critical to successful static routing.

---

# Quick Revision

- Configure all router interfaces and enable them.
- Assign IP addresses and default gateways to PCs.
- Plan the routing path before configuring routes.
- Configure four static routes across the three routers.
- Verify routes using `show ip route`.
- Test connectivity using `ping`.
- Confirm end-to-end communication between PC1 and PC2.
