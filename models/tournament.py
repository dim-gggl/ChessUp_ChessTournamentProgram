import random
from models.round import Round
from models.match import Match


class Tournament:
    def __init__(self, name, location, start_date, end_date, description, **kwargs):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.num_rounds = kwargs.get("num_rounds", 4)
        self.current_round = kwargs.get("current_round", 0)
        self.rounds = kwargs.get("rounds", [])
        self.players = kwargs.get("players", [])
        self.rankings = kwargs.get("rankings", None)

    @property
    def is_holding(self):
        return self.current_round == 0

    def start_first_round(self):
        self.current_round += 1
        open_round = Round(self.current_round)
        shuffled = self.players
        random.shuffle(shuffled)
        if len(shuffled) % 2 != 0:
            exempt_player = shuffled.pop(0)
            exempt_player.points += 1
            print(f"\n\033[1;33m[INFO]\033[0m {exempt_player.name} "
                  f"n'a pas d'adversaire. 1 point pour le premier round !")
        for i in range(0, len(shuffled), 2):
            open_round.matches.append(Match(shuffled[i], shuffled[i + 1]))
        self.rounds.append(open_round)
        return open_round

    def rank_players(self):
        self.players.sort(key=lambda p: p.points, reverse=True)
        for i, player in enumerate(self.players):
            player.rank = i + 1
        return self.players

    def start_next_round(self):
        self.current_round += 1
        self.rank_players()
        new_round = Round(int(self.current_round))
        previous_matches = {(m.player1, m.player2) for rnd in self.rounds for m in rnd.matches}
        players_sorted = self.players[:]
        while players_sorted:
            p1 = players_sorted.pop(0)
            paired = False
            for i, p2 in enumerate(players_sorted):
                if (p1, p2) not in previous_matches and (p2, p1) not in previous_matches:
                    new_round.matches.append(Match(p1, p2))
                    del players_sorted[i]
                    paired = True
                    break
                elif ((p1, p2) in previous_matches or (p2, p1) in previous_matches) and len(players_sorted) == 1:
                    p2 = players_sorted.pop(0)
                    new_round.matches.append(Match(p1, p2))
                    paired = True

            if not paired:
                p1.points += 1
                print(f"{p1.name} {p1.last_name} n'a pas d'adversaire. 1 point !")
        self.rounds.append(new_round)
        return self.rounds

    def set_final_rankings(self):
        self.rank_players()
        self.rankings = []
        if len(self.players) >= 1:
            champion_player = self.players[0]
            champion_str = (
                f"{champion_player.rank} ~ Champion : "
                f"{champion_player.last_name} {champion_player.first_name}"
            )
            self.rankings.append(champion_str)
            vice_player = self.players[1]
            vice_str = (
                f"{vice_player.rank} ~ Vice-champion : "
                f"{vice_player.last_name} {vice_player.first_name}"
            )
            self.rankings.append(vice_str)

        if len(self.players) > 2:
            for player in self.players[2:]:
                other_str = (
                    f"{player.rank} ~ {player.last_name} {player.first_name}"
                )
                self.rankings.append(other_str)

    def __repr__(self):
        if not self.rankings:
            return f"{self.name}, {self.start_date}, {self.end_date}"
        else:
            return f"[TERMINÉ] {self.name}, {self.start_date}, {self.end_date}"

    def __str__(self):
            return f"{self.name} - {self.start_date} - {self.end_date}\n"
