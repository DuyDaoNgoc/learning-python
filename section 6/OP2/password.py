print('Welcome to the password generator and access control system!')
import re
import secrets
import string
import subprocess
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password
max_attempts = 3
for i in range(max_attempts):
    if __name__ == '__main__':
        new_password = generate_password()
        user_name = input('Enter your username: ')
        savage_usernames = [user_name, user_name.lower(), user_name.upper(), user_name.capitalize()]
        print('Generated password:', new_password)

    UserName = input("Enter your username: ")
    ValuePassword = input("Enter your password: ")
    if UserName in savage_usernames and ValuePassword == new_password:
        if savage_usernames.index(UserName) == 0:
            print("Welcome, user!")
            print("Access granted")
            subprocess.run(["python", r"D:\learning-python\section 6\OP2\shortestpath.py"])
            break
        else:
            print('None')
    else:
        print("Access denied")
        remaining = max_attempts - i - 1

