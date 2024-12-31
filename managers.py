import json
import os
from abc import ABC, abstractmethod
from models import Tournament


class Manager(ABC):
    @abstractmethod
    def load(self, *args, **kwargs):
        pass

    @abstractmethod
    def save(self, *args, **kwargs):
        pass


class TournamentManager(Manager):
    def __init__(self, file_path="data/tournaments.json"):
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
                return [Tournament.from_dict(item) for item in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Erreur : Le fichier {self.file_path} contient un JSON invalide.")
            return []

    def save(self, tournament):
        try:
            tournaments = self.load_all()
        except json.JSONDecodeError:
            tournaments = []

        tournaments.append(tournament)
        with open(self.file_path, 'w') as file:
            json.dump([t.to_dict() for t in tournaments], file, indent=4)

    def load(self):
        return self.load_all()

    def load_by_name(self, name):
        tournaments = self.load_all()
        for tournament in tournaments:
            if tournament.name == name:
                return tournament
        return None