Boosteroid Account Checker 🚀

Boosteroid Account Checker is a Python script designed to check the validity of email and password combinations for Boosteroid.com accounts. The script reads a list of email:password combinations from a text file (accounts.txt), attempts to log in to each account, and then categorizes the accounts as either "valid" or "invalid" based on the login response. The script finally saves the valid and invalid accounts to separate text files in an "output" folder.

before starting script Replace <path_to_accounts_file> with the path to your accounts.txt in account_checker.py


Features:

🚀 Fully async operations for improved performance. 💻 Asynchronous website scraping using the requests library. 📝 Command-line interface (CLI) for easy usage. 📊 Summary of the number of valid and invalid accounts found.

How to Use:

1. Clone the Boosteroid Account Checker repository from GitHub:

`git clone https://github.com/TOBYNSN/boosteroid-account-checker`

2. Navigate to the Boosteroid Account Checker directory:

`cd boosteroid-account-checker`

3. Install the required Python packages:

`pip install -r requirements.txt`

4. Create a text file named accounts.txt in the same directory as the script, and add the email:password combinations you want to check, one per line.

5. Run the Boosteroid Account Checker script using the following command:

`python boosteroid_account_checker.py`

This will launch the script and start checking the validity of the accounts.

6. Once the script finishes running, it will create two text files in an "output" folder: good_accounts.txt and bad_accounts.txt.
The good_accounts.txt file will contain the valid email:password
combinations,and the bad_accounts.txt file will contain the invalid email:password combinations.

<img width="595" alt="image" src="https://github.com/TOBYNSN/boosteroid-account-checker/assets/68747036/50720cdb-91ab-4575-96d6-95bd5df794f0">


License:

● The Boosteroid Account Checker script is licensed under the GNU General Public License version 3 (GPLv3). 
  Please follow all rules and guidelines while using this tool.


Disclaimer:

● The Boosteroid Account Checker script is licensed under the GNU General Public License version 3 (GPLv3).

● This script is intended for educational purposes only and is not intended for any mischievous use.

● I am not responsible for what you do with this script. Please use it responsibly and within the boundaries of the law.
