from app_control import QuitProgram, quit_program
from login_funcs import edit_account, log_in
from trade_history import create_trade_report
from trades_database import load_trades_database
from trading_actions import create_trade_for_user
from user_database import load_user_database, save_user_database


def main():
    # LOAD DATABASE
    print("WELCOME TO THE CLI TRADING TOOL.")
    print("loading users...")
    load_user_database()
    print("loading complete.")

    try:
        while True:
            # LOG IN PROCESS
            current_user = None
            current_user = log_in()
            load_trades_database()
            print(f"current user = {current_user}")

            while current_user:
                # MAIN MENU
                print(f"\n\nlogged in as {current_user['name']}")

                menu = input(
                    f"\n\nSelect an option:\n[1]:Add buy/sell log\n[2]:See trade history\n[3]:Edit my account\n[4]:Log out\n[Q]:Quit program\n[{current_user['name']}]:"
                )
                if menu == "1":
                    result = create_trade_for_user(current_user)
                    if result == "quit":
                        raise QuitProgram

                elif menu == "2":
                    create_trade_report(current_user)

                elif menu == "3":
                    result = edit_account(current_user)
                    if result == "deleted":
                        current_user = None

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
                    raise QuitProgram

                else:
                    print("\ninvalid input, please try again...")

    except QuitProgram:
        quit_program()


if __name__ == "__main__":
    main()
