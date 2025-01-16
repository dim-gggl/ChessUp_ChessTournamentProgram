import re
from datetime import datetime
from utils.ansify import ansify


def is_valid_date(date_str):
    """
    Checks whether the date is in DD/MM/YYYY format.
    """
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validate_date(date_str):
    """
    Confirms the format of a date or prompts the user to re-enter it.
    """
    while not is_valid_date(date_str):
        print(ansify("\n      red_err([ERREUR]) Date invalide. Format attendu : JJ/MM/AAAA."))
        date_str = input(ansify("      bld(Entrez une date valide :) "))
    return date_str

def is_valid_chess_id(chess_id):
    """
    Returns True if the string is a valid Chess ID, False otherwise.
    """
    if chess_id == "":
        return True
    return bool(re.match(r"^[A-Z]{2}[0-9]{5}$", chess_id))

def validate_chess_id(chess_id):
    """
    Validates the format of a Chess ID or asks for it to be re-entered.
    """
    while True:
        if chess_id == "":
            return chess_id

        if is_valid_chess_id(chess_id):
            return chess_id
        print("\n      red_err([ERREUR]) Format invalide. L'I.N.E. doit contenir 2 lettres et 5 chiffres.")
        chess_id = input(ansify("      bld(Entrez un I.N.E. valide ou appuyez sur ENTRÉE pour passer :) "))
