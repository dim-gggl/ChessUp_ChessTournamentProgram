from models.round import Round
from models.player import Player


class Tournament:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.location = kwargs['location']
        self.starting_date = kwargs['starting_date']
        self.ending_date = kwargs['ending_date']
        self.description = kwargs.get('description', 'A chess tournament')
        self.rounds = []
        self.players = []
        self.current_round_number = 1


    def add_round(self, chess_round):
        if isinstance(chess_round, Round):
            self.rounds.append(chess_round)
        else:
            raise TypeError("round must be of type Round")

    def add_player(self, player):
        if isinstance(player, Player):
            self.players.append(player)
        else:
            raise TypeError("player must be of type Player")

    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'starting_date': self.starting_date,
            'ending_date': self.ending_date,
            'description': self.description,
            'rounds': [round.to_dict() for round in self.rounds],
            'players': [player.to_dict() for player in self.players],
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            location=data["location"],
            starting_date=data["starting_date"],
            ending_date=data["ending_date"],
            description=data.get("description", "A chess tournament"),
            rounds=[Round.from_dict(r) for r in data.get("rounds", [])],
            players=[Player.from_dict(p) for p in data.get("players", [])],
        )
