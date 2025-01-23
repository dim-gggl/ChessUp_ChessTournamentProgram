from models.tournament import Tournament
from utils.html_exporter import HTMLExporter
from utils.sort_tournaments import sort_tournaments
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

        selected = ""
        while selected != "r":

            menu_options = {
                "1": self.show_all_players,
                "2": self.show_all_tournaments,
                "3": self.pick_one_tournament,
                "4": self.html_menu,
            }

            selected = self.view.display_report_menu().strip().lower()

            action = menu_options.get(selected)
            if selected == "r":
                return

            if action:
                action()

            else:
                TournamentView.wrong_menu_input()

    def show_all_players(self):
        """Displays the alphabetical list of all players."""
        players = self.players_manager.players
        sorted_players = sorted(players, key=lambda p: (p.last_name, p.first_name))
        PlayerView.display_players(sorted_players)
        return

    def show_all_tournaments(self):
        """
        Displays the list of all tournaments sorted by status:
        0: open for registration (current_round == 0)
        1: is_holding
        2: is_running
        3: is_finished
        """
        all_tournaments = self.tournaments_manager.tournaments
        sort_tournaments(all_tournaments)
        self.view.display_all_tournaments(all_tournaments)
        return

    def pick_one_tournament(self, export_option=False):
        """Make the user select a tournament to view its details."""
        tournaments = self.tournaments_manager.tournaments

        selected_idx = TournamentView.display_tournament_list(tournaments, select_option=True).strip().lower()
        if selected_idx == "r":
            return

        try:
            i = int(selected_idx) - 1
            if 0 <= i < len(tournaments):
                if export_option:
                    return tournaments[i]
                else:
                    return self.report_options_menu(tournaments[i])

            else:
                TournamentView.invalid_selection()
        except ValueError or IndexError:
            TournamentView.wrong_number()
        return

    def report_options_menu(self, tournament):
        """Displays the options for the selected tournament."""

        selected = ""
        while selected != "r":

            menu_options = {
                "1": lambda: self.view.show_name_and_dates(tournament),
                "2": lambda: TournamentView().show_tournament_players(tournament),
                "3": lambda: self.view.show_rounds_and_matches(tournament),
            }

            selected = self.view.display_possible_options(tournament).strip().lower()
            if selected == "r":
                return

            action = menu_options.get(selected)
            if action:
                action()

            else:
                TournamentView().wrong_menu_input()
            return menu_options[selected]

    def html_menu(self):
        """Displays the options for exporting the data in HTML format."""

        all_tournaments = self.tournaments_manager.tournaments
        sort_tournaments(all_tournaments)
        selected = ""

        while selected != "r":

            menu_options = {
                "1": self.export_all_players,
                "2": lambda: self.export_all_tournaments(all_tournaments),
                "3": lambda: self.export_tournament_details(self.pick_one_tournament(export_option=True)),
            }

            selected = self.view.display_export_options().strip().lower()

            if selected == "r":
                return

            action = menu_options.get(selected)
            if action:
                action()

            else:
                TournamentView.wrong_menu_input()

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
        content = "\n<div class='all_players'>\n<ul class='all_players'>\n"
        for player in sorted_players:
            player_content = (
                f"\n<li><strong>{player.last_name.upper()}</strong> {player.first_name} ({player.birth_date}), "
                f" <strong>ID</strong> : {player.chess_id}</li>"
            )
            content += player_content
        content += "\n</ul>\n</div>\n"
        self.exporter.export_to_html("all_players_list.html", "Liste de tous les Joueurs", content)

    def export_all_tournaments(self, tournaments):
        """
        Exports the list of all tournaments in HTML format.
        """
        html_content = "\n<div>\n<ul class='all_tournaments'>\n"
        for tournament in tournaments:
            html_content += (
                f"\n<li><strong>{tournament.name}</strong>, "
                f"Ouverture : {tournament.start_date}. Fin: {tournament.end_date}."
                f"Lieu :{tournament.location}, {tournament.num_rounds} "
                f"rounds au total, {len(tournament.players)} participants\n"
                f"État : {str(tournament)}</li>\n"
            )
        html_content += "\n</ul>\n</div>\n"
        self.exporter.export_to_html("all_tournaments_list.html", "Liste de tous les tournois", html_content)

    def export_tournament_details(self, tournament):
        """
        Exports the details of the tournament selected by the user in HTML format.
        """
        if not isinstance(tournament, Tournament) or not tournament:
            TournamentView.wrong_menu_input()
            return

        filename = f"{tournament.name.lower().replace(' ', '_')}_details_report.html"
        title = f"{tournament.name}"
        content = (
            f"<div class='left-col'>\n"
            f"<h2 class='section-title blue'>Lieu :</h2>\n<p>\n "
            f"{tournament.location}\n</p>\n"
            f"<h2 class='section-title blue'>Dates :</h2>\n<p>\n {tournament.start_date} "
            f"—— {tournament.end_date}\n</p>\n"
            f"<h2 class='section-title blue'>Description :</h2>\n<p>\n{tournament.description}\n</p>\n"
            f"</div>"
        )
        if tournament.rankings:
            content += (
                "<div class='separator'></div>\n"
                "<div class='right-col'>\n<h2 class='section-title yellow'>\nCLASSEMENT\n</h2>"
            )
            clear_rankings = self.clear_rankings(tournament.rankings)
            content += "<ul class='ranking-list'>"
            players_str = clear_rankings
            for player_str in enumerate(players_str):
                if player_str == players_str[0]:
                    content += f"\n<li class='highlight'>{player_str}</li>"
                else:
                    content += f"\n<li>{player_str}</li>"
        else:
            content += (
                "\n<div class='players'>\n<h2 class='section-title>Joueurs inscrits</h2>\n<ul>"
            )
            html_players = sorted(tournament.players, key=lambda p: (p.last_name, p.first_name))
            for player in html_players:
                content += (
                    f"\n<li>{player.last_name} {player.first_name} ({player.birth_date}) ~~ ID: {player.chess_id}</li>"
                )
        content += "\n</ul>\n</div>"
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
