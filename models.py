import re


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


class Round:
    def __init__(self, number=1):
        self.name = f"Round {number}"
        self.matches = []

    def add_match(self, match):
        if isinstance(match, Match):
            self.matches.append(match)
        else:
            raise TypeError("match must be of type Match")

    def to_dict(self):
        return {
            'name': self.name,
            'matches': self.matches
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            number=data["name"].lstrip("Round_")
        )



class Match:
    def __init__(self, player1, player2, score_p1=0, score_p2=0):
        """
        Tuple of two lists, one for each player
        and their respective scores.
        :param player1: str = national ID of player 1
        :param player2: str = national ID of player 2
        """
        if isinstance(player1, Player) and isinstance(player2, Player):
            self.player1 = player1
            self.player2 = player2
        else:
            raise TypeError("players must be of type Player")
        self.score_p1 = score_p1
        self.score_p2 = score_p2

    def set_score(self):
        if 0 > self.score_p1 > 1 or 0 > self.score_p2 > 1:
            raise ValueError("Scores must be 0 and 1")
        else:
            match_results = (
                [self.player1, self.score_p1],
                [self.player2, self.score_p2]
            )
            return match_results

    def to_dict(self):
        return {
            {'player_1': self.player1}: {'score_p1': self.score_p1},
            {'player_2': self.player2}: {'score_p2': self.score_p2}
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            player1=data["player_1"],
            player2=data["player_2"],
            score_p1=data["score_p1"],
            score_p2=data["score_p2"]
        )


class Player:
    def __init__(self, **kwargs):
        # Persistent fields
        self.last_name = kwargs['last_name']
        self.first_name = kwargs['first_name']
        self.birth_date = kwargs['birth_date']
        self.national_id = kwargs['national_id']

        # Tournament field
        self.rank = kwargs['rank']

        if not isinstance(self.rank, int) or self.rank < 0:
            raise ValueError("Rank must be a non-negative integer")
        if not re.match(r"^[A-Z]{2}[0-9]{5}$", kwargs['national_id']):
            raise ValueError("National ID must be in the format 'AB12345'")

    def update_rank(self, new_rank):
        self.rank = new_rank

    def to_dict(self):
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'national_id': self.national_id,
            'rank': self.rank
        }

    @classmethod
    def from_dict(self, data):
        return cls(
            last_name=data["last_name"],
            first_name=data["first_name"],
            birth_date=data["birth_date"],
            national_id=data["national_id"],
            rank=data["rank"]
        )
