# Stockholm
This is a 42 Cybersecurity-Bootcamp project.
Encryption and decryption of files using a 128-bit key in CBC mode.
This project create a docker container, a safe environment to test the program, where the user can use the program stockholm.py to encrypt and decrypt files.

## Project description

This project is a program for encrypting and decrypting files within a specific folder recursively. 
It utilizes Fernet, a secure and reliable encryption implementation for Python using AES-128 (Advanced Encryption Standard) in CBC (Cipher Block Chaining) mode.

The project aims to provide a user-friendly and effective way to secure files using encryption techniques, with the added advantage of being implemented in Python, a popular and versatile programming language.

🟣 The encrypted key will be stored in a file named key.txt in the same directory as the program.

## Pre-requisites

* Docker: Ensure that you have Docker installed on your machine. If not, you can download it [here](https://www.docker.com/get-started).
* Unix-based operating system: This project was developed and tested on a Linux-based operating system. It is recommended to use a Linux-based or a GitBash terminal.

## Usage

1 - Clone the repository
<pre><code>git clone https://github.com/AppacheAZ/Stockholm.git name_repository</code></pre>

2 - Navigate to the repository
<pre><code>cd name_repository</code></pre>

3 - Launch the container
<pre><code>sh start.sh</code></pre>

4 - Acces to the container in other shell tab
<pre><code>sh acces.sh</code></pre>

5 - Run the program in the path /home/test
<pre><code>python3 stockholm.py</code></pre>

6 - To decrypt the files, run the program again with the flag -r and the key (into test/key.txt)
<pre><code>python3 stockholm.py -r 'key.....'</code></pre>

### Flags

* -h: Display the help message.
* -v: Display the version of the program.
* -r: Decrypt the files in the directory recursively. The key must be provided as an argument.
* -p: Specify the path to the directory to encrypt or decrypt. If not specified, the ./infection directory will be used.
