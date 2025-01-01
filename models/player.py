import re


class Player:
    """
    Instance of a chess player in a tournament.
    """
    def __init__(self, **kwargs):
        # Persistent fields
        self.last_name = kwargs['last_name']
        self.first_name = kwargs['first_name']
        self.birth_date = kwargs['birth_date']
        self.national_id = kwargs['national_id']

        # Tournament field
        self.rank = kwargs['rank']

        if not isinstance(self.rank, int) or self.rank < 0:
            raise ValueError("Rank must be a non-negative integer")
        if not re.match(r"^[A-Z]{2}[0-9]{5}$", kwargs['national_id']):
            raise ValueError("National ID must be in the format 'AB12345'")

    def update_rank(self, new_rank):
        self.rank = new_rank

    def to_dict(self):
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'national_id': self.national_id,
            'rank': self.rank
        }

    @classmethod
    def from_dict(cls, **data):
        return cls(
            last_name=data["last_name"],
            first_name=data["first_name"],
            birth_date=data["birth_date"],
            national_id=data["national_id"],
            rank=data["rank"]
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
