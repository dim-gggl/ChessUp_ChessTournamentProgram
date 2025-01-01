from models.player import Player


class PlayerController:
    def __init__(self, manager, view):
        self.manager = manager
        self.view = view

    def create_player(self):
        data = self.view.prompt_for_player_data()
        try:
            player = Player(**data)
            self.manager.save(player)
            self.view.success_message("Joueur ajouté avec succès.")
        except ValueError as e:
            self.view.error_message(str(e))

    def list_players(self):
        players = self.manager.load_all()
        self.view.show_player_list(players)

    def show_player(self, national_id):
        player = self.manager.load_by_national_id(national_id)
        if player:
            self.view.show_player_details(player)
        else:
            self.view.error_message("Joueur introuvable.")
