class Player:
    def __init__(self, first_name, last_name, birth_date, chess_id: str = "", points: float = 0.0, rank: int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.name = f"{self.first_name[0].upper()}.{self.last_name}"
        self.points = points
        self.rank = rank

    def update_player_info(self, **kwargs):
        """Updates player info"""
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        if self.chess_id != "":
            return self.chess_id == other.chess_id
        return self.first_name == other.first_name and self.last_name == other.last_name and self.birth_date == other.birth_date

    def __hash__(self):
        return hash(self.chess_id if self.chess_id else f"{self.first_name} {self.last_name} {self.birth_date}")

    def __repr__(self):
        return f"\t{self.first_name} {self.last_name} ({self.birth_date}),  \tID : ({self.chess_id})"

    def __str__(self):
        return f"\t{self.name} ~ ID: ({self.chess_id}) ~ \tPts: ({self.points})"
