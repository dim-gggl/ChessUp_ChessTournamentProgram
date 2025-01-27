from utils.validators import confirm_date_format, confirm_chess_id, confirm_name_format
from views.player_views import PlayerView
from models.player import Player
from views.tournament_views import TournamentView
from controllers.player_manager import PlayerManager


class PlayerController:
    """
    Manages the player menu and submenus service.
    """

    def __init__(self, manager: PlayerManager):
        self.view = PlayerView()
        self.manager = manager

    def player_menu(self):
        """Manages the players' main menu."""
        sorted_players = sorted(self.manager.players, key=lambda p: [p.last_name, p.first_name])
        selected = ""
        while selected != "r":

            menu_actions = {
                "1": self.add_new_player,
                "2": self.edit_selected_player,
                "3": lambda: self.view.display_players(sorted_players),
            }

            selected = self.view.display_players_menu().strip().lower()
            if selected == "r":
                break

            action = menu_actions.get(selected)

            if not self.manager.players and selected != "1":
                TournamentView.no_players_on_file_msg()
                selected = ""

            else:
                if action:
                    action()
                else:
                    TournamentView.wrong_menu_input()

    def add_new_player(self):
        """Adds a new player to the database."""
        player_names = self.view.get_new_player_names()
        first_name = confirm_name_format(player_names["first_name"].strip().capitalize(), digits_ok=False)
        last_name = confirm_name_format(player_names["last_name"].strip().capitalize(), digits_ok=False)
        birth_date_input = self.view.get_new_player_birth_date().strip()
        birth_date = confirm_date_format(birth_date_input)
        chess_input = self.view.get_player_chess_id().strip().upper()
        chess_id = confirm_chess_id(chess_input)
        new_player = Player(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            chess_id=chess_id,
        )
        self.manager.players.append(new_player)
        self.manager.save_all()
        self.view.new_player_saved_msg()
        return

    def edit_selected_player(self):
        """Selects a player to edit their details."""
        selected_idx = self.view.select_player_to_edit(self.manager.players)
        if selected_idx:
            selected_idx = selected_idx.strip().lower()
        else:
            return

        if selected_idx == "r":
            return

        try:
            idx = int(selected_idx) - 1
            player = self.manager.players[idx]
        except (ValueError, IndexError):
            TournamentView.wrong_menu_input()
            return

        self.edit_player_details(player)

    def edit_player_details(self, player):
        """Take care of the player's details editing process.'"""
        selected = ""
        while selected != "r":
            menu_actions = {
                "1": self.update_player_info,
                "2": lambda p: self.update_chess_id_only(p),
            }

            selected = self.view.edition_options(player).strip().lower()
            if selected == "r":
                break

            action = menu_actions.get(selected)

            if action:
                action(player)
                self.manager.save_all()

            else:
                TournamentView.wrong_menu_input()

    def update_player_info(self, player):
        """Manages the updating of a selected player's details"""
        updated_first_name = player.first_name
        updated_last_name = player.last_name
        updated_birth_date = player.birth_date
        updated_chess_id = player.chess_id

        new_names = self.view.get_new_player_names()

        if len(new_names) > 0:

            updated_first_name = new_names.get("first_name", player.first_name).strip().capitalize()
            updated_last_name = new_names.get("last_name", player.last_name).strip().capitalize()

        birth_date_input = self.view.get_new_player_birth_date().strip()
        if birth_date_input:
            updated_birth_date = confirm_date_format(birth_date_input)

        chess_input = self.view.get_player_chess_id().strip().upper()
        if chess_input:
            updated_chess_id = confirm_chess_id(chess_input)

        updated_data = dict(
            first_name=updated_first_name,
            last_name=updated_last_name,
            birth_date=updated_birth_date,
            chess_id=updated_chess_id,
        )
        self.view.data_updated_msg()
        updated_player = player.update_player_info(**updated_data)
        return updated_player

    def update_chess_id_only(self, player):
        """Just manages the National Chess ID update."""
        new_chess_input = self.view.enter_chess_id(player).strip().upper()
        new_chess_id = confirm_chess_id(new_chess_input)
        player.update_player_info(chess_id=new_chess_id)
