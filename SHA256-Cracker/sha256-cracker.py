# Import necessary libraries
from pwn import *
import sys
from tqdm import tqdm

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Invalid Argument")
    print("Usage: {} <SHA256 Hash> <Wordlist>".format(sys.argv[0]))
    exit()

# Get the SHA256 hash from the command-line argument
given_hash = sys.argv[1]

# Open the wordlist file for password cracking
with open(sys.argv[2], 'r', encoding='latin-1') as password_file:
    lines = [line.rstrip() for line in password_file]
    
    # Iterate through each line (password) in the wordlist
    for password in tqdm(lines):
        # Encode the password in latin-1 encoding
        encoded_password = password.encode("latin-1")
        
        # Calculate the SHA256 hash of the encoded password using sha256sumhex
        hashed_password = sha256sumhex(encoded_password)
        
        # Check if the calculated hash matches the given hash
        if given_hash == hashed_password:
            print("\n")
            print("{} Hash Cracked with Password {}\n".format(given_hash, encoded_password.decode("latin-1")))
            break
    else:
        # If no match is found, print "Not Found."
        print("Not Found.")
