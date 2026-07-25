# Lab 08 - Configuring Router and Switch Interfaces
**Source:** Jeremy's IT Lab CCNA - Interface Configuration Lab

**Lab Type:** Cisco Packet Tracer

**Difficulty:** Beginner

**Related Theory:**
- Switch Interfaces
- Interface Speed & Duplex
- Interface Status
- Cisco IOS Commands

---

# Objective

Configure a small LAN consisting of:

- 1 Router (R1)
- 2 Switches (SW1 & SW2)
- 4 PCs

The goal is to correctly configure interfaces, assign IP addresses, set interface descriptions, configure speed and duplex, disable unused interfaces, and save the configurations.

---

# Network Topology

```
               R1
               |
            G0/0
               |
             SW1
        _______|_______
       |               |
      PC1            G0/2
      PC2              |
                      SW2
                    ___|___
                   |       |
                 PC3     PC4
```

---

# Network Information

## LAN Network

```
172.16.0.0/16
```

Subnet Mask

```
255.255.0.0
```

Default Gateway

```
172.16.255.254
```

---

# Device Addressing

| Device | Interface | IP Address | Subnet Mask |
|---------|-----------|------------|-------------|
| R1 | G0/0 | 172.16.255.254 | 255.255.0.0 |
| PC1 | Fa0 | 172.16.0.1 | 255.255.0.0 |
| PC2 | Fa0 | 172.16.0.2 | 255.255.0.0 |
| PC3 | Fa0 | 172.16.0.3 | 255.255.0.0 |
| PC4 | Fa0 | 172.16.0.4 | 255.255.0.0 |

Default Gateway for every PC:

```
172.16.255.254
```

---

# Lab Tasks

- Configure hostnames.
- Configure router interfaces.
- Configure switch interfaces.
- Configure IP addressing.
- Configure Speed and Duplex.
- Configure interface descriptions.
- Disable unused interfaces.
- Save the running configuration.

---

# Part 1 - Configure Router R1

## Change Hostname

```bash
enable

configure terminal

hostname R1
```

---

## Configure Interface G0/0

```bash
interface g0/0

ip address 172.16.255.254 255.255.0.0

speed 1000

duplex full

description ## to SW1 ##

no shutdown
```

---

## Configure Unused Interfaces

```bash
interface g0/1

description ## not in use ##

shutdown
```

```bash
interface g0/2

description ## not in use ##

shutdown
```

---

## Verify Interface Status

```bash
show ip interface brief
```

Expected:

```
G0/0     Up/Up

G0/1     Administratively Down

G0/2     Administratively Down
```

---

# Part 2 - Configure PCs

Assign the following settings.

| PC | IP Address | Mask | Gateway |
|----|------------|------|----------|
| PC1 | 172.16.0.1 | 255.255.0.0 | 172.16.255.254 |
| PC2 | 172.16.0.2 | 255.255.0.0 | 172.16.255.254 |
| PC3 | 172.16.0.3 | 255.255.0.0 | 172.16.255.254 |
| PC4 | 172.16.0.4 | 255.255.0.0 | 172.16.255.254 |

---

# Part 3 - Configure Switch SW1

## Change Hostname

```bash
enable

configure terminal

hostname SW1
```

---

## Configure Uplink Interfaces

### G0/1

```bash
interface g0/1

speed 1000

duplex full

description ## to R1 ##
```

### G0/2

```bash
interface g0/2

speed 1000

duplex full

description ## to SW2 ##
```

---

## Configure PC Ports

```bash
interface range f0/1-2

description ## to end hosts ##
```

---

## Disable Unused Ports

```bash
interface range f0/3-24

description ## not in use ##

shutdown
```

---

# Part 4 - Configure Switch SW2

## Change Hostname

```bash
enable

configure terminal

hostname SW2
```

---

## Configure Uplink

```bash
interface g0/1

speed 1000

duplex full

description ## to SW1 ##
```

---

## Configure PC Ports

```bash
interface range f0/1-2

description ## to end hosts ##
```

---

## Disable Unused Interfaces

```bash
interface g0/2

description ## not in use ##

shutdown
```

```bash
interface range f0/3-24

description ## not in use ##

shutdown
```

---

# Save Configuration

Router

```bash
copy running-config startup-config
```

Switches

```bash
write
```

or

```bash
write memory
```

---

# Verification Commands

Check interface status

```bash
show ip interface brief
```

View interface details

```bash
show interfaces status
```

View startup configuration

```bash
show startup-config
```

View running configuration

```bash
show running-config
```

---

# Packet Tracer Observations

During this lab, Packet Tracer behaves slightly differently from real Cisco hardware.

### Observation 1

Even after manually configuring:

```bash
speed 1000

duplex full
```

Packet Tracer may still display:

```
a-1000

a-full
```

On real Cisco switches, manually configured interfaces display:

```
1000

full
```

without the **a-** prefix.

---

### Observation 2

Router interfaces may display:

```
Up

Protocol Down
```

until the connected switch interface is correctly configured.

This is a Packet Tracer simulation limitation rather than a configuration error.

---

# Security Best Practices

Always disable unused interfaces.

```bash
shutdown
```

Benefits:

- Prevents unauthorised device connections.
- Reduces attack surface.
- Improves network security.
- Follows Cisco best practices.

Also add clear interface descriptions to simplify troubleshooting.

Example:

```bash
description ## to SW1 ##
```

---

# Common Mistakes

❌ Forgetting `no shutdown` on router interfaces.

❌ Incorrect IP address or subnet mask.

❌ Missing default gateway on PCs.

❌ Leaving unused switch ports enabled.

❌ Forgetting to save the configuration.

---

# Important Commands Learned

```bash
hostname

interface

interface range

ip address

description

speed

duplex

shutdown

no shutdown

show ip interface brief

show interfaces status

show running-config

show startup-config

copy running-config startup-config

write

write memory
```

---

# Key Takeaways

- Router interfaces are **administratively down by default** and require `no shutdown`.
- Switch ports are **enabled by default**.
- Configure speed and duplex manually when required to prevent negotiation issues.
- Interface descriptions make administration and troubleshooting easier.
- Disable unused interfaces as a security measure.
- Always save configurations before exiting.
- Packet Tracer may not exactly match the behaviour of physical Cisco devices, but the configuration concepts remain the same.

---

# Quick Revision

- Configure hostname first.
- Assign IP addresses to router interfaces.
- Enable router interfaces using `no shutdown`.
- Configure switch uplinks with speed, duplex, and descriptions.
- Configure PC IP addresses and default gateways.
- Disable unused ports.
- Verify using `show ip interface brief`.
- Save the configuration using `copy running-config startup-config` or `write memory`.
