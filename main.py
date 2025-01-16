from controllers.main_controller import MainMenu
from controllers.player_manager import PlayerManager
from controllers.tournament_manager import TournamentManager
from views.tournament_views import TournamentView


def main():
    controller = MainMenu()
    controller.run()
    # manager = TournamentManager()
    # print(manager.tournaments)

if __name__ == "__main__":
    main()
