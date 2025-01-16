from utils.ansify import ansify
from utils.validators import validate_date, validate_chess_id
from views.player_views import PlayerView
from models.player import Player


class PlayerController():
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
            "2": self.select_player_to_edit,
            "3": self.view.display_players,
            "r": self.back_to_main_menu
        }
        selected = self.view.display_players_menu().strip().lower()
        if int(selected) == 3:
            return menu_options[selected](self.manager.players)
        else:
            return menu_options[selected]()

    def add_new_player(self):
        """Adds a new player to the database."""
        player_data = self.input_verification()
        new_player = Player(**player_data)
        self.manager.players.append(new_player)
        self.manager.save_all()
        return self.player_menu()

    def select_player_to_edit(self):
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
        menu_options = {
            "1": self.input_verification,
            "2": self.view.enter_chess_id,
            "r": self.player_menu
        }
        selected = self.view.modify_player(player).strip().lower()
        if int(selected):
            user_choice = menu_options[selected](player)
        else:
            user_choice = menu_options[selected]()
        try:
            player.update_player_info(**user_choice)
            self.manager.save_all()
        except ValueError or AttributeError or TypeError as e:
             raise e (ansify("      red_err([ERREUR])\n      Une erreur s'est produite"
                             "pendant la mise à jour du joueur"))
        return self.player_menu()

    def input_verification(self, player=None):
        """Validates the user input for player data."""
        valid_data = False
        while not valid_data:
            if player:
                raw_data = self.view.get_player_data(edit=True, player=player)
            else:
                raw_data = self.view.get_player_data()
            first_name = raw_data["first_name"].strip().capitalize() or player.first_name
            last_name = raw_data["last_name"].strip().capitalize() or player.last_name
            birth_date = validate_date(raw_data["birth_date"]) or player.birth_date
            chess_id = validate_chess_id(raw_data["chess_id"].strip()) or player.chess_id
            if all([first_name, last_name, birth_date, chess_id]):
                valid_data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "birth_date": birth_date,
                    "chess_id": chess_id
                }
                return valid_data

    def back_to_main_menu(self):
        """
        Back to the main menu.
        """
        return
