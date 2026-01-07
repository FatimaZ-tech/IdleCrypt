# IdleLock

IdleCrypt is a macOS-based security tool that automatically encrypts the contents of a sensitive folder when the system is left unattended for a specified period of time.

The project is designed to mitigate risks caused by unlocked systems in shared workspaces by enforcing **idle-based data protection** at the endpoint level.

---

## What IdleCrypt Does

1. The script monitors **keyboard and mouse activity** to determine user presence.
2. If no activity is detected for a configurable idle period (default: 10 minutes), the tool triggers encryption.
3. All files inside the target folder are encrypted recursively.
4. Encrypted files are marked with a `.enc` extension.
5. A separate script is used to decrypt the files when access is required.

Note: This project encrypts **file contents**, not the folder metadata itself. This is standard practice in file-level encryption systems.

---

## Tech Stack

- **Language:** Python
- **Cryptography:** `cryptography` (Fernet + PBKDF2)
- **Activity Monitoring:** `pynput`
- **Platform:** macOS

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/FatimaZ-tech/IdleCrypt.git
cd idlelock
pip install -r requirements.txt
```

---

## macOS Permissions (Important)

macOS restricts keyboard input monitoring by default.  
IdleCrypt requires explicit permission to detect user activity.

You **must allow** the following permissions:

- **Accessibility**
- **Input Monitoring**

---

### Steps to Grant Permissions

1. Open **System Settings**
2. Navigate to **Privacy & Security**
3. Enable the following sections:
   - **Accessibility**
   - **Input Monitoring**
4. Add:
   - **Terminal** (or the Python executable)

Note: Restart Terminal after granting permissions for the changes to take effect.

---

## Configure the Folder Path

You must configure the **same folder path** in **both scripts**.

---

### `encrypt_on_idle.py`

```python
TARGET_FOLDER = "FolderPath"
```

### `decrypt_folder.py`

```python
folder = "FolderPath"
```

---

## Running IdleCrypt (Encryption)

Run the encryption monitor:

```bash
python encrypt_on_idle.py
```

You will be prompted to set a password.

After starting, the script will:

- Monitor user keyboard and mouse activity  
- Detect periods of inactivity  
- Encrypt the files in the target folder after the idle timeout is reached

---

## Decrypting the Folder

When you want access to your files again, run:

```bash
python decrypt_folder.py
```

Enter the **same password** used during encryption. Encrypted files (`.enc`) will be restored to their original form

---

## Cryptographic Design Notes

- Password-based key derivation uses **PBKDF2 + SHA-256**
- A random **salt** is generated once and stored locally in a `.salt` file
- The salt is **not secret**, but is required for correct decryption
- Encrypted files are marked with a `.enc` extension
- This prevents accidental double encryption

---

## Auto-Run & Persistence (Not Implemented)

IdleCrypt does not implement any auto-run or persistence mechanism.

The tool is designed to be executed manually to keep the codebase
portable, transparent, and easy to audit.

Users who require automatic execution at login may **implement their own**
persistence mechanism (for example, using macOS LaunchAgents) by modifying
the code and providing system-specific absolute paths.

No auto-run functionality is included in this project.

---

## Configuring Idle Time

The idle timeout is configurable directly in the code.

In `encrypt_on_idle.py`, adjust the following value:

```python
IDLE_LIMIT = 600  # idle time in seconds
```

---

## Limitations

- This is **not** full-disk encryption
- Folder metadata (names and directory structure) remains visible
- No protection against attackers with administrative privileges
- If the password is lost, encrypted data **cannot be recovered**

---

## Ethical Considerations

IdleCrypt demonstrates techniques that may resemble those used by malware  
(e.g., file encryption and persistence).

The project is intended **strictly for educational and research purposes**.

---

## License

This project is licensed under the **MIT License**.

---

## Author

Developed by **Fatima Z**.





