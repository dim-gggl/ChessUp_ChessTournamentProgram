from controllers import TournamentController
from managers import TournamentManager
from views import TournamentView


def main():

    my_controller = TournamentController(TournamentManager("data/tournaments.json"), TournamentView())
    my_controller.list_tournaments()
    my_controller.create_tournament()

if __name__ == "__main__":
    main()