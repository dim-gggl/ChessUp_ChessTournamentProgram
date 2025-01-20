import re
from datetime import datetime
from utils.ansify import ansify


def is_valid_name(name, digits_ok=False):
    """
    Vérifie si le nom est valide.

    - Si digits_ok est False, le nom ne peut contenir que des lettres (y compris accentuées), espaces et tirets.
    - Si digits_ok est True, on autorise aussi les chiffres et autres symboles (mais le nom ne doit pas être vide).
    """
    if not name.strip():
        return False

    if digits_ok:
        return True

    else:
        pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s-]+$"
        return bool(re.match(pattern, name))

def confirm_name_format(name, digits_ok=False):
    """
    Confirms the format of a name.
    If the format of the name is invalid, the user is asked again to enter a valid name.
    """
    while not is_valid_name(name, digits_ok):
        if digits_ok:
            print(
                ansify(
                    "\n            red_err([ERREUR]) \n" "      Format de nom vide ou invalide.\n\n"
                )
            )
        else:
            print(
                ansify(
                    "\n            red_err([ERREUR]) \n" 
                    "      Saisie incorrecte (nom vide ou au format inhabituel).\n\n"
                )
            )
        input("Appuie sur ENTRÉE pour continuer...")
        name = input(ansify("\n\n      bld(Entrez un nom valide) : "))
    return name


def is_valid_location(location):
    """
    Checks whether the location is valid.
    Accepts :
    - letters (including accented letters),
    - spaces
    - hyphens
    - and a few common punctuation marks (comma, full stop, apostrophe).
    The field must not be empty.
    """
    if not location.strip():
        return False

    pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s,\-'.]+$"
    return bool(re.match(pattern, location))


def confirm_location_format(location):
    """
    Validates the location or asks the user to enter a new one.
    """
    while not is_valid_location(location):
        print(
            ansify(
                "\n            red_err([ERREUR]) \n"
                "Le lieu doit être composé de lettres, espaces, tirets, virgules, points ou apostrophes."
            )
        )
        input("Appuie sur ENTRÉE pour continuer...")
        location = input("Entre un lieu valide : ")
    return location


def is_valid_date(date_str):
    """
    Checks whether the date is in DD/MM/YYYY format.
    """
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def confirm_date_format(date_str):
    """
    Confirms the format of a date or prompts the user to re-enter it.
    """
    while not is_valid_date(date_str):
        print(
            ansify(
                "\n            red_err([ERREUR]) \n" 
                "      Date invalide. Format attendu : whte(JJ/MM/AAAA).\n\n"
            )
        )
        input("Appuie sur ENTRÉE pour continuer...")
        date_str = input(ansify("\n\n      bld(Entrez une date valide :) "))
    return date_str


def is_valid_chess_id(chess_id):
    """
    Returns True if the string is a valid Chess ID, False otherwise.
    """
    if chess_id == "":
        return True
    return bool(re.match(r"^[A-Z]{2}[0-9]{5}$", chess_id))


def confirm_chess_id(chess_id):
    """
    Validates the format of a Chess ID or asks for it to be re-entered.
    """
    while True:
        if chess_id == "":
            return chess_id

        if is_valid_chess_id(chess_id):
            return chess_id
        print(
            ansify(
                "\n            red_err([ERREUR]) \n"
                "      Format invalide. L'I.N.E. whte(doit) contenir pnk(2 lettres) et pnk(5 chiffres)."
            )
        )
        input("Appuie sur ENTRÉE pour continuer...")
        chess_id = input(ansify("      bld(Entrez un I.N.E. valide ou appuyez sur ENTRÉE pour passer :) "))
