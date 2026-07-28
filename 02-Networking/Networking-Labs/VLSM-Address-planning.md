# ============================================================
# CCNA Lab
# Lab 2 - VLSM Address Planning
# Date: 2026-07-28
# Last Updated: 2026-07-28
# Source: Jeremy's IT Lab CCNA - Day 15
# ============================================================

# Lab 2 - VLSM Address Planning

## Objective

Design and implement an efficient IPv4 addressing scheme using Variable Length Subnet Masking (VLSM) to meet different host requirements while minimising address wastage.

---

## Lab Overview

This Packet Tracer lab focused on planning and allocating IP address space using VLSM. Networks with different host requirements were assigned appropriately sized subnets, ensuring efficient IPv4 address utilisation without overlapping address ranges.

---

## Skills Practised

- VLSM address planning
- Host requirement analysis
- Prefix length selection
- Network allocation
- Broadcast address calculation
- Usable host range calculation
- Address verification

---

## VLSM Workflow

1. Identify the available network address.
2. List all LANs and their host requirements.
3. Sort host requirements from largest to smallest.
4. Allocate the largest subnet first.
5. Continue assigning the remaining subnets.
6. Calculate:
   - Network Address
   - First Usable Host
   - Last Usable Host
   - Broadcast Address
7. Verify that no subnet ranges overlap.

---

## Key Observations

- Larger networks require smaller prefix lengths (more host bits).
- Smaller networks can use larger prefix lengths (fewer host bits).
- Allocating subnets in descending order prevents address fragmentation.
- Careful planning ensures efficient use of the available IPv4 address space.

---

## Verification

- Verified all subnet boundaries.
- Confirmed correct network and broadcast addresses.
- Checked usable host ranges for each subnet.
- Ensured there were no overlapping subnet allocations.

---

## Key Learning

- VLSM allows different subnet sizes within the same network.
- Address planning should always begin with the largest host requirement.
- Correct subnet allocation improves scalability and conserves IPv4 addresses.
- Accurate calculations are essential to avoid addressing conflicts.

---

## Troubleshooting Notes

- Recalculate host requirements before selecting a prefix length.
- Verify subnet increments to prevent overlapping ranges.
- Double-check the network and broadcast addresses for every subnet.
- Ensure enough usable host addresses are available for each network.

---

## Conclusion

This lab demonstrated how VLSM provides a flexible and efficient approach to IPv4 addressing. By allocating subnets based on actual host requirements, networks can minimise address wastage while remaining scalable and easy to manage.
