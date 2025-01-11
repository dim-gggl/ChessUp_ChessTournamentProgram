from controllers.main_controller import MainMenu
from controllers.player_manager import PlayerManager
from controllers.tournament_manager import TournamentManager

def main():
    controller = MainMenu()
    controller.run()
    # player_manager = PlayerManager()
    # player_manager.load_all()
    # manager = TournamentManager(player_manager)
    # manager.load_all()
    # print([tournament.is_holding for tournament in manager.all_tournaments])


if __name__ == "__main__":
    main()
