import os
import subprocess

def generate_random_file(filename, size):
    with open(filename, 'wb') as f:
        f.write(os.urandom(size))

def load_iv_from_file(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    iv = content[16:]
    return iv

def append_files(file1, file2, output_file):
    with open(output_file, 'wb') as outfile:
        for fname in [file1, file2]:
            with open(fname, 'rb') as infile:
                outfile.write(infile.read())

generate_random_file('file1.bin', 32)
generate_random_file('file2.bin', 128)

key = os.urandom(32)  # 256 位密钥
# 生成随机的初始化向量（IV）
iv = os.urandom(16)

print(f'Key: {key.hex()}')
print(f'IV: {iv.hex()}')

# Encrypt the file using openssl command
openssl_cmd = f"openssl enc -e -aes-256-cbc -in file1.bin -out file1_enc.bin -K {key.hex()} -iv {iv.hex()} -nopad"
print(openssl_cmd)
try:
    subprocess.run(openssl_cmd, shell=True, check=True)
    print(f"Encrypted file1.bin to file1_enc.bin using openssl.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while encrypting with openssl: {e}")

new_iv = load_iv_from_file('file1_enc.bin')
print(f'New IV: {new_iv.hex()}')

# Encrypt the file using openssl command
openssl_cmd = f"openssl enc -e -aes-256-cbc -in file2.bin -out file2_enc.bin -K {key.hex()} -iv {new_iv.hex()} -nopad"
print(openssl_cmd)
try:
    subprocess.run(openssl_cmd, shell=True, check=True)
    print(f"Encrypted file2.bin to file2_enc.bin using openssl.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while encrypting with openssl: {e}")

append_files('file1_enc.bin', 'file2_enc.bin', 'combine.bin')

# Decrypt the file using openssl command
openssl_cmd = f"openssl enc -d -aes-256-cbc -in combine.bin -out combine_dec.bin -K {key.hex()} -iv {iv.hex()} -nopad"
print(openssl_cmd)
try:
    subprocess.run(openssl_cmd, shell=True, check=True)
    print(f"Decrypted combine.bin to combine_dec.bin using openssl.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while decrypting with openssl: {e}")
