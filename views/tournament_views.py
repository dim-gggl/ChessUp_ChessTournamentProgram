from utils.ansify import ansify
from views.player_views import PlayerView


class TournamentView:
    """Displays the tournament menu, submenus and messages."""

    @staticmethod
    def clear_screen():
        print("\n" * 100)

    @staticmethod
    def header(prompt):
        print(ansify(f"\n\n      ~~~~~~~~~  b_blue({prompt})  ~~~~~~~~~\n\n"))

    @staticmethod
    def display_tournament_main_menu():
        """Displays the tournaments' main menu."""
        TournamentView().clear_screen()
        TournamentView().header("MENU TOURNOIS")
        print(
            ansify(
                "\n      b_blue(1.) Créer un nouveau tournoi"
                "\n      b_blue(2.) Gérer un tournoi"
                "\n      b_blue(3.) Ajouter un joueur à un tournoi"
                "\n      b_blue(4.) Consulter la liste des tournois\n\n"
                "\n\n       ch_up(R. Retour)\n"
            )
        )
        return input(ansify("\n      bld(Choisissez une option :) "))

    @staticmethod
    def get_tournament_name():
        """Gather the details of a new tournament."""
        TournamentView().clear_screen()
        TournamentView().header("NOUVEAU TOURNOI")
        return input(ansify("\n\n\n\n      bld(Nom du tournoi) : "))

    @staticmethod
    def get_tournament_location():
        return input(ansify("      bld(Lieu) : "))

    @staticmethod
    def get_tournament_description():
        return input(ansify("      bld(Description) : "))

    @staticmethod
    def get_tournament_date(prompt):
        """
        Takes a prompt to distinguish between start and end date.
        For example: "DD/MM/YYYY (start)" or "DD/MM/YYYY (end)".
        """
        return input(ansify(f"      bld(Date {prompt}) : "))

    @staticmethod
    def get_tournament_num_rounds():
        return input(ansify("      bld(Nombre de Rounds, par défaut 4) : "))

    @staticmethod
    def ask_to_register_candidates():
        TournamentView().clear_screen()
        print(
            ansify(
                "\n      ~~~~~~~  b_blue(Tournoi enregistré avec succès !)  ~~~~~~~\n"
                "      Souhaitez-vous inscrire des joueurs ? (y/n)\n\n\n"
            )
        )
        return input(ansify("      bld(Entrez votre choix :) "))

    @staticmethod
    def display_tournament_list(tournaments=None, select_option=True):
        """Ask the user to pick a tournament from the list."""
        if not tournaments:
            TournamentView().clear_screen()
            print(ansify("              red_err([ERREUR]) \n" "         Aucun tournoi enregistré.\n\n\n"))
            input("      Appuyez sur ENTRÉE pour continuer")
            return None

        TournamentView().clear_screen()
        TournamentView().header("LISTE DES TOURNOIS")
        for i, tournament in enumerate(tournaments, start=1):
            print(ansify(f"    b_blue({i}.)" + str(tournament)))
        if select_option:
            print(ansify("\n      ch_up(R. Retour)\n"))
            return input(ansify("      bld(Entrez le numéro du tournoi :) "))

        input("      Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def invalid_selection():
        print(ansify("          red_err([ERREUR]) \n" "        Sélection invalide.\n"))
        input("      Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def wrong_number():
        PlayerView.clean_screen()
        print(ansify("          red_err([ERREUR]) \n" "        Sélection invalide.\n"))
        input("      Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def select_multiple_players(tournament, unregistered_players):
        """
        Displays the list of players not yet registered for the tournament
        and allows the user to select several players
        using hints separated by commas.
        """
        TournamentView().clear_screen()
        TournamentView().header("Inscription de joueurs")
        print(
            ansify(
                f"\n      bld(Nom du tournoi :) whte({tournament.name})\n\n"
                "      Joueurs disponibles :\n"
            )
        )
        for idx, player in enumerate(unregistered_players, start=1):
            print(
                ansify(
                    f"      b_blue({idx}.) bld({player.last_name.upper()}) {player.first_name} (bld(ID): {player.chess_id})"
                )
            )

        print(ansify("\n      bld(Entrez les numéros séparés par des virgules, ou tapez 'r' pour annuler.)\n"))
        return input(ansify("      bld(Choisissez des joueurs (ex: 1,2,3) :) "))

    @staticmethod
    def registration_succeed():
        PlayerView.clean_screen()
        print(ansify("            gld([INSCRIPTION(S) ENREGISTRÉ(S)])\n\n\n"))
        input("      Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def display_game_menu(tournament):
        """
        Displays the management menu for a specific tournament.
        """
        TournamentView().clear_screen()
        TournamentView().header("GESTION DE TOURNOI")
        print(
            ansify(
                f"             b_blue({tournament.name})\n\n"
                f"      b_blue(1.) Démarrer un nouveau round (b_blue({tournament.current_round})/{tournament.num_rounds})\n"
                f"      b_blue(2.) Entrer les scores des joueurs (clôturer le round en cours)\n"
                f"      b_blue(3.) Consulter les détails du tournoi\n\n\n"
                f"        ch_up(R. Retour)\n\n"
            )
        )
        return input(ansify("      bld(Entrez une option :) ")).strip()

    @staticmethod
    def show_round_pairs(tournament_round):
        """
        Displays the pairings for a round.
        """
        TournamentView().clear_screen()
        TournamentView().header(tournament_round.name)
        print(
            ansify(
                "         Appariements des joueurs :\n"
            )
        )
        for i, match in enumerate(tournament_round.matches, start=1):
            print(ansify(f"      b_blue(Match {i} :) {match.player1.name} ch_up(vs) {match.player2.name}"))
        input(ansify("\n\n\n      ch_up(Appuyez sur Entrée pour continuer.)"))

    @staticmethod
    def display_tournament_summary(tournament, players):
        """
        Displays a summary of the tournament.
        """
        TournamentView().clear_screen()
        TournamentView().header("RÉCAPITULATIF DU TOURNOI")
        print(
            ansify(
                f"      {str(tournament)}"
                f"      bld(Lieu) : {tournament.location}\n"
                f"      bld(Dates) : {tournament.start_date} à {tournament.end_date}\n"
                f"      bld(Description) : {tournament.description}\n"
            )
        )
        print(ansify("        ~~~~~  b_blue(Joueurs inscrits)  ~~~~~ \n"))
        for idx, player in enumerate(players, start=1):
            print(
                ansify(
                    f"      b_blue({idx}.) bld({player.last_name.upper()}), {player.first_name} (bld(ID) : {player.chess_id}) - "
                    f"bld(Points) : {player.points}"
                )
            )
        input(ansify("\n      bld(Appuyez sur Entrée pour continuer.)"))

    @staticmethod
    def show_tournament_players(tournament):
        """
        Displays the list of players in the tournament (with names, points, etc.).
        """
        tournament_players = sorted(tournament.players, key=lambda pl: (pl.last_name, pl.first_name))
        TournamentView().clear_screen()
        print(
            ansify(
                f"\n      bld_it(~~~~~~) ttl_blu(Joueurs du tournoi :) \n\n\n"
                f"      bld_it(~~~~~~) whte({tournament.name})\n\n"
            )
        )
        if not tournament_players:
            print(ansify("           ch_up([INFO]) \n      disc_b_blue(Aucun joueur dans ce tournoi.)"))
            input("Appuyez sur ENTRÉE pour continuer")
            return

        for p in tournament_players:
            print(
                ansify(
                    f"      b_blue({p.last_name.upper()},) {p.first_name} "
                    f"(b_blue(ID: {p.chess_id},) Points: {p.points})"
                )
            )
        input("Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def get_match_results(closing_round, match):
        """
        Displays a prompt to enter the match result (1, 2 or 3 for a draw).
        """
        TournamentView().clear_screen()
        TournamentView().header(closing_round.name)
        print(
            ansify(
                "                it_b_blue(Qui a gagné ?) \n"
                "\n"
                f"            {match.player1.name} ch_up(vs) {match.player2.name} \n\n\n"
                f"      b_blue(1.) whte({match.player1.name}) a gagné gldn(?)\n"
                f"      b_blue(2.) whte({match.player2.name}) a gagné gldn(?)\n"
                f"      b_blue(3.) cppr(Ou match nul ?)\n\n\n"
            )
        )
        return input("\nChoisissez une option : ")

    @staticmethod
    def display_tournament_results(tournament):
        """
        Displays the final results of the tournament (rankings).
        """
        TournamentView().clear_screen()
        TournamentView().header("RÉSULTATS DU TOURNOI")
        print(
            ansify(
                f"                cppr({tournament.name})\n"
                f"      whte(Lieu :) cppr({tournament.location})\n"
            )
        )
        return TournamentView.show_rankings(tournament)

    @staticmethod
    def show_rankings(tournament):
        """
        Displays the final ranking of a tournament.
        """
        print(ansify("\n      ~~~~~~~~~  gldn(✧ * ✧ Classement ✧ * ✧)  ~~~~~~~~~\n"))
        for i, rank_str in enumerate(tournament.rankings, start=1):
            print(ansify(f"      {rank_str}"))
        input(ansify("\n      ch_up(Appuyez sur Entrée pour continuer.)"))

    @staticmethod
    def show_closing_message(tournament):
        """
        Displays a message before the tournament closes.
        """
        TournamentView().clear_screen()
        print(
            ansify(
                f"      ~~~~~~~~~ ch_up(⏐ 𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎ ⏐) ~~~~~~~~~~\n\n"
                f"      ~~~~~~~~~ gld({tournament.name}) ~~~~~~~~~~~~\n\n"
                "                  ch_up(~    [INFO]    ~)\n"
                "            bld_it(Derniers scores à renseigner avant\n"
                "            l'affichage du classement. )\n"
            )
        )
        input("Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def success_match_entry():
        """
        Displays a confirmation message after a score has been recorded.
        """
        TournamentView.clear_screen()
        print(ansify("\n\n\n\n~~~~~~~~~ b_blue(SCORE ENREGISTRÉ) ~~~~~~~~~~~~\n\n"))
        input("Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def no_tournament_ready_msg():
        """
        Displays an error message if there are no tournaments ready to be managed.
        """
        TournamentView.clear_screen()
        print(ansify("\n\n\n      red_err([ERREUR]) Aucun tournoi en cours\n\n\n"))
        print(
            ansify(
                "\n      disc_it(Ici, s'afficheront les tournois à gérer"
                "\n       — qui ont suffisamment de joueurs inscrits ou"
                "\n      qui ont déjà commencé )\n\n"
            )
        )
        input("Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def no_players_on_file_msg():
        """
        Message if no player is available for registration.
        """
        TournamentView.clear_screen()
        print(
            ansify(
                "\n\n      ch_up([INFO])  Il n'y pas de joueur disponible dans le fichier. \n"
                "\n\n      Rendez-vous dans le menu JOUEURS, "
                "\n      pour en ajouter de nouveaux.\n\n "
            )
        )
        input("Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def no_tournament_on_file_msg():
        """
        Message if no tournament is registered in the JSON file.
        """
        TournamentView.clear_screen()
        print(
            ansify(
                "\n\n      ch_up([INFO])\n  "
                "      Il n'y pas de tournoi dans le fichier. \n"
                "\n\n "
            )
        )
        input("Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def complete_round_msg(closing_round):
        """
        Message indicating that a round has been closed.
        """
        TournamentView.clear_screen()
        print(
            ansify(
                f"\n      ~~~~~~~~~ ch_up({closing_round.name} CLÔTURÉ) ~~~~~~~~~\n"
                f"\n\n      ~~~~~~~~~ ch_up({closing_round.end_time}) ~~~~~~~~~\n\n\n"
            )
        )
        input("Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def no_round_running_msg():
        """
        Error message if no round is in progress.
        """
        TournamentView.clear_screen()
        print(ansify("\n\n\nred_err([ERREUR]) Aucun round en cours"))
        input("Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def last_round_message():
        """
        Message indicating that the current round is the last.
        """
        TournamentView.clear_screen()
        print(ansify("\n\n\n\n            ch_up([INFO]) \n" "         Ce round est le dernier\n\n\n"))
        input("Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def wrong_menu_input():
        """
        Invalid menu option error message.
        """
        TournamentView.clear_screen()
        print(ansify("\n\n\n\n            red_err([ERREUR]) \n" "          Saisie incorrecte\n\n\n"))
        input("Appuyez sur ENTRÉE pour continuer")
