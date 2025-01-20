from utils.ansify import ansify
from utils.validators import confirm_date_format, confirm_chess_id
from views.player_views import PlayerView
from models.player import Player
from views.tournament_views import TournamentView


class PlayerController:
    """
    Manages the player menu and submenus service.
    """

    def __init__(self, manager=None):
        self.view = PlayerView()
        self.manager = manager

    def player_menu(self):
        """Manages the players' main menu."""
        selected = ""
        while selected != "r":

            menu_actions = {
                "1": self.add_new_player,
                "2": self.edit_selected_player,
                "3": lambda: self.view.display_players(self.manager.players)
            }
            selected = self.view.display_players_menu().strip().lower()
            action = menu_actions.get(selected)
            if not self.manager.players and selected != 1:
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
        first_name = player_names["first_name"].strip().capitalize()
        last_name = player_names["last_name"].strip().capitalize()
        birth_date_input = self.view.get_new_player_birth_date().strip()
        birth_date = confirm_date_format(birth_date_input)
        chess_input = self.view.get_player_chess_id().strip().upper()
        if chess_input:
            chess_id = chess_input
        else:
            chess_id = ""
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
        selected_idx = self.view.select_player_to_edit(self.manager.players).strip().lower()
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
        selected = self.view.edition_options(player).strip().lower()
        menu_actions = {
            "1": self.update_player_info,
            "2": lambda p: self.update_chess_id_only(p),
        }
        action = menu_actions.get(selected)

        if action:
            action(player)
            self.manager.save_all()
        elif selected == "r":
            return
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
            first_name = updated_first_name,
            last_name = updated_last_name,
            birth_date = updated_birth_date,
            chess_id = updated_chess_id
        )
        self.view.data_updated_msg()
        return updated_data

    def update_chess_id_only(self, player):
        """Just manages the National Chess ID update."""
        new_chess_id = self.view.enter_chess_id(player).strip().upper()
        player.update_player_info(chess_id=new_chess_id)

    def back_to_main_menu(self):
        """
        Back to the main menu.
        """
        return
