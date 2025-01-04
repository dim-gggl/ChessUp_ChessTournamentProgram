class Match:
    def __init__(self, player1, player2, score1=0, score2=0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        """
        Génère un dict contenant les infos du match.
        """
        return {
            "player1": self.player1.chess_id,
            "player2": self.player2.chess_id,
            "score1": self.score1,
            "score2": self.score2,
        }

    @classmethod
    def from_dict(cls, data, players_dict):
        """
        Génère une instance de Match avec des données passées par
        la méthode from_dict de la classe Round
        """
        return cls(
            player1=players_dict[data["player1"]],
            player2=players_dict[data["player2"]],
            score1=data.get("score1", 0),
            score2=data.get("score2", 0),
        )

    def __repr__(self):
        """
        Un Match est représenté par une liste de 2 tuples (player_id, score)
        """
        return [(self.player1.chess_id, self.score1), (self.player2.chess_id, self.score2)]

    def __str__(self):
        """
        Affichage du match dans la console.
        """
        return f"\033[32m{self.player1.last_name}\033[0m ——\033[31m[{self.score1}]\033[0m—— vs ——\033[31m[{self.score2}]\033[0m—— \033[32m{self.player2.last_name}\033[0m"  # nqoa
