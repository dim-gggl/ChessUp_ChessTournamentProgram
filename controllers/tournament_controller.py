from datetime import datetime
from models.tournament import Tournament
from views.main_menu_view import MainMenuView
from views.tournament_views import TournamentView


class TournamentController:
    def __init__(self, tournament_manager, player_manager):
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager
        self.view = TournamentView()

    def tournament_menu_selection(self):
        """
        Gère les erreurs de saisies dans le menu des tournois.
        """
        selected = -1
        while int(selected) != 0:
            selected = self.view.display_tournament_main_menu().strip()
            if int(selected) >= 4:
                self.view.wrong_menu_input()
            elif selected == "0" or selected == "q" or selected == "r":
                self.view.bye_message()
                self.tournament_manager.save_all()
                return "-1"

            elif 1 <= int(selected) <= 3:
                self.handle_menu_choice(selected)
            else:
                self.view.wrong_menu_input()


    def handle_menu_choice(self, selected):
        """
        Gère les choix de l'utilisateur dans le menu des tournois.'
        """
        if selected == "1":
            details = self.view.get_tournament_details()
            new_tournament = Tournament(**details)
            self.tournament_manager.register_new_entry(new_tournament)
            self.tournament_manager.save_all()
            self.tournament_menu_selection()
            return

        elif selected == "2":
            tournaments_to_handle = self.tournament_manager.running_tournaments + self.tournament_manager.holding_tournaments
            tournament = self.view.select_tournament(tournaments_to_handle)
            self.handle_game_menu(tournament)

        elif selected == "3":
            tournament = self.view.select_tournament(self.tournament_manager.holding_tournaments)
            players = self.player_manager.players
            unregistered_players = []
            for player in players:
                if player not in tournament.players:
                    unregistered_players.append(player)
            registered_player = self.view.select_player(tournament, unregistered_players)
            tournament.players.append(registered_player)
            self.tournament_manager.save_all()
            self.player_manager.save_all()
            self.tournament_menu_selection()
        elif selected == "0" or selected == "q" or selected == "r":
            self.tournament_menu_selection()
        else:
            self.view.wrong_menu_input()

    def handle_game_menu(self, tournament):
        """
        Gère l'organisation interne d'un tournoi.
        """
        selected = -1
        while int(selected) != 0:
            selected = self.view.display_game_menu(tournament)

            if selected == "1":
                return self.start_new_round_conditions(tournament)

            elif selected == "2":
                return self.close_round(tournament)

            elif selected == "3":
                return self.game_status(tournament)

            else:
                self.view.wrong_menu_input()
                break

    def start_new_round_conditions(self, tournament):
        """
        Prévoit les cas de figure lors du lancement d'un nouveau tour.

        """
        if tournament.current_round == 0:
            new_round = tournament.start_first_round()
            self.view.show_round_pairs(new_round)
            self.tournament_manager.save_all()
            self.player_manager.save_all()

        elif tournament.current_round == tournament.num_rounds:
            self.view.last_round_message()

        else:
            tournament.start_next_round()
            new_round = tournament.rounds[-1]
            self.view.show_round_pairs(new_round)
            self.tournament_manager.save_all()
            self.player_manager.save_all()
        return self.handle_game_menu(tournament)

    def close_round(self, tournament):
        """
        Gère toute la logique de fin de tour.
        """
        if tournament.current_round == tournament.num_rounds:
            return self.close_last_round(tournament)
        else:
            closing_round = tournament.rounds[-1]
            closing_round.end_time = datetime.now().strftime("%x - %X")
            self.enter_match_results(closing_round)

            tournament.rank_players()
            self.tournament_manager.save_all()
            self.player_manager.save_all()
            return self.handle_game_menu(tournament)

    def game_status(self, tournament):
        """
        Génère un état des lieux du tournoi..
        """
        ranked_players = tournament.rank_players()
        self.view.display_tournament_summary(tournament, ranked_players)
        return self.handle_game_menu(tournament)

    def enter_match_results(self, closing_round):
        """
        Gère la saisie des scores des matchs.
        """
        for match in closing_round.matches:
            if not match.closed:
                match_scores = self.view.get_match_scores(closing_round, match)
                if match_scores == 1:
                    match.player1.points += 1
                    match.set_score_and_lock(1, 0)
                elif match_scores == 2:
                    match.player2.points += 1
                    match.set_score_and_lock(0, 1)
                elif match_scores == 3:
                    match.set_score_and_lock(0.5, 0.5)
                    match.player1.points += 0.5
                    match.player2.points += 0.5
                else:
                    self.view.wrong_menu_input()
            else:
                self.view.success_match_entry()
        self.view.complete_round_msg(closing_round)
        self.tournament_manager.save_all()
        self.player_manager.save_all()
        return closing_round

    def close_last_round(self, tournament):
        """
        Gère la logique autour de la clôture du dernier tour.
        """
        last_round = tournament.rounds[-1]
        if len(tournament.rounds) == 0:
            self.view.no_round_running_msg()
            return self.handle_game_menu(tournament)
        else:
            self.view.show_closing_message(tournament)
            last_round.end_time = datetime.now().strftime("%x - %X")
            self.enter_match_results(last_round)
            tournament.set_final_rankings()
            self.view.display_tournament_results(tournament)

        self.tournament_manager.save_all()
        self.player_manager.save_all()
        return tournament
