# Description: Encrypts a file using AES-CBC mode
# pip3 install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import struct

def pad(data):
    pad_length = AES.block_size - len(data) % AES.block_size
    print(pad_length)
    return data + bytes([pad_length] * pad_length)

def unpad(data):
    pad_length = data[-1]
    return data[:-pad_length]

"""
def encrypt_file(input_file, output_file, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)
    with open(output_file, 'wb') as f:
        f.write(plaintext)
"""
def my_encrypt_file(input_file, output_file, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    with open(output_file, 'wb') as f:
        f.write(ciphertext)

def my_decrypt_file(input_file, output_file, key, iv):
    with open(input_file, 'rb') as f:
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)
    with open(output_file, 'wb') as f:
        f.write(plaintext)

def generate_key_iv():
    key = get_random_bytes(32)  # AES-256
    iv = get_random_bytes(16)   # AES block size
    return key, iv

# Example usage

print(AES.block_size)
key, iv = generate_key_iv()
print(f"Key: {key.hex()}")
print(f"IV: {iv.hex()}")
iv_low, iv_high = struct.unpack('<QQ', iv)
print(f"IV low: {hex(iv_low)}")
print(f"IV high: {hex(iv_high)}")

"""
encrypt_file('plaintext.txt', 'encrypted.bin', key, iv)
decrypt_file('encrypted.bin', 'decrypted.txt', key, iv)
"""
my_encrypt_file('plaintext.txt', 'encrypted.bin', key, iv)
my_decrypt_file('encrypted.bin', 'decrypted.txt', key, iv)
