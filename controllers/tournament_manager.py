from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from utils.json_handler import save_to_json, load_from_json, serialize_tournaments
import os


class TournamentManager:
    """
    Manages tournament data and persistence.
    """

    def __init__(self, file_path="data/tournaments/tournaments.json"):
        self.file_path = file_path
        self.tournaments = self.load_all()

    def load_all(self):
        """
        Loads information from a JSON file and recreates objects.
        """
        self.tournaments = []
        try:
            data = load_from_json(self.file_path)
            for t_data in data:
                loaded_tournament = Tournament(
                    name=t_data["name"],
                    location=t_data["location"],
                    start_date=t_data["start_date"],
                    end_date=t_data["end_date"],
                    description=t_data["description"],
                    num_rounds=t_data.get("num_rounds", 4),
                    current_round=t_data.get("current_round", 0),
                    rankings=t_data.get("rankings", None),
                )
                players_data = t_data.get("players", [])
                if players_data:
                    loaded_tournament.players = self.recreate_players(players_data)
                else:
                    loaded_tournament.players = []
                players_by_id = {p.chess_id: p for p in loaded_tournament.players}
                rounds_data = t_data.get("rounds", [])
                if rounds_data:
                    loaded_tournament.rounds = self.recreate_rounds_and_matches(
                        rounds_data, loaded_tournament, players_by_id
                    )
                else:
                    loaded_tournament.rounds = []
                self.tournaments.append(loaded_tournament)
            return self.tournaments
        except FileNotFoundError:
            print(f"[INFO] Fichier {self.file_path} introuvable.")
            return self.tournaments

    def save_all(self):
        """
        Translates instance status into serialized data and saves it in a JSON file.
        """
        file_name = self.file_path.split("/")[-1]
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path.rstrip(file_name)), exist_ok=True)
        all_tournaments_data = serialize_tournaments(self.tournaments)
        save_to_json(self.file_path, all_tournaments_data, overwrite=True)

    @staticmethod
    def recreate_players(players_data: dict = None):
        """Recreates Player objects from serialized data."""
        players_list = []
        for player_data in players_data:
            player_obj = Player(
                first_name=player_data["first_name"],
                last_name=player_data["last_name"],
                birth_date=player_data["birth_date"],
                chess_id=player_data["chess_id"],
                points=player_data.get("points", 0),
                rank=player_data.get("rank", 0),
            )
            players_list.append(player_obj)
        return players_list

    @staticmethod
    def recreate_rounds_and_matches(rounds_data: dict, tournament, players_by_id: dict):
        """Recreates Round objects from serialized data."""
        for round_data in rounds_data:
            new_round = Round(
                number=round_data["number"],
                tournament=tournament,
                start_time=round_data["start_time"],
                end_time=round_data.get("end_time", None),
                matches=[],
            )
            if round_data["matches"]:
                for match_data in round_data["matches"]:
                    p1_id = match_data["player1"]
                    p2_id = match_data["player2"]
                    p1 = players_by_id.get(p1_id)
                    p2 = players_by_id.get(p2_id)
                    new_match = Match(player1=p1, player2=p2, score1=match_data["score1"], score2=match_data["score2"])
                    new_round.matches.append(new_match)
            tournament.rounds.append(new_round)
        return tournament.rounds
