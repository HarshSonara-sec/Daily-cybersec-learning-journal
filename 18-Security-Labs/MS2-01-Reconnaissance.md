# MS2 — Reconnaissance

**Target:** `192.168.89.128`

## FTP

```bash
ftp 192.168.89.128
```

Observed:
- `vsFTPd 2.3.4`
- Anonymous login succeeded.
- Directory listing succeeded.
- Anonymous write was denied.

## SMB

Example connection:

```bash
smbclient //192.168.89.128/tmp -N -m NT1
```

Observed:
- Anonymous login succeeded.
- SMB1/NT1 was available.
- `tmp` was readable.
- Files could be uploaded.
- Directory creation was possible.

Useful SMB commands:

```text
dir
pwd
put <local-file>
mkdir <directory>
exit
```

## HTTP

Useful enumeration:

```bash
curl -I http://192.168.89.128/
curl -i http://192.168.89.128/ | head -40
```

Gobuster:

```bash
gobuster dir -u http://192.168.89.128/ -w /usr/share/wordlists/dirb/common.txt --timeout 10s
```

Interesting paths observed included `/dav/`, `/phpMyAdmin/`, `/twiki/`, `/test/`, `/cgi-bin/` and `/phpinfo.php`.

## Nikto
Nikto identified multiple legacy/misconfiguration findings, including directory indexing, `phpinfo.php`, old Apache/PHP components, HTTP TRACE and other configuration issues.

Nikto was not relied upon as the primary proof. Manual requests were used to validate the important WebDAV behavior.

## Decision
WebDAV was selected because it provided a direct, manually verifiable path from unauthenticated access to PHP execution.
