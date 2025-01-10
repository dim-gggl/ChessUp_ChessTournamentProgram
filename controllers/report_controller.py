from utils.html_exporter import HTMLExporter
from views.player_views import PlayerView
from views.report_view import ReportView
from views.tournament_views import TournamentView


class ReportController:
    """
    Gère l'affichage et l'export des données statistiques
    """

    def __init__(self, players_manager=None, tournaments_manager=None):
        self.players_manager = players_manager
        self.tournaments_manager = tournaments_manager
        self.exporter = HTMLExporter()
        self.view = ReportView()

    def report_menu(self):
        selected = -1
        while selected != 0:
            choice = int(self.view.display_report_menu())
            if choice == 1:
                sorted_players = sorted(self.players_manager.players, key=lambda p: (p.last_name, p.first_name))
                return PlayerView().display_players(sorted_players)

            elif 1 < int(choice) <= 3:
                tournament = TournamentView().select_tournament(self.tournaments_manager.tournaments)
                if tournament:
                    return self.get_user_precisions(tournament)
            elif choice == 4:
                pass
            else:
                selected = 0



    def get_user_precisions(self, tournament):
        selected = -1
        while selected != 0:
            selected = int(self.view.display_possible_options(tournament))
            if selected == 1:
                return self.view.show_name_and_dates(tournament)
            elif selected == 2:
                return TournamentView().show_tournament_players(tournament)
            elif selected == 3:
                return self.view.show_rounds_and_matches(tournament)
            elif selected == 4:
                return self.ask_data_to_export()
            else:
                selected = 0

    def ask_data_to_export(self):
        selected = -1
        while selected != 0:
            selected = self.view.display_export_options()
            if selected == 1:
                self.export_all_players()
            elif selected == 2:
                self.export_all_tournaments()
            elif selected == 3:
                tournament = TournamentView().select_tournament(self.tournaments_manager.tournaments)
                if tournament:
                    self.export_tournament_details(tournament)
            else:
                selected = 0


    def export_all_players(self):
        """
        Exporte au format HTML la liste alphabétique de tous les joueurs.
        """
        players = self.players_manager.players
        sorted_players = sorted(players, key=lambda p: (p.last_name, p.first_name))
        content = "<ul class='all_players'>"
        for player in sorted_players:
            player_content = (
                f"\n<li><strong>{player.last_name.upper()}</strong> {player.first_name} ({player.birth_date}), "
                f" <strong>ID</strong> : {player.chess_id}</li>"
            )
            content += player_content
        content += "</ul>"
        self.exporter.export_to_html("all_players_list.html", "Liste de tous les Joueurs", content)

    def export_all_tournaments(self):
        """
        Exporte au format HTML la liste de tous les tournois.
        """
        tournaments = self.tournaments_manager.tournaments
        html_content = "<ul class='all_tournaments'>"
        for tournament in tournaments:
            html_content += (
                f"\n<li><strong>{tournament.name}</strong>, "
                f"Ouverture : {tournament.start_date}. Fin: {tournament.end_date}."
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
        content = (
            f"<h4>Lieu :</h4><p> {tournament.location}</p>"
            f"<h4>Dates :</h4><p> {tournament.start_date} —— {tournament.end_date}</p>"
            f"<h4>Description :</h4><p>{tournament.description}</p>"
            f"<h4>Joueurs :</h4><ul>"
        )
        if tournament.rankings:
            players_str = tournament.rankings
            for player_str in players_str:
                content += f"<li>{player_str}</li>"
        else:
            html_players = sorted(tournament.players, key=lambda p: (p.last_name, p.first_name))
            for player in html_players:
                content += f"<li>{player.last_name} {player.first_name} ({player.birth_date}) ~~ ID: {player.chess_id}</li>"
        content += "</ul>"
        self.exporter.export_to_html(filename, title, content)

    def export_tournament_rounds_and_matches(self, tournament):
        pass
