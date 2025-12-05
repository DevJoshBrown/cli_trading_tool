from workspace.cli_trading_tool.scripts.app_control import QuitProgram


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
        "\ncurrent market prices compared to GBP:"
    )  # TO ADD: CUSTOM MAIN CURRENCY DATA TO USER
    for currency in market_prices:
        print(f"{currency} = {market_prices[currency]}")


def get_user_stocks(current_user, trades):
    stock = {
        "GBP": 0,
        "EUR": 0,
        "USD": 0,
        "AUD": 0,
        "CAD": 0,
    }
    if trades is not None:
        for trade in trades:
            if trade.owner_id == current_user["number"]:
                if trade.trade_type == "buy":
                    stock[trade.item_name] += trade.quantity
                if trade.trade_type == "sell":
                    stock[trade.item_name] -= trade.quantity
        return stock
    else:
        return stock


def create_trade_for_user(current_user, trades):
    user_stock = get_user_stocks(current_user, trades)

    while True:
        print("Select an option:...")
        option = input(
            f"\n\n||: TRADE MENU :||\n\n[1]: View current available currencies to trade. \n[2]: View your current currency stocks \n[3]: Make a trade\n[4]: Previous menu\n[Q]: Quit the program\n\n[{current_user['name']}]:"
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
            # BUY INPUT
            cancel = False
            buy_item = None
            sell_item = None
            rounded_rate = 0.00
            expected_rate = 0.00

            while True:
                buy = input(
                    f"\n Which currency would you like to buy?\n[1]: GBP\n[2]: EUR\n[3]: USD\n[4]: AUD\n[5]: CAD\n[C]: Cancel Trade\n\n[{current_user['name']}]:"
                )
                if buy == "1":
                    buy_item = "GBP"
                    break
                elif buy == "2":
                    buy_item = "EUR"
                    break
                elif buy == "3":
                    buy_item = "USD"
                    break
                elif buy == "4":
                    buy_item = "AUD"
                    break
                elif buy == "5":
                    buy_item = "CAD"
                    break
                elif buy == "C" or buy == "c":
                    cancel = True
                else:
                    print("invalid input")
                if cancel:
                    break

            # SELL INPUT
            while True and not cancel:
                sell = input(
                    f"\n Which currency would you like to sell?\n[1]: GBP\n[2]: EUR\n[3]: USD\n[4]: AUD\n[5]: CAD\n[C]: Cancel Trade\n\n[{current_user['name']}]:"
                )
                if sell == "1":
                    sell_item = "GBP"
                    break
                elif sell == "2":
                    sell_item = "EUR"
                    break
                elif sell == "3":
                    sell_item = "USD"
                    break
                elif sell == "4":
                    sell_item = "AUD"
                    break
                elif sell == "5":
                    sell_item = "CAD"
                    break
                elif sell == "C" or sell == "c":
                    cancel = True
                else:
                    print("invalid input")
                if cancel:
                    break

            # Calc exchange rate
            if buy_item is not None and sell_item is not None:
                price_sell = get_market_prices(sell_item)
                price_buy = get_market_prices(buy_item)
                expected_rate = price_sell / price_buy
                rounded_rate = f"{expected_rate:.2f}"
                print(
                    f"\n\nfor every 1 {sell_item}, you will get {rounded_rate} {buy_item}."
                )

            print(f"\nbuying {buy_item} with {sell_item} at {rounded_rate}")

            # How much does the user want to sell?

            while True:
                print("\nPress[c] to go back, or [q] to save and quit")
                sell_amnt = input(f"how much {sell_item} do you want to sell?")
                if sell_amnt.lower() == "c":
                    break
                if sell_amnt.lower() == "q":
                    raise QuitProgram

                try:
                    sell_amnt_float = float(sell_amnt)
                    if sell_amnt_float <= 0:
                        print("amount must be positive")
                        continue

                    print(f"\nselling {round(sell_amnt_float, 2)} x {sell_item}.")
                    break
                except ValueError:
                    print("\n\nPlease enter only numeric characters and try again.\n")
