from utils.html_exporter import HTMLExporter


class ReportController:
    """
    Gère l'affichage et l'export des données statistiques
    """

    def __init__(self, player_controller, tournament_controller):
        self.player_controller = player_controller
        self.tournament_controller = tournament_controller
        self.exporter = HTMLExporter()

    def export_all_players(self):
        """
        Exporte au format HTML la liste alphabétique de tous les joueurs.
        """
        players = self.player_controller.load_players()
        sorted_players = sorted(players, key=lambda p: (p.last_name, p.first_name))
        content = "<ul class='all_players'>"
        for player in sorted_players:
            player_content = (
                f"\n<li><strong>{player.last_name}</strong> {player.first_name} ({player.birth_date}), "
                f" <strong>ID</strong> : {player.chess_id}</li>"
            )
            content += player_content
        content += "</ul>"
        self.exporter.export_to_html("all_players_list.html", "Liste de tous les Joueurs", content)

    def export_all_tournaments(self):
        """
        Exporte au format HTML la liste de tous les tournois.
        """
        tournaments = self.tournament_controller.tournaments
        html_content = "<ul class='all_tournaments'>"
        for tournament in tournaments:
            html_content += (
                f"\n<li><strong>{tournament.name}</strong>, "
                f"du {tournament.start_date} au {tournament.end_date}."
                f"Lieu :{tournament.location}</li>"
            )
        html_content += "</ul>"
        self.exporter.export_to_html("all_tournaments_list.html", "Liste de tous les tournois", html_content)

    def export_tournament_details(self, tournament):
        """
        Exporte au format HTML les détails du tournoi sélectionné par l'utilisateur.
        """
        filename = f"{tournament.name.replace(' ', '_')}_details_report.html"
        title = f"{tournament.name}"
        players = []
        if not tournament.rankings:
            players.extend(sorted(tournament.players, key=lambda p: (p.last_name, p.first_name)))
        else:
            for key, value in tournament.rankings:
                player = f"{int(key)} - {value[0]} - {value[1]} points"
                players.append(player)
        content = (
            f"<h4>Lieu :</h4><p> {tournament.location}</p>"
            f"<h4>Dates :</h4><p> {tournament.start_date} —— {tournament.end_date}</p>"
            f"<h4>Description :</h4><p>{tournament.description}</p>"
            f"<h4>Joueurs :</h4><ul>"
        )
        for player in players:
            content += f"<li>{player}</li>"
        content += "</ul>"
        self.exporter.export_to_html(filename, title, content)

    def export_tournament_rounds_and_matches(self, tournament):
        pass
