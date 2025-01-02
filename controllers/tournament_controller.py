from models.tournament import Tournament
from utils.json_handler import load_from_json, save_to_json
from views.tournament_views import TournamentView


class TournamentController:
    """
    Gère la logique métier des tournois : chargement, création, sauvegarde,
    et accès aux données depuis/vers le JSON.
    """

    def __init__(self, player_controller, file_path="data/tournaments/tournaments.json"):
        self.file_path = file_path
        self.player_controller = player_controller  # pour accéder à la liste de joueurs
        self.view = TournamentView()
        # On charge directement tous les tournois enregistrés
        self.tournaments = self.load_tournaments()

    def load_tournaments(self):
        """Charge les tournois depuis le fichier JSON et les reconstitue en objets `Tournament`."""
        data = load_from_json(self.file_path)
        # On fait une dict pour accéder aux joueurs par leur chess_id
        all_players = {p.chess_id: p for p in self.player_controller.players}

        tournaments = []
        for t_data in data:
            # On reconstitue la liste de joueurs du tournoi
            players = [all_players[cid] for cid in t_data["players"] if cid in all_players]
            tournament = Tournament.from_dict(t_data, players)
            tournaments.append(tournament)
        return tournaments

    def save_tournaments(self):
        """Enregistre la totalité des tournois dans un fichier JSON."""
        save_to_json(
            self.file_path,
            [tournament.to_dict() for tournament in self.tournaments],
            overwrite=True
        )

    def create_tournament(self):
        """
        Demande à la vue les infos d’un nouveau tournoi, vérifie s’il n’existe pas déjà,
        puis l’ajoute si tout est OK.
        """
        data = self.view.get_tournament_data()
        if any(tournament.name == data["name"] and tournament.start_date == data["start_date"]
               for tournament in self.tournaments):
            self.view.show_error_message("Un tournoi avec ce nom et cette date existe déjà.")
            return

        # Création et ajout du tournoi à la liste
        new_tournament = Tournament(**data)
        self.tournaments.append(new_tournament)
        self.save_tournaments()
        self.view.show_success_message("Tournoi créé avec succès.")

    def show_tournament_summary(self, tournament):
        """Utilise la vue pour afficher un résumé du tournoi."""
        self.view.display_tournament_summary(tournament)
