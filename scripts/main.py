import sys

from login_funcs import login_process
from user_database import load_user_database


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


def main():
    print("WELCOME TO THE CLI TRADING TOOL.")
    print("loading users...")
    load_user_database()
    print("loading complete.")

    login_failed = True
    while login_failed:
        result = login_process()
        if result:
            login_failed = False
            print("login successful!")
        else:
            print("\nlogin failed, please try again")
            continue


if __name__ == "__main__":
    main()
