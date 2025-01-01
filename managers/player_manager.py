import json
import os
from models.player import Player
from managers.manager import Manager


class PlayerManager(Manager):
    def __init__(self, file_path="data/players.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)

    def load_all(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read().strip()
                if not content:
                    return []
                data = json.loads(content)
                return [Player.from_dict(**item) for item in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Erreur : Le fichier {self.file_path} contient un JSON invalide.")
            return []

    def save(self, player):
        players = self.load_all()
        players.append(player)
        with open(self.file_path, 'w') as file:
            json.dump([p.to_dict() for p in players], file, indent=4)

    def load_by_national_id(self, national_id):
        players = self.load_all()
        print("Players chargés :", players)
        for player in players:
            if player.national_id == national_id:
                return player

        return None

    def load(self):
        return self.load_all()
