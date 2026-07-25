# Switch Interfaces
**Source:** Jeremy's IT Lab CCNA – Day 9

**OSI Layer:** Layer 1 (Physical) & Layer 2 (Data Link)

**Prerequisites:**
- Ethernet LAN Switching
- MAC Addresses
- Basic Cisco IOS CLI

---

# Overview

A **switch interface** (also called a **switchport**) is a physical port on a switch used to connect end devices such as computers, printers, servers, or other networking devices.

Unlike routers, Cisco switch interfaces are **enabled (no shutdown)** by default. Their primary purpose is to forward Ethernet frames based on MAC addresses rather than IP addresses.

Understanding interface status, speed, duplex settings, autonegotiation, and interface errors is essential for configuring and troubleshooting Ethernet networks.

---

# Learning Objectives

After completing this topic, you should be able to:

- Explain how switch interfaces operate.
- Interpret interface status information.
- Configure interface speed and duplex.
- Understand Ethernet autonegotiation.
- Identify duplex mismatch problems.
- Troubleshoot interfaces using interface counters.

---

# 1. Cisco Switch Interfaces

Every physical port on a switch is an individual interface.

Examples:

```
FastEthernet0/1
FastEthernet0/24
GigabitEthernet0/1
GigabitEthernet1/0/1
```

Switch interfaces generally:

- Operate at Layer 2.
- Forward Ethernet frames.
- Learn MAC addresses.
- Connect hosts within the same LAN.
- Do not require an IP address for normal switching.

> **Note:** An IP address can be assigned to a Switch Virtual Interface (SVI) for remote management, but not to a normal Layer 2 switchport.

---

# 2. Default Interface Behaviour

Cisco routers and switches behave differently by default.

| Device | Default Interface State |
|---------|------------------------|
| Router | Administratively Down |
| Switch | Enabled (No Shutdown) |

Therefore:

### Connected switch port

```
Status: up
Protocol: up
```

### Unused switch port

```
Status: down
Protocol: down
```

### Disabled switch port

```
Status: administratively down
Protocol: down
```

---

# 3. Checking Interface Status

## show ip interface brief

Displays a summary of interface information.

```bash
show ip interface brief
```

Useful information:

- Interface name
- IP address
- Interface status
- Line protocol

---

## show interfaces status

Displays Layer 2 information.

```bash
show interfaces status
```

Example output:

| Field | Description |
|--------|-------------|
| Port | Interface identifier |
| Name | Interface description |
| Status | Connected, Notconnect or Disabled |
| VLAN | Assigned VLAN |
| Duplex | Full, Half or Auto |
| Speed | Operating speed |
| Type | Physical interface type |

Example:

```
Fa0/1 Connected VLAN1 Full 100
```

---

# 4. Interface Speed

Speed determines how quickly data is transmitted across the cable.

Common Ethernet standards:

| Ethernet Standard | Speed |
|-------------------|-------|
| Ethernet | 10 Mbps |
| Fast Ethernet | 100 Mbps |
| Gigabit Ethernet | 1000 Mbps (1 Gbps) |
| 10 Gigabit Ethernet | 10 Gbps |

---

## Configure Speed

```bash
interface fa0/1
speed 100
```

Automatic configuration:

```bash
speed auto
```

---

# 5. Duplex Mode

**Duplex** refers to whether a device can send and receive data simultaneously.

---

## Half Duplex

Characteristics:

- Send OR receive.
- Cannot perform both simultaneously.
- Uses CSMA/CD.
- Shared collision domain.
- Common in legacy hub networks.

Example:

```
PC ---- Hub ---- PC
```

---

## Full Duplex

Characteristics:

- Send AND receive simultaneously.
- No collisions.
- Much higher performance.
- Standard in modern switched Ethernet.

Example:

```
PC ----- Switch
```

---

# Half Duplex vs Full Duplex

| Half Duplex | Full Duplex |
|--------------|-------------|
| Send or Receive | Send and Receive |
| Collisions occur | No collisions |
| Uses CSMA/CD | CSMA/CD not required |
| Lower performance | Higher performance |

---

# 6. CSMA/CD

**CSMA/CD** stands for:

**Carrier Sense Multiple Access with Collision Detection**

Used only in half-duplex Ethernet.

## Operation

1. Listen before transmitting.
2. If the cable is busy, wait.
3. Begin transmission.
4. Detect collisions.
5. Send a jamming signal.
6. Wait a random amount of time.
7. Retransmit.

Modern switched Ethernet using Full Duplex does **not** require CSMA/CD because collisions cannot occur.

---

# 7. Speed and Duplex Autonegotiation

Autonegotiation allows two Ethernet devices to automatically determine the best communication settings.

The devices negotiate:

- Interface speed
- Duplex mode

Example:

| Device A | Device B | Negotiated Speed |
|----------|----------|------------------|
| 10/100/1000 | 10/100 | 100 Mbps |

The highest speed supported by **both** devices is selected.

---

## If Autonegotiation is Disabled

When one device is manually configured:

- Speed can usually still be detected.
- Duplex often cannot be detected correctly.

For:

- 10 Mbps
- 100 Mbps

The other device normally assumes:

```
Half Duplex
```

For Gigabit Ethernet and above:

```
Full Duplex
```

---

# 8. Duplex Mismatch

A duplex mismatch occurs when one device operates in Half Duplex while the other operates in Full Duplex.

Example:

| Switch | PC |
|---------|----|
| Half Duplex | Full Duplex |

Problems include:

- Slow connections
- Packet retransmissions
- High latency
- CRC errors
- Input errors
- Poor application performance

This is one of the most common Ethernet troubleshooting issues.

---

# 9. Interface Range Command

Cisco IOS allows multiple interfaces to be configured simultaneously.

Example:

```bash
interface range fa0/1-12
```

Multiple ranges:

```bash
interface range fa0/1-5, fa0/10-15
```

Common uses:

- Shutdown unused ports
- Apply descriptions
- Configure access ports
- Configure VLAN membership

---

# 10. Securing Unused Interfaces

Unused switch ports should always be disabled.

Benefits:

- Prevents unauthorised access.
- Improves network security.
- Reduces attack surface.

Example:

```bash
interface range fa0/10-24

shutdown
```

---

# 11. Interface Counters

Detailed interface statistics can be viewed using:

```bash
show interfaces fa0/1
```

These counters are valuable for troubleshooting physical layer problems.

---

## Runts

Frames smaller than the minimum Ethernet frame size.

Less than:

```
64 Bytes
```

Possible causes:

- Collisions
- Faulty NICs (Network Interface Cards)

---

## Giants

Frames larger than the normal Ethernet frame size.

Greater than:

```
1518 Bytes
```

Possible causes:

- Misconfigured MTU
- Faulty devices

---

## CRC Errors

**CRC = Cyclic Redundancy Check**

The receiving device recalculates the Frame Check Sequence (FCS). If it does not match the transmitted value, a CRC error occurs.

Common causes:

- Damaged cables
- Electrical interference
- Duplex mismatch
- Faulty hardware

---

## Frame Errors

Frames with invalid or corrupted formatting.

Common causes:

- Physical layer problems
- Faulty interfaces

---

## Input Errors

Represents the total number of received errors.

Includes:

- Runts
- Giants
- CRC errors
- Frame errors

---

## Output Errors

Errors encountered while transmitting frames.

Usually caused by:

- Hardware issues
- Congestion
- Interface problems

---

# Useful Cisco IOS Commands

Display interface summary:

```bash
show ip interface brief
```

Display interface status:

```bash
show interfaces status
```

Display detailed interface statistics:

```bash
show interfaces
```

Configure interface:

```bash
interface fa0/1
```

Configure speed:

```bash
speed auto
```

Configure duplex:

```bash
duplex auto
```

Disable interface:

```bash
shutdown
```

Enable interface:

```bash
no shutdown
```

Configure multiple interfaces:

```bash
interface range fa0/1-24
```

---

# CCNA Exam Tips

- Switch interfaces are **enabled by default**.
- Router interfaces are **shutdown by default**.
- Modern Ethernet uses **Full Duplex**.
- **CSMA/CD** is only used in Half Duplex networks.
- Autonegotiation selects the highest supported speed and duplex.
- A **duplex mismatch** often causes CRC errors and poor performance.
- Use **show interfaces** to investigate interface counters and troubleshoot physical connectivity issues.
- Disable unused interfaces to improve network security.

---

# Key Terms

| Term | Full Form |
|------|-----------|
| Mbps | Megabits per Second |
| Gbps | Gigabits per Second |
| NIC | Network Interface Card |
| CRC | Cyclic Redundancy Check |
| FCS | Frame Check Sequence |
| CSMA/CD | Carrier Sense Multiple Access with Collision Detection |
| CLI | Command-Line Interface |
| IOS | Internetwork Operating System |
| SVI | Switch Virtual Interface |

---

# Quick Revision

- A switch interface is a Layer 2 port used to forward Ethernet frames.
- Switch ports are enabled by default.
- **Up/Up** indicates a functioning interface.
- Speed determines transmission rate; duplex determines communication direction.
- Full Duplex allows simultaneous sending and receiving.
- Half Duplex relies on CSMA/CD to handle collisions.
- Autonegotiation automatically selects the optimal speed and duplex.
- Duplex mismatches can significantly degrade network performance.
- Interface counters such as Runts, Giants, CRC, and Input Errors help diagnose physical and data-link layer issues.
- Use `show interfaces` and `show interfaces status` as your primary troubleshooting commands.
