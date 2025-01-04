from views import MainMenuView
from models import TournamentManager

class MainMenu:
    def __init__(self):
        self.view = MainMenuView()
        self.tournament_manager = TournamentManager()
        self.tournament_manager.load_all()

    def run(self):
        selected = -1
        while int(selected) != 0:
            selected = self.view.display_main_menu()