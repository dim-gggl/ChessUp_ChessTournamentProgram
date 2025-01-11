class PlayerView:

    @staticmethod
    def display_players_menu():
        print("\n" * 100)
        print("~~~~~~~~~~~~~~~  \033[1;95mMENU JOUEURS\033[0m  ~~~~~~~~~~~~~~~\n\n\n")
        print("\033[1;95m𝟭.\033[0m Ajouter un nouveau joueur")
        print("\033[1;95m𝟮.\033[0m Modifier les infos d'un joueur")
        print("\033[1;95m𝟯.\033[0m Lister les joueurs\n\n")
        print("\n\033[1;38;5;202m𝟬. Retour au menu principal\033[0m")
        return input("\nChoisissez une option : ").strip()

    @staticmethod
    def get_player_data(edit=False, player=None):
        if not edit:
            print("\n" * 100)
            print("\n\n\n\n~~~~~~~~~~~~~  \033[1;95mNOUVEAU JOUEUR\033[0m  ~~~~~~~~~~~~~\n\n\n")
            first_name = input("\n\n\n\033[1mPrénom : \033[0m").strip()
            last_name = input("\033[1mNom de Famille : \033[0m").strip()
            birth_date = input("\033[1mDate de naissance (JJ/MM/AAAA) : \033[0m").strip()
            chess_id = input("\033[1mID : \033[0m").strip()
            print("\n" * 100)
            print("\n\n\n\n\n\n    ~~~~~~~ \033[1;95m Joueur enregistré \033[0m  ~~~~~~~~    \n")
            print("             ~~~~~~~~~~~~~~~~~\n\n\n\n\n")
            input()
            return {
                "first_name": first_name,
                "last_name": last_name,
                "birth_date": birth_date,
                "chess_id": chess_id
            }
        else:
            print("\n" * 100)
            print("\n\n\n\n~~~~~~~~~~~~~  \033[1;95mMODIFICATIONS DE JOUEUR\033[0m  ~~~~~~~~~~~~~\n\n")
            print(f"\033[1;96   [INFO]\033[0m Si aucune information n'est saisie, les données de\n"
                  f"{player.first_name} {player.last_name.upper()} resteront inchangées !")
            first_name = input("\n\n\033[1mPrénom : \033[0m" or player.first_name).strip()
            last_name = input("\033[1mNom de Famille : \033[0m" or player.last_name).strip()
            birth_date = input("\033[1mDate de naissance (JJ/MM/AAAA) : \033[0m" or player.birth_date).strip()
            chess_id = input("\033[1mID : \033[0m" or player.chess_id).strip()
            print("\n" * 100)
            print("\n\n\n\n\n\n~~~~~~~~~~~~ \033[1;95m Joueur enregistré \033[0m  ~~~~~~~~~~~~\n\n\n")
            input("\n")
            return {
                "first_name": first_name,
                "last_name": last_name,
                "birth_date": birth_date,
                "chess_id": chess_id
            }

    @staticmethod
    def select_player_to_edit(players):
        if not players:
            print("\n" * 100)
            print("\n\033[1;95m[INFO]\033[0m Aucun Joueurs enregistré !\n\n")
            input("\n")
        else:
            print("\n" * 100)
            print("\n\n\n~~~~~~~~~~~~~~~  \033[1;95mMODIFIER UN JOUEUR\033[0m  ~~~~~~~~~~~~~~~\n")
            print("\033[1mChoisissez un joueur :\033[0m")
            for i, player in enumerate(players):
                print(f"\033[1;95m{i + 1}.\033[0m {player.name} ({player.chess_id})\033[0m")

            choice_index = input("\n\n\033[1mEntrez votre choix :\033[0m ").strip()
            return players[int(choice_index) - 1]

    @staticmethod
    def modify_player(player):
        print("\n" * 100)
        print(f"\n~~~~~~~~~~~~~~~ \033[1;95m{player.name}\033[0m  ~~~~~~~~~~~~~~~\n")
        print(f"\n\n\n\033[1;95m𝟭.\033[0m Tout modifier")
        print("\033[1;95m𝟮.\033[0m Mettre à jour l'I.N.E")
        return input("\n\n\033[1mEntrez votre choix :\033[0m ").strip()

    @staticmethod
    def enter_chess_id(player):
        print("\n" * 100)
        print(f"\n~~~~~~~~~~~~~~~ \033[1;95m{player.name}\033[0m  ~~~~~~~~~~~~~~~\n")
        print(f"\nSaisissez l'Identifiant National d'Échecs de :\n")
        print(f"\033[2;3;95m ~ {player.first_name}\033[0m \033[1;95m{player.last_name.upper()} \033[0m")
        chess_id = input("\n\n\033[1mEntrez l'identifiant :\033[0m" or player.chess_id).strip()
        return chess_id

    @staticmethod
    def display_players(players):
        print("\n" * 100)
        print("\n\n\n~~~~~~~~~~~~~~~  \033[1;95mTOUS LES JOUEURS\033[0m  ~~~~~~~~~~~~~~~\n")
        for player in players:
            print(f" ~ \033[1;95m{player.last_name.upper()}\033[0m {player.first_name}"
                  f" (\033[1;3;35mID:\033[0m {player.chess_id}) ~ \033[1;3;35mNé(e) le:\033[0m {player.birth_date} ~ ")
        input()
        return
