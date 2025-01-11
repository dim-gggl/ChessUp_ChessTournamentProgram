class TournamentView:

    @staticmethod
    def display_tournament_main_menu():
        print("\n" * 100)
        print("\n\n~~~~~~~~~~~~~~~  \033[1;96mMENU TOURNOIS\033[0m  ~~~~~~~~~~~~~~~\n")
        print("\n\033[1;96m𝟭.\033[0m Créer un nouveau tournoi")
        print("\033[1;96m𝟮.\033[0m Gérer un tournoi")
        print("\033[1;96m𝟯.\033[0m Ajouter des joueurs à un tournoi")
        print("\n")
        print("\n\033[1;91m𝟬. Retour\033[0m")
        return input("\nChoisissez une option : ").strip()

    @staticmethod
    def get_tournament_details():
        print("\n" * 100)
        print("\n\n\n~~~~~~~~~~~~~  \033[1;96mNOUVEAU TOURNOI\033[0m  ~~~~~~~~~~~~~\n")
        name = input("\n\n\n\033[1mNom : \033[0m").strip()
        location = input("\033[1mLieu : \033[0m").strip()
        start_date = input("\033[1mDate de début (JJ/MM/AAAA) : \033[0m").strip()
        end_date = input("\033[1mDate de fin (JJ/MM/AAAA) : \033[0m").strip()
        description = input("\033[1mDescription : \033[0m").strip()
        num_rounds = int(input("\033[1mNombre de Rounds \033[0m(4 par défaut) : ").strip() or 4)
        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
            "num_rounds": num_rounds
        }

    @staticmethod
    def select_tournament(tournaments=None):
        print("\n" * 100)
        print("\n\n\n      —————————\033[1;96m  Liste des Tournois\033[0m  —————————\n\n")
        if not tournaments:
            print("Aucun tournoi n'est encore enregistré !")
            return None
        else:
            for i, tournament in enumerate(tournaments):
                print(f"\033[1;96m{i + 1}.\033[0m\033[1;97m {tournament.name}\033[0m - "
                      f"({tournament.start_date}) - ({tournament.end_date})"
                      f"\033[2;3;96m ({len(tournament.players)} joueurs inscrits)\033[0m Rounds: {tournament.current_round}/{tournament.num_rounds}")
            valid = False
            while not valid:
                choice_index = input("\n\nFaîtes votre choix : ").strip()
                try:
                    idx = int(choice_index)
                except ValueError:
                    print("[ERREUR] Merci de saisir un nombre valide.")
                    continue

                if 1 <= idx <= len(tournaments):
                    valid = True
                    return tournaments[idx - 1]
                else:
                    print(f"[ERREUR] Le numéro doit être entre 1 et {len(tournaments)}.")

    @staticmethod
    def display_game_menu(tournament):
            print("\n" * 100)
            print("\n\n\n~~~~~~~~~~~~~  \033[1;96m GESTION DE TOURNOI\033[0m  ~~~~~~~~~~~~~\n")
            print(f"\033[1mNom du tournoi :\033[96m {tournament.name}\033[0m")
            print(f"\n\033[1;96m𝟭.\033[0m Lancer un nouveau round ({tournament.current_round}/{tournament.num_rounds})")
            print("\033[1;96m𝟮.\033[0m Entrer les scores des joueurs \033[38;5;243m(Clôture du round en cours)\033[0m")
            print("\033[1;96m𝟯.\033[0m Voir les détails du tournoi")
            print("\n\033[1;91m𝟬. Quitter la gestion du tournoi\033[0m")
            return input(f"\nEntrez votre choix : ").strip()

    @staticmethod
    def show_round_pairs(tournament_round):
            print("\n" * 100)
            print(f"\n\n\n~~~~~~~~~~~~~  \033[1;96m {tournament_round.name}\033[0m  ~~~~~~~~~~~~~")
            for i, match in enumerate(tournament_round.matches):
                print(f"\n                \033[1;96m Match {i +1} \033[0m    \n" + str(match))
            input()

    @staticmethod
    def display_tournament_summary(tournament, players=None):
        print("\n" * 100)
        print("\n\n\n~~~~~~~~~~~~~~~  \033[1;96mDÉTAILS DU TOURNOI\033[0m  ~~~~~~~~~~~~~~~")
        print(f"\033[1mNom du tournoi :\033[96m {tournament.name}\033[0m")
        print(f"\033[1mLieu :\033[0m {tournament.location}")
        print(f"\033[1mDates :\033[0m {tournament.start_date} - {tournament.end_date}")
        print(f"\033[1mDescription :\033[0m {tournament.description}")
        print(f"\033[1mRound actuel :\033[0m {tournament.current_round}/{tournament.num_rounds}")

        if not tournament.rankings:
            print("~~~~~~~~~~~~~~~ \033[1;93m✧ * ✧ Candidats ✧ * ✧\033[0m ~~~~~~~~~~~~~~~")
            print("\n\033[38;5;243m Classement Provisoire \033[0m")
            for i, player in enumerate(players):
                print(f" \033[1;93m{i + 1}\033[0m ~~ {player.last_name}, {player.first_name} (ID: {player.chess_id}, Points: {player.points})")
            input()
            return
        else:
            TournamentView.show_rankings(tournament)
            return

    @staticmethod
    def select_player(tournament, players):
        print("\n" * 100)
        print("\n\n\n      ~~~~~~~~~~    \033[1;96mJOUEURS INSCRITS\033[0m  ~~~~~~~~~~~\n")
        print(f"\033[1mNom du tournoi :\033[96m {tournament.name}\033[0m")
        print("\n\033[1mChoisissez un joueur :\033[0m")
        for i, player in enumerate(players):
            print(f"\033[1;96m{i + 1}.\033[0m {player.name} ({player.chess_id})\033[0m")
        choice_index = input("\n\n\033[1mEntrez votre choix :\033[0m ").strip()
        return players[int(choice_index) - 1]

    @staticmethod
    def show_tournament_players(tournament):
        tournament_players = sorted(tournament.players, key=lambda player: (player.last_name, player.first_name))
        print("\n" * 100)
        print(f"\n      ~~~~~~    \033[1;94m Joueurs du tournoi :\033[0m \n\n\n"
                f"\n      ~~~~~~    \033[1;97m{tournament.name}\033[0m\n\n")

        if not tournament_players:
            print("\033[94m[INFO]\033[0m\033[2;3m Aucun joueur dans ce tournoi.\033[0m")
            input()

        for player in tournament_players:
            print(f"\033[1;94m{player.last_name.upper()}\033[0m, {player.first_name} "
                    f"(\033[1;94mID: {player.chess_id}\033[0m, Points: {player.points})")
            input()
            return

    @staticmethod
    def get_match_scores(closing_round, match):
        print("\n" * 100)
        print(f"\n\n\n      ~~~~~~~~~~  \033[1;96m{closing_round.name}\033[0m  ~~~~~~~~~~")
        print("~~~~~~~~~~~~~~  \033[1;3;96m Qui a gagné ?\033[0m  ~~~~~~~~~~~~~~")
        print(f"           ~~~~~  \033[1;96m[Match]\033[0m ~~~~\n   "
              f"   ~~~~  {match.player1.name} \033[1;96mvs\033[0m {match.player2.name}  ~~~~~")
        print(f"\n\033[1;96m𝟭. \033[0m {match.player1.name} ~ {match.player1.chess_id} ?")
        print(f"\033[1;96m𝟮. \033[0m {match.player2.name} ~ {match.player2.chess_id} ?")
        print(f"\033[1;96m𝟯. \033[0m Match nul ?\n")
        print("\n\033[0m")
        return input("\nChoisissez une option : ").strip()

    @staticmethod
    def display_tournament_results(tournament):
        print("\n" * 100)
        print("\n\n\n~~~~~~~~~~~~~~~  \033[1;96mRÉSULTATS DU TOURNOI\033[0m  ~~~~~~~~~~~~~~~")
        print(f"\033[1m {tournament.name}\033[0m")
        print(f"\033[1mLieu :\033[0m {tournament.location}")
        return self.show_rankings(tournament)

    @staticmethod
    def show_rankings(tournament):
        print("~~~~~~~~~~~~~~~ \033[1;93m✧ * ✧ Classement ✧ * ✧\033[0m ~~~~~~~~~~~~~~~")
        for i, ranking in enumerate(tournament.rankings):
            print(ranking)
        input()
        return

    @staticmethod
    def show_closing_message(tournament):
        print("\n" * 100)
        print("      ~~~~~~~~~ \033[1;38;5;202m⏐ 𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎ ⏐\033[0m ~~~~~~~~~~\n\n")
        print(f"\n      ~~~~~~~~~ \033[1;38;5;202m{tournament.name}\033[0m ~~~~~~~~~~~~\n\n")
        print(f"\n\033[1;96m           ~    [INFO]    ~\033[0m")
        print("\n\033[2;3m      Derniers scores à renseigner avant"
              "\n      l'affichage du classement. \033[0m")
        print("\n")
        input()

    @staticmethod
    def success_match_entry():
        print("\n" * 100)
        print("\n\n\n\n~~~~~~~~~ SCORE ENREGISTRÉ ~~~~~~~~~~~~\n\n")
        input()

    @staticmethod
    def complete_round_msg(closing_round):
        print("\n" * 100)
        print(f"\n\n\n\n~~~~~~~~~ \033[1;38;5;202m{closing_round} CLÔTURÉ\033[0m ~~~~~~~~~~~~\n")
        print(f"\n~~~~~~~~~ \033[1;38;5;202m{closing_round.end_time}\033[0m ~~~~~~~~~~~~\n")
        input()

    @staticmethod
    def no_round_running_msg():
        print("\n" * 100)
        print("\n\n\n\n\033[1;91m[ERREUR]\033[0m Aucun round en cours")
        input()

    @staticmethod
    def last_round_message():
        print("\n" * 100)
        print("\n\n\n\n\033[1;38;5;202m[INFO]\033[0m Ce round est le dernier\n")
        input()

    @staticmethod
    def wrong_menu_input():
        print("\n\n\n\n\033[1;91m[ERREUR]\033[0m Saisie incorrecte")

    @staticmethod
    def bye_message():
        print("\n" * 100)
        print("\n\n\033[1m      ~~~~~~~~~ ]\033[1;38;5;202m * 𝐵𝑦𝑒 𝐵𝑦𝑒 * \033[1;0m[~~~~~~~\n\033[0m")
        print("      ~~~~~~~~~ \033[1;38;5;202m⏐ 𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎ ⏐\033[0m ~~~~~~~~~~\n\n")
        input()
