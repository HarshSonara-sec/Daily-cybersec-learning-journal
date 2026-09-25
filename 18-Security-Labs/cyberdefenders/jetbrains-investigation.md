# JetBrains — Investigation Report

## 1. Incident Overview

A TeamCity server was compromised following exploitation of a known vulnerability in the deployed web-server version.

Network traffic was analyzed to identify the attacker, determine the exploited vulnerability, investigate authentication, identify persistence/access mechanisms, and reconstruct post-exploitation activity.

---

## 2. Attacker Identification

**Attacker IP:**

```text
23.158.56.196
```

The source IP was identified from the network traffic associated with the malicious activity.

---

## 3. Targeted Service

The TeamCity server was running:

```text
2023.11.3
```

This version was relevant to the vulnerability exploited during the attack.

---

## 4. Exploited Vulnerability

The attacker exploited:

```text
CVE-2024-27198
```

This vulnerability was associated with the compromised TeamCity instance.

### Investigation significance

Identifying the exact software version allowed the analyst to correlate the observed attack with a known CVE rather than treating the traffic as an unidentified web attack.

---

## 5. Authentication

The attacker successfully authenticated against the TeamCity server using Basic Authentication.

Credentials identified during the investigation:

```text
c91oyemw:CL5vzdwLuK
```

> **Portfolio note:** This is a lab credential. Do not reuse or expose real credentials in public repositories.

---

## 6. Webshell Deployment

The attacker uploaded:

```text
NSt8bHTg.zip
```

The uploaded archive was associated with establishing webshell-based access to the compromised system.

This provided the attacker with a mechanism for executing commands through the compromised web application.

---

## 7. First Webshell Command

The first command executed through the webshell occurred at:

```text
2024-06-30 08:03
```

This timestamp is useful when constructing the incident timeline and correlating subsequent attacker activity.

---

## 8. Credential File Manipulation

The attacker modified:

```text
Creds.txt
```

The attacker wrote the following false credentials:

```text
a1l4m:youarecompromised
```

This activity was mapped to:

```text
T1565.001 — Stored Data Manipulation
```

The action demonstrates how an attacker can manipulate stored information to alter or falsify data after gaining access.

---

## 9. Docker-Based Host Access

Immediately after obtaining shell access, the attacker executed:

```bash
docker run --rm -it -v /:/host ubuntu chroot /host
```

### Command breakdown

```text
docker run
```

Creates and starts a Docker container.

```text
--rm
```

Removes the container after it exits.

```text
-it
```

Provides an interactive terminal.

```text
-v /:/host
```

Mounts the host filesystem at `/host` inside the container.

```text
ubuntu
```

Uses the Ubuntu image.

```text
chroot /host
```

Changes the apparent root directory to the mounted host filesystem.

### Security significance

The important portion of the command is:

```text
-v /:/host
```

Combined with:

```text
chroot /host
```

this gave the attacker access to the host filesystem from inside the container.

This demonstrates the security impact that can occur when an attacker obtains access to a Docker environment with excessive privileges or access to the host filesystem.

---

# 10. Attack Timeline

```text
Attacker
   │
   │
   │ 23.158.56.196
   ▼
TeamCity Server
   │
   │
   ├── Identify TeamCity 2023.11.3
   │
   ├── Exploit CVE-2024-27198
   │
   ├── Authenticate using Basic Auth
   │
   ├── Upload NSt8bHTg.zip
   │
   ├── Establish webshell access
   │
   ├── Execute first command
   │      2024-06-30 08:03
   │
   ├── Modify Creds.txt
   │
   └── Docker + chroot
          │
          └── Host filesystem access
```

---

# 11. SOC Investigation Takeaways

### Network Evidence

PCAP analysis can reveal:

* Attacker IP addresses
* HTTP requests
* Authentication attempts
* Uploaded files
* Command execution
* Attack timestamps
* Post-exploitation activity

### Endpoint / Server Evidence

Once network evidence identifies suspicious activity, an analyst should correlate it with:

* Web-server logs
* Authentication logs
* Process execution
* File modifications
* Container activity
* System logs

### Detection Opportunities

Potential detection points include:

* Requests targeting vulnerable TeamCity endpoints
* Suspicious Basic Authentication activity
* Unexpected archive uploads
* Webshell-related requests
* Unexpected command execution
* Modification of credential files
* Docker containers mounting `/`
* `chroot` execution from unusual processes

---

# 12. Final Assessment

The investigation identified a complete attack sequence beginning with exploitation of a vulnerable TeamCity instance and progressing to authenticated access, webshell deployment, command execution, data manipulation, and Docker-based host filesystem access.

The investigation demonstrates the importance of correlating **network evidence, application behavior, authentication activity, file manipulation, and command execution** during SOC investigations.
