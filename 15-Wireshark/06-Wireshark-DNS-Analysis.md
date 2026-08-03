# Wireshark DNS Analysis

> **Category:** Network Analysis
>
> **Difficulty:** Beginner → Intermediate
>
> **Prerequisites:**
>
> - Wireshark Fundamentals
> - Display Filters
> - Protocol Analysis
> - Basic DNS Knowledge
>
> **Recommended Before:**
>
> - 01-Wireshark-Fundamentals.md
> - 02-Wireshark-Display-Filters.md
> - 03-Wireshark-Capture-Filters.md
> - 04-Wireshark-Protocol-Analysis.md
> - 05-Wireshark-TCP-Analysis.md
>
> **Recommended After:**
>
> - 07-Wireshark-HTTP-HTTPS.md

---

# What is DNS?

**Domain Name System (DNS)** translates human-readable domain names into IP addresses.

Instead of remembering:

```
142.250.183.110
```

Users simply visit:

```
google.com
```

DNS acts like the Internet's phonebook.

---

# Why Analyze DNS?

DNS is involved in almost every network connection.

Analyzing DNS helps:

- Troubleshoot website connectivity
- Detect malware communications
- Identify malicious domains
- Investigate phishing attacks
- Monitor DNS tunneling
- Verify name resolution

DNS analysis is one of the first steps during incident response.

---

# How DNS Works

Example:

```
User enters

google.com

↓

DNS Resolver

↓

Root DNS Server

↓

TLD Server (.com)

↓

Authoritative Name Server

↓

IP Address Returned

↓

Browser Connects
```

---

# DNS Query Process

Typical sequence:

```
Client

↓

DNS Query

↓

DNS Server

↓

DNS Response

↓

Client Connects to IP
```

---

# Recursive Resolution

The DNS resolver performs all lookups on behalf of the client.

```
Client

↓

Resolver

↓

Internet DNS Servers

↓

Resolver

↓

Client
```

This is the most common method used by operating systems.

---

# Iterative Resolution

The DNS server returns referrals instead of performing all lookups.

Example:

```
Ask Root Server

↓

Go to .com Server

↓

Go to Authoritative Server

↓

Receive Answer
```

---

# DNS Packet Structure

A DNS packet contains:

- Transaction ID
- Flags
- Questions
- Answers
- Authority Records
- Additional Records

Each section can be expanded within Wireshark.

---

# Transaction ID

Every DNS query receives a unique Transaction ID.

Purpose:

- Match responses with requests.
- Detect unsolicited or forged responses.

Example:

```
Transaction ID

0x4f2a
```

The response should contain the same Transaction ID as the request.

---

# DNS Flags

Important flags include:

| Flag | Description |
|------|-------------|
| QR | Query (0) or Response (1) |
| AA | Authoritative Answer |
| TC | Message Truncated |
| RD | Recursion Desired |
| RA | Recursion Available |
| AD | Authenticated Data |
| CD | Checking Disabled |

These flags help determine how the query was processed.

---

# DNS Record Types

## A Record

Maps a hostname to an IPv4 address.

Example:

```
example.com

↓

93.184.216.34
```

---

## AAAA Record

Maps a hostname to an IPv6 address.

---

## CNAME Record

Creates an alias for another hostname.

Example:

```
www.example.com

↓

example.com
```

---

## MX Record

Specifies the mail server responsible for receiving email.

---

## NS Record

Identifies the authoritative name servers for a domain.

---

## TXT Record

Stores arbitrary text.

Common uses:

- SPF
- DKIM
- Domain verification

---

## PTR Record

Performs reverse DNS lookups.

Example:

```
8.8.8.8

↓

dns.google
```

---

## SOA Record

Start of Authority.

Contains administrative information about a DNS zone.

---

# DNS Response Codes (RCODE)

| Code | Meaning |
|------|----------|
| 0 | No Error |
| 1 | Format Error |
| 2 | Server Failure |
| 3 | NXDOMAIN (Domain Not Found) |
| 4 | Not Implemented |
| 5 | Refused |

---

# Common Wireshark Display Filters

Show all DNS traffic:

```
dns
```

---

DNS Queries Only:

```
dns.flags.response == 0
```

---

DNS Responses Only:

```
dns.flags.response == 1
```

---

NXDOMAIN Responses:

```
dns.flags.rcode == 3
```

---

A Records:

```
dns.a
```

---

AAAA Records:

```
dns.aaaa
```

---

MX Records:

```
dns.mx
```

---

PTR Records:

```
dns.ptr.domain_name
```

---

Specific Domain:

```
dns.qry.name == "example.com"
```

---

Specific Transaction ID:

```
dns.id == 0x4f2a
```

---

# Typical DNS Conversation

```
Client

↓

DNS Query

↓

Resolver

↓

DNS Response

↓

TCP Connection

↓

TLS

↓

HTTP
```

DNS is usually the first application-layer protocol observed before a web connection begins.

---

# DNS Cache

Operating systems cache DNS responses to reduce repeated queries.

Benefits:

- Faster browsing
- Lower latency
- Reduced DNS server load

Because of caching, repeated visits to the same website may not generate a new DNS query.

---

# DNS over TCP

Most DNS traffic uses **UDP port 53**.

TCP is used when:

- Responses exceed UDP size limits
- Zone transfers occur
- UDP responses are truncated

---

# DNS over HTTPS (DoH)

DNS queries are encrypted inside HTTPS.

Benefits:

- Improved privacy
- Prevents easy DNS monitoring
- Reduces DNS spoofing risks

Since traffic is encrypted, standard DNS filters may no longer reveal the queried domain names.

---

# DNS Security Threats

## DNS Spoofing

Attackers send forged DNS responses to redirect users to malicious websites.

Symptoms:

- Unexpected IP addresses
- Duplicate responses
- Transaction ID mismatches

---

## DNS Cache Poisoning

A malicious response is inserted into a DNS cache.

Victims continue receiving the incorrect IP address until the cache expires.

---

## DNS Tunneling

Attackers hide data inside DNS queries or responses.

Common signs:

- Very long subdomains
- High volume of TXT queries
- Repeated requests to the same domain

Often used for:

- Data exfiltration
- Command-and-Control (C2)

---

## DNS Amplification

A reflection-based Distributed Denial-of-Service (DDoS) attack.

Attackers:

1. Spoof the victim's IP address.
2. Send small DNS queries.
3. Open resolvers return much larger responses to the victim.

---

# Troubleshooting DNS

Common problems:

- No response from DNS server
- Incorrect IP address returned
- NXDOMAIN errors
- Slow responses
- Packet loss

Investigation workflow:

```
Capture Traffic

↓

Filter DNS

↓

Verify Query

↓

Check Response Code

↓

Inspect Returned Records

↓

Measure Response Time

↓

Verify Client Connection
```

---

# Cybersecurity Use Cases

## Blue Team

- Detect malware beaconing
- Identify suspicious domains
- Investigate phishing attempts
- Monitor DNS tunneling

---

## Red Team

- Verify payload callbacks
- Test DNS-based C2
- Troubleshoot domain resolution

---

## Incident Response

- Reconstruct attacker communications
- Identify compromised domains
- Track malicious infrastructure
- Correlate DNS activity with web traffic

---

# Best Practices

- Analyze DNS before examining HTTP or HTTPS traffic.
- Verify that every query has a corresponding response.
- Watch for excessive NXDOMAIN responses.
- Investigate unusually long domain names.
- Correlate DNS activity with subsequent TCP connections.

---

# Common Mistakes

❌ Assuming every DNS query receives a response.

❌ Ignoring cached DNS entries.

❌ Confusing recursive and iterative resolution.

❌ Overlooking DNS over HTTPS when no traditional DNS traffic is visible.

❌ Assuming all TXT records are malicious.

---

# Quick Summary

- DNS translates domain names into IP addresses.
- Queries and responses are matched using the Transaction ID.
- DNS supports many record types including A, AAAA, MX, CNAME, NS, TXT, PTR, and SOA.
- Most DNS traffic uses UDP port 53.
- Wireshark provides powerful filters for analyzing DNS activity.
- DNS analysis is critical for network troubleshooting, malware analysis, and incident response.

---

# Key Takeaways

- DNS is usually the first application-layer protocol observed before a network connection is established.
- Understanding DNS resolution makes it easier to investigate web traffic, malware communications, and suspicious domains.
- Wireshark allows analysts to inspect DNS queries, responses, flags, and record types in detail.
- Strong DNS analysis skills are essential for penetration testing, threat hunting, digital forensics, and enterprise security operations.
