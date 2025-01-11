import os
from models.player import Player
from utils.json_handler import load_from_json, save_to_json


class PlayerManager:
    def __init__(self):
        self.players = []
        self.file_path = "data/players/players.json"

    def load_all(self):
        for data in load_from_json(self.file_path):
            new_player = Player(**data)
            self.players.append(new_player)
        return self.players

    def save_all(self):
        file_name = self.file_path.split("/")[-1]
        if not os.path.exists(self.file_path.rstrip(file_name)):
            os.makedirs(os.path.dirname(self.file_path.rstrip(file_name)), exist_ok=True)
        all_players = self.serialize_players()
        save_to_json(self.file_path, all_players, overwrite=True)

    def serialize_players(self, players=None):
        if players is None:
            players = self.players
        json_players = []
        for player in players:
            json_player = {
                "first_name": player.first_name,
                "last_name": player.last_name,
                "birth_date": player.birth_date,
                "chess_id": player.chess_id,
                "points": player.points,
                "rank": player.rank
            }
            json_players.append(json_player)
        return json_players

    def recreate_players(self, players_data=None):
        if players_data is None:
            players_data = load_from_json(self.file_path)
        else:
            players_data = players_data
        real_players = []
        for player_data in players_data:
            new_player = Player(**player_data)
            real_players.append(new_player)
        return real_players
