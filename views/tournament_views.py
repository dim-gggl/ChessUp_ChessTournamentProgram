from models.player import Player


class TournamentView:
    """
    Gère tout l’affichage et la saisie d’infos spécifiques aux tournois
    (création, résumé, menu de gestion, ajout de joueurs, etc.).
    """

    @staticmethod
    def get_tournament_data():
        print("=== Créer un nouveau tournoi ===")
        name = input("Nom : ").strip()
        location = input("Lieu : ").strip()
        start_date = input("Date de début (YYYY-MM-DD) : ").strip()
        end_date = input("Date de fin (YYYY-MM-DD) : ").strip()
        description = input("Description : ").strip()

        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
        }

    @staticmethod
    def display_tournaments_list(tournaments):
        if not tournaments:
            print("\n[INFO] Aucun tournoi enregistré")
        else:
            print("\n=== Liste des Tournois ===")
            for i, t in enumerate(tournaments):
                print(f"{i + 1}. {t.name} ({t.start_date} - {t.end_date})")
            return input("Choisissez un tournoi par numéro : ")

    @staticmethod
    def display_tournament_summary(tournament):
        """
        Affiche un récap du tournoi : nom, dates, joueurs, rounds, etc.
        """
        print(f"\n=== Résumé du Tournoi : {tournament.name} ===")
        print(f"Lieu : {tournament.location}")
        print(f"Dates : {tournament.start_date} - {tournament.end_date}")
        print(f"Description : {tournament.description}")
        print(f"Nombre de rounds : {tournament.num_rounds}")
        print(f"Round actuel : {tournament.current_round}/{tournament.num_rounds}")

        print("\n--- Joueurs ---")
        for p in sorted(tournament.players, key=lambda pl: (pl.last_name, pl.first_name)):
            print(f"{p.last_name}, {p.first_name} (ID: {p.chess_id}, Points: {p.points})")

        print("\n--- Rounds ---")
        for rnd in tournament.rounds:
            print(f"\n{rnd.name} (Début : {rnd.start_time}, Fin : {rnd.end_time or 'En cours'})")
            for match in rnd.matches:
                print(str(match))

    @staticmethod
    def display_tournament_menu(tournament):
        """
        Affiche le menu d’options propre au tournoi en cours.
        """
        print(f"\n=== Gestion du Tournoi : {tournament.name} ===")
        print("1. Ajouter des joueurs")
        print("2. Démarrer le prochain round")
        print("3. Entrer les résultats des matchs")
        print("4. Voir le résumé du tournoi")
        print("q. Quitter la gestion du tournoi")

        return input("Choisissez une option : ")

    @staticmethod
    def get_player_to_add():
        """
        Demande les infos d’un joueur à ajouter au tournoi.
        Si c’est vide pour le first_name ou last_name, on considère que l’utilisateur veut annuler.
        """
        print("\n=== Ajouter un joueur au tournoi ===")
        first_name = input("Prénom : ").strip()
        last_name = input("Nom : ").strip()
        birth_date = input("Date de naissance (YYYY-MM-DD) : ").strip()
        chess_id = input("Identifiant national d'échecs : ").strip()

        if first_name and last_name and chess_id:
            return Player(first_name, last_name, birth_date, chess_id)
        else:
            print("[ERREUR] Saisie invalide ou annulée.")
            return None

    @staticmethod
    def show_rankings(rankings):
        for i in range(len(rankings)):
            print(rankings(i))

    @staticmethod
    def show_success_message(message):
        print("[SUCCÈS] : " + message)

    @staticmethod
    def show_error_message(message):
        print("[ERREUR] : " + message)
