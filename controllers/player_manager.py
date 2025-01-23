import os
from models.player import Player
from utils.ansify import ansify
from utils.json_handler import load_from_json, save_to_json, serialize_players


class PlayerManager:
    """Handles player data and persistence."""

    def __init__(self, file_path="data/players/players.json"):
        self.file_path = file_path
        self.players = []
        self.load_all()

    def load_all(self):
        """Loads information from a JSON file and recreates objects."""

        players_data = load_from_json(self.file_path)
        if players_data:
            for player_data in players_data:

                player_inst = Player(
                    first_name=player_data["first_name"],
                    last_name=player_data["last_name"],
                    birth_date=player_data["birth_date"],
                    chess_id=player_data["chess_id"],
                    points=player_data["points"],
                    rank=player_data["rank"],
                )

                self.players.append(player_inst)
        else:
            print("\n" * 50 + ansify("\t\tch_up([INFO]) \n\tAucune info joueur enregistrée"))

        return self.players

    def save_all(self):
        """Save all player data to a JSON file."""

        file_name = self.file_path.split("/")[-1]
        if not os.path.exists(self.file_path.rstrip(file_name)):
            os.makedirs(os.path.dirname(self.file_path.rstrip(file_name)), exist_ok=True)

        players_data = serialize_players(self.players)

        save_to_json(self.file_path, players_data, overwrite=True)
