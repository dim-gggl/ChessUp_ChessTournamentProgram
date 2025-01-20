from utils.ansify import ansify


class PlayerView:
    """Displays the players' menu and submenus."""

    @staticmethod
    def clean_screen():
        print("\n" * 100)

    @staticmethod
    def header(prompt):
        print(ansify(f"      ~~~~~~~~~  pnk({prompt})  ~~~~~~~~\n\n\n\n"))


    @staticmethod
    def display_players_menu():
        """Displays the players' menu."""
        PlayerView.clean_screen()
        PlayerView.header("MENU JOUEURS")
        print(
            ansify(
                "      pnk(1.) Ajouter un nouveau joueur\n"
                "      pnk(2.) Modifier les infos d'un joueur\n"
                "      pnk(3.) Lister les joueurs\n\n"
                "\n        ch_up(R. Retour )\n"
            )
        )
        return input("\n      Choisissez une option : ")

    @staticmethod
    def get_new_player_names():
        PlayerView.clean_screen()
        PlayerView.header("NOUVEAU JOUEUR")
        print(ansify("\n      whte(*Informations obligatoires) :\n\n"))
        first_name = input(ansify("\n      pnk(Prénom*) : "))
        last_name = input(ansify("      pnk(Nom de Famille*) : "))
        return {"first_name": first_name, "last_name": last_name}

    @staticmethod
    def get_new_player_birth_date():
        return input(ansify("      pnk(Date de naissance*) (JJ/MM/AAAA) : "))

    @staticmethod
    def get_player_chess_id(edit=False):
        """Ask the user to enter the player's chess ID."""
        if not edit:
            print(
                ansify(
                    "\n\n\n               ch_up([INFO])"
                    "\n      L'Identifiant National d'Échecs peut être renseigné"
                    "\n      ultérieurement. Mais s'il est saisi, merci de respecter\n"
                    "      le format it_pnk(2 lettres suivies de 5 chiffres). \n\n"
                )
            )
            input("Appuyez sur ENTRÉE pour continuer")
        else:
            print(
                ansify(
                    "\n\n\n               ch_up([INFO]"
                    "\n      Si vous n'êtes pas sûr du format, vous pouvez passer.\n\n\n"
                )
            )
        return input(ansify("      pnk(I.N.E.) ou ENTRÉE : "))

    @staticmethod
    def new_player_saved_msg():
        PlayerView.clean_screen()
        print(ansify("\n            pnk([ NOUVEAU JOUEUR ENREGISTRÉ ! ])\n\n\n"))
        input("Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def data_updated_msg():
        PlayerView.clean_screen()
        print(ansify("\n            pnk([ Mises à jour enregistrées ! ])\n\n\n"))
        input("      Appuyez sur ENTRÉE pour continuer")


    @staticmethod
    def select_player_to_edit(players):
        """Displays the players' list and returns the selected player's index."""
        if not players:
            PlayerView.clean_screen()
            print(ansify("\n            ch_up([INFO])\n" "      Aucun Joueurs enregistré !\n\n"))
            input("\n")
        else:
            PlayerView.clean_screen()
            PlayerView.header("MODIFIER UN JOUEUR")
            for i, player in enumerate(players, start=1):
                print(ansify(f"      pnk({i}.) bld({player.last_name}) {player.first_name}, ({player.chess_id})"))

            print(ansify("\n\n      ch_up(R. Retour)\n"))

            return input(ansify("\n\n      bld(Entrez votre choix) :\033[0m "))

    @staticmethod
    def edition_options(player):
        """Ask the user what to modify about the player."""
        PlayerView.clean_screen()
        PlayerView.header(player.name)
        print(
            ansify(
                f"      pnk(𝟭.) Tout modifier\n"
                f"      pnk(𝟮.) Mettre à jour l'I.N.E\n\n\n"
                f"      ch_up(R.) Retour\n\n"
            )
        )
        return input(ansify("\n\n      bld(Entrez votre choix) : "))

    @staticmethod
    def enter_chess_id(player):
        """Ask the user to enter the player's chess ID."""
        PlayerView.clean_screen()
        PlayerView.header(player.name)
        print(
            ansify(

                f"      disc_it_pnk( ~ {player.first_name}) pnk({player.last_name.upper()})\n\n\n"
            )
        )
        return input(ansify("\n\n      bld(Entrez l'I.N.E) : "))

    @staticmethod
    def display_players(players):
        """Displays the players' list.'"""
        PlayerView.clean_screen()
        PlayerView.header("TOUS LES JOUEURS")
        for player in players:
            print(
                ansify(
                    f"       ~ pnk({player.last_name.upper()}) whte({player.first_name})"
                    f" it_pnk(ID:) {player.chess_id}) ~ it_pnk(Né(e)) le:) {player.birth_date} ~ "
                )
            )
        input("      Appuyez sur ENTRÉE pour continuer")
        return
