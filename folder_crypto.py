import os

def encrypt_folder(folder_path, fernet):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".enc"):
                continue

            path = os.path.join(root, file)
            with open(path, "rb") as f:
                data = f.read()

            encrypted = fernet.encrypt(data)

            with open(path + ".enc", "wb") as f:
                f.write(encrypted)

            os.remove(path)


def decrypt_folder(folder_path, fernet):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if not file.endswith(".enc"):
                continue

            path = os.path.join(root, file)
            with open(path, "rb") as f:
                encrypted = f.read()

            decrypted = fernet.decrypt(encrypted)

            original_path = path[:-4]  # remove .enc
            with open(original_path, "wb") as f:
                f.write(decrypted)

            os.remove(path)
