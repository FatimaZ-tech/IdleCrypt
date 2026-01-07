import time
import os
from cryptography.fernet import Fernet
from activity_monitor import start_activity_monitor, idle_seconds
from crypto_utils import derive_key
from folder_crypto import encrypt_folder

IDLE_LIMIT = 600  #10 minutes
TARGET_FOLDER = "SensitiveData"

start_activity_monitor()

password = input("Set encryption password: ")
SALT_FILE = ".salt"

if os.path.exists(SALT_FILE):
    with open(SALT_FILE, "rb") as f:
        salt = f.read()
else:
    salt = os.urandom(16)
    with open(SALT_FILE, "wb") as f:
        f.write(salt)

key = derive_key(password, salt)
fernet = Fernet(key)

print("\n[+] Monitoring user activity...")

while True:
    if idle_seconds() > IDLE_LIMIT:
        print("\n[+] Idle detected. Encrypting folder...")
        encrypt_folder(TARGET_FOLDER, fernet)
        print("\n[+] Encryption complete.")
        break
    time.sleep(5)
