import sys

from user_database import save_user_database


class QuitProgram(Exception):
    """Raised when the user chooses to exit the application."""

    pass


def quit_program():
    print("Saving and quitting the program...")
    save_success = save_user_database()
    if save_success:
        print("Save Successful")
        sys.exit(0)
    else:
        raise Exception("Error: Failed to save data")
