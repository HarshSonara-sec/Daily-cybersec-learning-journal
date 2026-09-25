# JetBrains — MITRE ATT&CK Mapping

## Attack Chain

```text
Initial Access
      ↓
Exploitation of Public-Facing Application
      ↓
Execution
      ↓
Webshell / Command Execution
      ↓
Container / Host Access
      ↓
Data Manipulation
      ↓
Command & Control / Continued Access
```

---

## MITRE ATT&CK Mapping

| Stage                        | Technique / Sub-technique                 | ID            | Evidence                                      |
| ---------------------------- | ----------------------------------------- | ------------- | --------------------------------------------- |
| Initial Access               | Exploitation of Public-Facing Application | T1190         | TeamCity vulnerability exploitation           |
| Execution                    | Command and Scripting Interpreter*        | —             | Commands executed through the webshell        |
| Persistence / Access         | Webshell activity*                        | —             | Uploaded `NSt8bHTg.zip` used for shell access |
| Defense Evasion / Impact     | Stored Data Manipulation                  | **T1565.001** | Modification of `Creds.txt`                   |
| Execution / Privilege Access | Container Administration Command*         | —             | Docker command used to mount host filesystem  |
| Host Access                  | Chroot / filesystem access*               | —             | `chroot /host` after mounting `/`             |

> `*` These entries describe the observed behavior; the exact ATT&CK technique mapping should be verified against the ATT&CK version used by the lab rather than inferred solely from the command.

---

# Confirmed ATT&CK Mapping

## T1190 — Exploit Public-Facing Application

The attacker exploited the externally accessible TeamCity service using:

```text
CVE-2024-27198
```

### Evidence

```text
TeamCity 2023.11.3
CVE-2024-27198
```

### Tactical Context

**Tactic:** Initial Access

---

## T1565.001 — Stored Data Manipulation

The attacker modified:

```text
Creds.txt
```

and inserted:

```text
a1l4m:youarecompromised
```

### Tactical Context

**Tactic:** Impact

### Why it matters

This demonstrates manipulation of stored information after compromise. For a SOC analyst, unexpected modification of credential-related files should be treated as suspicious and correlated with the surrounding authentication and process activity.

---

# Docker Host-Filesystem Access

The attacker executed:

```bash
docker run --rm -it -v /:/host ubuntu chroot /host
```

### Important Indicators

```text
-v /:/host
```

Mounts the host root filesystem.

```text
chroot /host
```

Changes the process root to the mounted host filesystem.

### Security Significance

This activity demonstrates how access to a privileged Docker environment can potentially be leveraged to access the underlying host filesystem.

---

# MITRE Investigation Methodology

When mapping an incident to MITRE ATT&CK:

```text
Observed Evidence
       ↓
Attacker Behavior
       ↓
Technique Identification
       ↓
Technique ID
       ↓
Tactic
       ↓
Detection Opportunity
```

Avoid mapping a technique simply because a command "looks similar."

The mapping should be supported by:

* Network evidence
* Process evidence
* File activity
* Command execution
* Authentication activity
* ATT&CK technique definitions

---

# SOC Detection Ideas

Potential detection rules for similar activity:

### TeamCity exploitation

Monitor:

```text
Unusual requests to TeamCity endpoints
Repeated exploitation attempts
Unexpected administrative activity
```

### Webshell

Monitor:

```text
Unexpected archive uploads
New executable/script files in web directories
HTTP requests resulting in command execution
Suspicious POST requests
```

### Credential-file manipulation

Monitor:

```text
Unexpected writes to credential/configuration files
Changes made by unusual users/processes
Modification immediately following exploitation
```

### Docker abuse

Monitor:

```text
docker run
-v /:/host
privileged containers
unexpected container creation
chroot execution
```

---

# Analyst Takeaway

The JetBrains investigation demonstrates how a SOC analyst can move from a suspicious network event to a complete attack narrative:

```text
IP
 ↓
Service
 ↓
Vulnerability
 ↓
Authentication
 ↓
Webshell
 ↓
Command Execution
 ↓
File Manipulation
 ↓
Host Access
 ↓
MITRE ATT&CK
```

The key lesson is **correlation**: individual events become much more meaningful when connected into a timeline showing attacker behavior.
