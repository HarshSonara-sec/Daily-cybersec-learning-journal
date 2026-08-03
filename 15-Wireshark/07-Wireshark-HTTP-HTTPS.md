# Wireshark HTTP & HTTPS Analysis

> **Category:** Network Analysis
>
> **Difficulty:** Beginner → Intermediate
>
> **Prerequisites:**
>
> - Wireshark Fundamentals
> - Display Filters
> - Protocol Analysis
> - TCP Analysis
> - DNS Analysis
>
> **Recommended Before:**
>
> - 01-Wireshark-Fundamentals.md
> - 02-Wireshark-Display-Filters.md
> - 03-Wireshark-Capture-Filters.md
> - 04-Wireshark-Protocol-Analysis.md
> - 05-Wireshark-TCP-Analysis.md
> - 06-Wireshark-DNS-Analysis.md
>
> **Recommended After:**
>
> - 08-Wireshark-Statistics-and-Tools.md

---

# What is HTTP?

**Hypertext Transfer Protocol (HTTP)** is an application-layer protocol used to transfer web content between a client and a web server.

HTTP is:

- Stateless
- Request/Response based
- Human-readable
- Usually uses TCP Port 80

Example:

```
Browser

↓

HTTP Request

↓

Web Server

↓

HTTP Response

↓

Browser Displays Page
```

---

# What is HTTPS?

**HTTPS (Hypertext Transfer Protocol Secure)** is HTTP protected using **Transport Layer Security (TLS)**.

HTTPS provides:

- Encryption
- Authentication
- Integrity

Default Port:

```
443/TCP
```

Modern websites almost always use HTTPS.

---

# HTTP vs HTTPS

| Feature | HTTP | HTTPS |
|----------|------|--------|
| Encryption | ❌ No | ✅ Yes |
| Default Port | 80 | 443 |
| Confidentiality | ❌ | ✅ |
| Authentication | ❌ | ✅ (Certificate) |
| Integrity | ❌ | ✅ |

---

# Web Communication Flow

A typical web request follows this order:

```
ARP

↓

DNS

↓

TCP Three-Way Handshake

↓

TLS Handshake (HTTPS only)

↓

HTTP Request

↓

HTTP Response

↓

TCP Connection Close
```

Understanding this sequence makes troubleshooting much easier.

---

# HTTP Request Structure

An HTTP request contains:

```
Request Line

Headers

Blank Line

Body (Optional)
```

Example:

```
GET /index.html HTTP/1.1

Host: example.com

User-Agent: Mozilla...

Accept: text/html
```

---

# HTTP Response Structure

The server replies with:

```
Status Line

Headers

Blank Line

Body
```

Example:

```
HTTP/1.1 200 OK

Content-Type: text/html

Content-Length: 5421

<html>
...
```

---

# Common HTTP Methods

| Method | Purpose |
|----------|----------|
| GET | Retrieve data |
| POST | Submit data |
| PUT | Replace a resource |
| PATCH | Update part of a resource |
| DELETE | Remove a resource |
| HEAD | Retrieve headers only |
| OPTIONS | Display supported methods |

---

# Common HTTP Status Codes

## Success

| Code | Meaning |
|------|----------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |

---

## Redirection

| Code | Meaning |
|------|----------|
| 301 | Permanent Redirect |
| 302 | Temporary Redirect |
| 304 | Not Modified |

---

## Client Errors

| Code | Meaning |
|------|----------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |

---

## Server Errors

| Code | Meaning |
|------|----------|
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |

---

# Important HTTP Headers

## Host

Identifies the requested website.

Example:

```
Host: example.com
```

---

## User-Agent

Identifies the client application.

Example:

```
Mozilla Firefox

Google Chrome

curl

wget
```

Useful during investigations to identify automated tools.

---

## Accept

Lists content types accepted by the client.

---

## Content-Type

Describes the format of transmitted data.

Examples:

```
text/html

application/json

image/png

text/css
```

---

## Content-Length

Specifies the size of the HTTP body.

---

## Cookie

Stores session information.

Cookies commonly contain:

- Session IDs
- User preferences
- Authentication tokens

---

## Set-Cookie

Sent by the server to create or update cookies.

---

## Authorization

Contains authentication credentials.

Common types:

- Basic Authentication
- Bearer Tokens

---

# HTTP Display Filters

Show HTTP traffic:

```
http
```

---

GET Requests:

```
http.request.method == "GET"
```

---

POST Requests:

```
http.request.method == "POST"
```

---

HTTP Responses:

```
http.response
```

---

404 Responses:

```
http.response.code == 404
```

---

200 Responses:

```
http.response.code == 200
```

---

Specific Host:

```
http.host == "example.com"
```

---

Specific URI:

```
http.request.uri contains "login"
```

---

# Following HTTP Streams

Right-click a packet:

```
Follow

↓

HTTP Stream
```

or

```
Follow

↓

TCP Stream
```

Useful for reconstructing complete web conversations.

---

# Hypertext Transfer Protocol Versions

## HTTP/1.1

- Most widely recognized
- One request at a time per connection (without pipelining)

---

## HTTP/2

Features:

- Multiplexing
- Header Compression
- Better Performance

---

## HTTP/3

Uses:

```
QUIC

↓

UDP
```

Instead of TCP.

Improves:

- Speed
- Reliability
- Connection establishment

---

# TLS Handshake

HTTPS begins with a TLS handshake.

Typical sequence:

```
Client Hello

↓

Server Hello

↓

Certificate

↓

Key Exchange

↓

Encrypted Communication
```

---

# TLS Certificates

Certificates verify the server's identity.

A certificate contains:

- Subject
- Issuer
- Validity Period
- Public Key
- Signature Algorithm

Wireshark can display certificate details during the TLS handshake.

---

# Server Name Indication (SNI)

SNI allows a client to specify the hostname during the TLS handshake.

Useful because multiple websites can share the same IP address.

Display Filter:

```
tls.handshake.extensions_server_name
```

Example:

```
example.com
```

> **Note:** In modern TLS (Encrypted Client Hello - ECH), SNI may also become encrypted, reducing its visibility.

---

# Exporting Objects

Wireshark can extract transferred files.

Navigate to:

```
File

↓

Export Objects

↓

HTTP
```

Useful for:

- Malware Analysis
- Digital Forensics
- Incident Response

You can export:

- Images
- Documents
- Executables
- JavaScript files

---

# Cybersecurity Use Cases

## Blue Team

- Investigate web attacks
- Detect suspicious downloads
- Analyze user browsing activity
- Monitor web server communication

---

## Red Team

- Validate payload delivery
- Observe exploit requests
- Troubleshoot web shells
- Analyze C2 web traffic

---

## Incident Response

- Recover downloaded malware
- Identify malicious URLs
- Trace attacker activity
- Reconstruct web sessions

---

# Best Practices

- Analyze DNS before HTTP.
- Verify the TCP handshake before investigating web traffic.
- Inspect HTTP headers carefully.
- Follow complete HTTP/TCP streams.
- Remember that HTTPS encrypts application data, limiting payload visibility.

---

# Common Mistakes

❌ Assuming HTTPS traffic can always be decrypted.

❌ Ignoring HTTP response codes.

❌ Focusing only on packet summaries.

❌ Forgetting to inspect cookies and headers.

❌ Assuming every TCP connection contains HTTP traffic.

---

# Quick Summary

- HTTP transfers web content in plaintext.
- HTTPS protects HTTP using TLS encryption.
- HTTP uses a request/response model.
- Headers provide valuable information about clients and servers.
- Wireshark can analyze HTTP requests, responses, and TLS handshakes.
- Following TCP/HTTP streams helps reconstruct entire web sessions.

---

# Key Takeaways

- HTTP and HTTPS analysis is essential for understanding web application communication.
- Combining DNS, TCP, TLS, and HTTP analysis provides a complete picture of client-server interactions.
- Wireshark enables analysts to inspect web traffic, troubleshoot application issues, investigate attacks, and recover transferred files.
- Strong HTTP/HTTPS analysis skills are fundamental for penetration testing, digital forensics, malware analysis, threat hunting, and incident response.
