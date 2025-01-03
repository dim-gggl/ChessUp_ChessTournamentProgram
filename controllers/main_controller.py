from views.main_menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from controllers.tournament_manager import TournamentManager
from views.tournament_views import TournamentView
from models.tournament import Tournament


class MainController:
    """
    Point d'entrée principal du programme, gère la navigation via le menu.
    """

    def __init__(self):
        self.menu = MenuView()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController(self.player_controller)
        self.tournament_view = TournamentView()
        self.report_controller = ReportController(
            self.player_controller,
            self.tournament_controller,
        )
        self.tournament = None
        self.manager = None

    def run(self):
        """Boucle principale du programme, affiche le menu et réagit aux choix de l'utilisateur."""
        while True:
            choice = self.menu.display_main_menu()

            if choice == "1":
                self.player_controller.add_player()
            elif choice == "2":
                self.player_controller.view_all_players()
            elif choice == "3":
                self.tournament_controller.create_tournament()
            elif choice == "4":
                self.tournament = self.select_tournament()
                if self.tournament:
                    self.manage_tournament(self.tournament)
            elif choice == "5":
                self.report_controller.show_all_players()
                self.report_controller.export_all_players()
            elif choice == "6":
                self.report_controller.show_all_tournaments()
            elif choice == "7":
                tournament = self.select_tournament()
                if isinstance(tournament, Tournament):
                    self.report_controller.show_tournament_details(tournament)
                    self.report_controller.export_tournament_details(tournament)
                else:
                    self.tournament_view.show_error_message("Choix invalide.")
            elif choice == "8":
                tournament = self.select_tournament()
                if tournament:
                    self.report_controller.show_tournament_players(tournament)
            elif choice == "9":
                tournament = self.select_tournament()
                if tournament:
                    self.report_controller.show_tournament_rounds_and_matches(tournament)
            elif choice == "q":
                print("Merci d'avoir utilisé le programme !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    def manage_tournament(self, tournament):
        """Permet la gestion d'un tournoi.'"""
        self.manager = TournamentManager(
            tournament, self.player_controller, self.tournament_view, self.tournament_controller
        )
        self.manager.manage()

    def select_tournament(self):
        """Permet de sélectionner un tournoi parmi la liste de tournois existants."""
        tournaments = self.tournament_controller.tournaments
        try:
            choice = int(self.tournament_view.display_tournaments_list(tournaments)) - 1
            if 0 <= choice < len(tournaments):
                return tournaments[choice]
            else:
                self.tournament_view.show_error_message("Choix invalide.")
                return None
        except ValueError:
            self.tournament_view.show_error_message("Numéro invalide.")
            return None


