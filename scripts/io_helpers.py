from app_control import QuitProgram


def yes_no_input(question):
    valid = False
    while not valid:
        response = input(
            "\n"
            + question
            + "\nPlease enter [Y] for yes, [N] for no, or [Q] to quit, and press'ENTER': "
        )
        if response == "y" or response == "Y":
            valid = True
            return "yes"
        if response == "n" or response == "N":
            valid = True
            return "no"
        if response == "q" or response == "Q":
            raise QuitProgram()
        else:
            print("\ninvalid input, please try again...")


def string_input(question):
    valid = False
    while not valid:
        response = input(
            "\n" + question + "\nPlease type your response and press 'ENTER': "
        )
        return response
