class Match:
    def __init__(self, player1, player2, score1=0, score2=0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        return {
            "player1": self.player1.chess_id,
            "player2": self.player2.chess_id,
            "score1": self.score1,
            "score2": self.score2,
        }

    @classmethod
    def from_dict(cls, data, players_dict):
        """
        data est un dict contenant {
        'player1': <chess_id>, 'player2': <chess_id>,
        'score1': <float>, 'score2': <float>
        }
        players_dict est un dict : { chess_id: Player }
        """
        return cls(
            player1=players_dict[data["player1"]],
            player2=players_dict[data["player2"]],
            score1=data.get("score1", 0),
            score2=data.get("score2", 0),
        )

    def __str__(self):
        return f"\n{
        self.player1.last_name} [{self.score1}] -- [{
        self.score2}] {self.player2.last_name
        }"
