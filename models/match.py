class Match:
    def __init__(self, player1, player2, score1=0, score2=0, closed=False):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
        self.closed = False

    def set_score(self, score1, score2):
        self.score1 = score1
        self.score2 = score2
        if self.score1 + self.score2 == 1:
            self.closed = True
            return self

    def __repr__(self):
        return [self.player1.name, self.score1], [self.player2.name, self.score2]

    def __str__(self):
        return (f"\n\033[1;96m  {self.player1.name}\033[0m ~~\033[1m[{self.score1}]\033[0m~~ "
                f"\033[1;96mvs\033[0m ~~\033[1m[{self.score2}]\033[0m~~ \033[1;96m{self.player2.name}\033[0m")
