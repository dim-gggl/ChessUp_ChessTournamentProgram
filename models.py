class Tournament:
    def __init__(self, name, location, date, description):
        self.name = name
        self.location = location
        self.date = date
        self.description = description
        self.rounds = []

    def add_round(self, round):
        self.rounds.append(round)


class Round:
    def __init__(self, name):
        self.name = name
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)


class Match:
    def __init__(self, player1, player2, score1=0, score2=0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def set_score(self, score1, score2):
        self.score1 = score1
        self.score2 = score2

class Player:
    def __init__(self, name, rank, national_id):
        self.name = name
        self.rank = rank
        self.national_id = national_id

    def update_rank(self, new_rank):
        self.rank = new_rank