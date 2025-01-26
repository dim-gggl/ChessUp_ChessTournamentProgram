import json
import os
from typing import Union
from models.player import Player
from models.tournament import Tournament
from utils.ansify import ansify


def save_to_json(file_path, new_data, overwrite=True):
    """
    Saves the data in a JSON file.
    - If overwrite is False, new_data is added to the existing data.
    - Otherwise, overwrite everything (overwrite = True).
    """
    try:

        if not overwrite:
            with open(file_path, "r", encoding="utf-8") as file:
                existing_data = json.load(file)
        else:
            existing_data = []

    except FileNotFoundError:
        existing_data = []

    if isinstance(new_data, list):
        existing_data.extend(new_data)

    else:
        existing_data.append(new_data)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4)


def load_from_json(file_path):
    """
    Loads data from a JSON file and returns a list of dicts.
    Returns an empty list if the file does not exist or is empty.
    """

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:

        try:

            data = f.read().strip()
            if not data:
                print(ansify(f"\n\n\n\t\tch_up([INFO])n\t\tFichier vide {file_path}."))
                return []

            return json.loads(data)

        except json.JSONDecodeError as e:
            print(ansify(f"\t\t\tred_err([ERREUR])\n\t\tProblème de format JSON dans {file_path}: {e}"))
            return []


def serialize_players(players) -> list[dict]:
    """
    Takes one or more instances of Player and returns a dict list of their arguments.
    If receives None, returns an empty list
    """

    if not players:
        return []

    all_players_data = []

    for player in players:

        player_data = {
            "_player_id": player._player_id,
            "first_name": player.first_name,
            "last_name": player.last_name,
            "birth_date": player.birth_date,
            "chess_id": player.chess_id,
            "points": player.points,
            "rank": player.rank,
        }

        all_players_data.append(player_data)

    return all_players_data


def serialize_tournaments(tournaments):
    """JSON serialization of Tournament objects."""

    all_tournaments_data = []
    players_data = []
    for tournament_obj in tournaments:
        if tournament_obj.players:
            players_data = serialize_players(tournament_obj.players)

        t_data = {
            "name": tournament_obj.name,
            "location": tournament_obj.location,
            "start_date": tournament_obj.start_date,
            "end_date": tournament_obj.end_date,
            "description": tournament_obj.description,
            "num_rounds": tournament_obj.num_rounds,
            "current_round": tournament_obj.current_round,
            "rounds": [],
            "players": players_data,
            "rankings": tournament_obj.rankings,
        }
        if tournament_obj.rounds:
            for round_obj in tournament_obj.rounds:

                round_data = {
                    "number": round_obj.number,
                    "start_time": round_obj.start_time,
                    "end_time": round_obj.end_time,
                    "matches": [],
                }
                for match_obj in round_obj.matches:

                    match_data = {
                        "player1_id": match_obj.player1._player_id,
                        "player2_id": match_obj.player2._player_id,
                        "score1": match_obj.score1,
                        "score2": match_obj.score2,
                    }

                    round_data["matches"].append(match_data)
                t_data["rounds"].append(round_data)
        else:
            t_data["rounds"] = []

        all_tournaments_data.append(t_data)

    return all_tournaments_data
