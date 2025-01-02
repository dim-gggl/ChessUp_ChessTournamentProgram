import re
from datetime import datetime
from models.player import Player


class PlayerView:
    """
    Gère l'affichage/interaction spécifique aux joueurs
    (saisie de données, affichage de la liste de joueurs, etc.).
    """

    def get_player_data(self):
        print("=== Ajouter un nouveau joueur ===")
        first_name = input("Prénom : ").strip()
        last_name = input("Nom de famille : ").strip()
        birth_date = self.get_valid_birth_date()
        chess_id = self.get_valid_chess_id()
        return {
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date,
            "chess_id": chess_id
        }

    @staticmethod
    def get_valid_birth_date():
        """Demande à l'utilisateur une date de naissance valide au format YYYY-MM-DD."""
        while True:
            birth_date = input("Date de naissance (YYYY-MM-DD) : ").strip()
            try:
                datetime.strptime(birth_date, "%Y-%m-%d")
                return birth_date
            except ValueError:
                print("[ERREUR] Format de date invalide. Veuillez entrer une date au format YYYY-MM-DD.")

    @staticmethod
    def get_valid_chess_id():
        """Demande à l'utilisateur un ID d'échecs (2 lettres + 5 chiffres)."""
        while True:
            chess_id = input("Identifiant national d'échecs (2 lettres + 5 chiffres) : ").strip()
            if re.match(r"^[A-Z]{2}\d{5}$", chess_id, re.IGNORECASE):
                return chess_id.upper()
            else:
                print("[ERREUR] L'identifiant doit comporter 2 lettres suivies de 5 chiffres (exemple : AB12345).")

    @staticmethod
    def display_players(players):
        """Affiche la liste des joueurs, classés par ordre alphabétique."""
        print("\n=== Liste des Joueurs ===")
        if not players:
            print("[INFO] Aucun joueur enregistré.")
            return

        for player in sorted(players, key=lambda p: (p.last_name, p.first_name)):
            print(f"{player.last_name}, {player.first_name} "
                  f"(ID: {player.chess_id}, Points: {player.points})")

    @staticmethod
    def show_success_message(message):
        print("[SUCCÈS] : " + message)

    @staticmethod
    def show_error_message(message):
        print("[ERREUR] : " + message)
