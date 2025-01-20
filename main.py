from controllers.main_controller import MainMenu
from controllers.player_manager import PlayerManager
from controllers.tournament_manager import TournamentManager
from views.tournament_views import TournamentView


def main():
    controller = MainMenu()
    controller.run()
    # from datetime import datetime
    # from time import sleep
    # no_time = datetime.now()
    # today = no_time.strftime("\n\n\033[5m\033[1;48;5;0m\033[1;38;5;160m[%d/%m/%Y]\n")
    # now = no_time.strftime("%X")
    # print(today)
    # sleep(1)
    # print("\033[5m\033[1;38;5;255m.")
    # sleep(1)
    # print(".")
    # sleep(1)
    # print(".")
    # sleep(1)
    # print(f"\033[5m\033[1;38;5;255m{now}")
    # sleep(1)
    # print("\033[0m")
    # exit(0)

if __name__ == "__main__":
    main()
