import sys

from user_database import add_user, remove_user, user_database


def main():
    print("testing user adding...")
    add_user("josh", "devjoshbrown@gmail.com")
    print(user_database)
    add_user("paul", "mrplumpy@aol.org")
    print(user_database)
    add_user("jim", "jimdoesgood@mail.net")
    print(user_database)
    add_user("bob", "jimdoesgood@mail.net")
    print(user_database)
    remove_user("devjoshbrown@gmail.com")
    print(user_database)
    remove_user("jimdoesgood@mail.net")
    print(user_database)
    add_user("bob", "jimdoesgood@mail.net")
    print(user_database)


if __name__ == "__main__":
    main()
