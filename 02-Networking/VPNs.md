# Virtual Private Networks (VPNs)

## What is a VPN?

A **Virtual Private Network (VPN)** creates a secure, encrypted tunnel between two or more devices over an untrusted network (such as the Internet). It protects the confidentiality and integrity of transmitted data while allowing users to securely access remote networks.

---

## Why Use a VPN?

* Encrypts network traffic.
* Protects data from eavesdropping.
* Provides secure remote access.
* Helps bypass insecure public Wi-Fi networks.
* Used by organizations to connect remote employees securely.

---

## Types of VPNs

### 1. Remote Access VPN

* Connects an individual user to a private network.
* Commonly used by remote employees.
* Example: Connecting to Hack The Box using OpenVPN.

### 2. Site-to-Site VPN

* Connects two separate networks securely.
* Commonly used between company branches.

---

## Common VPN Protocols

### OpenVPN

* Open-source VPN protocol.
* Uses SSL/TLS encryption.
* Highly secure and widely adopted.
* Used by Hack The Box labs.

### IPsec (Internet Protocol Security)

Provides:

* Confidentiality
* Integrity
* Authentication

Components:

* **AH (Authentication Header)** – Provides authentication and integrity.
* **ESP (Encapsulating Security Payload)** – Provides encryption, authentication, and integrity.

Modes:

* **Transport Mode** – Encrypts only the payload.
* **Tunnel Mode** – Encrypts the entire IP packet.

### PPTP (Point-to-Point Tunneling Protocol)

* One of the earliest VPN protocols.
* Simple to configure.
* Fast but considered insecure.
* Vulnerable to modern attacks.
* Largely replaced by OpenVPN and IPsec.

---

## VPNs in Penetration Testing

VPNs allow penetration testers to securely access isolated lab environments.

Examples:

* Hack The Box
* TryHackMe
* Corporate internal assessments

Always verify the VPN interface before beginning enumeration.

Example:

```bash
ip a | grep tun0
```

---

## Key Takeaways

* VPNs provide encrypted communication over untrusted networks.
* OpenVPN is widely used for penetration testing labs.
* IPsec is commonly deployed in enterprise environments.
* PPTP is considered obsolete due to security weaknesses.
