# EtherChannel

## What is EtherChannel?

- Combines multiple physical links into a single logical link.
- Increases bandwidth.
- Provides link redundancy.
- Prevents unnecessary STP blocking.

---

## EtherChannel Modes

### Static
- Manual configuration.
- No negotiation protocol.

### PAgP (Port Aggregation Protocol)
- Cisco proprietary.
- Modes:
  - Desirable
  - Auto

### LACP (Link Aggregation Control Protocol)
- IEEE 802.3ad (802.1AX)
- Industry standard.
- Modes:
  - Active
  - Passive

---

## Requirements

- Same interface speed.
- Same duplex settings.
- Same VLAN/trunk configuration.
- Same switchport mode.
- Interfaces should belong to the same switch.

---

## Advantages

- Increased bandwidth.
- Link redundancy.
- Load balancing.
- Faster failover.
- Simplifies network management.

---

## Enterprise Use Cases

- Switch-to-switch uplinks.
- Core to Distribution switches.
- Distribution to Access switches.
- Server NIC teaming.
- Storage network connections.

---

## Verification Commands

```cisco
show etherchannel summary
show etherchannel port-channel
show interfaces trunk
show spanning-tree
```

---

## Best Practices

- Prefer LACP in enterprise environments.
- Configure all member interfaces identically.
- Verify Port-Channel status after configuration.
- Monitor failed member links.

---

## Key Takeaways

- EtherChannel increases both bandwidth and availability.
- STP treats the Port-Channel as a single logical interface.
- LACP is the preferred EtherChannel protocol for enterprise networks.
- Understanding EtherChannel concepts is more valuable than memorizing Packet Tracer configurations.
