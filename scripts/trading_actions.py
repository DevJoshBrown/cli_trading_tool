def get_market_prices():
    market_prices = {
        "GBP": 1.00,
        "EUR": 1.15,
        "USD": 0.80,
        "AUD": 0.50,
        "CAD": 0.60,
    }
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

    print("Select an option:...")
    option = input(
        "[1]: View current available currencies to trade. \n[2]: View your current currency stocks \n[3]: Make a trade\n"
    )
    if option == "1":
        get_market_prices()

    if option == "2":
        print(user_stock)

    if option == "3":
