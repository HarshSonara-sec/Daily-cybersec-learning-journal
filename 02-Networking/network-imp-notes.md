# Networking Theory Notes

---

# Vendor Specific Information

## Cisco

Cisco is one of the world's largest networking equipment manufacturers.

### Cisco IOS

Full Form:

Internetwork Operating System

Purpose:

Operating system used on Cisco routers and switches.

Provides:

- Device configuration
- Routing
- Switching
- Security
- Network management

---

### Cisco CLI

Full Form:

Command Line Interface

Purpose:

Text-based interface used to configure Cisco devices.

Modes include:

- User EXEC
- Privileged EXEC
- Global Configuration
- Interface Configuration

---

### Cisco Protocols

Examples include:

- CDP (Cisco Discovery Protocol)
- VTP (VLAN Trunking Protocol)
- DTP (Dynamic Trunking Protocol)
- EIGRP (Enhanced Interior Gateway Routing Protocol)

These are proprietary Cisco protocols.

---

# VLAN

Full Form

Virtual Local Area Network

Purpose

Logically separates a physical network into multiple broadcast domains.

Advantages

- Improved security
- Reduced broadcasts
- Better network management
- Easier segmentation

---

## VLAN Membership

Determines which devices belong to a VLAN.

Membership can be:

- Static
- Dynamic

---

## VLAN Identification

Each VLAN is assigned a unique VLAN ID.

Examples

VLAN 10

VLAN 20

VLAN IDs range from 1–4094.

---

# Key Exchange Mechanisms

## DH

Diffie-Hellman

Allows two parties to establish a shared secret over an insecure network.

---

## ECDH

Elliptic Curve Diffie-Hellman

A more efficient version of Diffie-Hellman using Elliptic Curve Cryptography.

---

## RSA

Rivest-Shamir-Adleman

Public-key cryptographic algorithm used for encryption and digital signatures.

---

## ECDSA

Elliptic Curve Digital Signature Algorithm

Used to generate and verify digital signatures.

---

## IKE

Internet Key Exchange

Used by IPsec VPNs to negotiate encryption keys.

---

## PSK

Pre-Shared Key

A password shared between communicating parties before connection.

---

# Authentication Protocols

## Kerberos

Network authentication protocol that uses secret-key cryptography and ticket-based authentication.

---

## SRP

Secure Remote Password

Password-authenticated key exchange protocol.

---

## SSL

Secure Sockets Layer

Deprecated protocol previously used to secure communications.

---

## TLS

Transport Layer Security

Modern replacement for SSL.

Provides:

- Encryption
- Authentication
- Integrity

---

## OAuth

Open Authorization

Allows third-party applications to access user resources without sharing passwords.

---

## OpenID

OpenID Connect

Authentication layer built on top of OAuth 2.0.

---

## SAML

Security Assertion Markup Language

XML-based authentication standard commonly used for enterprise Single Sign-On.

---

## 2FA

Two-Factor Authentication

Requires two different authentication factors.

---

## MFA

Multi-Factor Authentication

Requires two or more authentication factors.

---

## FIDO

Fast Identity Online

Passwordless authentication standard.

---

## PKI

Public Key Infrastructure

Framework used to manage digital certificates and public-key encryption.

---

## SSO

Single Sign-On

Allows users to authenticate once and access multiple applications.

---

## PAP

Password Authentication Protocol

Simple authentication protocol that sends passwords in plaintext.

Not secure.

---

## CHAP

Challenge Handshake Authentication Protocol

Uses challenge-response authentication.

More secure than PAP.

---

## EAP

Extensible Authentication Protocol

Framework supporting multiple authentication methods.

Commonly used in wireless networks.

---

## SSH

Secure Shell

Secure remote administration protocol.

Default Port:

22

---

## HTTPS

HyperText Transfer Protocol Secure

HTTP secured using TLS.

Default Port:

443

---

## LEAP

Lightweight Extensible Authentication Protocol

Cisco proprietary wireless authentication protocol.

Now considered insecure.

---

## PEAP

Protected Extensible Authentication Protocol

Encapsulates EAP within a TLS tunnel.

---

## EAP-TLS

Extensible Authentication Protocol - Transport Layer Security

Certificate-based authentication method.

One of the most secure EAP methods.

---

# TCP vs UDP

## TCP

Transmission Control Protocol

Characteristics

- Connection-oriented
- Reliable
- Ordered delivery
- Error checking
- Flow control
- Retransmissions

Common Uses

- HTTP
- HTTPS
- SSH
- FTP

---

## UDP

User Datagram Protocol

Characteristics

- Connectionless
- Faster
- No guaranteed delivery
- Lower overhead

Common Uses

- DNS
- VoIP
- Video streaming
- Online gaming

---

# IP Packet

An IP packet consists of:

- IP Header
- Payload

---

## IP Header

Contains routing information including:

- Source IP
- Destination IP
- TTL
- Protocol
- Flags
- Header Length

---

## Payload

Actual data being transported by the packet.

---

## Record Route Field

Optional IPv4 header field.

Records routers traversed by the packet for troubleshooting.

Rarely used today due to security and performance concerns.

---

## Blind Spoofing

Attack where an attacker sends packets with a forged source IP address without seeing responses.

Often used in denial-of-service attacks.

---

# Introduction to Cryptography

Cryptography protects data confidentiality, integrity, and authenticity.

---

## Symmetric Encryption

Uses one shared key for encryption and decryption.

Advantages

- Fast
- Efficient

Examples

- DES
- AES

---

## Asymmetric Encryption

Uses two keys.

- Public Key
- Private Key

Used for:

- Secure key exchange
- Digital signatures

---

## Public Key Encryption

Anyone can encrypt using the public key.

Only the private key owner can decrypt.

---

## DES

Data Encryption Standard

56-bit symmetric encryption algorithm.

Now considered insecure.

---

## AES

Advanced Encryption Standard

Modern symmetric encryption standard.

Common key sizes:

- 128-bit
- 192-bit
- 256-bit

---

# Cipher Modes

## ECB

Electronic Codebook

Simple but insecure due to repeating patterns.

---

## CBC

Cipher Block Chaining

Each block depends on the previous encrypted block.

---

## CFB

Cipher Feedback

Converts a block cipher into a stream cipher.

---

## OFB

Output Feedback

Generates a keystream independent of plaintext.

---

## CTR

Counter Mode

Uses incrementing counters.

Highly parallelizable and efficient.

---

## GCM

Galois/Counter Mode

Provides:

- Confidentiality
- Integrity
- Authentication

Widely used in TLS and modern secure communication protocols.
