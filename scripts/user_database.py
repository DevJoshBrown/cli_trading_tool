import json
from pathlib import Path

user_database = []
count = 0

# Path logic:
CURRENT_FILE = Path(__file__).resolve()
SCRIPTS_FOLDER = CURRENT_FILE.parent
PROJECT_ROOT = SCRIPTS_FOLDER.parent
USER_DATA_FILE = PROJECT_ROOT / "data" / "users.json"


def load_user_database():
    global user_database, count
    try:
        with open(USER_DATA_FILE, "r") as file:
            user_database = json.load(file)
            count = 0
            for user in user_database:
                if user["number"] > count:
                    count = user["number"]
    except FileNotFoundError:
        user_database = []
        print("No database found, starting an empty list")
    except json.JSONDecodeError:
        user_database = []
        print("file is corrupted or empty")


def save_user_database():
    try:
        # ensure the directory exists
        folder = USER_DATA_FILE.parent
        folder.mkdir(parents=True, exist_ok=True)

        # write to a temp file first
        tmp_path = USER_DATA_FILE.with_suffix(".json.tmp")
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(user_database, f, indent=2, ensure_ascii=False)
            f.write("\n")

        tmp_path.replace(USER_DATA_FILE)
        return True
    except (OSError, IOError) as e:
        print(f"Failed to save database: {e}")
        return False


def add_user(name, email):
    global count  # access the count out of scope.
    norm_email = email.strip().lower()

    for u in user_database:
        if u["email"] == norm_email:
            print(f"{email} already in use, user not added.")
            return False
    count += 1
    user = {"number": count, "name": name, "email": norm_email}
    user_database.append(user)
    save_user_database()
    return True


def remove_user(email):
    norm_email = email.strip().lower()
    for number, u in enumerate(user_database):
        if u["email"] == norm_email:
            del user_database[number]
            save_user_database()
            return True
    print(f"User not found with email {norm_email}")
    print("No users removed")
    return False


def search_user(search_term):
    norm_search_term = search_term.lower().strip()
    results = []
    for user in user_database:
        if norm_search_term.lower() in user["name"].lower().strip():
            results.append(user)
    return results


def search_email(search_term):
    norm_search_term = search_term.lower().strip()
    results = []
    for user in user_database:
        if norm_search_term in user["email"].lower().strip():
            results.append(user)
    return results
