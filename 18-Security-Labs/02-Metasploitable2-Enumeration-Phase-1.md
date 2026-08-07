# Metasploitable 2 – Enumeration Phase 1

## Objective

Perform initial reconnaissance to identify the attack surface before attempting exploitation.

---

## Environment

- Host OS: Kali Linux
- Virtualization: VMware Workstation Pro
- Target: Metasploitable 2
- Enumeration Tools:
  - Nmap
  - Nikto
  - Firefox (Manual Enumeration)

---

## VMware Troubleshooting

### Issue

- VM failed to start due to missing `vmmon` module.

### Resolution

- Restarted VMware services.
- Loaded `vmmon` and `vmnet` kernel modules.
- Successfully powered on the virtual machine.

---

## Host Discovery

- Verified target IP address.
- Confirmed connectivity between Kali and Metasploitable 2.

---

## Nmap Enumeration

Performed service and version detection.

### Discovered Services

- HTTP (Apache)
- FTP
- SMB
- SSH
- MySQL
- WebDAV

---

## Web Enumeration (Nikto)

Identified multiple web applications:

- DVWA (Login Required)
- Mutillidae (Login Required)
- phpMyAdmin
- TWiki
- WebDAV

---

## Manual Enumeration

Visited the web server and explored available applications.

Observed:

- Multiple intentionally vulnerable applications.
- Different authentication requirements.
- Public and restricted attack surfaces.

---

## Initial Attack Path

1. Enumerate HTTP services.
2. Identify login portals.
3. Search for default or weak credentials.
4. Enumerate SMB shares.
5. Enumerate FTP contents.
6. Investigate phpMyAdmin authentication.
7. Build a complete attack map before exploitation.

---

## Key Takeaways

- Enumeration should always come before exploitation.
- Build an attack path instead of attacking random services.
- Combine automated scans with manual verification.
- Every discovered service may reveal additional attack vectors.

---

## Next Steps

- Enumerate SMB shares.
- Enumerate FTP files.
- Test common credentials where appropriate.
- Investigate phpMyAdmin.
- Continue mapping relationships between discovered services.
