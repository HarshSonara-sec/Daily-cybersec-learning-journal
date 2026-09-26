# SOC Analyst Levels

> SOC tier structures vary between organizations. The model below represents a common structure.

## Tier 1 — Monitoring and Triage

Tier 1 analysts are commonly the first level of alert handling.

### Responsibilities

- Monitor security alerts
- Review SIEM alerts
- Perform initial investigation
- Validate whether an alert is suspicious
- Identify false positives
- Collect basic evidence
- Prioritize alerts
- Escalate complex or confirmed incidents

### Typical Questions

- What triggered the alert?
- Which user was involved?
- Which IP address was involved?
- Which host was affected?
- When did it happen?
- Is the activity expected?
- Is there evidence of compromise?
- Does the alert require escalation?

### Example

```text
SIEM Alert
    ↓
Tier 1 Analyst
    ↓
Check user / host / IP / time / activity
    ↓
Benign → Close
Suspicious → Escalate
```

---

# Tier 2 — Investigation and Incident Response

Tier 2 analysts generally handle more complex investigations.

### Responsibilities

- Perform deeper alert investigation
- Analyze multiple log sources
- Investigate confirmed incidents
- Correlate events
- Analyze attack techniques
- Identify affected systems
- Support containment
- Investigate IOCs
- Perform timeline analysis
- Escalate advanced cases

### Example

```text
Tier 1
  ↓
Suspicious activity confirmed
  ↓
Tier 2
  ↓
Analyze:
- Authentication logs
- Endpoint activity
- Network connections
- Processes
- User activity
  ↓
Determine scope
  ↓
Response / Containment
```

---

# Tier 3 — Advanced Security Analysis

Tier 3 analysts generally handle advanced or highly complex investigations.

### Responsibilities

- Advanced threat hunting
- Malware analysis
- Advanced incident investigation
- Detection engineering
- Advanced forensic analysis
- Threat intelligence analysis
- Development of detection rules
- Investigation of sophisticated attacks

---

# Tier 4 — Advanced Research

Some organizations use a Tier 4 classification, while others do not.

Possible responsibilities include:

- Advanced threat research
- Threat intelligence research
- Malware research
- Vulnerability research
- Red team / adversary simulation
- Advanced threat hunting
- Security research

---

# Comparison

| Tier | Main Focus | Typical Work |
|---|---|---|
| Tier 1 | Monitoring & Triage | Alert review, basic investigation, escalation |
| Tier 2 | Investigation & Response | Deep investigation, incident handling, containment |
| Tier 3 | Advanced Analysis | Threat hunting, malware analysis, detection engineering |
| Tier 4 | Advanced Research | Threat research and advanced security research |

---

# Important

Higher tiers generally represent increasing investigation complexity and specialization rather than simply a ranking of analysts.

Organizations may:

- Combine tiers
- Rename roles
- Assign different responsibilities
- Use different team structures

For an entry-level SOC analyst, important foundations include:

- Networking
- Linux
- Windows fundamentals
- Log analysis
- SIEM
- Authentication
- Common attack techniques
- Incident Response
- Documentation
- Analytical thinking
