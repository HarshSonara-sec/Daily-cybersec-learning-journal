# WireGuard VPN with Proton VPN on Kali Linux

## Objective
Set up and verify a manual Proton VPN connection using WireGuard on Kali Linux, including IPv4/IPv6 tunneling, VPN DNS, policy-based routing, and a fail-closed kill switch.

## Environment
- Kali Linux Rolling
- Proton VPN
- WireGuard
- Wi-Fi interface: `wlan0`
- VPN interface: `proton`

## WireGuard Setup
```bash
sudo apt install wireguard
sudo modprobe wireguard
lsmod | grep wireguard
wg --version
```

## Proton WireGuard Configuration
Generate the configuration through Proton VPN's official configuration generator.

Typical structure:
```ini
[Interface]
PrivateKey = <keep secret>
Address = 10.2.0.2/32
DNS = 10.2.0.1

[Peer]
PublicKey = <server public key>
AllowedIPs = 0.0.0.0/0, ::/0
Endpoint = <VPN_SERVER>:51820
PersistentKeepalive = 25
```

- `PrivateKey` must never be shared or committed to Git.
- `AllowedIPs = 0.0.0.0/0, ::/0` creates a full IPv4 + IPv6 tunnel.
- `DNS` specifies the VPN DNS resolver.

## Store Configuration Securely
```bash
sudo mkdir -p /etc/wireguard
sudo cp ~/Downloads/<config>.conf /etc/wireguard/proton.conf
sudo chmod 600 /etc/wireguard/proton.conf
```

## Start and Verify
```bash
sudo wg-quick up proton
sudo wg show proton
```

A recent `latest handshake` and increasing transfer counters indicate active communication with the VPN peer.

## Policy-Based Routing
```bash
ip rule
ip -6 rule
ip route show table all
ip -6 route show table all
```

WireGuard can use an `fwmark` and dedicated routing table to send normal traffic through the VPN while keeping the VPN's own encrypted packets outside the tunnel.

## Verify VPN Routing
```bash
curl -4 https://icanhazip.com
curl -6 https://icanhazip.com
resolvectl status
```

Verify that IPv4 changes, IPv6 does not expose the original connection, DNS uses the VPN, and the WireGuard handshake is recent.

## Fail-Closed Kill Switch
A full-tunnel VPN does not automatically guarantee a kill switch.

Goal:
```text
VPN UP   → traffic allowed through VPN
VPN DOWN → direct Internet traffic blocked
```

Use `PostUp`/`PostDown` firewall rules to enforce this behavior. Cover both IPv4 and IPv6.

## Kill-Switch Test
```bash
sudo wg-quick down proton
curl -4 --max-time 5 https://icanhazip.com
curl -6 --max-time 5 https://icanhazip.com
```

Expected: direct Internet traffic is blocked.

Reconnect:
```bash
sudo wg-quick up proton
sudo wg show proton
```

## Key Concepts
- WireGuard VPN
- Public/private key cryptography
- Full-tunnel routing
- `AllowedIPs`
- Policy-based routing
- `fwmark`
- Routing tables
- IPv4/IPv6 leak prevention
- VPN DNS
- Firewall rules
- Fail-closed security
- Kill switches
- Verification and testing

## Security Lessons
1. VPN privacy is not the same as complete anonymity.
2. Full-tunnel routing does not automatically mean a kill switch.
3. IPv6 must be tested separately.
4. DNS must be verified rather than assumed.
5. Never expose a WireGuard private key.
6. Verify VPN behavior through routing, IP, DNS, and failure tests.

## Practical Result
Successfully configured and tested a manual Proton VPN WireGuard connection on Kali Linux with full IPv4/IPv6 tunneling, VPN DNS, policy-based routing, firewall-based fail-closed behavior, and a successful kill-switch test.
