import sys

from login_funcs import login_process
from user_database import load_user_database


def log_in():
    login_failed = True
    while login_failed:
        result, account = login_process()
        if result:
            login_failed = False
            current_user = account
            if current_user is not None:
                print(f"hi {current_user['name']}, login successful!")
                return current_user

            else:
                login_failed = True
                continue
        else:
            continue


def main():
    print("WELCOME TO THE CLI TRADING TOOL.")
    print("loading users...")
    load_user_database()
    print("loading complete.")
    current_user = log_in()

    # MAIN MENU
    while current_user is not None:
        print(f"logged in as {current_user['name']}")
        # main menu
        return


if __name__ == "__main__":
    main()
