# VLAN Trunking & Router-on-a-Stick Lab

Packet Tracer lab covering inter-VLAN routing across two switches using 802.1Q trunking and router subinterfaces.

## Topology

- **SW1**
  - F0/1, F0/2 → VLAN10 (10.0.0.0/26) — PCs .1, .2
  - F0/3, F0/4 → VLAN30 (10.0.0.128/26) — PCs .129, .130
  - G0/1 → trunk to SW2
- **SW2**
  - F0/1 → VLAN20 (10.0.0.64/26) — PC .65
  - F0/2, F0/3 → VLAN10 (10.0.0.0/26) — PCs .3, .4
  - G0/1 → trunk to SW1
  - G0/2 → trunk to R1
- **R1**
  - G0/0 → router-on-a-stick to SW2, subinterfaces per VLAN

## Task 1 — Access Ports

**SW1**
```
interface range fastEthernet0/1-2
 switchport mode access
 switchport access vlan 10
interface range fastEthernet0/3-4
 switchport mode access
 switchport access vlan 30
```

**SW2**
```
interface fastEthernet0/1
 switchport mode access
 switchport access vlan 20
interface range fastEthernet0/2-3
 switchport mode access
 switchport access vlan 10
```

## Task 2 — SW1 ↔ SW2 Trunk

VLAN10 and VLAN30 need to cross this link (VLAN20 stays local to SW2). VLAN99 used as unused native VLAN.

**Both switches** — create VLANs first:
```
vlan 10
vlan 30
vlan 99
```
(SW2 also needs `vlan 20` for its access port.)

**SW1 G0/1** (mirror on SW2 G0/1):
```
interface gigabitEthernet0/1
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,30,99
```

## Task 3 — SW2 ↔ R1 (Router-on-a-Stick)

All three VLANs must cross this link.

**SW2 G0/2:**
```
interface gigabitEthernet0/2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

**R1** — subinterfaces use the last usable address of each /26:

| VLAN | Subnet | Subinterface IP |
|---|---|---|
| 10 | 10.0.0.0/26 | 10.0.0.62 |
| 20 | 10.0.0.64/26 | 10.0.0.126 |
| 30 | 10.0.0.128/26 | 10.0.0.190 |

```
interface gigabitEthernet0/0
 no shutdown
interface gigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.0.0.62 255.255.255.192
interface gigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 10.0.0.126 255.255.255.192
interface gigabitEthernet0/0.30
 encapsulation dot1Q 30
 ip address 10.0.0.190 255.255.255.192
```

## Task 4 — Test Connectivity

Each PC's IP config:

| VLAN | PCs | Subnet Mask | Gateway |
|---|---|---|---|
| 10 | .1, .2, .3, .4 | 255.255.255.192 | 10.0.0.62 |
| 20 | .65 | 255.255.255.192 | 10.0.0.126 |
| 30 | .129, .130 | 255.255.255.192 | 10.0.0.190 |

Test with `ping <ip>` from any PC's command prompt. All PCs should reach each other.

**Troubleshooting checklist if a ping fails:**
- `show ip interface brief` on R1 — subinterfaces should be up/up
- `show vlan brief` on both switches — confirm correct port-to-VLAN mapping
- `show interfaces trunk` on SW1/SW2 — confirm correct allowed VLANs on each trunk
- Double-check PC gateway/mask for typos
