import uuid


class Player:
    def __init__(self, first_name, last_name, birth_date, chess_id: str = "", points: float = 0.0, rank: int = 0, _player_id= None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.name = f"{self.first_name[0].upper()}.{self.last_name}"
        self.points = points
        self.rank = rank
        self._player_id = _player_id if _player_id else str(uuid.uuid4())

    def update_player_info(self, **kwargs):
        """Updates player info"""
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self._player_id == other._player_id 
    
    def __hash__(self):
        return hash(self._player_id)
    
    def __repr__(self):
        return f"\t{self.first_name} {self.last_name} ({self.birth_date}),  \tID : ({self.chess_id})"

    def __str__(self):
        return f"\t{self.name} ~ ID: ({self.chess_id}) ~ \tPts: ({self.points})"
