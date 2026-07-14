# Hack The Box – Starting Point Notes

## Meow

* Learned basic VPN connection and HTB workflow.
* Introduction to Telnet service.
* Practiced remote login and flag retrieval.

---

## Fawn

* Introduction to FTP.
* Learned anonymous FTP login.
* Practiced basic file enumeration and download.

---

## Dancing

* Introduction to SMB shares.
* Learned SMB enumeration.
* Practiced accessing shared resources.

---

## Appointment

* Introduction to SQL Injection (SQLi).
* Learned how insecure input handling can lead to authentication bypass.
* Understood the importance of parameterized queries and input validation.

---

### Overall Progress

* Improved Linux command-line usage.
* Gained experience connecting to HTB VPN.
* Practiced service enumeration and identifying common network services.
* Developed a better understanding of common beginner attack surfaces.

## Sequel

* Introduction to MySQL service enumeration.
* Learned basic SQL commands for exploring databases and tables.
* Practiced interacting with a remote database service.
* Understood the importance of inspecting database contents during enumeration.

---

## Crocodile

* Introduction to FTP-based enumeration and credential discovery.
* Learned how exposed files can reveal sensitive information.
* Practiced using discovered credentials on another service.
* Reinforced the methodology of enumerating every exposed service before attempting exploitation.

---

### Overall Progress

* Strengthened service enumeration methodology.
* Improved confidence interacting with MySQL and FTP services.
* Reinforced the importance of gathering information before exploitation.
* Continued building practical penetration testing skills through hands-on Hack The Box labs.

# Responder

## Machine Information

* Platform: Hack The Box
* Track: Starting Point
* Tier: 1
* Completed: 2026-07-12

---

## Objective

Learn how attackers can capture network authentication attempts, crack recovered password hashes, and use valid credentials to gain remote access to a Windows system.

---

## Skills Learned

* Network enumeration
* Service identification
* VPN interface verification
* Authentication hash capture
* Offline password cracking
* Remote Windows management
* Basic Windows post-authentication workflow

---

## Commands Used

### Initial Enumeration

```bash
nmap -sC -sV --min-rate <target_ip>
```

### Verify VPN Interface

```bash
ip a | grep tun0
```

### Start Responder

```bash
responder
```

### Crack Captured Hashes

```bash
john
```

### Remote Access

```bash
evil-winrm
```

---

## Key Lessons

* Enumeration should always be the first step.
* Verify your VPN interface before running network attacks.
* Captured hashes are valuable and should be handled securely.
* Offline password cracking can reveal valid credentials.
* WinRM is a common Windows remote management service encountered during penetration tests.

---

## Personal Reflection

This machine introduced a realistic Windows-oriented attack chain that combined reconnaissance, credential capture, password cracking, and remote administration. It reinforced the importance of following a structured methodology rather than rushing toward exploitation.

-------------------------------------------------------------------------------------------------------------------------

### Archetype

## Machine Information

* Platform: Hack The Box
* Track: Starting Point
* Tier: 1
* Operating System: Windows
* Completion Date: 2026-07-13

---

## Objective

Practice Windows-focused enumeration, SMB interaction, credential discovery, and remote administration using common penetration testing tools.

---

## Skills Learned

* SMB enumeration
* Reading configuration files
* Discovering exposed credentials
* File transfer techniques
* Working with Impacket
* Remote Windows administration using PsExec

---

## Commands Used

### Initial Enumeration

```bash
nmap
```

### SMB Enumeration

```bash
smbclient
dir
get
more
```

### Tool Usage

```bash
impacket
```

### File Transfer

```bash
sudo python -m http.server 1337
```

### File Discovery

```bash
locate
```

### Remote Access

```bash
psexec.py
```

---

## Attack Chain

Reconnaissance

↓

SMB Enumeration

↓

Configuration File Discovery

↓

Credential Discovery

↓

Remote Access

↓

Privilege Escalation

↓

Flag

---

## Key Lessons

* Enumeration remains the most important phase of an assessment.
* Configuration files frequently contain valuable information.
* SMB shares should always be thoroughly investigated.
* Impacket provides powerful tools for Windows penetration testing.
* PsExec is commonly used for remote administration when valid credentials are available.

---

## Personal Reflection

Archetype was the most challenging Starting Point machine I have completed so far. I attempted the machine independently before using parts of the walkthrough to understand the remaining steps. The walkthrough helped me understand the attack methodology rather than simply copying commands, making it a valuable learning experience.

Future goal: solve similar Windows machines with progressively less external guidance.
