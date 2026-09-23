# Threat Intelligence for SOC

## What is Threat Intelligence?

**Threat intelligence** is information about threats that can help security teams understand, identify and investigate malicious activity.

In a SOC, threat intelligence can provide additional context for security events and alerts.

## Threat Intelligence Feeds

A threat intelligence feed can provide information such as:

* Malicious IP addresses
* Malicious domains
* URLs
* File hashes
* Malware indicators
* Other Indicators of Compromise (IOCs)

## IOC

An **Indicator of Compromise (IOC)** is an observable piece of information that may indicate malicious activity.

Examples include:

```text
IP Address
Domain
URL
File Hash
Email Address
```

An IOC by itself does not always prove that an incident occurred. The analyst should investigate the surrounding context.

## SOC Investigation Example

```text
SIEM Alert
    ↓
Suspicious IP detected
    ↓
Check threat intelligence
    ↓
Compare IOC information
    ↓
Review related logs
    ↓
Determine significance
    ↓
Escalate / Respond if required
```

## Threat Intelligence + SIEM

Threat intelligence can be incorporated into SOC monitoring and detection workflows.

For example:

```text
Threat Intelligence
        ↓
IOC
        ↓
Detection / Correlation
        ↓
SIEM Alert
        ↓
SOC Analyst
        ↓
Investigation
```

## Important Principle

Threat intelligence should provide **context**, not replace investigation.

An analyst should consider:

* When the activity occurred
* Which system was involved
* Which user was involved
* What communication occurred
* Whether the IOC is relevant
* Whether additional evidence supports the alert

## Connection to Existing Studies

Threat intelligence connects with:

* Networking
* SIEM
* Log analysis
* Incident response
* Web security
* Digital forensics
* Malware analysis

## Key Takeaway

Threat intelligence helps SOC Analysts add context to security events and identify potentially malicious indicators during investigations.

## Source

Let'sDefend — SOC Fundamentals
