# Threat Model — IdleCrypt

## Overview

IdleCrypt is designed to protect sensitive files on a user workstation from unauthorized access that may occur when a system is accidentally left unattended.

This threat model defines the scope, assumptions, goals, and limitations of the project.

---

## Assets

- Sensitive user files stored within the protected directory
- User provided encryption password
- Locally stored encryption artifacts (e.g., encrypted files, salt file)

---

## Threat Actor

IdleCrypt primarily considers the following threat actor:

- An individual with **temporary physical access** to an unlocked user system
  (e.g. coworker or passerby)

The attacker is assumed to have:
- No administrative privileges
- No prior knowledge of the encryption password

---

## In-Scope Threats

IdleCrypt is designed to mitigate the following threat:

- Unauthorized access to sensitive files when a user accidentally leaves their system unlocked and unattended in a workplace environment

---

## Out-of-Scope Threats

IdleCrypt does **not** attempt to protect against:

- Attackers with administrative or root privileges
- Malware execution or remote code execution
- Memory inspection or live process analysis
- Attacks occurring after successful decryption
- Full-disk forensic analysis

---

## Assumptions

IdleCrypt operates under the following assumptions:

- The operating system and filesystem are not compromised
- The encryption password remains confidential
- The user intentionally executes the tool and controls its configuration

---

## Security Goals

- Protect file contents at rest during periods of user inactivity
- Minimize accidental data exposure on unlocked systems

---

## Non-Goals

- Replacing full-disk encryption
- Preventing all forms of insider threat
- Providing enterprise level endpoint detection

---

## Summary

IdleCrypt is a focused endpoint security utility designed to address a specific and realistic risk scenario involving unattended systems. Its scope is intentionally limited to to keep the codebase portable and transparent.
