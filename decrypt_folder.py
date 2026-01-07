from cryptography.fernet import Fernet
from crypto_utils import derive_key
from folder_crypto import decrypt_folder
import os

folder = "FolderPath"
password = input("Enter password: ")
SALT_FILE = ".salt"

with open(SALT_FILE, "rb") as f:
    salt = f.read()

key = derive_key(password, salt)
fernet = Fernet(key)


decrypt_folder(folder, fernet)
print("\n[+] Folder decrypted.")
