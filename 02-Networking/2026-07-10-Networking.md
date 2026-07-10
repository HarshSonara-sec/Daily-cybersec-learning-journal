# Networking Fundamentals – Study Notes

**Date:** July 10, 2026

## Topics Covered

* Introduction to Computer Networks
* IPv4 Addressing
* Public vs. Private IP Addresses
* MAC Addresses
* Routers and Switches
* ICMP (`ping`)
* OSI Model
* TCP vs UDP
* DNS (Domain Name System)
* DHCP (Dynamic Host Configuration Protocol)
* ARP (Address Resolution Protocol)

## Key Notes

* Networks allow devices to communicate and share resources.
* IP addresses identify devices, while MAC addresses identify network interfaces on a local network.
* Routers connect different networks; switches connect devices within the same LAN.
* ICMP is used for connectivity testing and network diagnostics.
* The OSI model divides network communication into seven layers for easier understanding and troubleshooting.
* TCP is connection-oriented and reliable, whereas UDP is faster but does not guarantee delivery.
* DNS translates domain names into IP addresses.
* DHCP automatically assigns IP addresses and other network configuration to devices.
* ARP resolves IPv4 addresses to MAC addresses within a local network.

## Commands Practiced

```bash
ip a
ip route
ping <target>
```

## Security Perspective

A strong understanding of networking is the foundation of cybersecurity. Concepts such as IP addressing, DNS, ARP, TCP, and UDP are essential for network enumeration, vulnerability assessment, traffic analysis, and incident response.

## Topics to Review

* CIDR Notation & Subnetting
* Common Ports & Services
* NAT (Network Address Translation)
* Traceroute
* Wireshark Packet Analysis
