import re
from models.player import Player


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
