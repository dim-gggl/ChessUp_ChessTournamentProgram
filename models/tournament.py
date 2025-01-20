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
            return input(
                ansify(
                    "ch_up([INFO]) bld(C'était le dernier tour ! )"
                    "\nSouhaitez-vous ouvrir un round supplémentaire ?disc_it((y/n)) :  "
                )
            )
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
        champions = [p for p in self.players if p.rank == 1]
        vice_champions = [p for p in self.players if p.rank == 2]
        others = [p for p in self.players if p.rank >= 3]
        for player in champions:
            self.rankings.append(
                f"gldn({player.rank}er) ~ gldn(Champion) : gldn({player.last_name} {player.first_name}) ~"
            )
        for player in vice_champions:
            self.rankings.append(
                f"whte({player.rank}nd) ~ whte(Vice-champion) : whte({player.last_name} {player.first_name}) ~"
            )
        for player in others:
            self.rankings.append(f"bld({player.rank}e) ~ bld({player.last_name} {player.first_name}) ~")
        for player in self.players:
            player.points = 0
            player.rank = 0
        return self.rankings

    def __str__(self):
        if self.is_holding:
            return f" ttl_blu([PRÊT]) ~ ttl_blu({self.name}), {self.start_date}, {self.end_date}"
        if self.is_running and not self.rounds[-1].is_finished:
            return f" red_err([EN COURS]) ~ red_err({self.name}) ~ Status :  ch_up(Round {self.current_round}) red_err(OUVERT), en attente des résultats"
        if self.is_running and self.rounds[-1].is_finished:
            return f" red_err([EN COURS]) ~ red_err({self.name}) ~ Status : le ttl_blu(Round {self.current_round + 1}) peut être lancé !"
        if self.is_finished:
            return f" ch_up([TERMINÉ]) ~ ch_up({self.name}), ch_up({self.num_rounds}) rounds disputés, ch_up({len(self.players)}) joueurs ont participé"
        else:
            return (f" pnk([BESOIN DE JOUEURS]) ~ whte({self.name}), red_err({len(self.players)}) joueur(s) inscrit(s) pour l'instant.\n"
                    f"            Et  red_err({self.num_rounds}) rounds sont prévus !")
