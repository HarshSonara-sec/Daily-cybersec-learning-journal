# Linux Fundamentals - Session 1

**Date:** 2026-07-10

---

## Objective

Today I wanted to understand how Linux executes commands instead of only memorizing terminal commands.
After Linux practice, I completed my HTB tasks and labs.

---

## Topics Covered

- Linux Kernel
- Shell
- Zsh
- Terminal
- PATH
- Environment Variables
- File System Navigation

---

## Notes

### What is Linux?
Linux is a free, open-source, Unix-like operating system originally created by Linus Torvalds in 1991.
It functions as the core kernel that manages hardware resources, serving as the bridge between computer hardware and software applications.
Unlike proprietary systems like Windows or macOS, Linux allows users to freely view, modify, and distribute its source code under the GNU General Public License (GPL).

unlike user-space apps, the kernel operates in a privileged "kernel mode", allowing directly to control hardware without the interference of the individual programs.
Monolithic architechture, meaning it runs as a single large programme.

### Shell and Zsh.
the term shell is a general category for command line interpreters, whereas Zsh is an advanced shell application.

BASH- bourne again shell is another shell specific and the most common default on linux systems,
while Zsh has been the default on  MacOS since 2019.
# Terminal and Path.
The Linux terminal is a text-based command-line interface that allows users to interact directly with the operating system, execute commands, manage files, and automate tasks more efficiently than a graphical interface.
The PATH is an environment variable that stores a colon-separated list of directories where the shell searches for executable programs when a command is entered. 

# Environment Variables.
Environment variables in Linux are key-value pairs that define the operating environment for processes, storing configuration data such as executable paths, user information, locale settings, and default tools. 
They are inherited by child processes, ensuring that applications and scripts run with the correct context without needing hard-coded values

# File system Nav.
File system navigation in Linux involves moving through a hierarchical tree structure rooted at / (root) using terminal commands.
The primary commands for this process are pwd to display the current directory path, ls to list directory contents, and cd to change directories.

### Networking - HTB (CJCA Certi pathway)
As of today, Network foundation on HTB CJCA Pathway is done with practical labs.
Introduction to Networking is the new chapter that i started yesterday.
today's topic covered is

# Networking Structure
Network types
Topologies
Proxies

(P.S. ->Find further details and notes in Networking Folder) 


