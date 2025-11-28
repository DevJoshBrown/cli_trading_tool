import sys

from login_funcs import login_process
from trade import Trade
from trades_database import load_trades_database, save_trades_database
from trading_actions import create_trade_for_user
from user_database import load_user_database, save_user_database


def log_in():
    while True:
        result, account = login_process()
        if result and account is not None:
            print(f"\nhi {account['name']}, login successful!\n")
            return account
        else:
            continue


def quit_program():
    print("Saving and quitting the program...")
    save_success = save_user_database()
    if save_success:
        print("Save Successful")
        sys.exit(0)
    else:
        raise Exception("Error: Failed to save data")


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
        print("loading trades...")

        while current_user:
            # MAIN MENU
            print(f"\n\nlogged in as {current_user['name']}")
            menu = input(
                f"Select an option:\n[1]:Add buy/sell log\n[2]:See trade history\n[3]:Edit my account\n[4]:Log out\n[Q]:Quit program\n[{current_user['name']}]:"
            )
            if menu == "1":
                option = input(
                    f"\n\nSelect an option:\n[1]:create a trade\n[2]:Back to menu\n[Q]:Quit Program\n[{current_user['name']}]:"
                )
                if option == "1":
                    create_trade_for_user(current_user, load_trades_database())

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
                quit_program()

            else:
                print("\ninvalid input, please try again...")


if __name__ == "__main__":
    main()
