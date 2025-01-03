from models.player import Player
from views.player_views import PlayerView
from utils.json_handler import load_from_json, save_to_json


class PlayerController:
    """
    Gère la logique métier pour les joueurs : création, listing, sauvegarde, etc.
    """

    def __init__(self):
        self.file_path = "data/players/players.json"
        self.view = PlayerView()
        # On charge ici la liste des joueurs existants (depuis JSON si dispo)
        self.players = self.load_players()

    def load_players(self):
        """Charge la liste des joueurs depuis un fichier JSON."""
        data = load_from_json(self.file_path)
        return [Player.from_dict(player_data) for player_data in data]

    def save_players(self):
        """Sauvegarde la liste des joueurs dans le fichier JSON (en écrasant l’existant)."""
        save_to_json(self.file_path, [p.to_dict() for p in self.players], overwrite=True)

    def add_player(self):
        """Demande à la vue les infos d'un nouveau joueur, puis l'ajoute s'il n'existe pas déjà."""
        player_data = self.view.get_player_data()
        if any(p.chess_id == player_data["chess_id"] for p in self.players):
            self.view.show_error_message("Un joueur avec cet ID existe déjà.")
            return
        for p in self.players:
            if  p.points is None:
                p.points = 0,
            else:
                p.points = float(player_data["points"])
            if  p.rank is None:
                p.rank = 0,
            else:
                p.rank = int(player_data["rank"])
        new_player = Player(**player_data)
        self.players.append(new_player)
        self.save_players()
        self.view.show_success_message("Nouveau joueur ajouté avec succès !")

    def view_all_players(self):
        """Affiche la liste de tous les joueurs."""
        self.view.display_players(self.players)
