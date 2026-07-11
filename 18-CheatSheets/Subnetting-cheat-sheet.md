# IPv4 Subnetting Cheat Sheet

## Seven CIDRs to Memorize

| CIDR | Subnet Mask     | Block Size | Usable Hosts |
| ---- | --------------- | ---------: | -----------: |
| /24  | 255.255.255.0   |        256 |          254 |
| /25  | 255.255.255.128 |        128 |          126 |
| /26  | 255.255.255.192 |         64 |           62 |
| /27  | 255.255.255.224 |         32 |           30 |
| /28  | 255.255.255.240 |         16 |           14 |
| /29  | 255.255.255.248 |          8 |            6 |
| /30  | 255.255.255.252 |          4 |            2 |

## Fast Rules

* Block Size = 256 − Last Subnet Mask Octet.
* Network Address = Largest subnet boundary less than or equal to the host IP.
* Broadcast Address = Next subnet − 1.
* First Host = Network + 1.
* Last Host = Broadcast − 1.
* Usable Hosts = 2^(32 − CIDR) − 2.

## Block Size Reference

| Mask | Block Size |
| ---- | ---------: |
| 128  |        128 |
| 192  |         64 |
| 224  |         32 |
| 240  |         16 |
| 248  |          8 |
| 252  |          4 |
| 254  |          2 |

## VLSM Workflow

1. Sort host requirements from largest to smallest.
2. Choose the smallest subnet that fits each requirement.
3. Allocate the subnet at the next available address.
4. Continue from the next available network.
5. Ensure no subnet overlaps another.

## Mental Workflow

CIDR → Subnet Mask → Block Size → Network Boundary → Broadcast → Host Range
