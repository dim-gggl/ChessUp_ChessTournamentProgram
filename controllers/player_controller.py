from views.player_views import PlayerView
from models.player import Player


class PlayerController():

    def __init__(self, manager=None):
        self.view = PlayerView()
        self.manager = manager

    def player_menu(self):
        selected = -1
        while int(selected) != 0:
            selected = self.view.display_players_menu()
            if int(selected) == 1:
                new_player_details = self.view.get_player_data()
                new_player = Player(**new_player_details)
                self.manager.players.append(new_player)
                self.manager.save_all()
            elif int(selected) == 2:
                players = self.manager.players
                player = self.view.select_player_to_edit(players)
                self.edit_player_details(player)
                self.manager.save_all()
            elif int(selected) == 3:
                sorted_players = sorted(self.manager.players, key=lambda p: (p.last_name, p.first_name))
                self.view.display_players(sorted_players)


            else:
                selected = 0

    def add_new_player(self):
        new_player_details = self.view.get_player_data()
        new_player = Player(**new_player_details)
        self.manager.players.append(new_player)
        self.manager.save_all()
        return self.player_menu()

    def edit_player_details(self, player):
        selected = -1
        while selected != 0:
            selected = int(self.view.modify_player(player))
            if selected == 1:
                new_infos = self.view.get_player_data(edit=True, player=player)
                player.update_player_info(**new_infos)
                self.manager.save_all()
                return self.player_menu()

            elif selected == 2:
                new_chess_id = self.view.enter_chess_id(player)
                player.chess_id = new_chess_id
                self.manager.save_all()
                return self.player_menu()

            else:
                return self.player_menu()
