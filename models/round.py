from datetime import datetime
from models.match import Match


class Round:
    def __init__(self, name):
        self.name = name
        self.start_time = datetime.now()
        self.end_time = None
        self.matches = []

    def end_round(self):
        self.end_time = datetime.now()

    def to_dict(self):
        return {
            "name": self.name,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "matches": [m.to_dict() for m in self.matches],
        }

    @classmethod
    def from_dict(cls, data, players_dict):
        """
        data = {
          'name': str,
          'start_time': str (isoformat),
          'end_time': str ou None,
          'matches': [ {match_dict}, {match_dict} ... ]
        }
        players_dict = {chess_id: Player}
        """
        round_ = cls(data["name"])
        round_.start_time = datetime.fromisoformat(data["start_time"])
        if data["end_time"]:
            round_.end_time = datetime.fromisoformat(data["end_time"])

        # Reconstitue les instances de Match
        round_.matches = [Match.from_dict(m, players_dict) for m in data["matches"]]
        return round_
