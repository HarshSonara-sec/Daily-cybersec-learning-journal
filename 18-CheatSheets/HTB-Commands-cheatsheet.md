# IPv4 Subnetting Cheat Sheet

## Seven CIDRs to Memorize

| CIDR | Subnet Mask     | Block Size | Usable Hosts |
| ---- | --------------- | ---------: | -----------: |
| /24  | 255.255.255.0   |        256 |          254 |
| /25  | 255.255.255.128 |        128 |          126 |
| /26  | 255.255.255.192 |         64 |           62 |
| /27  | 255.255.255.224 |         32 |           30 |
| /28  | 255.255.255.240 |         16 |           14 |
| /29  | 255.255.255.248 |          8 |            6 |
| /30  | 255.255.255.252 |          4 |            2 |

## Fast Rules

* Block Size = 256 − Last Subnet Mask Octet.
* Network Address = Largest subnet boundary less than or equal to the host IP.
* Broadcast Address = Next subnet − 1.
* First Host = Network + 1.
* Last Host = Broadcast − 1.
* Usable Hosts = 2^(32 − CIDR) − 2.

## Block Size Reference

| Mask | Block Size |
| ---- | ---------: |
| 128  |        128 |
| 192  |         64 |
| 224  |         32 |
| 240  |         16 |
| 248  |          8 |
| 252  |          4 |
| 254  |          2 |

## VLSM Workflow

1. Sort host requirements from largest to smallest.
2. Choose the smallest subnet that fits each requirement.
3. Allocate the subnet at the next available address.
4. Continue from the next available network.
5. Ensure no subnet overlaps another.

## Mental Workflow

CIDR → Subnet Mask → Block Size → Network Boundary → Broadcast → Host Range

### Jul-14-2026

# HTB Commands Cheat Sheet

## Network Enumeration

### Nmap

Default enumeration with service/version detection and default NSE scripts.

```bash
nmap -sC -sV --min-rate <target_ip>
```

* `-sC` → Run default NSE scripts
* `-sV` → Detect service versions
* `--min-rate` → Increase scan speed

---

## VPN Verification

Check whether the Hack The Box VPN interface is active.

```bash
ip a | grep tun0
```

---

## SMB Enumeration

Connect to SMB shares.

```bash
smbclient //<target_ip>/<share>
```

List files inside a share.

```bash
dir
```

Download a file.

```bash
get <filename>
```

Read the contents of a text file.

```bash
more <filename>
```

---

## MySQL Enumeration

Connect to a MySQL server.

```bash
mysql -h <target_ip> -u root
```

Useful SQL commands:

```sql
SHOW DATABASES;
USE <database>;
SHOW TABLES;
SELECT * FROM <table>;
```

---

## FTP Enumeration

Connect to an FTP server.

```bash
ftp <target_ip>
```

Useful FTP commands:

```bash
ls
pwd
cd
get <filename>
mget *
bye
```

---

## Responder

Start Responder to listen for authentication requests.

```bash
responder
```

---

## Password Cracking

Crack captured password hashes.

```bash
john <hash_file>
```

---

## Windows Remote Management

Connect to a Windows machine using Evil-WinRM.

```bash
evil-winrm -i <target_ip> -u <username> -p <password>
```

---

## Python HTTP Server

Host files from the current directory.

```bash
sudo python -m http.server 1337
```

Useful for transferring tools or payloads between systems.

---

## Locate Files

Search for files on Linux.

```bash
locate <filename>
```

---

## Impacket

Collection of Python tools used during Windows penetration testing.

Example:

```bash
impacket-<tool>
```

Examples include:

```bash
psexec.py
wmiexec.py
secretsdump.py
smbserver.py
```

---

## PsExec

Obtain remote command execution on a Windows machine using valid credentials.

```bash
psexec.py
```

---

# Enumeration Workflow

```text
Verify VPN
↓

Nmap Scan
↓

Identify Services
↓

Enumerate Each Service
↓

Collect Information
↓

Discover Credentials
↓

Crack Passwords (if required)
↓

Gain Remote Access
↓

Privilege Escalation
```

---

# Commands Learned So Far

## Starting Point Machines

### Meow

* telnet

### Fawn

* ftp
* ls
* get

### Dancing

* smbclient

### Appointment

* SQL authentication concepts

### Sequel

* mysql
* SHOW DATABASES;
* USE
* SHOW TABLES;
* SELECT

### Crocodile

* ftp
* get

### Responder

* nmap -sC -sV --min-rate
* ip a | grep tun0
* responder
* john
* evil-winrm

### Archetype

* nmap
* smbclient
* dir
* get
* more
* impacket
* sudo python -m http.server 1337
* locate
* psexec.py

```
```

