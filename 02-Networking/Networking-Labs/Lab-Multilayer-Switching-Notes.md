# Day 18 Lab – Multilayer Switching

**Topic:** Replacing Router-on-a-Stick (ROAS) with a point-to-point Layer 3 link + inter-VLAN routing via SVIs on a multilayer switch.

---

## Topology Summary

| Device | Role |
|---|---|
| SW1 | Access-layer switch, trunked to SW2 |
| SW2 | Multilayer switch (replaces old SW2 from Day 17) |
| R1 | Edge router, connects SW2 to the internet |

| VLAN | Subnet | Hosts | Location |
|---|---|---|---|
| 10 | 10.0.0.0/26 | .1, .2 | SW1 (F0/1, F0/2) |
| 10 | 10.0.0.0/26 | .3, .4 | SW2 (G1/0/4, G1/0/5) — directly attached |
| 20 | 10.0.0.64/26 | .65 | SW2 (G1/0/3) — directly attached |
| 30 | 10.0.0.128/26 | .129, .130 | SW1 (F0/3, F0/4) |

R1 ↔ SW2 link: **10.0.0.192/30** — R1 G0/0 = `.194`, SW2 G1/0/2 = `.193`

SW1 ↔ SW2: trunk (carries VLAN10 and VLAN30 across to SW2)

---

## Task 1: Replace ROAS with a Point-to-Point L3 Link

**Why:** ROAS relies on subinterfaces + trunk encapsulation to route between VLANs over one physical link. A multilayer switch can route natively, so the R1–SW2 link no longer needs to carry VLAN tags — it becomes a plain routed link between two Layer 3 interfaces.

**R1 — remove old ROAS subinterfaces, make G0/0 a routed interface:**
```
R1(config)# no interface g0/0.10
R1(config)# no interface g0/0.20
R1(config)# no interface g0/0.30
R1(config)# interface g0/0
R1(config-if)# ip address 10.0.0.194 255.255.255.252
R1(config-if)# no shutdown
```

**SW2 — convert G1/0/2 from trunk to routed port:**
```
SW2(config)# interface g1/0/2
SW2(config-if)# no switchport
SW2(config-if)# ip address 10.0.0.193 255.255.255.252
SW2(config-if)# no shutdown
```
`no switchport` is the key command — it strips Layer 2 (switching) behavior off the port and turns it into a Layer 3 routed interface, same as a router port.

**Default route on SW2 (next hop = R1's G0/0):**
```
SW2(config)# ip route 0.0.0.0 0.0.0.0 10.0.0.194
```

---

## Task 2: Configure SVIs on SW2

**Why:** An SVI (Switch Virtual Interface) is a virtual Layer 3 interface bound to a VLAN — it acts as that VLAN's default gateway. Requires `ip routing` enabled globally, or the switch will only ever behave as Layer 2.

```
SW2(config)# ip routing
```

**Subnetting — last usable address per /26:**

| VLAN | Subnet | Broadcast | Last usable (SVI IP) |
|---|---|---|---|
| 10 | 10.0.0.0/26 | .63 | **10.0.0.62** |
| 20 | 10.0.0.64/26 | .127 | **10.0.0.126** |
| 30 | 10.0.0.128/26 | .191 | **10.0.0.190** |

*(last usable = broadcast address − 1)*

```
SW2(config)# interface vlan10
SW2(config-if)# ip address 10.0.0.62 255.255.255.192
SW2(config-if)# no shutdown

SW2(config)# interface vlan20
SW2(config-if)# ip address 10.0.0.126 255.255.255.192
SW2(config-if)# no shutdown

SW2(config)# interface vlan30
SW2(config-if)# ip address 10.0.0.190 255.255.255.192
SW2(config-if)# no shutdown
```

**Note:** an SVI only comes up if that VLAN exists on the switch *and* has at least one active port — VLAN10/20 come up immediately (directly attached hosts), VLAN30 comes up via the trunk to SW1.

---

## Task 3: Update PC Default Gateways

Old ROAS gateways no longer apply — each VLAN's gateway is now the SVI's last-usable address. Set via **Desktop → IP Configuration** on each PC:

| Host(s) | New Default Gateway |
|---|---|
| VLAN10 (.1, .2, .3, .4) | 10.0.0.62 |
| VLAN20 (.65) | 10.0.0.126 |
| VLAN30 (.129, .130) | 10.0.0.190 |

**Why it matters:** a host only forwards traffic to its gateway when the destination is outside its own subnet. Wrong/stale gateway = inter-VLAN traffic never leaves the source host correctly, regardless of how correct the switch config is.

---

## Task 4: Verification

**On SW2:**
```
show ip route
show ip interface brief
show vlan brief
```
Confirmed:
- `C 10.0.0.192/30` + `S* 0.0.0.0/0 via 10.0.0.194` — routed link + default route up
- `C`/`L` entries for `10.0.0.0/26`, `.64/26`, `.128/26` via Vlan10/20/30 — SVIs active
- G1/0/2 shows `up/up`, method `manual`

**Inter-VLAN ping tests (host to host, different VLANs):**
```
ping 10.0.0.130   ' VLAN10 → VLAN30
ping 10.0.0.65    ' VLAN30 → VLAN20
ping 10.0.0.3     ' VLAN20 → VLAN10 (SW2-side host)
```
All successful — confirms SVIs are routing correctly and the SW1↔SW2 trunk is passing VLAN10/30 traffic.

**Internet reachability:**
```
ping 1.1.1.1
```
Path: PC → SVI gateway → SW2 default route → R1 (10.0.0.194) → Internet router → 1.1.1.1, with a working return path already configured on R1 and the internet router. Successful — confirms end-to-end connectivity including the return path (no asymmetric routing issue).

---

## Key Concepts / Takeaways

- **`no switchport`** — converts a switch port into a Layer 3 routed port (no VLAN/trunk behavior).
- **`ip routing`** — required on a multilayer switch before SVIs will route between VLANs; without it, the switch stays purely Layer 2.
- **SVI vs. ROAS subinterface** — both act as a VLAN's gateway, but an SVI lives on the switch itself (native routing), while ROAS relies on a router's subinterfaces + trunk encapsulation over one physical link.
- **Last usable address** = broadcast address − 1; broadcast = first address of the *next* block − 1.
- **Default route (`0.0.0.0/0`)** = "gateway of last resort" — used when no more specific route matches.
- Always re-check PC default gateways after re-addressing SVIs — a correct switch config won't help if the host is still pointed at the old gateway.
