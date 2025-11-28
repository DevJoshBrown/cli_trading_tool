import sys

from io_helpers import string_input, yes_no_input
from user_database import add_user, search_email


def login_process():
    has_account = yes_no_input("Do you have an account already?")

    ##### LOGIN TO EXISTING ACCOUNT #####
    if has_account == "yes":
        email = string_input("What is your email address")
        user = search_email(email)
        if user:
            account = user[0]
            confirm = yes_no_input(
                f"is this your account?\nNAME:{account['name']}\nEMAIL:{account['email']}"
            )
            if confirm == "yes":
                print(f"\nLogging in as {account['name']}")
                return True, account
            if confirm == "no":
                return False, account

        else:
            print(f"{email} not found as an existing user.")
            return False, None

    ##### SIGN UP #####
    elif has_account == "no":
        create_account_start = yes_no_input("Do you want create a new account?")
        if create_account_start == "yes":  # create new account
            print("creating a new account...")
            result = create_account()
            if result:
                print("\naccount created, please log-in!")
            else:
                print("account creation failed, please try again")
            return False, None

        else:  # continue as guest
            continue_as_guest = yes_no_input("Do you want to continue as a guest?")
            if continue_as_guest == "yes":
                ##!!## continueasguest()
                user = search_email("guest")
                if user:
                    account = user[0]
                    print("continuing as a guest")
                    return True, account
                return False, None
            elif continue_as_guest == "no":
                return False, None

    else:
        raise Exception("Unexpected error, exiting the application: Errorcode-001")
        sys.exit(1)
    return False, None


def create_account():
    name = string_input("What is your name")
    email = string_input("What is your email address")
    account_created = add_user(name, email)

    return account_created  # True or False depending on success.
