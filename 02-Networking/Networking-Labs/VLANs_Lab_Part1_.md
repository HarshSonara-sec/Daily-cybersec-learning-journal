# VLANs Lab (Part 1) -- My Notes

**Date:** 2026-07-30

## Objective

Today I configured a basic multi-VLAN network in Cisco Packet Tracer
using one router interface per VLAN (three physical links between R1 and
SW1).

## Topology

-   VLAN 10 -- Engineering -- 10.0.0.0/26
-   VLAN 20 -- HR -- 10.0.0.64/26
-   VLAN 30 -- Sales -- 10.0.0.128/26

Gateway = **Last usable IP** of each subnet.

  VLAN   Gateway
  ------ ------------
  10     10.0.0.62
  20     10.0.0.126
  30     10.0.0.190

## PC Configuration

  Device      IP           Mask              Gateway
  ----------- ------------ ----------------- ------------
  Eng PC1     10.0.0.1     255.255.255.192   10.0.0.62
  Eng PC2     10.0.0.2     255.255.255.192   10.0.0.62
  HR PC1      10.0.0.65    255.255.255.192   10.0.0.126
  HR PC2      10.0.0.66    255.255.255.192   10.0.0.126
  Sales PC1   10.0.0.129   255.255.255.192   10.0.0.190
  Sales PC2   10.0.0.130   255.255.255.192   10.0.0.190

## Router Configuration

``` text
enable
configure terminal

interface g0/0
 ip address 10.0.0.62 255.255.255.192
 no shutdown
exit

interface g0/1
 ip address 10.0.0.126 255.255.255.192
 no shutdown
exit

interface g0/2
 ip address 10.0.0.190 255.255.255.192
 no shutdown
exit

end
copy running-config startup-config
```

## Switch Configuration

``` text
enable
configure terminal

vlan 10
 name Engineering
exit

vlan 20
 name HR
exit

vlan 30
 name Sales
exit
```

### Access Ports

-   Fa3/1, Fa4/1 -\> VLAN 10
-   Fa5/1, Fa6/1 -\> VLAN 20
-   Fa7/1, Fa8/1 -\> VLAN 30
-   Gi0/1 -\> VLAN 10 (to R1)
-   Gi1/1 -\> VLAN 20 (to R1)
-   Gi2/1 -\> VLAN 30 (to R1)

Example:

``` text
interface fa3/1
 switchport mode access
 switchport access vlan 10
exit
```

## Verification

-   Ping within VLAN ✔
-   Ping across VLANs through R1 ✔
-   Broadcast ping in Simulation Mode reached only devices in the same
    VLAN ✔

## What I Learned

-   A /26 subnet has 64 addresses (62 usable).
-   The last usable address can be used as the default gateway.
-   VLANs create separate broadcast domains.
-   Inter-VLAN communication requires Layer 3 routing.
-   When using one physical router interface per VLAN, the switch ports
    connecting to the router are configured as access ports in the
    matching VLAN.

## Commands to Remember

``` text
enable
configure terminal
vlan <id>
name <name>
interface <port>
switchport mode access
switchport access vlan <id>
ip address <ip> <mask>
no shutdown
copy running-config startup-config
```
