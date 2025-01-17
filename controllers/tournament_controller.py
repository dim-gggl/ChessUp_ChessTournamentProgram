from datetime import datetime
from models.tournament import Tournament
from views.tournament_views import TournamentView
from utils.validators import confirm_date_format, confirm_chess_id


class TournamentController:
    """
    Manages the tournament menu and submenus service.
    """

    def __init__(self, tournament_manager, players):
        self.tournament_manager = tournament_manager
        self.players = players
        self.view = TournamentView()

    def tournament_menu(self):
        """
        Tournaments' main menu.
        """
        menu_options = {
            "1": self.create_new_tournament,
            "2": self.manage_existing_tournament,
            "3": self.add_player,
            "4": self.list_tournaments,
            "r": self.return_to_main_menu,
        }
        selected = self.view.display_tournament_main_menu()
        return menu_options.get(selected, self.view.wrong_menu_input)()

    def create_new_tournament(self):
        """
        Creates a new tournament from user data.
        """
        valid_data = False
        while not valid_data:
            raw_data = self.view.get_tournament_details()
            name = raw_data["name"].strip().capitalize()
            location = raw_data["location"].strip()
            start_date = confirm_date_format(raw_data["start_date"])
            end_date = confirm_date_format(raw_data["end_date"])
            description = raw_data["description"].strip() or "Aucune description disponible."
            num_rounds = int(raw_data.get("num_rounds", 4))

            if all([name, location, start_date, end_date, description, num_rounds]):
                valid_data = True

            new_tournament = Tournament(
                name=name,
                location=location,
                start_date=start_date,
                end_date=end_date,
                description=description,
                num_rounds=num_rounds,
            )
            self.tournament_manager.tournaments.append(new_tournament)
            self.tournament_manager.save_all()

            if self.view.ask_to_register_candidates().lower() == "y":
                self.recruit_players(new_tournament)
            return self.tournament_menu()

    def manage_existing_tournament(self):
        """
        Allows user to manage an existing tournament (add players, start a round, etc.).
        """
        tournaments_to_manage = [t for t in self.tournament_manager.tournaments if t.is_holding or t.is_running]
        if not tournaments_to_manage:
            self.view.no_tournament_ready_msg()
            return self.tournament_menu()

        selected_tournament = self.view.select_tournament(tournaments_to_manage)
        if selected_tournament:
            return self.handle_game_menu(selected_tournament)
        return self.tournament_menu()

    def add_player(self):
        """
        Allows user to add one player to a selected tournament.
        """
        selected_tournament = self.view.select_tournament(self.tournament_manager.tournaments)
        if selected_tournament:
            self.recruit_players(selected_tournament)

    def list_tournaments(self):
        """
        Lists registered tournaments.
        """
        all_tournaments = self.tournament_manager.tournaments
        self.view.select_tournament(all_tournaments)
        return self.tournament_menu()

    def recruit_players(self, tournament):
        """
        Register players for a tournament.
        """
        unregistered_players = [p for p in self.players if p not in tournament.players]
        if not unregistered_players:
            self.view.no_players_on_file_msg()
            return self.tournament_menu()

        user_input = self.view.select_multiple_players(tournament, unregistered_players)
        if not user_input:
            return self.tournament_menu()

        user_input = user_input.strip().lower()
        if user_input == "r":
            return self.tournament_menu()
        selected_indices = [x.strip() for x in user_input.split(",") if x.strip()]
        for index_str in selected_indices:
            try:
                idx = int(index_str)
                new_player = unregistered_players.pop(idx - 1)
                tournament.players.append(new_player)
                self.tournament_manager.save_all()
            except (ValueError, IndexError):
                self.view.wrong_menu_input()
                return self.recruit_players(tournament)
        return self.tournament_menu()

    def handle_game_menu(self, tournament):
        """
        Manages the internal menu of a tournament.
        """
        game_menu_options = {
            "1": self.start_new_round,
            "2": self.close_current_round,
            "3": self.show_game_status,
            "R": self.return_to_main_menu,
        }

        selected = self.view.display_game_menu(tournament).strip().lower()
        if selected == "r":
            return self.tournament_menu()
        return game_menu_options.get(selected, self.view.wrong_menu_input())(tournament)

    def start_new_round(self, tournament):
        """
        Starts a new round in a tournament.
        """
        if not tournament.rounds[-1].is_finished:
            print(str(tournament.rounds[-1]))
            return self.handle_game_menu(tournament)
        elif tournament.current_round < tournament.num_rounds:
            new_round = tournament.start_new_round()
            self.view.show_round_pairs(new_round)
            self.tournament_manager.save_all()
        else:
            self.view.last_round_message()
        return self.handle_game_menu(tournament)

    def close_current_round(self, tournament):
        """
        Closes the current round.
        """
        if int(tournament.current_round) == int(tournament.num_rounds):
            return self.close_last_round(tournament)

        closing_round = tournament.rounds[-1]
        closing_round.end_time = datetime.now().strftime("%x - %X")
        self.enter_match_results(closing_round)

        tournament.rank_players()
        self.tournament_manager.save_all()
        return self.handle_game_menu(tournament)

    def close_last_round(self, tournament):
        """
        Closes the last round and displays the final results.
        """
        last_round = tournament.rounds[-1]
        if not last_round.matches:
            self.view.no_round_running_msg()
            return self.handle_game_menu(tournament)

        self.view.show_closing_message(tournament)
        last_round.end_time = datetime.now().strftime("%x - %X")
        self.enter_match_results(last_round)

        tournament.set_final_rankings()
        self.view.display_tournament_results(tournament)
        self.tournament_manager.save_all()
        return self.tournament_menu()

    def show_game_status(self, tournament):
        """
        Displays the current status of a tournament.
        """
        ranked_players = tournament.rank_players()
        self.view.display_tournament_summary(tournament, ranked_players)
        return self.handle_game_menu(tournament)

    def enter_match_results(self, closing_round):
        """
        Manages the entry of match scores.
        """
        for match in closing_round.matches:
            if not match.is_over:
                match_scores = self.view.get_match_results(closing_round, match)
                self.update_match_scores(match, match_scores)
        self.view.complete_round_msg(closing_round)
        self.tournament_manager.save_all()

    @staticmethod
    def update_match_scores(match, scores):
        """
        Updates the scores for a given match.
        """
        if scores == "1":
            match.player1.points += 1
            match.set_score_and_lock(1, 0)
        elif scores == "2":
            match.player2.points += 1
            match.set_score_and_lock(0, 1)
        elif scores == "3":
            match.player1.points += 0.5
            match.player2.points += 0.5
            match.set_score_and_lock(0.5, 0.5)

    @staticmethod
    def return_to_main_menu():
        """
        Back to the main menu.
        """
        return None
