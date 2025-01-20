from datetime import datetime
from models.tournament import Tournament
from utils.sort_tournaments import sort_tournaments
from views.tournament_views import TournamentView
from utils.validators import confirm_date_format, confirm_name_format, confirm_location_format


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
        selected = ""
        while selected != "r":
            menu_options = {
                "1": self.create_new_tournament,
                "2": self.manage_existing_tournament,
                "3": self.pick_tournament_for_new_players,
                "4": self.list_tournaments
            }
            selected = self.view.display_tournament_main_menu().strip().lower()
            action = menu_options.get(selected)
            if action:
                action()
            else:
                self.view.wrong_menu_input()

    def create_new_tournament(self):
        """
        Creates a new tournament from user data.
        """
        tournament_data = {}

        name_input = self.view.get_tournament_name().strip()
        tournament_data["name"] = confirm_name_format(name_input, digits_ok=True).capitalize()

        location = self.view.get_tournament_location().strip()
        tournament_data["location"] = confirm_location_format(location)

        start_date = self.view.get_tournament_date("de début (JJ/MM/AAAA)").strip()
        tournament_data["start_date"] = confirm_date_format(start_date)
        end_date = self.view.get_tournament_date("de fin (JJ/MM/AAAA)").strip()
        tournament_data["end_date"] = confirm_date_format(end_date)

        description = self.view.get_tournament_description().strip()
        tournament_data["description"] = description if description else "Aucune description disponible"

        num_rounds = self.view.get_tournament_num_rounds().strip()
        try:
            tournament_data["num_rounds"] = int(num_rounds)
        except ValueError:
            tournament_data["num_rounds"] = 4

        new_tournament = Tournament(**tournament_data)
        self.tournament_manager.tournaments.append(new_tournament)
        self.tournament_manager.save_all()

        if self.view.ask_to_register_candidates().lower() == "y":
            self.recruit_players(new_tournament)
        return

    def manage_existing_tournament(self):
        """
        Allows user to manage an existing tournament (add players, start a round, etc.).
        """
        tournaments_to_manage = []
        for tournament in self.tournament_manager.tournaments:
            if tournament.is_holding or tournament.is_running:
                tournaments_to_manage.append(tournament)
        if not tournaments_to_manage:
            self.view.no_tournament_ready_msg()
            return

        choice_index = self.view.display_tournament_list(tournaments_to_manage, select_option=True).strip().lower()
        if choice_index == "r":
            return
        try:
            i = int(choice_index) - 1
            selected_tournament = tournaments_to_manage[i]
            return self.handle_game_menu(selected_tournament)
        except ValueError:
            self.view.wrong_number()

    def pick_tournament_for_new_players(self):
        """
        Allows user to add one player to a selected tournament.
        """
        available_tournaments = []
        for tournament in self.tournament_manager.tournaments:
            if tournament.current_round == 0:
                available_tournaments.append(tournament)
        if available_tournaments:
            sort_tournaments(available_tournaments)
            choice = self.view.display_tournament_list(available_tournaments, select_option=True).lower()
            if choice == "r":
                return

            try:
                i = int(choice) - 1
                if 0 <= i < len(available_tournaments):
                    self.recruit_players(available_tournaments[i])

                else:
                    self.view.invalid_selection()
            except ValueError:
                self.view.wrong_number()
            return


    def list_tournaments(self):
        """
        Lists registered tournaments.
        """
        all_tournaments = self.tournament_manager.tournaments
        if all_tournaments:
            sort_tournaments(all_tournaments)
            self.view.display_tournament_list(all_tournaments, select_option=False)
        else:
            self.view.no_tournament_on_file_msg()
        return

    def recruit_players(self, tournament):
        """
        Register players for a tournament.
        """
        unregistered_players = [p for p in self.players if p not in tournament.players]
        if not unregistered_players:
            self.view.no_players_on_file_msg()
            return

        user_input = self.view.select_multiple_players(tournament, unregistered_players)
        if not user_input:
            return

        user_input = user_input.strip().lower()
        if user_input == "r":
            return
        selected_indices = [x.strip() for x in user_input.split(",") if x.strip()]
        chosen_players = []
        for index_str in selected_indices:
            try:
                idx = int(index_str)
                chosen_players.append(unregistered_players[idx - 1])
            except (ValueError, IndexError):
                self.view.wrong_menu_input()
                return

        for player in chosen_players:
            if player not in tournament.players:
                tournament.players.append(player)

        self.view.registration_succeed()

        self.tournament_manager.save_all()
        return

    def handle_game_menu(self, tournament):
        """
        Manages the internal menu of a tournament.
        """
        selected = ""
        while selected != "r" and selected != "q":
            game_menu_options = {
                "1": lambda : self.start_new_round(tournament),
                "2": lambda : self.close_current_round(tournament),
                "3": lambda : self.show_game_status(tournament)
            }

            selected = self.view.display_game_menu(tournament).strip().lower()
            action = game_menu_options.get(selected)
            if action:
                action()
            else:
                self.view.wrong_menu_input()

    def start_new_round(self, tournament):
        """
        Starts a new round in a tournament.
        """
        if len(tournament.rounds) > 0 and not tournament.rounds[-1].is_finished:
            print(str(tournament.rounds[-1]))
            input("Appuyez sur ENTRÉE pour continnuer")
            return

        elif tournament.current_round < tournament.num_rounds:
            new_round = tournament.start_new_round()
            self.view.show_round_pairs(new_round)
            self.tournament_manager.save_all()

        else:
            self.view.last_round_message()
        return

    def close_current_round(self, tournament):
        """
        Closes the current round.
        """
        if tournament.current_round == tournament.num_rounds:
            return self.close_last_round(tournament)

        closing_round = tournament.rounds[-1]
        closing_round.end_time = datetime.now().strftime("%x - %X")
        self.enter_match_results(closing_round)

        tournament.rank_players()
        self.tournament_manager.save_all()
        return

    def close_last_round(self, tournament):
        """
        Closes the last round and displays the final results.
        """
        last_round = tournament.rounds[-1]
        if not last_round.matches:
            self.view.no_round_running_msg()
            return

        self.view.show_closing_message(tournament)
        last_round.end_time = datetime.now().strftime("%x - %X")
        self.enter_match_results(last_round)

        tournament.set_final_rankings()
        self.view.display_tournament_results(tournament)
        self.tournament_manager.save_all()
        return "r"

    def show_game_status(self, tournament):
        """
        Displays the current status of a tournament.
        """
        ranked_players = tournament.rank_players()
        self.view.display_tournament_summary(tournament, ranked_players)
        return

    def enter_match_results(self, closing_round):
        """
        Manages the entry of match scores.
        """
        for match in closing_round.matches:
            while not match.is_over:
                match_scores = self.view.get_match_results(closing_round, match).strip().lower()
                try:
                    1 <= int(match_scores) <=3
                    self.update_match_scores(match, match_scores)
                except ValueError:
                    self.view.wrong_number()
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
        return match

