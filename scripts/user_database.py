user_database = []
count = 0


def add_user(name, email):
    global count  # access the count out of scope.

    for u in user_database:
        if u["email"] == email:
            print(f"{email} already in use, user not added.")
            return None
    count += 1
    user = {"number": count, "name": name, "email": email}
    user_database.append(user)
    return count


def remove_user(email):
    for number, u in enumerate(user_database):
        if u["email"] == email:
            del user_database[number]
            return True
    print(f"User not found with email {email}")
    print("No users removed")
    return False


def search_user(search_term):
    results = []
    for user in user_database:
        if search_term in user["name"]:
            results.append(user)
            return results
    else:
        return False


def search_email(search_term):
    results = []
    for user in user_database:
        if search_term in user["email"]:
            results.append(user)
            return results
    else:
        return False
