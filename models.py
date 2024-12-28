class Tournament:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.location = kwargs['location']
        self.date = kwargs['date']
        self.description = kwargs.get('description', 'A chess tournament')
        self.rounds = []

    def add_round(self, chess_round):
        if isinstance(chess_round, Round):
            self.rounds.append(chess_round)
        else:
            raise TypeError("round must be of type Round")


class Round:
    def __init__(self, name):
        self.name = name
        self.matches = []

    def add_match(self, match):
        if isinstance(match, Match):
            self.matches.append(match)
        else:
            raise TypeError("match must be of type Match")


class Match:
    def __init__(self, player1, player2, score1=0, score2=0):
        if isinstance(player1, Player) and isinstance(player2, Player):
            self.player1 = player1
            self.player2 = player2
        else:
            raise TypeError("players must be of type Player")

        self.score1 = score1
        self.score2 = score2

    def set_score(self, score1, score2):
        self.score1 = score1
        self.score2 = score2


class Player:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.rank = kwargs['rank']
        self.national_id = kwargs['national_id']

    def update_rank(self, new_rank):
        self.rank['rank'] = new_rank
