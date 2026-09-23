# EDR for SOC Investigation

## What is EDR?

**EDR (Endpoint Detection and Response)** is a security technology used to monitor endpoint activity and help detect, investigate and respond to suspicious behaviour.

Endpoints can include:

* Workstations
* Laptops
* Servers
* Other systems running an EDR agent

## Why EDR Matters in a SOC

A SOC Analyst can use EDR information to investigate activity occurring directly on an endpoint.

Useful investigation information can include:

* Processes
* Parent and child processes
* Users
* Files
* Network connections
* Command execution
* Endpoint activity
* Security alerts

## Investigation Perspective

When an endpoint generates an alert, the analyst should establish:

1. What happened?
2. Which endpoint was involved?
3. Which user was involved?
4. Which process caused the activity?
5. What parent process started it?
6. Was a file created or executed?
7. Were network connections made?
8. Is the behaviour expected or suspicious?

## Process Relationships

Understanding process relationships is important during endpoint investigation.

For example:

```text
Parent Process
      ↓
Child Process
      ↓
Suspicious Activity
```

The process tree can help an analyst understand how an activity started and what happened afterward.

## EDR + SIEM

EDR and SIEM can complement each other.

```text
Endpoint
   ↓
EDR
   ↓
Security Events
   ↓
SIEM
   ↓
SOC Analyst
   ↓
Investigation / Response
```

The SIEM can provide broader correlation across multiple systems, while EDR provides detailed endpoint-level visibility.

## Connection to Existing Studies

EDR connects with existing knowledge of:

* Linux processes
* Linux services
* Network connections
* File activity
* System behaviour
* Digital forensics
* Incident investigation

## Key Takeaway

EDR gives the SOC Analyst visibility into endpoint behaviour and provides useful evidence for investigating security alerts and incidents.

## Source

Let'sDefend — SOC Fundamentals
