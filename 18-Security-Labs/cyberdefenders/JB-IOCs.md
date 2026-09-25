# JetBrains — Indicators of Compromise

## Network

| Type        | Indicator       |
| ----------- | --------------- |
| Attacker IP | `23.158.56.196` |

## Vulnerability

| Type             | Indicator        |
| ---------------- | ---------------- |
| TeamCity Version | `2023.11.3`      |
| CVE              | `CVE-2024-27198` |

## Authentication

**Lab credential observed:**

```text
c91oyemw:CL5vzdwLuK
```

> This is a CyberDefenders lab credential. Never place real credentials in a public repository.

## File

```text
NSt8bHTg.zip
```

## Modified File

```text
Creds.txt
```

## Injected Credentials

```text
a1l4m:youarecompromised
```

## Timestamp

```text
2024-06-30 08:03
```

## Command

```bash
docker run --rm -it -v /:/host ubuntu chroot /host
```

## MITRE ATT&CK

```text
T1190
T1565.001
```

## Defensive Detection Indicators

Look for:

```text
23.158.56.196
CVE-2024-27198 exploitation attempts
Unexpected TeamCity authentication
NSt8bHTg.zip
Unexpected modification of Creds.txt
docker run with host filesystem mounts
-v /:/host
chroot /host
```

> **Public GitHub recommendation:** Consider replacing credentials and other lab secrets with `[REDACTED]` before publishing this file. The goal of the repository should be to demonstrate your investigation methodology, not to publish usable credentials.
