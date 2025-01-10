from datetime import datetime
from models.tournament import Tournament
from views.tournament_command_view import TournamentCommandView
from views.tournament_views import TournamentView


class TournamentController:
    def __init__(self, manager, player_manager):
        self.view = TournamentView()
        self.manager = manager
        self.player_manager = player_manager
        self.command_view = TournamentCommandView()

    def tournament_menu_selection(self):
        """
        Gère les erreurs de saisies dans le menu des tournois.
        """
        selected = self.view.display_tournament_main_menu().strip()
        if int(selected) >= 4:
            self.view.wrong_menu_input()
        elif int(selected) == 0:
            self.view.bye_message()
            self.manager.save_all()
            return
        else:
            return self.handle_menu_choice(int(selected))

    def handle_menu_choice(self, selected=0):
        """
        Gère les choix de l'utilisateur dans le menu des tournois.'
        """
        if selected == 1:
            details = self.view.get_tournament_details()
            new_tournament = Tournament(**details)
            self.manager.tournaments.append(new_tournament)
            self.manager.save_all()
            return self.tournament_menu_selection()

        elif selected == 2:
            tournament = self.view.select_tournament(self.manager.tournaments)
            return self.handle_game_menu(tournament)

        elif selected == 3:
            tournament = self.view.select_tournament(self.manager.tournaments)
            players = self.player_manager.players
            unregistered_players = []
            for player in players:
                if player not in tournament.players:
                    unregistered_players.append(player)
            registered_player = self.view.select_player(tournament, unregistered_players)
            tournament.players.append(registered_player)
            self.manager.save_all()
            self.player_manager.save_all()
            return self.tournament_menu_selection()
        else:
            return self.tournament_menu_selection()

    def handle_game_menu(self, tournament):
        """
        Gère l'organisation interne d'un tournoi.
        """
        selected = -1
        while int(selected) != 0:
            selected = int(self.view.display_game_menu(tournament))

            if selected == 1:
                self.start_new_round_conditions(tournament)

            elif selected == 2:
                return self.close_round(tournament)

            elif selected == 3:
                return self.game_status(tournament)
            else:
                return self.tournament_menu_selection()

    def start_new_round_conditions(self, tournament):
        """
        Prévoit les cas de figure lors du lancement d'un nouveau tour.

        """
        if tournament.current_round == 0:
            new_round = tournament.start_first_round()
            self.view.show_round_pairs(new_round)
            self.manager.save_all()
            self.player_manager.save_all()

        elif tournament.current_round == tournament.num_rounds:
            self.view.last_round_message()

        else:
            tournament.start_next_round()
            new_round = tournament.rounds[-1]
            self.view.show_round_pairs(new_round)
            self.manager.save_all()
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
            self.manager.save_all()
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
                    match.set_score(1, 0)
                elif match_scores == 2:
                    match.player2.points += 1
                    match.set_score(0, 1)
                elif match_scores == 3:
                    match.set_score(0.5, 0.5)
                    match.player1.points += 0.5
                    match.player2.points += 0.5
                else:
                    self.view.wrong_menu_input()
            else:
                self.view.success_match_entry()
        self.view.complete_round_msg(closing_round)
        self.manager.save_all()
        self.player_manager.save_all()
        return closing_round

    def close_last_round(self, tournament):
        """
        Gère la logique autour de la clôture du dernier tour.
        """
        self.view.show_closing_message(tournament)
        if len(tournament.rounds) == 0:
            self.view.no_round_running_msg()
            return self.handle_game_menu(tournament)
        else:
            tournament.rounds[-1].end_time = datetime.now().strftime("%x - %X")
            closing_round = tournament.rounds[-1]
            self.enter_match_results(closing_round)

            tournament.set_final_rankings()


        self.manager.save_all()
        self.player_manager.save_all()
        return tournament
