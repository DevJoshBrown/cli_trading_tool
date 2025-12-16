import json
from pathlib import Path

from trade import Trade

trades = []


CURRENT_FILE = Path(__file__).resolve()
SCRIPTS_FOLDER = CURRENT_FILE.parent
PROJECT_ROOT = SCRIPTS_FOLDER.parent
TRADES_DATA_FILE = PROJECT_ROOT / "data" / "trades.json"


def load_trades_database():
    global trades
    try:
        with open(TRADES_DATA_FILE, "r") as file:
            data = json.load(
                file
            )  # DATA - THIS IS WHERE THE LIST OF DICTIONARIES READ FROM THE JSON IS STORED

            # BELOW ARE ALL GRACEFUL FAILURE DEFENCES
    # If there is no trades database, create an empty list
    except FileNotFoundError:
        trades = []
        print("No database found, created an empty list")
        return trades
    # If the trades database is empty or corrupt, create an empty list
    except json.JSONDecodeError:
        trades = []
        # print("file is corrupted or empty")
        return trades

    # CREATE AN EMPTY LIST TO STORE THE NEW TRADE OBJECTS (That havent been created yet)
    trades = []

    # for every dictionary in the list of dicts we just loaded...
    for trade_dict in data:
        # convert the dictionaries to trade objects one by one and append them to the list "trades[]"
        trade_obj = Trade.from_dict(trade_dict)
        trades.append(trade_obj)
    return trades


def save_trades_database():
    data = []
    for t in trades:
        one_trade_dict = t.to_dict()
        data.append(one_trade_dict)

    try:
        folder = TRADES_DATA_FILE.parent
        folder.mkdir(parents=True, exist_ok=True)

        tmp_path = TRADES_DATA_FILE.with_suffix(".json.tmp")
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")

        tmp_path.replace(TRADES_DATA_FILE)
        return True
    except (OSError, IOError) as e:
        print(f"Failed to save database: {e}")
        return False


def add_trade_to_memory(trade):
    trades.append(trade)
    if save_trades_database():
        return True
    else:
        raise Exception("Failed to add and save the trade to the database")
