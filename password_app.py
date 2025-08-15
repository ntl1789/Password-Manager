from cryptography.fernet import Fernet
import json

class PasswordApp():
    def __init__(self) -> None:
        self.key_file = "test_key.txt"
        self.password_file = "passwords.json"
    
    def generate_key(self):
        #using fernet to create key
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as file:
            file.write(key)
        return key

    def load_key(self):
        return open(self.key_file, "rb").read()
    
    
    def encrypt(self, password, key):
        #using the generated key to initialise a Fernet cipher
        f = Fernet(key)
        return f.encrypt(password.encode()).decode()


    def decrypt(self, password, key):
        f = Fernet(key)
        bytes_password = password.encode()
        return f.decrypt(bytes_password).decode()


    def save_passwords(self, encrypted_passwords: dict):
        with open(self.password_file, "w") as file:
            json.dump(encrypted_passwords, file)


    def load_passwords(self) -> dict:
        try: 
            with open(self.password_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            with open(self.password_file, "a"): pass
            my_dict = {}
            return my_dict
        except json.JSONDecodeError:
            my_dict = {}
            return my_dict

    def add_password(self, account, username, password, key):
        #load dict
        passwords = self.load_passwords()
        #encrypt new password 
        encrypted_password = self.encrypt(password, key)
        my_dict = {
                    account: {
                                "username": username,
                                "password": encrypted_password,
                            }
                }
        passwords.update(my_dict)
        self.save_passwords(passwords)
        print(f"Password for {account} saved successfully.")
        
