# Linux Package Management

## apt

Installs packages from configured repositories.

Example:

```bash
sudo apt install nmap
```

---

## dpkg

Installs local Debian packages.

Example:

```bash
sudo dpkg -i package.deb
```

---

## Common Problems

### Dependency Errors

Occurs when required packages are missing.

Possible fixes:

```bash
sudo apt --fix-broken install
```

```bash
sudo apt update
```

```bash
sudo apt upgrade
```

---

## Useful Commands

Update repositories

```bash
sudo apt update
```

Upgrade packages

```bash
sudo apt upgrade
```

Remove package

```bash
sudo apt remove package
```

Search package

```bash
apt search package
```

Show package info

```bash
apt show package
```

List installed packages

```bash
apt list --installed
```

Clean package cache

```bash
sudo apt autoremove
```

```bash
sudo apt autoclean
```
