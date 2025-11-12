user_database = []


def add_user(name, email):
    user_number = len(user_database) + 1

    print(f"Adding user number: {user_number}")
    user = {}

    user["number"] = user_number
    user["name"] = name

    unique_user = True

    for existing_user in user_database:
        if existing_user["email"] == email:
            print(f"{email} is already in use, user:{user_number} not added.")
            unique_user = False
            break

    if unique_user:
        user["email"] = email
        user_database.append(user)


def remove_user(email):
    pass
