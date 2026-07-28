# ============================================================
# CCNA Notes
# Topic: Variable Length Subnet Masking (VLSM)
# Date: 2026-07-28
# Last Updated: 2026-07-28
# Source: Jeremy's IT Lab CCNA - Day 15
# ============================================================

# Variable Length Subnet Masking (VLSM)

## Overview

Variable Length Subnet Masking (VLSM) allows different subnet sizes to be created within the same network. Instead of assigning equal-sized subnets, each subnet receives only the number of IP addresses it requires, resulting in efficient IPv4 address utilisation.

---

## Learning Objectives

By the end of this topic, you should be able to:

- Understand the purpose of VLSM.
- Allocate IP addresses efficiently.
- Design networks with different host requirements.
- Perform VLSM calculations.
- Avoid overlapping subnets.

---

## Prerequisites

- IPv4 Addressing Fundamentals
- CIDR Notation
- Basic Subnetting
- Host & Subnet Calculations

---

## Topics Covered

- Introduction to VLSM
- Why VLSM is Used
- VLSM Workflow
- VLSM Address Planning
- VLSM Practice Questions
- VLSM Packet Tracer Lab

---

# What is VLSM?

VLSM (Variable Length Subnet Masking) is the process of assigning different subnet masks to different networks based on their host requirements.

Unlike Fixed Length Subnet Masking (FLSM), VLSM does not require every subnet to be the same size.

---

# Why Use VLSM?

Without VLSM:

- Wastes IPv4 addresses.
- Every subnet has the same size.
- Poor address utilisation.

With VLSM:

- Conserves IPv4 addresses.
- Allocates only the required number of hosts.
- Supports networks of different sizes.
- Simplifies network expansion.

---

# VLSM Workflow

Follow these steps when solving VLSM problems:

1. Identify the available network.
2. List all required LANs and WAN links.
3. Determine the number of hosts required for each network.
4. Sort the networks from largest to smallest.
5. Allocate the largest subnet first.
6. Continue allocating the remaining subnets.
7. Verify that no subnet ranges overlap.

---

# VLSM Example

**Available Network**

```
192.168.10.0/24
```

**Host Requirements**

| Network | Hosts Required |
|----------|---------------:|
| LAN 1 | 60 |
| LAN 2 | 25 |
| LAN 3 | 10 |
| WAN Link | 2 |

**Allocation Order**

| Hosts | Prefix |
|-------:|:------|
| 60 | /26 |
| 25 | /27 |
| 10 | /28 |
| 2 | /30 |

Always allocate the **largest subnet first** to maximise address efficiency.

---

# VLSM Best Practices

- Allocate subnets from largest to smallest.
- Keep subnet boundaries aligned.
- Record every allocated subnet.
- Verify network and broadcast addresses.
- Ensure no address ranges overlap.

---

# Advantages

- Efficient IPv4 address utilisation.
- Reduces address wastage.
- Supports networks with different sizes.
- Scalable and flexible.
- Commonly used in enterprise environments.

---

# Common Mistakes

- Allocating smaller subnets before larger ones.
- Overlapping subnet ranges.
- Choosing an incorrect prefix length.
- Miscalculating usable hosts.
- Forgetting to verify subnet boundaries.

---

# CCNA Exam Tips

- Sort host requirements before starting.
- Allocate the largest subnet first.
- Double-check every network and broadcast address.
- Verify remaining address space after each allocation.
- Show all calculations to reduce mistakes.

---

# Cybersecurity Relevance

VLSM is widely used in:

- Enterprise Network Design
- VLAN Deployments
- DMZ Networks
- Branch Office Networks
- IP Address Planning
- Internal Network Segmentation

---

# Key Takeaways

- VLSM assigns different subnet sizes based on host requirements.
- Always allocate the largest subnet first.
- VLSM conserves IPv4 address space.
- Proper planning prevents overlapping subnets.
- VLSM is a fundamental skill for CCNA, enterprise networking, and cybersecurity.
