# Network Protocols - Quick Notes

## What is a Network Protocol?

A network protocol is a standardized set of rules that allows devices to communicate reliably over a network.

Protocols define:

* Data format
* Communication rules
* Error handling
* Authentication
* Data delivery

---

## Categories of Protocols

### Web

* HTTP — HyperText Transfer Protocol
* HTTPS — HyperText Transfer Protocol Secure

---

### Remote Administration

* SSH — Secure Shell
* Telnet

---

### File Transfer

* FTP
* TFTP
* SFTP
* SMB
* NFS

---

### Email

* SMTP
* POP3
* IMAP

---

### Name Resolution

* DNS

---

### Address Assignment

* DHCP

---

### Directory Services

* LDAP
* Kerberos

---

### Network Management

* SNMP
* NTP

---

### Remote Desktop

* RDP
* VNC

---

### Voice & Multimedia

* SIP
* RTP

---

### Core Networking

* TCP
* UDP
* ICMP
* ARP
* IP

---

## Enumeration Mindset

Whenever a service is discovered:

1. Identify the protocol.
2. Determine its default port.
3. Check for anonymous or default authentication.
4. Enumerate available information.
5. Look for misconfigurations before searching for exploits.

Understanding protocols is one of the most important skills in penetration testing because every exposed port represents a potential attack surface.
