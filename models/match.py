from utils.ansify import ansify


class Match:
    def __init__(self, player1, player2, score1=0, score2=0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    @property
    def is_over(self):
        """Returns True when the match is over"""
        return self.score1 + self.score2 == 1

    def set_score_and_lock(self, score1, score2):
        """Sets scores and locks the match"""
        self.score1 = score1
        self.score2 = score2
        return self

    def __str__(self):
        return ansify(f"bld({self.player1.first_name} {self.player1.last_name}) ~~ ch_up(vs) ~~ bld{self.player2.first_name} {self.player2.last_name})")
