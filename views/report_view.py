from utils.html_exporter import HTMLExporter


class ReportView:
    """
    Gère l'affichage sur le terminal et l’export HTML
    des différents rapports (joueurs, tournois, rounds...).
    """

    @staticmethod
    def display_all_players(players):
        print("\n=== Liste des joueurs (ordre alphabétique) ===")
        if not players:
            print("[INFO] Aucun joueur à afficher.")
            return

        for player in players:
            print(f"{player.last_name}, {player.first_name} (ID: {player.chess_id}, Points: {player.points})")

    @staticmethod
    def display_all_tournaments(tournaments):
        print("\n=== Liste des tournois ===")
        if not tournaments:
            print("[INFO] Aucun tournoi à afficher.")
            return

        for t in tournaments:
            print(f"{t.name} ({t.start_date} - {t.end_date})")

    @staticmethod
    def display_tournament_details(tournament):
        print(f"\n=== Détails du tournoi : {tournament.name} ===")
        print(f"Lieu : {tournament.location}")
        print(f"Dates : {tournament.start_date} - {tournament.end_date}")
        print(f"Description : {tournament.description}")

    @staticmethod
    def display_tournament_players(players, tournament_name):
        print(f"\n=== Joueurs du tournoi {tournament_name} ===")
        if not players:
            print("[INFO] Aucun joueur dans ce tournoi.")
            return

        for player in players:
            print(f"{player.last_name}, {player.first_name} (ID: {player.chess_id}, Points: {player.points})")

    @staticmethod
    def display_tournament_rounds_and_matches(tournament):
        print(f"\n=== Rounds et matchs du tournoi : {tournament.name} ===")
        if not tournament.rounds:
            print("[INFO] Aucun round pour ce tournoi.")
            return

        for round_ in tournament.rounds:
            print(f"\n{round_.name} (Début : {round_.start_time}, Fin : {round_.end_time or 'En cours'})")
            for match in round_.matches:
                print(str(match))
