from utils.ansify import ansify
from utils.validators import confirm_date_format, confirm_chess_id
from views.player_views import PlayerView
from models.player import Player


class PlayerController:
    """
    Manages the player menu and submenus service.
    """

    def __init__(self, manager=None):
        self.view = PlayerView()
        self.manager = manager

    def player_menu(self):
        """Manages the players' main menu."""
        menu_options = {
            "1": self.add_new_player,
            "2": self.edit_selected_player,
            "3": self.view.display_players,
            "r": self.back_to_main_menu,
        }
        selected = self.view.display_players_menu().strip().lower()
        if selected == "3":
            menu_options[selected](self.manager.players)
            return self.player_menu()
        else:
            return menu_options[selected]()

    def add_new_player(self):
        """Adds a new player to the database."""
        player_names = self.view.get_new_player_names()
        first_name = player_names["first_name"].strip().capitalize()
        last_name = player_names["last_name"].strip().capitalize()
        birth_date = ""
        valid_date = False
        while not valid_date:
            birth_date_input = self.view.get_new_player_birth_date().strip()
            valid_date = confirm_date_format(birth_date_input)
            if valid_date:
                birth_date = birth_date_input
            else:
                self.view.date_format_error_msg()

        chess_id = ""
        valid_chess_id = False
        while not valid_chess_id:
            chess_input = self.view.get_player_chess_id().strip().upper() or ""
            valid_chess_id = confirm_chess_id(chess_input)
            if valid_chess_id:
                chess_id = chess_input
            else:
                self.view.invalid_chess_id_msg()

        new_player = Player(first_name=first_name, last_name=last_name, birth_date=birth_date, chess_id=chess_id)
        self.manager.players.append(new_player)
        self.manager.save_all()
        self.view.new_player_saved_msg()
        return self.player_menu()

    def edit_selected_player(self):
        """Selects a player to edit their details."""
        player_idx = self.view.select_player_to_edit(self.manager.players).strip().lower()
        if player_idx == "r":
            return self.player_menu()
        try:
            player = self.manager.players[int(player_idx) - 1]
            self.edit_player_details(player)
        except (ValueError, IndexError):
            return self.player_menu()

    def edit_player_details(self, player):
        """Take care of the player's details editing process.'"""
        menu_options = {"1": self.update_player_info, "2": self.view.enter_chess_id, "r": self.player_menu}
        selected = self.view.modify_player(player).strip().lower()
        if selected != "r":
            updated_data = menu_options[selected](player)
        else:
            updated_data = menu_options[selected]()
        try:
            player.update_player_info(**updated_data)
            self.manager.save_all()
            return self.player_menu()
        except TypeError:
            player.update_player_info(chess_id=updated_data)
            self.manager.save_all()
            return self.player_menu()

    def update_player_info(self, player):
        new_names = self.view.get_new_player_names()
        valid_date = False
        valid_chess_id = False
        while not valid_date:
            updated_birth_date = self.view.get_new_player_birth_date().strip()
            valid_date = confirm_date_format(updated_birth_date)
        while not valid_chess_id:
            updated_chez_id = self.view.get_player_chess_id().strip().upper() or ""
            valid_chess_id = confirm_chess_id(updated_chez_id)
        proper_first_name = new_names.get("first_name", player.first_name).strip().capitalize()
        proper_last_name = new_names.get("last_name", player.last_name).strip().capitalize()
        updated_data = dict(
            first_name=proper_first_name or player.first_name,
            last_name=proper_last_name or player.last_name,
            birth_date=updated_birth_date or player.birth_date,
            chess_id=updated_chez_id or player.chess_id,
        )
        self.view.data_updated_msg()
        return updated_data

    def back_to_main_menu(self):
        """
        Back to the main menu.
        """
        return
