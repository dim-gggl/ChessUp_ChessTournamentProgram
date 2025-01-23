from utils.ansify import ansify


class PlayerView:
    """Displays the players' menu and submenus."""

    @staticmethod
    def clean_screen():
        print("\n" * 100)

    @staticmethod
    def header(prompt):
        print(ansify(f"\t~~~~~~~~~  pnk({prompt})  ~~~~~~~~\n\n"))

    @staticmethod
    def display_players_menu():
        """Displays the players' menu."""
        PlayerView.clean_screen()
        PlayerView.header("MENU JOUEURS")
        print(
            ansify(
                "\tpnk(1.) Ajouter un nouveau joueur\n"
                "\tpnk(2.) Modifier les infos d'un joueur\n"
                "\tpnk(3.) Lister les joueurs\n\n"
                "\n\tch_up(R. Retour )\n"
            )
        )
        return input("\n\tChoisissez une option : ")

    @staticmethod
    def get_new_player_names():
        PlayerView.clean_screen()
        PlayerView.header("NOUVEAU JOUEUR")
        print(ansify("\n\twhte(*Informations obligatoires) :\n\n"))
        first_name = input(ansify("\n\tpnk(Prénom *) : "))
        last_name = input(ansify("\tpnk(Nom de Famille *) : "))
        return {"first_name": first_name, "last_name": last_name}

    @staticmethod
    def get_new_player_birth_date():
        return input(ansify("\tpnk(Date de naissance *) (JJ/MM/AAAA) : "))

    @staticmethod
    def get_player_chess_id(edit=False):
        """Ask the user to enter the player's chess ID."""
        print(
            ansify(
                "\n\n\n\t\t\tch_up([INFO])"
                "\n\t\tL'Identifiant National d'Échecs peut être renseigné"
                "\n\t\tultérieurement. Mais s'il est saisi, merci de respecter\n"
                "\t\tle format it_pnk(2 lettres suivies de 5 chiffres). \n\n"
            )
        )
        input("\tAppuyez sur ENTRÉE pour continuer")
        return input(ansify("\tpnk(I.N.E.) ou ENTRÉE : "))

    @staticmethod
    def new_player_saved_msg():
        PlayerView.clean_screen()
        print(ansify("\n\t\t\tpnk([ NOUVEAU JOUEUR ENREGISTRÉ ! ])\n\n\n"))
        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def data_updated_msg():
        PlayerView.clean_screen()
        print(ansify("\n\t\tpnk([ Mises à jour enregistrées ! ])\n\n\n"))
        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def select_player_to_edit(players):
        """Displays the players' list and returns the selected player's index."""
        if not players:
            PlayerView.clean_screen()
            print(ansify("\n\t\t\tch_up([INFO])\n\t\tAucun Joueurs enregistré !\n\n"))
            input("\n")
        else:
            PlayerView.clean_screen()
            PlayerView.header("MODIFIER UN JOUEUR")
            for i, player in enumerate(players, start=1):
                print(ansify(f"\tpnk({i}.) bld({player.last_name}) {player.first_name}, ({player.chess_id})"))

            print(ansify("\n\n\tch_up(R. Retour)\n"))

            return input(ansify("\n\n\tbld(Entrez votre choix) :\033[0m "))

    @staticmethod
    def edition_options(player):
        """Ask the user what to modify about the player."""
        PlayerView.clean_screen()
        PlayerView.header(player.name)
        print(
            ansify(
                "\tpnk(𝟭.) Tout modifier\n"
                "\tpnk(𝟮.) Mettre à jour l'I.N.E\n\n\n"
                "\tch_up(R.) Retour\n\n"
            )
        )
        return input(ansify("\n\n\tbld(Entrez votre choix) : "))

    @staticmethod
    def enter_chess_id(player):
        """Ask the user to enter the player's chess ID."""
        PlayerView.clean_screen()
        PlayerView.header(player.name)
        print(
            ansify(

                f"\t~ pnk({player.first_name}) pnk({player.last_name.upper()})\n\n\n"
            )
        )
        return input(ansify("\n\n\tbld(Entrez l'I.N.E) : "))

    @staticmethod
    def display_players(players):
        """Displays the players' list.'"""
        PlayerView.clean_screen()
        PlayerView.header("TOUS LES JOUEURS")
        for player in players:
            print(
                ansify(
                    f"  ~ pnk({player.last_name.upper()}) whte({player.first_name})"
                    f" pnk(ID:) whte({player.chess_id}) ~ pnk(Né.e) le {player.birth_date} ~ "
                )
            )
        input("\tAppuyez sur ENTRÉE pour continuer")
        return
