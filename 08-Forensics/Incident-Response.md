# Incident Response

## What is Incident Response?

**Incident Response (IR)** is the structured process used to identify, investigate, contain, eradicate, and recover from cybersecurity incidents.

A commonly used lifecycle is:

1. Preparation
2. Detection and Analysis
3. Containment
4. Eradication
5. Recovery
6. Lessons Learned

---

# 1. Preparation

Prepare people, processes, and technology before an incident occurs.

Examples:

- Incident Response plans
- Security policies
- Monitoring tools
- Access controls
- Backups
- Security training
- Response playbooks
- Communication procedures

---

# 2. Detection and Analysis

Identify and investigate suspicious activity.

Activities include:

- Reviewing alerts
- Analyzing logs
- Identifying affected systems
- Finding IOCs
- Determining the attack method
- Establishing a timeline
- Determining incident severity
- Assessing scope

Example:

```text
Alert
 ↓
Collect evidence
 ↓
Analyze logs
 ↓
Identify affected host/user
 ↓
Determine whether incident is real
 ↓
Determine scope and severity
```

---

# 3. Containment

Containment limits the attack and prevents further damage.

Examples:

- Isolate a compromised endpoint
- Block a malicious IP
- Disable a compromised account
- Block a malicious domain
- Restrict network access

## Short-Term Containment

Immediate action to limit active damage.

## Long-Term Containment

Additional controls used while investigation and remediation continue.

---

# 4. Eradication

Remove the threat and its root cause.

Examples:

- Remove malware
- Delete malicious files
- Remove persistence mechanisms
- Patch vulnerabilities
- Reset compromised credentials
- Remove unauthorized accounts

---

# 5. Recovery

Return affected systems to normal operation.

Examples:

- Restore systems
- Restore clean backups
- Re-enable services
- Verify system integrity
- Monitor affected systems
- Confirm that malicious activity has stopped

---

# 6. Lessons Learned

Review the incident after recovery.

Questions:

- What happened?
- How did the attacker gain access?
- Which systems were affected?
- How was the incident detected?
- Why was it not detected earlier?
- Which controls worked?
- Which controls failed?
- What should be improved?

---

# Incident Response Flow

```text
Preparation
    ↓
Detection & Analysis
    ↓
Containment
    ↓
Eradication
    ↓
Recovery
    ↓
Lessons Learned
    ↓
Improve Security Controls
```

---

# SOC and Incident Response

The SOC often plays an important role in the early stages of Incident Response.

```text
Security Monitoring
       ↓
Alert
       ↓
Triage
       ↓
Investigation
       ↓
Incident Confirmed
       ↓
Incident Response
       ↓
Containment
       ↓
Eradication / Recovery
       ↓
Lessons Learned
```

The exact responsibilities depend on the organization's SOC and Incident Response structure.
