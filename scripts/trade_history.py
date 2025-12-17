import trades_database
from app_control import QuitProgram
from io_helpers import select_currency


def create_trade_report(
    current_user,
):
    user_trades = []
    for trade in trades_database.trades:
        if trade.owner_id == current_user["number"]:
            user_trades.append(trade)

    while True:
        print("Please select from the following options:")
        report_type = input(
            f"\n[1] Show all trades\n[2] Filter by currency\n[C] Cancel\n[Q] Save & quit\n[{current_user['name']}]:"
        )

        if report_type == "1":
            for trade in user_trades:
                print(
                    f"Date/Time:{trade.date} - {trade.time} | TYPE:{trade.trade_type} | ITEM:{trade.item_name} | AMNT:{trade.quantity} | PPU:{trade.price_per_unit}"
                )
            print("END OF REPORT\n\n")

        if report_type == "2":
            print("which currency would you like to filter by?\n")
            currency = select_currency(current_user)
            for trade in user_trades:
                if trade.item_name == currency:
                    print(
                        f"Date/Time:{trade.date} - {trade.time} | TYPE:{trade.trade_type} | ITEM:{trade.item_name} | AMNT:{trade.quantity} | PPU:{trade.price_per_unit}"
                    )
            print("END OF REPORT\n\n")
        if report_type.lower() == "c":
            break
        if report_type.lower() == "q":
            raise QuitProgram
