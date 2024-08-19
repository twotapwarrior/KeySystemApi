from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import base64
import json

def generate_key():
    return base64.urlsafe_b64encode(os.urandom(32))

def encrypt(data: object, key: bytes) -> str:
    key = base64.urlsafe_b64decode(key)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    json_data = json.dumps(data).encode('utf-8')
    padded_data = padder.update(json_data) + padder.finalize()
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    encrypted_data = iv + ciphertext
    return base64.urlsafe_b64encode(encrypted_data).decode('utf-8')

def decrypt(encrypted_data: str, key: bytes):
    key = base64.urlsafe_b64decode(key)
    encrypted_data = base64.urlsafe_b64decode(encrypted_data)
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    json_data = unpadder.update(padded_data) + unpadder.finalize()
    
    return json.loads(json_data)
