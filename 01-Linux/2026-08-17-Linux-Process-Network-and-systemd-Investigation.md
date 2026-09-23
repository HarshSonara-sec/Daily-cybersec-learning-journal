# Linux Process, Network & systemd Investigation

**Date:** 17 August 2026  
**Area:** Linux / Host Security / Incident Response Foundations

## 1. Process Enumeration

### `ps`

```bash
ps aux
ps aux | head
ps -p <PID> -o pid,ppid,user,stat,cmd
```

Useful fields:

- `PID` — process ID
- `PPID` — parent process ID
- `USER` — account running the process
- `STAT` — process state
- `COMMAND` / `CMD` — command or executable

### `pstree`

```bash
pstree -p
pstree -p 1
```

Shows parent/child process relationships. PID 1 is the ancestor of the userspace process tree on a normal Linux boot.

---

## 2. `/proc` Process Investigation

Linux exposes live process information through `/proc`.

### Find the executable of a process

```bash
readlink -f /proc/<PID>/exe
```

Example for PID 1:

```bash
readlink -f /proc/1/exe
```

### Inspect open file descriptors

```bash
ls -l /proc/<PID>/fd
```

A process may have entries such as:

```text
socket:[123456]
```

The number is a socket inode used to correlate the process with kernel networking information.

---

## 3. Socket Investigation

### Practical method: `ss`

```bash
ss -tulpn
ss -tunap
ss -unp
```

`ss` can show network sockets and, when permissions allow, the owning process/PID.

Useful protocol tables:

```text
/proc/net/tcp    → TCP
/proc/net/tcp6   → IPv6 TCP
/proc/net/udp    → UDP
/proc/net/udp6   → IPv6 UDP
/proc/net/unix   → Unix-domain sockets
```

A key troubleshooting lesson:

> If a socket inode is absent from `/proc/net/tcp`, it may not be TCP. Check the other socket tables.

This was demonstrated by tracing a `socket:[inode]` entry that turned out to be **UDP**.

### Investigation chain

```text
Process
  ↓
PID
  ↓
/proc/<PID>/fd
  ↓
socket:[inode]
  ↓
TCP / UDP / Unix socket table
  ↓
network connection
```

---

# 4. systemd and Linux Services

On modern Linux systems, `systemd` commonly acts as PID 1 and manages system services.

Conceptually:

```text
Kernel
  ↓
systemd (PID 1)
  ↓
service/unit
  ↓
process
  ↓
files / sockets / network exposure
```

## List running services

```bash
systemctl list-units --type=service --state=running
```

## Inspect a service

```bash
systemctl status <service>
```

Important information includes:

- Active state
- Main PID
- Loaded unit file
- Recent service messages

## Active vs enabled

```bash
systemctl is-active <service>
systemctl is-enabled <service>
```

These answer different questions:

- `is-active` — is the service running **right now**?
- `is-enabled` — is the service configured to start automatically through the normal boot process?

A service can therefore be **disabled and inactive** without being broken.

---

# 5. systemd Unit Definitions

Read a service definition with:

```bash
systemctl cat <service>
```

Look for:

```ini
[Service]
ExecStart=...
```

`ExecStart` identifies the command systemd launches for the service.

This lets an investigator connect:

```text
service
  ↓
unit definition
  ↓
ExecStart
  ↓
executable
  ↓
process/PID
```

### Example concept

```ini
[Service]
ExecStart=/usr/sbin/example -D
```

The exact command depends on the service.

`-D` commonly means running in the foreground for daemons such as `sshd`, allowing the service manager to supervise the process.

---

# 6. Dependencies

```bash
systemctl list-dependencies <service>
```

This shows the unit's dependency relationships and helps explain what systemd starts or requires around a service.

---

# 7. Service Logs

Query the systemd journal for a service:

```bash
journalctl -u <service>
journalctl -u <service> -n 20 --no-pager
```

Useful for investigating:

- Start/stop events
- Failures
- Configuration problems
- Historical service activity

No journal entries for a service do not automatically mean something is wrong; it may simply not have generated relevant journal messages.

---

# 8. Custom systemd Services and Security Investigation

Custom service definitions are worth investigating during host-security and incident-response work.

Find service files under the administrator-managed systemd directory:

```bash
find /etc/systemd/system -type f -name "*.service" -ls
```

Inspect a service:

```bash
systemctl cat <service>
```

Security questions to ask:

1. Who owns the unit file?
2. When was it created or modified?
3. What does `ExecStart` execute?
4. Where is the executable located?
5. Which user does the service run as?
6. Is the service enabled?
7. Does its behavior match its stated purpose?

A suspicious filename or unusual path **does not by itself prove maliciousness**. It is an investigation clue that requires contextual verification.

Potentially interesting executable locations may include temporary or unusual directories, but legitimate software can also use non-standard paths.

---

# 9. Security Investigation Workflow

A useful host-investigation workflow is:

```text
Listening port
      ↓
Network service
      ↓
systemd service (if applicable)
      ↓
Unit file
      ↓
ExecStart
      ↓
PID / process
      ↓
/proc/<PID>
      ↓
Open files / sockets
      ↓
Logs and behavior
```

This allows an analyst to move from a visible network exposure back to the process and service responsible for it.

---

## Commands Practiced

```bash
ps aux
ps -p <PID> -o pid,ppid,user,stat,cmd
pstree -p
pstree -p 1
readlink -f /proc/<PID>/exe
ls -l /proc/<PID>/fd
ss -tulpn
ss -tunap
ss -unp
systemctl list-units --type=service --state=running
systemctl status <service>
systemctl is-active <service>
systemctl is-enabled <service>
systemctl cat <service>
systemctl list-dependencies <service>
journalctl -u <service>
journalctl -u <service> -n 20 --no-pager
systemctl show --property=UnitPath
find /etc/systemd/system -type f -name "*.service" -ls
```

## Key Takeaways

- A process, service, and network socket are different layers of the same investigation.
- `/proc` exposes live kernel/process information.
- `socket:[inode]` identifies a kernel socket object; the socket type determines which `/proc/net/*` table contains it.
- `ss` is the practical tool for correlating sockets with network state and processes.
- `systemctl` investigates service state and configuration.
- `is-active` and `is-enabled` answer different questions.
- `ExecStart` reveals what a systemd unit launches.
- systemd services can be relevant when investigating persistence, but unusual configuration requires evidence rather than assumptions.
