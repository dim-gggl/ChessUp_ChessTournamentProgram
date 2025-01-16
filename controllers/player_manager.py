import os
from models.player import Player
from utils.json_handler import load_from_json, save_to_json, serialize_players


class PlayerManager:
    """Handles player data and persistence."""

    def __init__(self, file_path="data/players/players.json"):
        self.file_path = file_path
        self.players = self.load_all()


    def load_all(self):
        """Loads information from a JSON file and recreates objects."""
        self.players = []
        for data in load_from_json(self.file_path):
            try:
                new_player = Player(
                    first_name = data["name"],
                    last_name = data["last_name"],
                    birth_date = data["birth_date"],
                    chess_id = data.get("chess_id", ""),
                    points = data.get("points", 0),
                    rank = data.get("rank", 0)
                )
                self.players.append(new_player)
            except KeyError or FileNotFoundError as e:
                print(f"[ERROR] {e}")
            return self.players

    def save_all(self):
        """Save all player data to a JSON file."""
        file_name = self.file_path.split("/")[-1]
        if not os.path.exists(self.file_path.rstrip(file_name)):
            os.makedirs(os.path.dirname(self.file_path.rstrip(file_name)), exist_ok=True)
        all_players = serialize_players(self.players)
        save_to_json(self.file_path, all_players, overwrite=True)
