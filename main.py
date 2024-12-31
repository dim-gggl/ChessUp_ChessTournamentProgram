from controllers.tournament_controller import TournamentController
from managers.tournament_manager import TournamentManager
from views.tournament_views import TournamentView


def main():

    my_controller = TournamentController(TournamentManager("data/tournaments.json"), TournamentView())
    my_controller.list_tournaments()
    my_controller.create_tournament()

if __name__ == "__main__":
    main()