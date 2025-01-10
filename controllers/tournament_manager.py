from models.tournament import Tournament
from models.round import Round
from models.match import Match
from utils.json_handler import save_to_json, load_from_json
import os


class TournamentManager:
    """
    Gère les données des tournois et leur persistence.
    """

    def __init__(self, players_manager=None):
        self.tournaments = []
        self.file_path = "data/tournaments/tournaments.json"
        self.players_manager = players_manager

    def load_all(self):
        """
        Charge les infos depuis un fichier JSON et recrée les objets.
        """
        data = load_from_json(self.file_path)
        self.tournaments = []
        for t_data in data:
            new_tournament = Tournament(
                name=t_data["name"],
                location=t_data["location"],
                start_date=t_data["start_date"],
                end_date=t_data["end_date"],
                description=t_data["description"],
                num_rounds=t_data.get("num_rounds", 4),
                current_round=t_data.get("current_round", 0),
                rankings=t_data.get("rankings", None)
            )
            rounds_data = t_data.get("rounds", [])
            for rd in rounds_data:
                new_round = Round(
                    number=rd["number"],
                    start_time=rd["start_time"],
                    end_time=rd["end_time"],
                )
                for match_d in rd.get("matches", []):
                    new_match = Match(
                        player1=match_d["player1"],
                        player2=match_d["player2"],
                        score1=match_d["score1"],
                        score2=match_d["score2"],
                        closed=match_d.get("closed", False)
                    )
                    new_round.matches.append(new_match)

            players_data = t_data.get("players", [])
            new_tournament.players = self.players_manager.recreate_players(players_data)

            self.tournaments.append(new_tournament)

        return self.tournaments

    def save_all(self):
        """
        Traduit l'état des instances en données serializes et les enregistre dans un fichier JSON.
        """
        file_name = self.file_path.split("/")[-1]
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path.rstrip(file_name)), exist_ok=True)
        all_tournaments_data = []
        for t in self.tournaments:
            t_data = {
                "name": t.name,
                "location": t.location,
                "start_date": t.start_date,
                "end_date": t.end_date,
                "description": t.description,
                "num_rounds": t.num_rounds,
                "current_round": t.current_round,
                "rounds": [],
                "players": [],
                "rankings": t.rankings
            }
            for round_obj in t.rounds:
                round_data = {
                    "number": round_obj.number,
                    "start_time": round_obj.start_time,
                    "end_time": round_obj.end_time,
                    "matches": []
                }
                for match_obj in round_obj.matches:
                    match_data = {
                        "player1": match_obj.player1.chess_id,
                        "player2": match_obj.player2.chess_id,
                        "score1": match_obj.score1,
                        "score2": match_obj.score2,
                        "closed": match_obj.closed
                    }
                    round_data["matches"].append(match_data)

                t_data["rounds"].append(round_data)

            for p in t.players:
                p_data = {
                    "first_name": p.first_name,
                    "last_name": p.last_name,
                    "birth_date": p.birth_date,
                    "chess_id": p.chess_id,
                    "points": p.points,
                    "rank": p.rank
                }
                t_data["players"].append(p_data)

            all_tournaments_data.append(t_data)

        save_to_json(self.file_path, all_tournaments_data, overwrite=True)
