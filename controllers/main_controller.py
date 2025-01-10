from controllers.player_controller import PlayerController
from controllers.player_manager import PlayerManager
from views.main_menu_view import MainMenuView
from controllers.tournament_manager import TournamentManager
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController


class MainMenu:
    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager(self.player_manager)
        self.tournament_manager.load_all()
        self.player_manager.load_all()

    def run(self):
        selected = -1
        MainMenuView.display_main_menu_intro()
        while int(selected) != 0:
            selected = MainMenuView().display_main_menu()
            if int(selected) == 1:
                TournamentController(self.tournament_manager,
                                     self.player_manager).tournament_menu_selection()
            elif int(selected) == 2:
                PlayerController(self.player_manager).player_menu()
            elif int(selected) == 3:
                ReportController(self.player_manager, self.tournament_manager).report_menu()
            elif int(selected) == 0:
                self.player_manager.save_all()
                self.tournament_manager.save_all()
                break
            else:
                self.player_manager.save_all()
                self.tournament_manager.save_all()
                MainMenuView().bye_message()
                break