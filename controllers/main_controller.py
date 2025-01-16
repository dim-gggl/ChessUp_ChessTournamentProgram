from controllers.player_controller import PlayerController
from controllers.player_manager import PlayerManager
from views.main_menu_view import MainMenuView
from controllers.tournament_manager import TournamentManager
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from views.player_views import PlayerView
from views.tournament_views import TournamentView
from models.player import Player


class MainMenu:
    """Manages the application's main menu service."""
    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.tournament_controller = TournamentController(self.tournament_manager, self.player_manager.players)

    def run(self):
        """
        Runs the application's main menu.'
        """
        MainMenuView.display_main_menu_intro()
        selected = -1
        while int(selected) != 0:
            selected = MainMenuView().display_main_menu().strip()
            if selected == "1":
                self.tournament_controller.tournament_menu()
            elif selected == "2":
                PlayerController(self.player_manager).player_menu()
            elif selected == "3":
                ReportController(self.player_manager, self.tournament_manager).report_menu()
            elif selected == "q":
                self.player_manager.save_all()
                self.tournament_manager.save_all()
                MainMenuView.bye_message()
                return  0
            else:
                TournamentView.wrong_menu_input()
                selected = -1
