from models import Tournament


class TournamentController:
    def __init__(self, manager, view):
        self.manager = manager
        self.view = view

    def create_tournament(self):
        data = self.view.prompt_for_tournament_data()
        tournament = Tournament(**data)
        self.manager.save(tournament)
        self.view.success_message()

    def list_tournaments(self):
        tournaments = self.manager.load_all()
        self.view.show_tournament_list(tournaments)

    def show_tournament(self, name):
        tournament = self.manager.load_by_name(name)
        if tournament:
            self.view.show_tournament_details(tournament)
        else:
            self.view.failure_message()