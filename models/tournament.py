from models.round import Round
from utils.ansify import ansify
from itertools import groupby
import random


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
    def is_open_to_inscription(self):
        """Returns True when the tournament has not started"""
        return self.current_round == 0 and not self.is_finished

    @property
    def is_holding(self):
        """Returns True when the tournament has not started and has enough players"""
        return self.current_round == 0 and len(self.players) >= int(self.num_rounds) and not self.is_finished

    @property
    def is_running(self):
        """Returns True when the tournament has started"""
        return 0 < self.current_round <= int(self.num_rounds) and not self.rankings

    @property
    def is_finished(self):
        """Returns True when the tournament has ended"""
        return self.current_round == int(self.num_rounds) and self.rankings

    def start_new_round(self):
        """Opens a new round"""
        if self.is_holding:
            self.current_round += 1
            open_round = Round(self.current_round, self)
            open_round.match_players()
            self.rounds.append(open_round)
        elif self.current_round < int(self.num_rounds):
            self.current_round += 1
            self.rank_players()
            open_round = Round(self.current_round, self)
            open_round.match_players()
            self.rounds.append(open_round)
        else:
            return input(ansify("ch_up([INFO]) bld(C'était le dernier tour ! )"
                                "\nSouhaitez-vous ouvrir un round supplémentaire ?disc_it((y/n)) :  "))
        return open_round

    def rank_players(self):
        """Ranks players by points"""
        self.players.sort(key=lambda p: p.points, reverse=True)
        new_list = []
        for points, group_iterator in groupby(self.players, key=lambda p: p.points):
            group_list = list(group_iterator)
            random.shuffle(group_list)
            new_list.extend(group_list)
        current_rank = 1
        previous_points = None
        for i, player in enumerate(new_list):
            if i == 0 or player.points != previous_points:
                current_rank = i + 1
            player.rank = current_rank
            previous_points = player.points
        return self.players


    def set_final_rankings(self):
        """Sets final rankings"""
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
        return self.rankings

    def __repr__(self):
        if not self.rankings:
            return f"{self.name}, {self.start_date}, {self.end_date}"
        else:
            return f"[TERMINÉ] {self.name}, {self.start_date}, {self.end_date}"

    def __str__(self):
            return f"{self.name} - {self.start_date} - {self.end_date}\n"
