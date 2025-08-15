import hashlib
from cryptography.fernet import Fernet
import json

message = "encode me pleasee".encode()
hashed = hashlib.sha3_256(message).hexdigest()

KEY_FILE = "test_key.txt"
PASSWORD_FILE = "passwords.json"


def generate_key():
#using fernet to create key
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as file:
        file.write(key)
    return key

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt(password, key):
    #using the generated key to initialise a Fernet cipher
    f = Fernet(key)
    return f.encrypt(password.encode())


def decrypt(password, key):
    f = Fernet(key)
    return f.decrypt(password.decode())


def save_passwords(encrypted_passwords: dict):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(str(encrypted_passwords), file)


def load_passwords() -> dict:
    with open(PASSWORD_FILE, "r") as file:
        passwords_dict = json.load(file)
    return passwords_dict

def add_password(account, password, key):
    passwords =load_passwords()
    encrypted_password = encrypt(password, key)
    passwords[account] = encrypt.decode()
    save_passwords(passwords)
    print(f"Password for {account} saved successfully.")

logged_in = False
manager = True

print("Welcome to your password manager.")

while not logged_in:
    username = input("Enter your username: ")
    master_password = input("Enter your password: ")

    if username == "user" and master_password == "test":
        print("Username and password correct.\n")
        logged_in = True
    else:
        print("Username or password incorrect. Try again.") 

try:
    key = load_key()
except FileNotFoundError:
    key = generate_key()

try:
    passwords_dict = load_passwords()
    print(passwords_dict)
except FileNotFoundError:
    print("No passwords exist yet. Creating file.")
    with open(PASSWORD_FILE, "a"): pass
    passwords_dict = {}
except json.JSONDecodeError:
    passwords_dict = {}

while manager:
    option = input("Choose your option [1 - 4]\n"
                    "[1] Retrieve a password\n"
                    "[2] Add a new password\n"
                    "[3] Delete a password\n"
                    "[4] Exit program" )
    if option == "1":
        #search for username and password for particular account:
        account = input("What account do you want the details for?")

        if account in passwords_dict.items():
            username = passwords_dict[account]["username"]
            encrypted_password = passwords_dict[account]["password"]
            decrypted_password = decrypt(encrypted_password, key)
            print(f"Username: {username}\nPassword: {decrypted_password}")
        else:
            print("No details for this account.")
    elif option == "2":
        pass_done = False
        while not pass_done:
            new_account = input("What is the name of the account?: ")
            new_username = input("What is your username?: ")
            new_password = input("What is your password?: ")
            confirm = (f"For {new_account}, your username is: {new_username}, and your password is: {new_password}.\n"
                "Is this correct? [yes/no]: ").lower()
            if confirm == "yes" or "y": 
                pass_done = True
            #what if account already in passwords?

        new_encrypted_password = encrypt(new_password, key)

        new_dict = {new_account: {
                                        "username": new_username,
                                        "password": new_encrypted_password
            }}
        
        print(type(passwords_dict))
        passwords_dict.update(new_dict)

        save_passwords(passwords_dict)


template = {
                'Google': {
                            'username': 'example@email.com', 
                            'password': 'rgergr'
                        }, 
                'Amazon': {
                            'username': 'example@email.com', 
                            'password': 'enfdjkwe'
                        }
            }

new_dict = {"username": "blahh", "Password": "test"
}










