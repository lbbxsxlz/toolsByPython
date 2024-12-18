# Description: Encrypts a file using AES-CBC mode
# pip3 install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import struct

def generate_random_file(filename, size):
    with open(filename, 'wb') as f:
        f.write(get_random_bytes(size))

generate_random_file('random.bin', 100)

def pad(data):
    pad_length = AES.block_size - len(data) % AES.block_size
    return data + bytes([pad_length] * pad_length)

def unpad(data):
    pad_length = data[-1]
    return data[:-pad_length]

def encrypt_file(input_file, output_file, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext)
    with open(output_file, 'wb') as f:
        f.write(ciphertext)

def decrypt_file(input_file, output_file, key, iv):
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

def save_key_iv_to_file(key, iv, filename):
    with open(filename, 'wb') as f:
        f.write(key + iv)

def load_key_iv_from_file(filename):
    with open(filename, 'rb') as f:
        key_iv = f.read()
    key = key_iv[:32]
    iv = key_iv[32:]
    return key, iv

key, iv = generate_key_iv()
print(f"Key: {key.hex()}")
print(f"IV: {iv.hex()}")

encrypt_file('random.bin', 'enc_py.bin', key, iv)

# Save key and IV to a file
save_key_iv_to_file(key, iv, 'key_iv.bin')

# Load key and IV from a file
loaded_key, loaded_iv = load_key_iv_from_file('key_iv.bin')
print(f"Loaded Key: {loaded_key.hex()}")
print(f"Loaded IV: {loaded_iv.hex()}")

decrypt_file('enc_py.bin', 'dec_py.bin', loaded_key, loaded_iv)
