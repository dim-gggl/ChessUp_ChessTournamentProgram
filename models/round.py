from models.match import Match


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
