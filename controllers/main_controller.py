from controllers.player_controller import PlayerController
from controllers.player_manager import PlayerManager
from views.main_menu_view import MainMenuView
from controllers.tournament_manager import TournamentManager
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from views.tournament_views import TournamentView


class MainMenu:
    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager(self.player_manager)
        self.tournament_manager.load_all()
        self.player_manager.load_all()

    def run(self):

        MainMenuView.display_main_menu_intro()
        selected = -1
        while int(selected) != 0:
            selected = MainMenuView().display_main_menu().strip()
            if selected == "1":
                return TournamentController(self.tournament_manager,
                                     self.player_manager).tournament_menu_selection()
            elif selected == "2":
                return PlayerController(self.player_manager).player_menu()
            elif selected == "3":
                return ReportController(self.player_manager, self.tournament_manager).report_menu()
            elif selected == "0" or selected == "q" or selected == "r":
                self.player_manager.save_all()
                self.tournament_manager.save_all()
                MainMenuView.bye_message()
                return selected == 0
            else:
                TournamentView.wrong_menu_input()
                selected = -1
