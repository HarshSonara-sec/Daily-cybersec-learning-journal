# Metasploitable 2 — Home Lab

## Lab Purpose
Metasploitable 2 is used as an intentionally vulnerable target for practicing enumeration, vulnerability validation, exploitation and privilege escalation in an isolated VMware environment.

## Today's Attack Chain

```text
192.168.89.128 MS2
        |
        v
HTTP / WebDAV /dav/
        |
        v
Anonymous PUT
        |
        v
PHP upload + execution
        |
        v
www-data
        |
        v
SUID enumeration
        |
        v
/usr/bin/nmap
Nmap 4.53
        |
        v
Interactive mode
        |
        v
root
```

## Lab Network

| System | Interface | Address |
|---|---|---|
| Kali | VMware `vmnet8` | `192.168.89.1` |
| MS2 | VMware guest | `192.168.89.128` |

`vmnet1` was `192.168.123.1` and was not the network used for MS2 during this session.

## Lab Rules
- Use only the intentionally vulnerable MS2 VM.
- Keep the lab isolated from production systems.
- Keep WireGuard off during the MS2 exercise because it previously interfered with the VMware lab network.
- Clean up test artifacts after exploitation.
