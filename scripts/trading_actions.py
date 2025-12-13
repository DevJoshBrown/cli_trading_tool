from datetime import datetime

from app_control import QuitProgram
from trade import Trade
from trades_database import add_trade_to_memory


def select_currency(current_user):
    while True:
        option = input(
            f"[1]: GBP\n[2]: EUR\n[3]: USD\n[4]: AUD\n[5]: CAD\n[C]: Cancel Trade\n[{current_user['name']}]:"
        )
        if option == "1" or option.lower() == "gbp":
            return "GBP"
        if option == "2" or option.lower() == "eur":
            return "EUR"
        if option == "3" or option.lower() == "usd":
            return "USD"
        if option == "4" or option.lower() == "aud":
            return "AUD"
        if option == "5" or option.lower() == "cad":
            return "CAD"
        if option.lower() == "c":
            return None
        else:
            print("Invalid input")


def get_market_prices(item):
    market_prices = {
        "GBP": 1.00,
        "EUR": 1.15,
        "USD": 0.80,
        "AUD": 0.50,
        "CAD": 0.60,
    }
    return market_prices[item]


def print_market_prices():
    market_prices = {
        "GBP": 1.00,
        "EUR": 1.15,
        "USD": 0.80,
        "AUD": 0.50,
        "CAD": 0.60,
    }
    print(
        "\nCurrent market prices compared to GBP:"
    )  # TO ADD: CUSTOM MAIN CURRENCY DATA TO USER
    for currency in market_prices:
        print(f"{currency} = {market_prices[currency]}")


def get_user_stocks(current_user, trades):
    stock = {
        "GBP": 0.00,
        "EUR": 0.00,
        "USD": 0.00,
        "AUD": 0.00,
        "CAD": 0.00,
    }
    if trades is not None:
        for trade in trades:
            if trade.owner_id == current_user["number"]:
                if trade.trade_type == "buy":
                    stock[trade.item_name] += trade.quantity
                if trade.trade_type == "sell":
                    stock[trade.item_name] -= trade.quantity
    return stock


def create_deposit(current_user, trades):
    print("\nWhat currency would you like to deposit?:")
    deposit_currency = select_currency(current_user)
    while True and deposit_currency is not None:
        amount = input(
            f"\nHow much {deposit_currency} do you want to deposit?\n[{current_user['name']}]:"
        )
        if amount.lower() == "c":
            break
        if amount.lower() == "q":
            raise QuitProgram

        try:
            amount_float = float(amount)
            if deposit_currency is not None:
                if amount_float <= 0:
                    print("\nERROR: Amount must be positive")
                    continue
            print(f"depositing {deposit_currency}:{amount_float} to your account.")
            now = datetime.now()
            date_now = now.strftime("%d:%m:%y")
            time_now = now.strftime("%H:%M")
            deposit = Trade(
                deposit_currency,
                "deposit",
                amount_float,
                0.00,
                date_now,
                time_now,
                current_user["number"],
            )
            result = add_trade_to_memory(deposit)
            if result:
                print("deposit success")
                break
            else:
                print("ERROR: deposit failed.")
                break

        except ValueError:
            print("\n\nPlease enter only numeric characters and try again.\n")


def create_trade_for_user(current_user, trades):
    user_stock = get_user_stocks(current_user, trades)

    # CHECK IF USER HAS NO CURRENCIES
    has_currency = False
    for i in user_stock:
        if user_stock[i] != 0.00:
            has_currency = True
            break

    # SUGGEST USER DEPOSITS IF NO CURRENCIES
    if not has_currency:
        print("You currently have no currencies in your account.")
        option = input(
            f"would you like to make a deposit? \n[1]: Yes\n[2]: No\n[3]: Previous menu\n[Q]: Quit the program\n\n[{current_user['name']}]:"
        )

        if option == "1":
            create_deposit(current_user, trades)

        if option == "2":
            print(
                "Cannot trade without currency in account, returning to previous menu."
            )
            return

        if option == "3":
            return

        if option == "Q" or option == "q":
            return "quit"

    while True:
        option = input(
            f"\n||: TRADE MENU :||\n\n[1]: View current available currencies to trade. \n[2]: View your current currency stocks \n[3]: Make a trade\n[4]: Previous menu\n[Q]: Quit the program\n\n[{current_user['name']}]:"
        )

        if option == "Q" or option == "q":
            return "quit"

        if option == "4":
            break

        if option == "1":
            print_market_prices()

        if option == "2":
            print(f"Your stock:\n{user_stock}\n")

        if option == "3":
            print(f"\nYour stock:\n{user_stock}\n")

            # init
            cancel = False
            buy_item = None
            sell_item = None
            rounded_rate = 0.00
            expected_rate = 0.00

            # BUY INPUT
            while True:
                print("Which currency would you like to buy?")
                answer = select_currency(current_user)
                if answer is None:
                    cancel = True
                    break
                else:
                    buy_item = answer
                    break

            # SELL INPUT
            while True and not cancel:
                print("Which currency would you like to sell?")
                answer = select_currency(current_user)
                if answer is None:
                    cancel = True
                    break
                else:
                    sell_item = answer
                    break

            # Calc exchange rate
            if cancel is False:
                price_sell = get_market_prices(sell_item)
                price_buy = get_market_prices(buy_item)
                expected_rate = price_sell / price_buy
                rounded_rate = f"{expected_rate:.2f}"
                print(
                    f"\n\nFor every 1 {sell_item}, you will get {rounded_rate} {buy_item}."
                )

            print(f"\nBuying {buy_item} with {sell_item} at {rounded_rate}")

            # How much does the user want to sell?

            while True and not cancel:
                print("\nPress[c] to go back, or [q] to save and quit")
                sell_amnt = input(f"\nHow much {sell_item} do you want to sell?")
                if sell_amnt.lower() == "c":
                    break
                if sell_amnt.lower() == "q":
                    raise QuitProgram

                try:
                    sell_amnt_float = float(sell_amnt)
                    if sell_item is not None:
                        if sell_amnt_float <= 0:
                            print("\nERROR: Amount must be positive")
                            continue
                        if sell_amnt_float > user_stock[sell_item]:
                            print("\nERROR: Insufficient balance")
                            continue

                    print(f"\nselling {round(sell_amnt_float, 2)} x {sell_item}.")
                    break
                except ValueError:
                    print("\n\nPlease enter only numeric characters and try again.\n")
