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


def select_currency(current_user):
    while True:
        option = input(
            f"[1]: GBP\n[2]: EUR\n[3]: USD\n[4]: AUD\n[5]: CAD\n[C]: Cancel Trade\n[{current_user['name']}]:"
        )
        if option == "1" or option.lower() == "gbp":
            return "GBP"
        if option == "2" or option.lower() == "eur":
            return "EUR"
        if option == "3" or option.lower() == "usd":
            return "USD"
        if option == "4" or option.lower() == "aud":
            return "AUD"
        if option == "5" or option.lower() == "cad":
            return "CAD"
        if option.lower() == "c":
            return None
        else:
            print("Invalid input")
