# cli_trading_tool
A CLI tool for accepting buy/sell orders, storing orders to a ledger, and creating custom reports from the ledger.
Users can create accounts, deposit currencies, trade between currencies using exchange rates, and all data is persisted locally using JSON. Built to exercise state management, persistence, and user-driven workflows.

# Features
- User account creation, login, editing, and deletion
- Persistent storage using JSON
- Deposit and currency trading system
- Balance validation (cannot trade more than owned)
- Trade history reports with filtering
- Safe quit handling

# Technologies
- Python 3
- JSON for data persistence
- Standard library only (no external dependencies)

# How to Run
1. Clone the repository:
   - git clone https://github.com/your-username/your-repo-name.git
   - cd your-repo-name
   
2. Run the program
  - python3 scripts/main.py
  
# Project Structure
  scripts/
    main.py
    login_funcs.py
    trading_actions.py
    trades_database.py
    user_database.py
  data/
    (runtime JSON files, ignored by git)

# Limitations / Future improvements:
  - No password authentication or Hashing
  - Exchange rates and currecny prices are simulated and static
  - No real market data
  - More realistic front-end or API integration to greatly improve usablitly

# Why this project exists:
  - Python fundamentals
  - Program structure and modular design
  - Data persistence
  - User input handling
  - Debugging real-world logic issues
