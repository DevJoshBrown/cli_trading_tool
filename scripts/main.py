import sys

from login_funcs import login_process
from user_database import load_user_database, save_user_database


def log_in():
    while True:
        result, account = login_process()
        if result and account is not None:
            print(f"\nhi {account['name']}, login successful!\n")
            return account
        else:
            continue


def main():
    # LOAD DATABASE
    print("WELCOME TO THE CLI TRADING TOOL.")
    print("loading users...")
    load_user_database()
    print("loading complete.")

    while True:
        # LOG IN PROCESS
        current_user = None
        current_user = log_in()
        print(f"current user = {current_user}")

        while current_user:
            # MAIN MENU
            print(f"\n\nlogged in as {current_user['name']}")
            menu = input(
                f"Select an option:\n[1]:Add Buy/Sell Log\n[2]:See Trade History\n[3]:Edit my account\n[4]:Log Out\n[Q]:Quit Program\n[{current_user['name']}]:"
            )
            if menu == "1":
                # ADD BUY / SELL LOG
                pass

            elif menu == "2":
                # SEE TRADE HISTORY
                pass

            elif menu == "3":
                # EDIT MY ACCOUNT
                pass

            elif menu == "4":
                # LOG OUT
                print("Saving and logging out...")
                save_success = save_user_database()
                if save_success:
                    print("Save Successful")
                    break
                else:
                    raise Exception("Error: Failed to save data")

            elif menu == "q" or menu == "Q":
                # QUIT PROGRAM
                print("Saving and quitting the program...")
                save_success = save_user_database()
                if save_success:
                    print("Save Successful")
                    sys.exit(0)
                else:
                    raise Exception("Error: Failed to save data")

            else:
                print("\ninvalid input, please try again...")


if __name__ == "__main__":
    main()
