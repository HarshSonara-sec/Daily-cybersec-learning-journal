# CCNA Lab Debugging Notes -- VLSM & Static Routing

**Date:** 2026-07-28

## Objective

Configure VLSM for `192.168.5.0/24`, assign IPs, configure static
routes, and verify end-to-end connectivity.

## VLSM Layout

  Network   Prefix             Router IP           PC IP
  --------- ------------------ ------------------- -------------------
  LAN2      192.168.5.0/25     192.168.5.126       192.168.5.1
  LAN1      192.168.5.128/26   192.168.5.190       192.168.5.129
  LAN3      192.168.5.192/28   192.168.5.206       192.168.5.193
  LAN4      192.168.5.208/28   192.168.5.222       192.168.5.209
  R1--R2    192.168.5.224/30   R1: 192.168.5.226   R2: 192.168.5.225

## Problems Encountered

-   Ping failures between LANs.
-   Error: `%Invalid next hop address (it's this router)`.
-   Incorrect static route masks on R2 (`/28` used instead of `/25` and
    `/26`).
-   Initially suspected subnetting, but issue was routing.

## Root Cause

1.  Used the router's own IP as the next hop.
2.  Wrong destination subnet masks in static routes.
3.  Needed systematic troubleshooting instead of changing multiple
    things at once.

## Correct Static Routes

### R1

``` bash
ip route 192.168.5.192 255.255.255.240 192.168.5.225
ip route 192.168.5.208 255.255.255.240 192.168.5.225
```

### R2

``` bash
ip route 192.168.5.0 255.255.255.128 192.168.5.226
ip route 192.168.5.128 255.255.255.192 192.168.5.226
```

## Commands Used

``` bash
show ip interface brief
show ip route
show running-config
ping <ip>
traceroute <ip>

conf t
interface g0/0/0
ip address 192.168.5.226 255.255.255.252
no shutdown

interface g0/0/0
ip address 192.168.5.225 255.255.255.252
no shutdown

no ip route <destination> <mask> <next-hop>
ip route <destination> <mask> <next-hop>
```

## Troubleshooting Process

1.  Verified interface status (`show ip interface brief`) → all `up/up`.
2.  Verified WAN connectivity (R1 ↔ R2 ping).
3.  Checked routing tables (`show ip route`).
4.  Corrected invalid next-hop usage.
5.  Corrected destination subnet masks.
6.  Verified PC IP, subnet mask and default gateway.
7.  Tested hop-by-hop:
    -   PC → Gateway
    -   R1 LAN → R1 WAN
    -   R1 WAN → R2 WAN
    -   R2 WAN → R2 LAN
    -   Destination PC

## Key Lessons

-   Static route syntax:
    `ip route <destination-network> <destination-mask> <neighbor-router-IP>`
-   The subnet mask in a static route is **the destination network's
    mask**, not the WAN mask.
-   Never use the local router's own IP as the next hop.
-   Read Cisco error messages carefully---they often identify the exact
    mistake.

## Troubleshooting Checklist

-   [ ] Interfaces up/up?
-   [ ] Correct IP/subnet mask?
-   [ ] Correct default gateway?
-   [ ] WAN link reachable?
-   [ ] Static routes present?
-   [ ] Correct next hop?
-   [ ] Correct destination mask?
-   [ ] Test one hop at a time.

## Git Commit Suggestion

``` text
docs: add CCNA Day 15 VLSM and static routing troubleshooting notes
```
