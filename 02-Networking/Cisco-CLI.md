# Cisco CLI (Command Line Interface)

## What is Cisco IOS?

**Cisco IOS (Internetwork Operating System)** is the operating system used on Cisco routers and switches. Most network configuration and troubleshooting tasks are performed through the Command Line Interface (CLI).

---

## Cisco CLI Modes

### User EXEC Mode

Prompt:

```text
Router>
```

Purpose:

* Basic monitoring commands
* Limited access

---

### Privileged EXEC Mode

Enter:

```text
enable
```

Prompt:

```text
Router#
```

Purpose:

* Administrative commands
* Access to configuration mode

---

### Global Configuration Mode

Enter:

```text
configure terminal
```

Prompt:

```text
Router(config)#
```

Purpose:

* Configure the entire device

---

### Interface Configuration Mode

Enter:

```text
interface <interface-name>
```

Example:

```text
interface GigabitEthernet0/0
```

Prompt:

```text
Router(config-if)#
```

Purpose:

* Configure individual interfaces

---

## Common Cisco CLI Commands

```text
enable
disable
configure terminal
exit
end
hostname
interface
show running-config
show startup-config
show ip interface brief
copy running-config startup-config
reload
no shutdown
shutdown
```

---

## Packet Tracer Practice

Practiced:

* Navigating between CLI modes.
* Entering configuration mode.
* Viewing interface information.
* Saving configuration.
* Basic router and switch configuration.

---

## Key Takeaways

* Cisco devices are primarily managed through the CLI.
* Understanding IOS modes is fundamental for CCNA.
* Packet Tracer is an excellent environment for practicing CLI commands before working on real hardware.
