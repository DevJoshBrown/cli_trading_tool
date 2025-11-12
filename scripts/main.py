import sys

from user_database import add_user, load_user_database, search_email, user_database


def yes_no_input(question):
    valid = False
    while not valid:
        response = input(
            "\n" + question + "\nPlease Enter [Y] for yes, [N] for no, or [Q] to quit: "
        )
        if response == "y" or response == "Y":
            valid = True
            return "yes"
        if response == "n" or response == "N":
            valid = True
            return "no"
        if response == "q" or response == "Q":
            valid = True
            print("\nClosing the application\n")
            sys.exit(0)
        else:
            print("\ninvalid input, please try again...")


def string_input(question):
    valid = False
    while not valid:
        response = input(
            "\n" + question + "\nPlease type your response and press Enter: "
        )
        return response


def login_process():
    has_account = yes_no_input("Do you have an account already?")

    ##### LOGIN TO EXISTING ACCOUNT #####
    if has_account == "yes":
        email = string_input("What is your email address")
        user = search_email(email)
        if user:
            account = user[0]
            confirm = yes_no_input(f"is this your account? {account}")
            if confirm == "yes":
                print(f"Logging in as {account}")
                return "login success"
            if confirm == "no":
                return "login failed"

        else:
            print(f"{email} not found as an existing user.")
            return "login failed"

    ##### SIGN UP #####
    elif has_account == "no":
        create_account_start = yes_no_input("Do you want create a new account?")
        if create_account_start == "yes":
            print("creating a new account...")
            return create_account()

        else:
            continue_as_guest = yes_no_input("Do you want to continue as a guest?")
            if continue_as_guest == "yes":
                ##!!## continueasguest()
                print("continuing as a guest")
            elif continue_as_guest == "no":
                return "login failed"

    else:
        raise Exception("Unexpected error, exiting the application: Errorcode-001")
        sys.exit(1)


def create_account():
    name = string_input("What is your name")
    email = string_input("What is your email address")
    account_created = add_user(name, email)
    if account_created:
        return "Successfully created a new account."
    return "Failed to make a new account."


def main():
    print("WELCOME TO THE CLI TRADING TOOL.")
    print("loading users...")
    load_user_database()
    print("loading complete.")

    login_failed = True
    while login_failed:
        result = login_process()
        if result == "login success":
            login_failed = False
            print("login successful!")
        else:
            print("\nlogin failed")
            continue


if __name__ == "__main__":
    main()
