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
        """Reports main menu."""
        menu_options = {
            "1": self.show_all_players,
            "2": self.show_all_tournaments,
            "3": self.pick_one_tournament,
            "4": self.html_menu,
            "r": self.back_to_main_menu,
        }
        selected = self.view.display_report_menu().strip().lower()
        return menu_options[selected]()

    def show_all_players(self):
        """Displays the alphabetical list of all players."""
        players = self.players_manager.players
        sorted_players = sorted(players, key=lambda p: (p.last_name, p.first_name))
        PlayerView().display_players(sorted_players)
        return self.report_menu()

    def show_all_tournaments(self):
        """Displays the list of all tournaments."""
        tournaments = self.tournaments_manager.load_all()
        self.view.display_all_tournaments(tournaments)
        return self.report_menu()

    def pick_one_tournament(self):
        """Make the user select a tournament to view its details."""
        tournaments = self.tournaments_manager.tournaments
        tournament = TournamentView().select_tournament(tournaments)
        if tournament:
            return self.report_options_menu(tournament)
        return self.report_menu()

    def report_options_menu(self, tournament):
        """Displays the options for the selected tournament."""
        menu_options = {
            "1": self.view.show_name_and_dates,
            "2": TournamentView().show_tournament_players,
            "3": self.view.show_rounds_and_matches,
        }
        selected = self.view.display_possible_options(tournament).strip().lower()
        if selected == "r":
            return self.report_menu()
        return menu_options[selected](tournament)

    def html_menu(self):
        """Displays the options for exporting the data in HTML format."""
        menu_options = {
            "1": self.export_all_players,
            "2": self.export_all_tournaments,
            "3": self.pick_one_tournament,
            "r": self.report_menu,
        }
        selected = self.view.display_export_options().strip().lower()
        if selected == "3":
            tournament = TournamentView().select_tournament(self.tournaments_manager.tournaments)
            if tournament:
                self.export_tournament_details(tournament)
                self.view.export_success_msg()
                return self.report_menu()
        try:
            menu_options[selected]()
        except KeyError:
            return self.report_menu()

    def export_all_players(self):
        """
        Exports the alphabetical list of all players in HTML format.
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
        Exports the list of all tournaments in HTML format.
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
        Exports the details of the tournament selected by the user in HTML format.
        """
        filename = f"{tournament.name.lower().replace(' ', '_')}_details_report.html"
        title = f"{tournament.name}"
        content = (
            f"<h4>Lieu :</h4><p> {tournament.location}</p>"
            f"<h4>Dates :</h4><p> {tournament.start_date} —— {tournament.end_date}</p>"
            f"<h4>Description :</h4><p>{tournament.description}</p>"
        )
        if tournament.rankings:
            clear_rankings = self.clear_rankings(tournament.rankings)
            content += "<h4 class='rankings title'>Classement :</h4>"
            content += "<ul class='rankings list'>"
            players_str = clear_rankings
            for player_str in players_str:
                content += f"<li>{player_str}</li>"
        else:
            content += "<ul>"
            html_players = sorted(tournament.players, key=lambda p: (p.last_name, p.first_name))
            for player in html_players:
                content += (
                    f"<li>{player.last_name} {player.first_name} ({player.birth_date}) ~~ ID: {player.chess_id}</li>"
                )
        content += "</ul>"
        self.exporter.export_to_html(filename, title, content)

    @staticmethod
    def clear_rankings(rankings):
        """
        Cleans up the results of ansify arguments for export to HTML.
        """
        clear_rankings = []
        for ranking in rankings:
            if ranking.startswith("gldn("):
                clear_rankings.append(ranking.replace("gldn(", "").replace(")", ""))
            elif ranking.startswith("whte("):
                clear_rankings.append(ranking.replace("whte(", "").replace(")", ""))
            elif ranking.startswith("bld("):
                clear_rankings.append(ranking.replace("bld(", "").replace(")", ""))
        return clear_rankings

    @staticmethod
    def back_to_main_menu():
        return
