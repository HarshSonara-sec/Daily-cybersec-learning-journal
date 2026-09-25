# JetBrains — CyberDefenders

**Platform:** CyberDefenders
**Category:** Network Forensics
**Difficulty:** Easy
**Role:** SOC Analyst / Blue Team
**Primary Tools:** Wireshark, NetworkMiner, Brim

## Overview

The **JetBrains** lab is a network-forensics investigation involving the compromise of a TeamCity web server.

The investigation covers:

* Attacker IP identification
* Web-server version identification
* Vulnerability identification
* Basic Authentication credential discovery
* Webshell deployment
* Command execution
* Credential-file manipulation
* Docker-based host filesystem access
* MITRE ATT&CK mapping
* IOC extraction

## Attack Summary

The attacker originated from:

```text
23.158.56.196
```

The targeted TeamCity server was running:

```text
2023.11.3
```

The attacker exploited:

```text
CVE-2024-27198
```

After successful authentication, the attacker uploaded:

```text
NSt8bHTg.zip
```

The uploaded webshell was subsequently used to execute commands on the compromised server.

The attacker then used Docker to mount the host filesystem and `chroot` into it, providing access to the host filesystem.

## Key Investigation Findings

| Finding                        | Result                  |
| ------------------------------ | ----------------------- |
| Attacker IP                    | `23.158.56.196`         |
| TeamCity Version               | `2023.11.3`             |
| Exploited CVE                  | `CVE-2024-27198`        |
| Uploaded File                  | `NSt8bHTg.zip`          |
| First Webshell Command         | `2024-06-30 08:03`      |
| Modified File                  | `Creds.txt`             |
| Data Manipulation              | `T1565.001`             |
| Container Escape / Host Access | Docker mount + `chroot` |

## SOC Analyst Skills Practiced

* PCAP investigation
* HTTP traffic analysis
* Attacker identification
* Vulnerability identification
* Webshell investigation
* Command execution analysis
* Credential-related investigation
* IOC extraction
* Attack timeline reconstruction
* MITRE ATT&CK mapping
* Incident documentation

## Lab Status

**Completed ✅**

## Related Notes

* [Investigation](Investigation.md)
* [MITRE ATT&CK Mapping](MITRE-ATT&CK.md)
* [IOCs](IOCs.md)
