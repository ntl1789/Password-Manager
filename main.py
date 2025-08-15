from password_app import PasswordApp


def main():

    logged_in = False
    manager = True

    app = PasswordApp()

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
        key = app.load_key()
    except FileNotFoundError:
        key = app.generate_key()

    passwords_dict = app.load_passwords()

    while manager:
        option = input("Choose your option [1 - 4]\n"
                        "[1] Retrieve a password\n"
                        "[2] Add a new password\n"
                        "[3] Delete a password\n"
                        "[4] Exit program\n" )
        if option == "1":
            #search for username and password for particular account:
            account = input("What account do you want the details for?: ")

            if account in passwords_dict.keys():
                username = passwords_dict[account]["username"]
                encrypted_password = passwords_dict[account]["password"]
                decrypted_password = app.decrypt(encrypted_password, key)
                print(f"Username: {username}\nPassword: {decrypted_password}")
            else:
                print("No details for this account.")
        elif option == "2":
            pass_done = False
            while not pass_done:
                new_account = input("What is the name of the account?: ")
                new_username = input("What is your username?: ")
                new_password = input("What is your password?: ")
                confirm = input(f"For {new_account}, your username is: {new_username}, and your password is: {new_password}.\n"
                    "Is this correct? [yes/no]: ").lower()
                if confirm == "yes" or "y": 
                    pass_done = True
                #what if account already in passwords?
                app.add_password(new_account, new_username, new_password, key)
        elif option == "3":
            #remove password
            print("to be written")
        elif option == "4":
            manager = False
        else:
            print("Invalid option entered. Enter a number between 1 - 4: ")

main()












