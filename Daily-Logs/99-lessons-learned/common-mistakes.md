# Things to Keep in Mind

## Git

* Always run `git status` before `git add` and `git commit`.
* Pull the latest changes before starting a study session.
* Commit only completed work.
* Push after reviewing notes.

## Linux

* Avoid working as `root` unless required.
* Read terminal output carefully before searching for solutions.
* Learn what commands do instead of memorizing them.
* Check `man` pages whenever possible.

## Cybersecurity

* Enumeration comes before exploitation.
* Understand *why* a technique works, not just *how*.
* Keep lab notes separate from permanent concept notes.
* Never publish flags or walkthroughs for active labs.

## Documentation

* One daily log per day.
* One permanent note per topic.
* Keep notes concise and update them instead of creating duplicates.

## Mindset

* Learn consistently.
* Stay curious.
* Practice more than you read.
* Build understanding before speed.
# Subnetting Mistakes Learned

## Mistake 1

Confused the given network address with the next subnet.

### Fix

If the problem already gives a network (for example, `192.168.50.0/26`), that address is the network address. Do not jump to the next subnet.

---

## Mistake 2

Miscounted usable hosts.

### Fix

Never count host addresses manually. Use:

Usable Hosts = 2^(32 − CIDR) − 2

or memorize the common values:

* /26 → 62
* /27 → 30
* /28 → 14
* /29 → 6
* /30 → 2

---

## Mistake 3

Started subnetting problems with binary.

### Better Approach

CIDR → Block Size → Subnet Boundaries → Network → Broadcast → Hosts

This approach is significantly faster for certification exams and practical networking tasks.
