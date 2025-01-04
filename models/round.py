from datetime import datetime
from models.match import Match


class Round:
    def __init__(self, name):
        self.name = name
        self.start_time = datetime.now()
        self.end_time = None
        self.matches = []

    def end_round(self):
        """
        Génère l'heure de fin du round.
        Méthode appelée dans la méthode enter_results de la classe TournamentManager.
        """
        self.end_time = datetime.now()

    def to_dict(self):
        """
        Génère un dict contenant les infos du round.
        """
        return {
            "name": self.name,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "matches": [m.to_dict() for m in self.matches],
        }

    @classmethod
    def from_dict(cls, data, players_dict):
        """
        Génère une instance de Round à partir d'un dict. passé par la méthode
        from_dict de la classe Tournament.
        """
        round_ = cls(data["name"])
        round_.matches = [Match.from_dict(m_data, players_dict) for m_data in data.get("matches", [])]
        return round_
