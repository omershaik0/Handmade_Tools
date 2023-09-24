# SHA256 Hash Cracker

A simple Python script for cracking SHA256 hashes using a wordlist.

## Description

This Python script allows you to crack SHA256 hashes by comparing them to a list of potential passwords provided in a wordlist file. It's a basic example of password cracking using a dictionary attack.

## Features

- Crack SHA256 hashes with a provided wordlist.
- Progress visualization using `tqdm`.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Required Python libraries: `pwn`, `tqdm`

## Usage

   ```bash
   https://github.com/omershaik0/Handmade_Tools/tree/main/SHA256-Cracker
   cd SHA256-Cracker
   python sha256_cracker.py <SHA256_Hash> <Wordlist_File>
   python sha256_cracker.py f89e9192d8a0e3ebc1d01cabaefb35da06a8ac21ca57d0e92a4d40b4b21e22b1 wordlist.txt or path to the wordlist.
   ```
![Script Execution](https://github.com/omershaik0/Handmade_Tools/blob/main/SHA256-Cracker/cracked.png)
