from utils.ansify import ansify


class PlayerView:
    """Displays the players' menu and submenus."""

    @staticmethod
    def display_players_menu():
        """Displays the players' menu."""
        print("\n" * 100)
        print(ansify("      ~~~~~~~~~  pnk(MENU JOUEURS)  ~~~~~~~~\n\n\n\n"
              "      pnk(1.) Ajouter un nouveau joueur\n"
              "      pnk(2.) Modifier les infos d'un joueur\n"
              "      pnk(3.) Lister les joueurs\n\n"
              "\n        ch_up(R. Retour )\n"))
        return input("\n      Choisissez une option : ")


    @staticmethod
    def get_new_player_names():
        print("\n" * 100)
        print(ansify("\n      ~~~~~~~  pnk(NOUVEAU JOUEUR)  ~~~~~~~\n\n\n"
                     "\n      whte(Informations obligatoires) :\n\n"))
        first_name = input(ansify("\n      pnk(Prénom) : "))
        last_name = input(ansify("      pnk(Nom de Famille) : "))
        return {
            "first_name": first_name,
            "last_name": last_name
        }

    @staticmethod
    def get_new_player_birth_date():
        return input(ansify("      pnk(Date de naissance) (JJ/MM/AAAA) : "))

    @staticmethod
    def get_player_chess_id(edit=False):
        """Ask the user to enter the player's chess ID."""
        if not edit:
            print(ansify("\n\n\n               ch_up([INFO])"
                         "\n      L'Identifiant National d'Échecs peut être renseigné"
                         "\n      ultérieurement. Mais s'il est saisi, merci de respecter\n"
                         "      le format it_pnk(2 lettres suivies de 5 chiffres). \n\n"))
            input()
        else:
            print(ansify("\n\n\n               ch_up([INFO]"
                         "\n      Si vous n'êtes pas sûr du format, vous pouvez passer.\n\n\n"))
        return input(ansify("      pnk(I.N.E.) ou ENTRÉE : "))

    @staticmethod
    def new_player_saved_msg():
        print("\n" * 50)
        print(ansify("\n            pnk([ NOUVEAU JOUEUR ENREGISTRÉ ! ])\n\n\n"))
        input()

    @staticmethod
    def data_updated_msg():
        print("\n" * 50)
        print(ansify("\n            pnk([ Mises à jour enregistrées ! ])\n\n\n"))
        input()

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
        print(ansify("\n\n\n      ~~~~~~~~~  pnk(TOUS LES JOUEURS)  ~~~~~~~~~      \n"))
        for player in players:
            print(ansify(f"       ~ pnk({player.last_name.upper()}) {player.first_name}"
                  f" (disc_it_pnk(ID:) {player.chess_id}) ~ disc_it_pnk(Né(e) le:) {player.birth_date} ~ "))
        input()
        return
