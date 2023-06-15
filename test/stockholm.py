import os
import sys
import argparse
import cryptography
from cryptography.fernet import Fernet

def init(path, key):
    print("Encrypting files...")

def encrypt(path):
    pass

def decrypt(path):
    pass

def main():
    path = ('/infection/')
    key = Fernet.generate_key()
    
    with open('infection/key.txt', 'wb') as key_file:
        key_file.write(key)
    
    parser = argparse.ArgumentParser(description='Encrypt/Decrypt files')
    parser.add_argument('path', help='Path to encrypt/decrypt', action='store_true')
    parser.add_argument('key', help='Key to encrypt/decrypt', action='store_true')
    parser.add_argument('-v', '--version', help='Show version', action='store_true')
    parser.add_argument('-r', '--reverse', help='Reverse string', action='store_true')
    args = parser.parse_args()

    if args.version:
        print("Stockholm v0.1")
    elif args.reverse:
        print("Decrypting files...")
        key = args.reverse
        decrypt(path, args.key)
    else:
        if args.path:
            path = args.path
        else:
            init(path, key)

if __name__ == '__main__':
    main()