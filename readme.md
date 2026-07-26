# 🛡️ Anti-Keylogger

> A Python-based cybersecurity project that demonstrates **how keyloggers work** and **how an anti-keylogger can detect and stop them**.

## 📖 Overview

Keyloggers are one of the most common types of malware used to capture keyboard input without a user's knowledge. They are often used to steal usernames, passwords, banking credentials, and other sensitive information.

This project was developed to understand both sides of the problem:

1. **Attack Perspective**
   - Demonstrates how a basic software keylogger captures keyboard events.
   - Helps understand the techniques attackers commonly use.

2. **Defense Perspective**
   - Scans running processes.
   - Detects suspicious Python keylogger processes.
   - Identifies suspicious command-line arguments.
   - Detects loaded keyboard-hook related libraries.
   - Attempts to terminate detected keylogger processes.

The goal of this repository is **education and defensive cybersecurity research**.

---

# Project Architecture

```

┌──────────────────┐
│ Keyboard Input   │
└────────┬─────────┘
│
▼
┌──────────────────┐
│ Keylogger Demo   │
│ (Educational)    │
└────────┬─────────┘
│
│ Captures Keys
│
▼
┌──────────────────┐
│ Anti-Keylogger   │
│ Detection Engine │
└────────┬─────────┘
│
├── Scan Running Processes
├── Check Command Line
├── Check Memory Maps
├── Check Open Files
└── Kill Suspicious Process
│
▼
Security Report

```

---

# Features

## Keylogger Module

- Keyboard event monitoring
- Records typed text
- Stores logs into CSV
- Supports:
  - Letters
  - Numbers
  - Symbols
  - Space
  - Backspace
  - Enter
- Timestamp logging

---

## Anti-Keylogger Module

- Detects Python-based keyloggers
- Searches for suspicious process names
- Detects suspicious command-line arguments
- Scans loaded memory modules
- Checks suspicious open files
- Attempts to terminate detected processes
- Displays detection reason

---

# Folder Structure

```

Anti-Keylogger/
│
├── anti-keylogger.py
├── keylogger.py
├── key_log.csv
├── README.md
├── requirements.txt
└── screenshots/
├── demo.png
└── detection.png

```

---

# Technologies Used

- Python 3
- psutil
- pynput
- csv
- datetime
- os
- time

---

# Detection Workflow

The anti-keylogger follows these steps:

### Step 1

Enumerate all running processes.

↓

### Step 2

Identify Python processes.

↓

### Step 3

Inspect command-line arguments.

↓

### Step 4

Search for suspicious keywords such as

- pynput
- keylog
- keylogger
- keyboard
- keystroke

↓

### Step 5

Inspect

- Loaded memory mappings
- Open files

↓

### Step 6

If suspicious activity is found

- Display process information
- Attempt graceful termination
- Force kill if necessary

---

# Installation

Clone the repository

```bash
git clone https://github.com/YourUsername/Anti-Keylogger.git
```

Move into the project

```bash
cd Anti-Keylogger
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

### Run Keylogger Demo

```bash
python keylogger.py
```

Press **ESC** to stop logging.

---

### Run Anti-Keylogger

```bash
python anti-keylogger.py
```

The scanner will:

- Detect suspicious Python processes
- Display detection reasons
- Attempt to terminate detected keyloggers

---

# Example Output

```
Running scan...

Detected Process

PID : 3124

Name : python.exe

Reason :

- suspicious_cmdline
- pynput_in_memory_maps

Status :

Successfully terminated.
```

---

# Learning Outcomes

This project demonstrates:

- Keyboard event handling
- Malware behavior analysis
- Process enumeration
- Python process inspection
- Memory inspection
- Defensive scripting
- Endpoint security concepts
- Malware detection fundamentals

---

# Limitations

This project is intended for **educational purposes** and detects only **basic Python-based keyloggers**.

It does **not** detect:

- Kernel-level keyloggers
- Hardware keyloggers
- DLL injection attacks
- Rootkits
- Obfuscated malware
- Signed malicious software

Future versions can include:

- Machine Learning based detection
- Digital signature verification
- File hash reputation checking
- YARA rule integration
- VirusTotal API support
- GUI Dashboard
- Real-time monitoring
- Windows Startup Registry monitoring

---

# Future Improvements

- AI-based anomaly detection
- Real-time process monitoring
- Automatic quarantine
- PDF security reports
- Threat scoring system
- Email alerts
- Windows service support
- Live dashboard

---

# Educational Purpose

This repository has been created to help students and cybersecurity enthusiasts understand:

- How keyloggers operate
- How defenders can detect malicious behavior
- The relationship between offensive and defensive security

The included keylogger exists solely as a controlled demonstration for testing the anti-keylogger component.

---

# Disclaimer

This software is provided strictly for educational and defensive cybersecurity research.

The keylogger component is included only to demonstrate attack techniques in a controlled environment and to test the anti-keylogger module.

The author does not encourage or support unauthorized monitoring of users or deployment of malicious software.

Users are solely responsible for ensuring that this project is used legally and ethically.
