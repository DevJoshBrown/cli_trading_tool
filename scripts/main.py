import sys

from login_funcs import login_process
from user_database import load_user_database


def main():
    print("WELCOME TO THE CLI TRADING TOOL.")
    print("loading users...")
    load_user_database()
    print("loading complete.")

    login_failed = True
    while login_failed:
        result, account = login_process()
        if result:
            login_failed = False
            current_user = account
            if current_user is not None:
                print(f"hi {current_user['name']}, login successful!")
            else:
                login_failed = True
                continue
        else:
            continue


if __name__ == "__main__":
    main()
