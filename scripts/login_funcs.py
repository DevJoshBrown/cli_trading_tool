import sys

import trades_database
import user_database
from app_control import QuitProgram
from io_helpers import string_input, yes_no_input
from user_database import add_user, save_user_database, search_email


def log_in():
    while True:
        result, account = login_process()
        if result and account is not None:
            print(f"\nhi {account['name']}, login successful!\n")
            return account
        else:
            continue


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

        else:
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


def edit_username(current_user):
    new_name = string_input("What would you like your new username to be?")
    confirm = yes_no_input(
        f"Changing your name from {current_user['name']} to {new_name}, are you sure?"
    )
    if confirm == "yes":
        current_user["name"] = new_name
        save_user_database()

    elif confirm == "no":
        print("Name change cancelled.")


def edit_email(current_user):
    new_email = string_input("What would you like your new email to be?")
    confirm = yes_no_input(
        f"Changing your email from {current_user['email']} to {new_email}, are you sure?"
    )
    if confirm == "yes":
        current_user["email"] = new_email
        save_user_database()

    elif confirm == "no":
        print("Email change cancelled.")


def delete_account(current_user):
    print(
        "Deleting your account will remove your user and all your trades from the system, this process is irreversible."
    )
    confirm = yes_no_input("Are you sure you want to delete your account?")
    if confirm == "yes":
        user_id = current_user["number"]
        for user in user_database.user_database:
            if user["number"] == user_id:
                user_database.user_database.remove(user)
                break
        user_database.save_user_database()
        new_trade_list = []
        for trade in trades_database.trades:
            if trade.owner_id != user_id:
                new_trade_list.append(trade)
        trades_database.trades = new_trade_list
        trades_database.save_trades_database()
        return "deleted"

    elif confirm == "no":
        print("Account deletion cancelled.")


def edit_account(current_user):
    while True:
        option = input(
            f"\nWhat would you like to do?\n[1]: Change my username\n[2]: Change my email\n[3]: Delete my account\n[C]: Previous menu\n[Q]: Save & Quit\n\n[{current_user['name']}]:"
        )
        if option == "1":
            edit_username(current_user)
        if option == "2":
            edit_email(current_user)
        if option == "3":
            deleted = delete_account(current_user)
            if deleted == "deleted":
                print("account deleted")
                current_user = None
                return "deleted"
        if option.lower() == "c":
            break
        if option.lower() == "q":
            raise QuitProgram
