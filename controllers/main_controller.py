from controllers.player_controller import PlayerController
from controllers.player_manager import PlayerManager
from views.main_menu_view import MainMenuView
from controllers.tournament_manager import TournamentManager
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from views.tournament_views import TournamentView


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
        selected = ""
        while selected != "q":
            selected = MainMenuView().display_main_menu().strip().lower()

            menu_actions = {
                "1": self.tournament_controller.tournament_menu,
                "2": PlayerController(self.player_manager).player_menu,
                "3": ReportController(self.player_manager, self.tournament_manager).report_menu,
                "4": self.save_all,
                "q": self.quit_app,
            }

            action = menu_actions.get(selected)

            if action:
                action()
            else:
                TournamentView.wrong_menu_input()

    def save_all(self):
        self.player_manager.save_all()
        self.tournament_manager.save_all()
        MainMenuView.data_saved_msg()

    def quit_app(self):
        """
        Manages the application's own output.
        """
        self.save_all()
        MainMenuView.bye_message()