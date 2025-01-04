from models.round import Round


class Tournament:
    def __init__(self, name, location, start_date, end_date, description, num_rounds=4):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.num_rounds = num_rounds
        self.current_round = 0
        self.rounds = []
        self.players = []
        self.rankings = None

    def to_dict(self):
        """
        Génère un dict contenant les infos du tournoi.
        """
        if not self.rankings:
            return {
                "name": self.name,
                "location": self.location,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "description": self.description,
                "num_rounds": self.num_rounds,
                "current_round": self.current_round,
                "rounds": [r.to_dict() for r in self.rounds],
                "players": [p.chess_id for p in self.players],
            }
        else:
            return {
                "name": self.name,
                "location": self.location,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "description": self.description,
                "num_rounds": self.num_rounds,
                "rounds": [r.to_dict() for r in self.rounds],
                "players": [p.chess_id for p in self.players],
                "rankings": self.rankings,
            }

    @classmethod
    def from_dict(cls, data, players):
        """
        Génère une instance de Tournoi à partir d'un dict.
        data: dict contenant les infos du tournoi (nom, location, etc.)
        players: liste des instances de Player associées à ce tournoi
        """
        t = cls(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            description=data["description"],
            num_rounds=data.get("num_rounds", 4),
        )
        t.current_round = data.get("current_round", 0)
        t.players = players

        # On construit un dict {chess_id: Player} pour reconstruire les matchs
        players_dict = {p.chess_id: p for p in players}
        t.rounds = [Round.from_dict(round_data, players_dict) for round_data in data.get("rounds", [])]
        return t
