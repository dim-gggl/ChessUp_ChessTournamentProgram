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
                print(
                    f"- {match.player1.last_name} vs {match.player2.last_name} " f"({match.score1} - {match.score2})"
                )

    # ===== Méthodes d’export HTML =====
    @staticmethod
    def export_all_players(players):
        title = "Liste des joueurs (ordre alphabétique)"
        content = "<ul>"
        for player in players:
            content += (
                f"<li>{player.last_name}, {player.first_name} "
                f"(ID: {player.chess_id}, Points: {player.points})</li>"
            )
        content += "</ul>"
        HTMLExporter.export_to_html("all_players.html", title, content)

    @staticmethod
    def export_all_tournaments(tournaments):
        title = "Liste des tournois"
        content = "<ul>"
        for t in tournaments:
            content += f"<li>{t.name} ({t.start_date} - {t.end_date})</li>"
        content += "</ul>"
        HTMLExporter.export_to_html("all_tournaments.html", title, content)

    @staticmethod
    def export_tournament_details(tournament):
        title = f"Détails du tournoi : {tournament.name}"
        content = (
            f"<p><strong>Lieu :</strong> {tournament.location}</p>"
            f"<p><strong>Dates :</strong> {tournament.start_date} - {tournament.end_date}</p>"
            f"<p><strong>Description :</strong> {tournament.description}</p>"
        )
        filename = f"tournament_{tournament.name.replace(' ', '_')}.html"
        HTMLExporter.export_to_html(filename, title, content)

    @staticmethod
    def export_tournament_rounds_and_matches(tournament):
        title = f"Rounds et matchs du tournoi : {tournament.name}"
        content = ""
        if not tournament.rounds:
            content = "<p>[INFO] Aucun round pour ce tournoi.</p>"
        else:
            for round_ in tournament.rounds:
                content += f"<h2>{round_.name}</h2>"
                content += (
                    f"<p><strong>Début :</strong> {round_.start_time}, "
                    f"<strong>Fin :</strong> {round_.end_time or 'En cours'}</p>"
                )
                content += "<ul>"
                for match in round_.matches:
                    content += (
                        f"<li>{match.player1.last_name} vs {match.player2.last_name} "
                        f"({match.score1} - {match.score2})</li>"
                    )
                content += "</ul>"

        filename = f"tournament_{tournament.name.replace(' ', '_')}_rounds.html"
        HTMLExporter.export_to_html(filename, title, content)
