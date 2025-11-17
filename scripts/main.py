import sys

from login_funcs import login_process
from user_database import load_user_database, save_user_database


def log_in():
    login_failed = True
    while login_failed:
        result, account = login_process()
        if result:
            login_failed = False
            current_user = account
            if current_user is not None:
                print(f"\nhi {current_user['name']}, login successful!\n")
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
        print(f"\n\nlogged in as {current_user['name']}")
        menu = input(
            f"Select an option:\n[1]:Add Buy/Sell Logs\n[2]:See Trade Log\n[3]:Edit my account\n[4]:Log Out\n[Q]:Quit Program\n[{current_user['name']}]:"
        )
        if menu == "1":
            pass
        elif menu == "2":
            pass
        elif menu == "3":
            pass
        elif menu == "4":
            pass
        elif menu == "q" or menu == "Q":
            print("Saving and quitting the program...")
            save_success = save_user_database()
            if save_success:
                print("Save Successful")
                sys.exit(0)
            else:
                raise Exception("Error: Failed to save data")
                sys.exit(1)

        else:
            print("\ninvalid input, please try again...")
        return


if __name__ == "__main__":
    main()
