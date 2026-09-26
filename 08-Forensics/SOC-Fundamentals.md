# SOC Fundamentals

## What is a SOC?

A **Security Operations Center (SOC)** is a centralized security function responsible for monitoring, detecting, investigating, and responding to cybersecurity threats.

The main objective is to identify suspicious activity and security incidents as early as possible and support an appropriate response.

---

## Core SOC Functions

### 1. Monitoring
Continuously monitor systems, networks, endpoints, applications, and security tools for suspicious activity.

### 2. Detection
Identify potentially malicious activity using security tools, detection rules, and security analytics.

### 3. Alert Triage
Review alerts and determine their priority and whether further investigation is required.

### 4. Investigation
Analyze alerts, logs, events, users, hosts, IP addresses, and other evidence to understand what happened.

### 5. Incident Response
Respond to confirmed or suspected security incidents and help contain their impact.

### 6. Threat Intelligence
Use information about known threats, malicious infrastructure, malware, indicators, and attacker techniques.

### 7. Threat Hunting
Proactively search for suspicious activity that may not have generated an existing alert.

### 8. Reporting and Documentation
Document investigations, evidence, actions, findings, and incident details.

---

# Common SOC Technologies

## SIEM

**Security Information and Event Management (SIEM)**

A SIEM collects and analyzes logs and security events from multiple sources.

Common sources include:

- Firewalls
- Servers
- Workstations
- Authentication systems
- Active Directory
- Network devices
- Endpoint security tools
- Applications
- Cloud services

Typical SIEM functions:

- Log collection
- Search
- Correlation
- Detection
- Alerting
- Dashboards
- Reporting
- Investigation

---

## EDR

**Endpoint Detection and Response (EDR)**

Monitors endpoints such as:

- Workstations
- Laptops
- Servers

EDR can provide visibility into:

- Processes
- File activity
- Network connections
- User activity
- Suspicious behavior
- Malware activity

It can also support response actions such as isolating a compromised endpoint.

---

## IDS / IPS

### IDS — Intrusion Detection System

Detects suspicious or malicious network activity and generates alerts.

### IPS — Intrusion Prevention System

Detects suspicious activity and can take preventive action, such as blocking or dropping traffic.

---

## Firewall

A firewall controls network traffic according to predefined rules.

Rules may consider:

- Source IP
- Destination IP
- Port
- Protocol
- Application

---

## SOAR

**Security Orchestration, Automation and Response**

SOAR platforms help automate repetitive security operations.

Example:

```text
Alert
  ↓
SOAR
  ↓
Extract IOC
  ↓
Threat Intelligence Check
  ↓
Response Action
  ↓
Create Ticket / Notify Analyst
```

---

# Threat Intelligence

Threat intelligence provides information that helps security teams understand and investigate threats.

Examples:

- Malicious IP addresses
- Malicious domains
- File hashes
- Malicious URLs
- Malware information
- Attacker techniques
- Threat actor information

## IOC

**Indicator of Compromise (IOC)**

An observable artifact that may indicate malicious activity.

Examples:

- Malicious IP
- Suspicious domain
- Malicious file hash
- Suspicious URL
- Compromised account

---

# Alerts

A security alert is generated when a security tool detects activity matching a suspicious condition or detection rule.

```text
Suspicious Activity
       ↓
Detection Rule
       ↓
Security Alert
       ↓
SOC Analyst
       ↓
Triage / Investigation
```

An alert does **not automatically mean that a security incident has occurred**.

The analyst must investigate the available evidence.

---

# False Positive vs True Positive

## False Positive

An alert is generated, but the activity is legitimate or benign.

Example:

```text
Admin performs unusual login activity
        ↓
Alert generated
        ↓
Investigation confirms legitimate activity
        ↓
False Positive
```

## True Positive

An alert correctly identifies suspicious or malicious activity.

Example:

```text
Multiple failed logins
        ↓
Successful unusual login
        ↓
Additional suspicious activity
        ↓
True Positive
```

---

# Security Incident

A security incident is an event that threatens or compromises the confidentiality, integrity, or availability of systems or information.

Examples:

- Malware infection
- Account compromise
- Phishing
- Unauthorized access
- Data exfiltration
- Ransomware
- Brute-force attacks

---

# SOC Workflow

```text
Security Events
      ↓
Log Collection
      ↓
Security Tools / SIEM
      ↓
Detection
      ↓
Alert
      ↓
Triage
      ↓
Investigation
      ↓
Incident?
   ↙       ↘
 No         Yes
 ↓           ↓
Close      Response
             ↓
         Containment
             ↓
         Eradication
             ↓
           Recovery
             ↓
       Lessons Learned
```

---

# SOC Analyst Responsibilities

Typical activities include:

- Monitor security alerts
- Analyze logs
- Investigate suspicious activity
- Perform alert triage
- Identify IOCs
- Analyze authentication activity
- Analyze network activity
- Document findings
- Escalate confirmed incidents
- Support Incident Response
- Improve detection processes
- Communicate findings

---

# Key Terms

| Term | Meaning |
|---|---|
| SOC | Security Operations Center |
| SIEM | Security Information and Event Management |
| EDR | Endpoint Detection and Response |
| IDS | Intrusion Detection System |
| IPS | Intrusion Prevention System |
| SOAR | Security Orchestration, Automation and Response |
| IOC | Indicator of Compromise |
| IR | Incident Response |
| Alert | Notification of potentially suspicious activity |
| Incident | Security event requiring investigation/response |
| Triage | Initial assessment and prioritization of an alert |
| Threat Hunting | Proactive search for threats |
| Threat Intelligence | Information about threats and threat activity |
| False Positive | Alert that turns out to be benign |
| True Positive | Alert that correctly identifies suspicious activity |
