from utils.ansify import ansify


class PlayerView:
    """Displays the players' menu and submenus."""

    @staticmethod
    def display_players_menu():
        """Displays the players' menu."""
        print("\n" * 100)
        print(ansify("      ~~~~~~~~~  pnk(MENU JOUEURS)  ~~~~~~~~\n\n\n"
              "      pnk(𝟭.) Ajouter un nouveau joueur\n"
              "      pnk(𝟮.) Modifier les infos d'un joueur\n"
              "      pnk(𝟯.) Lister les joueurs\n\n"
              "\n        ch_up(R. Retour )"))
        return input("\n      Choisissez une option : ")

    @staticmethod
    def get_player_data(edit=False, player=None):
        """Gather player data."""
        if not edit:
            print("\n" * 100)
            print(ansify("\n      ~~~~~~~  pnk(NOUVEAU JOUEUR)  ~~~~~~~\n\n\n"))
            first_name = input(ansify("\n\n\n      bld(Prénom) : "))
            last_name = input(ansify("      bld(Nom de Famille) : "))
            birth_date = input(ansify("      bld(Date de naissance) (JJ/MM/AAAA) : "))
            chess_id = input(ansify("      bld(ID) : "))
            print("\n" * 100)
            print(ansify("\n\n\n\n\n         ~~~~~~~~~~~~~~~~~"
                         "\n      ~~~~~~~  pnk(Joueur enregistré)  ~~~~~~~~    \n"
                         "         ~~~~~~~~~~~~~~~~~\n\n\n\n\n"))
            input()
        else:
            print("\n" * 100)
            print(ansify(f"\n\n      ~~~~~~~  pnk(MODIFICATION DE JOUEUR)  ~~~~~~~\n\n"
                         f"\n            pnk([INFO]) \n"
                         f"      Si aucune information n'est saisie, les données de\n"
                  f"      {player.first_name} pnk({player.last_name}) resteront inchangées !"))
            first_name = input(ansify("\n\n      pnk(Prénom) : "))
            last_name = input(ansify("      pnk(Nom de Famille) : "))
            birth_date = input(ansify("      pnk(Date de naissance) (JJ/MM/AAAA) : "))
            chess_id = input(ansify("      pnk(ID) : "))
            print("\n" * 100)
            print(ansify("\n\n\n\n\n                   ~~~~~~~~~~~~~~~~~"
                         "\n      ~~~~~~~  pnk(Joueur enregistré)  ~~~~~~~~    \n"
                         "                   ~~~~~~~~~~~~~~~~~\n\n\n\n\n"))
            input()
        return {
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date,
            "chess_id": chess_id
        }

    @staticmethod
    def select_player_to_edit(players):
        """Displays the players' list and returns the selected player's index."""
        if not players:
            print("\n" * 100)
            print(ansify("\n            ch_up([INFO])\n"
                  "      Aucun Joueurs enregistré !\n\n"))
            input("\n")
        else:
            print("\n" * 100)
            print(ansify("\n\n\n      ~~~~~~~~~  pnk(MODIFIER UN JOUEUR)  ~~~~~~~~~\n"
                  "      bld(Choisissez un joueur) :"))
            for i, player in enumerate(players, start=1):
                print(ansify(f"      pnk({i}.) bld({player.last_name}) {player.first_name}, ({player.chess_id})"))

            print(ansify("\n\n      ch_up(R. Retour)\n"))

            return input("\n\n      bld(Entrez votre choix) :\033[0m ")

    @staticmethod
    def modify_player(player):
        """Ask the user what to modify about the player."""
        print("\n" * 100)
        print(ansify(f"\n            ~~~~~~~~  pnk({player.name})  ~~~~~~~~~\n\n\n\n"
                     f"      pnk(𝟭.) Tout modifier\n"
                     f"      pnk(𝟮.) Mettre à jour l'I.N.E\n\n\n"
                     f"      ch_up(R.) Retour\n\n"))
        return input("\n\n      bld(Entrez votre choix) : ")

    @staticmethod
    def enter_chess_id(player):
        """Ask the user to enter the player's chess ID."""
        print("\n" * 100)
        print(f"\n            ~~~~~~~~  pnk({player.name})  ~~~~~~~~~\n\n")
        print(f"\n      Saisissez l'Identifiant National d'Échecs de :\n")
        print(f"      disc_it_pnk( ~ {player.first_name}) pnk({player.last_name.upper()})\n\n\n")
        return input(ansify("\n\n      bld(Entrez l'I.N.E) : "))

    @staticmethod
    def display_players(players):
        """Displays the players' list.'"""
        print("\n" * 100)
        print("\n\n\n~~~~~~~~~~~~~~~  \033[1;95mTOUS LES JOUEURS\033[0m  ~~~~~~~~~~~~~~~\n")
        for player in players:
            print(f" ~ \033[1;95m{player.last_name.upper()}\033[0m {player.first_name}"
                  f" (\033[1;3;35mID:\033[0m {player.chess_id}) ~ \033[1;3;35mNé(e) le:\033[0m {player.birth_date} ~ ")
        input()
        return
