# Linux Process, Network & systemd Investigation — Command Cheat Sheet

## Process Enumeration

```bash
ps aux
ps aux | head
ps -p <PID> -o pid,ppid,user,stat,cmd
pstree -p
pstree -p 1
```

## `/proc` Investigation

```bash
readlink -f /proc/<PID>/exe
ls -l /proc/<PID>/fd
```

Socket entries may appear as:

```text
socket:[INODE]
```

## Socket / Network Enumeration

```bash
ss -tulpn
ss -tunap
ss -unp
```

Common kernel socket tables:

```text
/proc/net/tcp
/proc/net/tcp6
/proc/net/udp
/proc/net/udp6
/proc/net/unix
```

Search a socket inode:

```bash
grep "<INODE>" /proc/net/tcp
grep "<INODE>" /proc/net/udp
grep "<INODE>" /proc/net/unix
```

If a TCP lookup returns nothing, **check whether the socket is actually UDP, UDP6, TCP6, or Unix**.

## systemd Services

```bash
systemctl list-units --type=service --state=running
systemctl status <service>
systemctl is-active <service>
systemctl is-enabled <service>
systemctl cat <service>
systemctl list-dependencies <service>
```

### Logs

```bash
journalctl -u <service>
journalctl -u <service> -n 20 --no-pager
```

### Unit locations

```bash
systemctl show --property=UnitPath
find /etc/systemd/system -type f -name "*.service" -ls
```

## Investigation Chain

```text
Service
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
Network exposure
  ↓
Logs
```

## Key Distinction

```text
systemctl is-active  → Is it running now?
systemctl is-enabled → Will it normally start automatically?
```
