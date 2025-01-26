from utils.ansify import ansify
from views.player_views import PlayerView


class TournamentView:
    """Displays the tournament menu, submenus and messages."""

    @staticmethod
    def clear_screen():
        print("\n" * 100)

    @staticmethod
    def header(prompt):
        print(ansify(f"\n\n\t~~~~~~~~~  b_blue({prompt})  ~~~~~~~~~\n\n"))

    @staticmethod
    def display_tournament_main_menu():
        """Displays the tournaments' main menu."""
        TournamentView().clear_screen()
        TournamentView().header("MENU TOURNOIS")
        print(
            ansify(
                "\n\tb_blue(1.) Créer un nouveau tournoi"
                "\n\tb_blue(2.) Gérer un tournoi"
                "\n\tb_blue(3.) Ajouter un joueur à un tournoi"
                "\n\tb_blue(4.) Consulter la liste des tournois\n\n"
                "\n\n\tch_up(R. Retour)\n"
            )
        )
        return input(ansify("\n\tbld(Choisissez une option :) "))

    @staticmethod
    def get_tournament_name():
        """Gather the details of a new tournament."""
        TournamentView().clear_screen()
        TournamentView().header("NOUVEAU TOURNOI")
        return input(ansify("\n\n\n\n\tbld(Nom du tournoi) : "))

    @staticmethod
    def get_tournament_location():
        return input(ansify("\tbld(Lieu) : "))

    @staticmethod
    def get_tournament_description():
        return input(ansify("\tbld(Description) : "))

    @staticmethod
    def get_tournament_date(prompt):
        """
        Takes a prompt to distinguish between start and end date.
        For example: "DD/MM/YYYY (start)" or "DD/MM/YYYY (end)".
        """
        return input(ansify(f"\tbld(Date {prompt}) : "))

    @staticmethod
    def get_tournament_num_rounds():
        return input(ansify("\tbld(Nombre de Rounds, par défaut 4) : "))

    @staticmethod
    def ask_to_register_candidates():
        TournamentView().clear_screen()
        print(
            ansify(
                "\n\t~~~~~~~  b_blue(Tournoi enregistré avec succès !)  ~~~~~~~\n"
                "\tSouhaitez-vous inscrire des joueurs ? (y/n)\n\n\n"
            )
        )
        return input(ansify("\tbld(Entrez votre choix :) "))

    @staticmethod
    def display_tournament_list(tournaments=None, select_option=True):
        """Ask the user to pick a tournament from the list."""
        if not tournaments:
            TournamentView().clear_screen()
            print(ansify("\t\tred_err([ERREUR]) \n" "\tAucun tournoi enregistré.\n\n\n"))
            input("\tAppuyez sur ENTRÉE pour continuer")
            return None

        TournamentView().clear_screen()
        TournamentView().header("LISTE DES TOURNOIS")
        for i, tournament in enumerate(tournaments, start=1):
            print(ansify(f"whte({i}.)" + str(tournament)))
        if select_option:
            print(ansify("\n\tch_up(R. Retour)\n"))
            return input(ansify("\tbld(Entrez le numéro du tournoi :) "))
        else:
            input()

        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def no_open_round_msg():
        TournamentView.clear_screen()
        print(ansify("\n\t\tred_err([INFO])\n\tIl n'y a pas encore de round à clôturer\n"))
        input("\n\n\tAppuyer sur ENTRÉE pour continuer")

    @staticmethod
    def invalid_selection():
        print(ansify("\n\t\tred_err([ERREUR])\n\tSélection invalide.\n"))
        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def wrong_number():
        PlayerView.clean_screen()
        print(ansify("\t\tred_err([ERREUR])\n\tSélection invalide.\n"))
        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def wrong_match_score():
        print(ansify("\t\tred_err([ERREUR])\n\tChoix incorrect. Réponses valides : 1, 2 ou 3"))
        input()

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
                f"\n\t\twhte({tournament.name})\n\n"
                "\t\tJoueurs disponibles :\n"
            )
        )
        for idx, player in enumerate(unregistered_players, start=1):
            print(
                ansify(
                    f"b_blue({idx}.) b_blue({player.last_name.upper()}) "
                    f"{player.first_name}  \t  \tb_blue(ID): whte({player.chess_id})"
                )
            )

        print(ansify("\n\tbld(Entrez les numéros séparés par des virgules, ou tapez 'r' pour annuler.)\n"))
        return input(ansify("\tbld(Choisissez des joueurs [ex: 1,2,3] :) "))

    @staticmethod
    def registration_succeed():
        PlayerView.clean_screen()
        print(ansify("\tgld([INSCRIPTIONS ENREGISTRÉES])\n\n\n"))
        input("\n\n\n\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def display_game_menu(tournament):
        """
        Displays the management menu for a specific tournament.
        """
        TournamentView().clear_screen()
        TournamentView().header("GESTION DE TOURNOI")
        print(
            ansify(
                f"\t\tb_blue({tournament.name})\n\n"
                f"\tb_blue(1.) Démarrer un nouveau round "
                f"(b_blue({tournament.current_round})/{tournament.num_rounds})\n"
                f"\tb_blue(2.) Entrer les scores des joueurs (clôturer le round en cours)\n"
                f"\tb_blue(3.) Consulter les détails du tournoi\n\n\n"
                f"\tch_up(R. Retour)\n\n"
            )
        )
        return input(ansify("\tbld(Entrez une option :) ")).strip()

    @staticmethod
    def show_round_pairs(tournament_round):
        """
        Displays the pairings for a round.
        """
        TournamentView().clear_screen()
        TournamentView().header(tournament_round.name)
        print(
            ansify(
                "\t\twhte(Appariements des joueurs) \n"
            )
        )
        for i, match in enumerate(tournament_round.matches, start=1):
            print(ansify(f"\t\t     b_blue(Match {i})\nwhte({match.player1.name})"
                         f" \t  \tch_up(  vs  )\t\twhte({match.player2.name})\n"))
        input(ansify("\n\tch_up(Appuyez sur Entrée pour continuer.)"))

    @staticmethod
    def display_tournament_summary(tournament, players):
        """
        Displays a summary of the tournament.
        """
        TournamentView().clear_screen()
        TournamentView().header("RÉCAPITULATIF DU TOURNOI")
        print(
            ansify(
                f"{str(tournament)}\n"
                f"\tit_b_blue({tournament.start_date} ~ {tournament.end_date})\n"
                f"\tit_whte({tournament.description})\n"
            )
        )
        print(ansify("\t~~~~~  b_blue(Participant.e.s)  ~~~~~ "))
        for idx, player in enumerate(players, start=1):
            print(
                ansify(
                    f"b_blue(|)  whte({player.last_name.upper()}), {player.first_name}    "
                    f" \t \t b_blue(Points) : gldn({player.points}) b_blue(|)"
                )
            )
        input(ansify("\n\tbld(Appuyez sur Entrée pour continuer.)"))

    @staticmethod
    def show_tournament_players(tournament):
        """
        Displays the list of players in the tournament (with names, points, etc.).
        """
        tournament_players = sorted(tournament.players, key=lambda pl: (pl.last_name, pl.first_name))
        TournamentView().clear_screen()
        print(
            ansify(
                f"\n\t\tttl_blu(Joueurs du tournoi) \n\n\n"
                f"\t\t whte({tournament.name})\n\n"
            )
        )
        if not tournament_players:
            print(ansify("\t\tch_up([INFO]) \n\tdisc_b_blue(Aucun joueur dans ce tournoi.)"))
            input("\tAppuyez sur ENTRÉE pour continuer")
            return

        for p in tournament_players:
            print(
                ansify(
                    f"\tb_blue({p.last_name.upper()},) {p.first_name} "
                    f"b_blue(ID: {p.chess_id}) \tPoints: gldn({p.points})"
                )
            )
        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def get_match_results(closing_round, match):
        """
        Displays a prompt to enter the match result (1, 2 or 3 for a draw).
        """
        TournamentView().clear_screen()
        TournamentView().header(closing_round.name)
        print(
            ansify(
                "\t      whte(Qui a gagné ?)\n\n"
                f"whte({match.player1.name.upper()}) \t  "
                f"\tch_up( vs )\t\twhte({match.player2.name.upper()}) \n\n"
                f"\tb_blue(1.) whte({match.player1.name.upper()}) a gagné gldn(?)\n"
                f"\tb_blue(2.) whte({match.player2.name.upper()}) a gagné gldn(?)\n"
                f"\n\tb_blue(3.) Ou... ch_up(match nul) ?\n"
            )
        )
        return input("\n\tChoisissez une option : ")

    @staticmethod
    def display_tournament_results(tournament):
        """
        Displays the final results of the tournament (rankings).
        """
        TournamentView().clear_screen()
        TournamentView().header("RÉSULTATS DU TOURNOI")
        print(
            ansify(
                f"\tcppr({tournament.name})\n"
                f"\tcppr({tournament.location})\n"
            )
        )
        return TournamentView.show_rankings(tournament)

    @staticmethod
    def show_rankings(tournament):
        """
        Displays the final ranking of a tournament.
        """
        print(ansify("\n\t~~~~~~~~~ gldn(✧ * ✧ Classement ✧ * ✧)  ~~~~~~~~~\n"))
        for i, rank_str in enumerate(tournament.rankings, start=1):
            print(ansify(f"\t{rank_str}"))
        input(ansify("\n\tch_up(Appuyez sur Entrée pour continuer.)"))

    @staticmethod
    def show_closing_message(tournament):
        """
        Displays a message before the tournament closes.
        """
        TournamentView().clear_screen()
        print(
            ansify(
                f"\t\t\tch_up(⏐ 𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎ ⏐)\n\n"
                f"\t\twhte({tournament.name})\n\n"
                "\t\t\tch_up(~[INFO]~)\n"
                "\t\twhte(Derniers scores à renseigner avant\n"
                "\t\tl'affichage du classement. )\n"
            )
        )
        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def no_tournament_ready_msg():
        """
        Displays an error message if there are no tournaments ready to be managed.
        """
        TournamentView.clear_screen()
        print(ansify("\n\n\n\t\t\tred_err([ERREUR])\n\t\t Aucun tournoi en cours\n\n\n"))
        print(
            ansify(
                "\n\t\tIci, s'afficheront les tournois à gérer"
                "\n\t\t— qui ont suffisamment de joueurs inscrits ou"
                "\n\t\tqui ont déjà commencé\n\n"
            )
        )
        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def no_players_on_file_msg():
        """
        Message if no player is available for registration.
        """
        TournamentView.clear_screen()
        print(
            ansify(
                "\n\n\t\t\tch_up([INFO])\n\t\tIl n'y pas de joueur disponible dans le fichier. \n"
                "\n\n\tRendez-vous dans le menu JOUEURS, "
                "\n\tpour en ajouter de nouveaux.\n\n "
            )
        )
        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def no_tournament_on_file_msg():
        """
        Message if no tournament is registered in the JSON file.
        """
        TournamentView.clear_screen()
        print(
            ansify(
                "\n\n\t\t\tch_up([INFO])\n  "
                "\t\tIl n'y pas de tournoi dans le fichier. \n"
                "\n\n "
            )
        )
        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def complete_round_msg(closing_round):
        """
        Message indicating that a round has been closed.
        """
        TournamentView.clear_screen()
        print(
            ansify(
                f"\n\t\tch_up({closing_round.name} CLÔTURÉ)\n"
                f"\n\n\t\tch_up({closing_round.end_time})\n\n\n"
            )
        )
        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def last_round_message():
        """
        Message indicating that the current round is the last.
        """
        TournamentView.clear_screen()
        print(ansify("\n\n\n\n\t\t\tch_up([INFO]) \n" "\t\tCe round est le dernier\n\n\n"))
        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def wrong_menu_input():
        """
        Invalid menu option error message.
        """
        TournamentView.clear_screen()
        print(ansify("\n\n\n\n\t\t\tred_err([ERREUR]) \n" "\t\tSaisie incorrecte\n\n\n"))
        input("\tAppuyez sur ENTRÉE pour continuer")
