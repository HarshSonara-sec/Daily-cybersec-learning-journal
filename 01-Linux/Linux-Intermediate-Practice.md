# Linux Intermediate Practice - 26 July 2026

## Objective
Strengthen Linux command-line skills through hands-on practice with file searching, text processing, log analysis, redirection, and filesystem concepts.

---

# Topics Covered

## 1. File Searching with `find`

Learned how to locate files and directories based on:
- File name
- File type
- File extension
- Size

Examples:

```bash
find . -name "*.log"
find . -type d
find . -size +10M
```

**Key Concept**

`find` searches the filesystem for files and directories.

---

## 2. Searching Text with `grep`

Used `grep` to search inside files and command output.

Examples:

```bash
grep "ERROR" security.log
history | grep ssh
```

### Important Difference

| find | grep |
|------|------|
| Searches for files/directories | Searches inside text |
| Works on the filesystem | Works on file contents or command output |

---

## 3. Viewing Large Files with `less`

Learned to efficiently navigate large files.

Useful shortcuts:

- `/` → Search
- `n` → Next match
- `N` → Previous match
- `g` → Top of file
- `G` → End of file
- `Space` → Next page
- `b` → Previous page
- `q` → Quit

---

## 4. Hashing with SHA-256

Generated hashes using:

```bash
sha256sum filename
```

Purpose:
- Verify file integrity
- Detect file modifications
- Compare downloaded files

---

## 5. Pipes (`|`)

Combined commands by sending the output of one command into another.

Examples:

```bash
ip a | grep inet
grep "ERROR" security.log | wc -l
history | grep ssh
```

**Key Concept**

A pipe connects multiple commands into a workflow.

---

## 6. Input & Output Redirection

### Overwrite

```bash
command > file.txt
```

### Append

```bash
command >> file.txt
```

### Redirect Errors

```bash
command 2> errors.txt
```

### Redirect Both Output and Errors

```bash
command > output.txt 2> errors.txt
```

or

```bash
command > everything.txt 2>&1
```

---

## 7. Using `tee`

Displayed output while saving it to a file.

```bash
command | tee output.txt
```

Useful when running scans or generating reports.

---

## 8. `head`, `tail` and `tail -f`

Viewed the beginning and end of log files.

Examples:

```bash
head security.log
tail security.log
tail -f security.log
```

### Learned

`tail -f` continuously follows a growing log file in real time.

Useful for:
- Monitoring authentication logs
- Watching application logs
- Security monitoring

---

## 9. Hard Links

Created a hard link using:

```bash
ln report.txt report-hard
```

### Learned

- Hard links share the same inode.
- Both filenames point to the same file data.
- Editing one updates the other.
- Deleting the original filename does **not** remove the data if another hard link exists.

Verified using:

```bash
ls -li
```

Observed:
- Same inode number
- Increased link count

---

# Mini Incident Response Lab

Practiced:

- Finding log files
- Counting ERROR entries
- Monitoring logs using `tail -f`
- Creating incident reports
- Redirecting command output into report files

---

# Key Takeaways

- `find` locates files.
- `grep` searches inside text.
- `less` is ideal for reading large files.
- Pipes connect commands together.
- Redirection controls where output and errors go.
- `tee` displays and saves output simultaneously.
- `tail -f` monitors logs in real time.
- Hard links are additional directory entries pointing to the same inode rather than copies of a file.

---

# Commands Used

```bash
find
grep
less
head
tail
tail -f
sha256sum
tee
wc
cat
echo
pwd
date
touch
rm
ln
ls -li
history
```

---

# Skills Gained

- Linux text searching
- Log investigation
- Command chaining
- Report generation
- Basic incident response workflow
- Understanding Linux filesystem internals through hard links
