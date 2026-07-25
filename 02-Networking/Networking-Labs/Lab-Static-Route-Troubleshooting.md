# Lab 10 - Static Route Troubleshooting
**Source:** Jeremy's IT Lab CCNA - Static Route Troubleshooting Lab

**Lab Type:** Cisco Packet Tracer

**Difficulty:** Intermediate

**Related Theory:**
- Static Routing
- Routing Tables
- Troubleshooting Methodology
- Cisco IOS Verification Commands

---

# Objective

Troubleshoot a network where two end devices cannot communicate due to router misconfigurations.

The goal is to:

- Verify connectivity.
- Identify configuration errors.
- Correct the misconfigurations.
- Restore end-to-end communication.
- Learn a structured troubleshooting approach.

---

# Network Topology

```
      LAN 1
  192.168.1.0/24

      PC1
       |
      SW1
       |
      R1
       |
 192.168.12.0/24
       |
      R2
       |
 192.168.13.0/24
       |
      R3
       |
      SW2
       |
      PC2

      LAN 2
  192.168.3.0/24
```

---

# Lab Scenario

The network topology is already configured.

However:

- PC1 cannot communicate with PC2.
- Each router contains **one configuration error**.
- Your task is to identify and fix each issue.

This lab focuses on troubleshooting rather than initial configuration.

---

# Troubleshooting Methodology

Always follow a logical sequence instead of making random configuration changes.

### Step 1

Confirm the problem.

### Step 2

Verify the end devices.

### Step 3

Check interface status.

### Step 4

Inspect the routing table.

### Step 5

Review the running configuration.

### Step 6

Correct the issue.

### Step 7

Verify the fix.

### Step 8

Test connectivity again.

---

# Step 1 - Confirm the Problem

From PC1

```bash
ping 192.168.3.1
```

Expected result

```
Request timed out
```

This confirms communication is failing.

---

# Step 2 - Verify PC Configuration

Open Command Prompt on PC1.

Display network configuration.

```bash
ipconfig
```

Displays:

- IP Address
- Subnet Mask
- Default Gateway

For more detailed information:

```bash
ipconfig /all
```

Additional information includes:

- Physical Address (MAC Address)
- DHCP status
- DNS information
- Adapter details

---

# Step 3 - Verify Local Connectivity

Test communication with the default gateway.

```bash
ping 192.168.1.254
```

If successful:

- PC configuration is correct.
- Local LAN connectivity is working.
- Continue troubleshooting the routers.

---

# Step 4 - Troubleshoot Router R1

Enter privileged EXEC mode.

```bash
enable
```

Verify interface status.

```bash
show ip interface brief
```

Result:

```
Interfaces Up/Up
```

No interface problems were found.

---

## Check Routing Table

```bash
show ip route
```

Incorrect route:

```
S 192.168.3.0/24

via 192.168.12.3
```

Problem:

The next-hop IP address is incorrect.

Correct next-hop:

```
192.168.12.2
```

---

## View Running Configuration

```bash
show running-config | include ip route
```

Current configuration:

```bash
ip route 192.168.3.0 255.255.255.0 192.168.12.3
```

---

## Remove Incorrect Route

```bash
configure terminal

no ip route 192.168.3.0 255.255.255.0 192.168.12.3
```

---

## Configure Correct Route

```bash
ip route 192.168.3.0 255.255.255.0 192.168.12.2
```

Verify:

```bash
show ip route
```

---

# Step 5 - Troubleshoot Router R2

Check interface status.

```bash
show ip interface brief
```

Interfaces are operational.

---

## Check Routing Table

```bash
show ip route
```

Incorrect route:

```
192.168.3.0/24

Exit Interface

G0/0
```

Problem:

Traffic to LAN 2 should leave through

```
G0/1
```

instead of

```
G0/0
```

---

## Configure Correct Route

If the correct route is entered without removing the incorrect one:

```bash
ip route 192.168.3.0 255.255.255.0 g0/1
```

Both routes remain.

The router may perform **Equal-Cost Load Balancing (ECMP)**, sending packets across both paths.

Since one path is incorrect, connectivity remains unreliable.

---

## Remove Incorrect Route

```bash
show running-config | include ip route
```

```bash
configure terminal

no ip route 192.168.3.0 255.255.255.0 g0/0
```

---

## Configure Correct Route

```bash
ip route 192.168.3.0 255.255.255.0 g0/1
```

Verify:

```bash
show ip route
```

---

# Step 6 - Troubleshoot Router R3

Verify interfaces.

```bash
show ip interface brief
```

Problem discovered:

```
Incorrect

192.168.23.3
```

Correct address:

```
192.168.13.3
```

---

## Correct the Interface

```bash
configure terminal

interface g0/0

ip address 192.168.13.3 255.255.255.0
```

Unlike static routes, configuring a new IP address automatically replaces the old one.

No `no ip address` command is required.

---

Verify:

```bash
show running-config
```

or

```bash
show ip interface brief
```

---

# Step 7 - Verify Routing

Display routing table.

```bash
show ip route
```

Ensure:

- Connected Routes (C)
- Local Routes (L)
- Static Routes (S)

are all present and correct.

---

# Step 8 - Final Connectivity Test

Return to PC1.

```bash
ping 192.168.3.1
```

The first ping may fail due to ARP resolution.

Subsequent replies should succeed.

Example:

```
!!!!!

Success
```

End-to-end communication has been restored.

---

# Cisco IOS Commands Practised

Enter privileged EXEC mode

```bash
enable
```

View interfaces

```bash
show ip interface brief
```

View routing table

```bash
show ip route
```

View running configuration

```bash
show running-config
```

Filter configuration

```bash
show running-config | include ip route
```

Enter global configuration

```bash
configure terminal
```

Configure interface

```bash
interface g0/0
```

Assign IP address

```bash
ip address 192.168.13.3 255.255.255.0
```

Delete static route

```bash
no ip route
```

Create static route

```bash
ip route
```

Test connectivity

```bash
ping
```

---

# Common Troubleshooting Mistakes

❌ Assuming the first device is at fault.

❌ Forgetting to verify interface status.

❌ Not checking the routing table.

❌ Forgetting to remove incorrect static routes before adding new ones.

❌ Ignoring return-path routing.

❌ Making multiple configuration changes without testing.

---

# Troubleshooting Best Practices

- Start with the end device.
- Verify Layer 1 and Layer 2 connectivity before investigating Layer 3.
- Use verification commands before making configuration changes.
- Change only one thing at a time.
- Test after every fix.
- Confirm routing in both directions.

---

# Key Concepts Learned

### Routing Table Verification

Always verify routing before modifying configurations.

---

### Static Route Removal

Static routes are removed using:

```bash
no ip route ...
```

---

### IP Address Replacement

Assigning a new IP address to an interface automatically replaces the previous one.

---

### Pipe (`|`) Filtering

The pipe operator filters command output, making troubleshooting much faster.

Example:

```bash
show running-config | include ip route
```

---

### Equal-Cost Multi-Path (ECMP)

If multiple routes to the same destination exist with equal cost, the router may perform **Equal-Cost Multi-Path (ECMP)** load balancing.

This is useful only when all configured paths are valid.

---

# Key Terms

| Abbreviation | Full Form |
|--------------|-----------|
| IP | Internet Protocol |
| MAC | Media Access Control |
| ARP | Address Resolution Protocol |
| CLI | Command-Line Interface |
| IOS | Internetwork Operating System |
| ECMP | Equal-Cost Multi-Path |

---

# Key Takeaways

- Follow a structured troubleshooting methodology instead of guessing.
- Verify PC configuration before investigating routers.
- `show ip interface brief` quickly identifies interface issues.
- `show ip route` is the primary command for routing verification.
- Remove incorrect static routes before configuring new ones.
- Pipe filtering (`| include`) greatly speeds up troubleshooting.
- Always verify changes before moving to the next device.
- Successful troubleshooting requires both correct configuration **and** systematic verification.

---

# Quick Revision

- Confirm the problem with `ping`.
- Verify PC configuration using `ipconfig`.
- Check router interfaces with `show ip interface brief`.
- Inspect the routing table using `show ip route`.
- Review configuration using `show running-config`.
- Remove incorrect routes using `no ip route`.
- Correct interface IP addresses if required.
- Verify the routing table again.
- Test end-to-end connectivity.
- Follow the **Verify → Identify → Fix → Test** troubleshooting cycle.
