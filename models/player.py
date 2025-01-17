class Player:
    def __init__(self, first_name, last_name, birth_date, chess_id: str="", **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.name = f"{self.first_name[0].upper()}.{self.last_name}"
        self.points = kwargs.get("points", 0)
        self.rank = kwargs.get("rank", 0)

    def update_player_info(self, **kwargs):
        """Updates player info"""
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.birth_date}),  ID : ({self.chess_id})"

    def __str__(self):
        return f"{self.name} ~ ID: ({self.chess_id}) ~ Pts: ({self.points})"
