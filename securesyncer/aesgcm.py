import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend


class AESGCM:
    def __init__(self, key=None):
        self.key = key if key else os.urandom(32)  # 256-bit key for AES-256

    def encrypt(self, plaintext):
        backend = default_backend()
        iv = os.urandom(12)
        cipher = Cipher(algorithms.AES(self.key),
                        modes.GCM(iv), backend=backend)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return (iv, ciphertext, encryptor.tag)

    def decrypt(self, iv, ciphertext, tag):
        backend = default_backend()
        cipher = Cipher(algorithms.AES(self.key),
                        modes.GCM(iv, tag), backend=backend)
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()

    def encrypted_key(self, password, salt=None):
        salt = salt if salt else os.urandom(16)
        backend = default_backend()
        kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=backend)
        encrypted_key = kdf.derive(password.encode())
        return (salt, encrypted_key)


plaintext = b"Hello, world!"
password = "my_secure_password"

# Create an AESGCM instance
aes_gcm = AESGCM()

# Encrypt the plaintext
iv, ciphertext, tag = aes_gcm.encrypt(plaintext)
print("IV:", iv)
print("Ciphertext:", ciphertext)
print("Tag:", tag)

# Decrypt the ciphertext
decrypted_text = aes_gcm.decrypt(iv, ciphertext, tag)
print("Decrypted text:", decrypted_text)

# Derive an encrypted key from a password
salt, encrypted_key = aes_gcm.encrypted_key(password)
print("Salt:", salt)
print("Encrypted key:", encrypted_key)
