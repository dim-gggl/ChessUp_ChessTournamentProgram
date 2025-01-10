from datetime import datetime


class Round:
    def __init__(self, number=0, **kwargs):
        self.number = number
        self.name = f"Round {self.number}"
        self.matches = kwargs.get("matches", [])
        self.start_time = kwargs.get("start_time", datetime.now().strftime("%x - %X"))
        self.end_time = kwargs.get("end_time", None)

    def __repr__(self):
        if self.end_time:
            description =  f"{self.name} :\n Matches : "
            for i, match in range(len(self.matches)):
                description += f"\n {i+1} - {str(match)}"
            return description
        else:
            return f"{self.name} en cours. En attente des résultats."

    def __str__(self):
        if self.end_time:
            return f"{self.name}"
        else:
            return f"{self.name} en cours. En attente des résultats."
