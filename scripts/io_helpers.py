import sys


def yes_no_input(question):
    valid = False
    while not valid:
        response = input(
            "\n" + question + "\nPlease Enter [Y] for yes, [N] for no, or [Q] to quit: "
        )
        if response == "y" or response == "Y":
            valid = True
            return "yes"
        if response == "n" or response == "N":
            valid = True
            return "no"
        if response == "q" or response == "Q":
            valid = True
            print("\nClosing the application\n")
            sys.exit(0)
        else:
            print("\ninvalid input, please try again...")


def string_input(question):
    valid = False
    while not valid:
        response = input(
            "\n" + question + "\nPlease type your response and press Enter: "
        )
        return response


def multiple_choice_input(question, possible_answers):
    valid = False
    while not valid:
        response = input(
            "\n"
            + question
            + f"\nPlease enter one of {possible_answers}, or [Q] to exit:"
        )
        if response == "q" or response == "Q":
            valid = True
            print("\nClosing the application\n")
            sys.exit(0)
        if response == possible_answers[0]:
            pass
        if response not in possible_answers:
            valid = False
            print("\ninvalid input, please try again...")
