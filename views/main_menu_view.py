from utils.ansify import ansify
from views.tournament_views import TournamentView


class MainMenuView:
    """
    Displays the main menu.
    """

    @staticmethod
    def display_main_menu_intro():
        """
        Displays the introductory message of the application.
        """
        print("\n" * 100)
        print(
            ansify(
                "\t\t  it_ttl( 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 ) \n\t\t\twhte(𝙩𝙤)"
                "\n\t\t  ttl_blu(⏐𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎⏐)\n\n\n"
                "\n\n\n"
                "\n "
            )
        )
        input(ansify("\tAppuyez sur ↵ pour continuer"))
        return

    @staticmethod
    def display_main_menu():
        """
        Displays the main menu.
        """
        TournamentView.clear_screen()
        print(
            ansify(
                "\tbld_it(~~~~~~~~~) ttl_blu(⏐ 𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎ ⏐) bld_it(~~~~~~~~~~)\n\n"
                "\n\tttl_blu(1.) Menu bld(TOURNOIS)"
                "\n\tttl_blu(2.) Menu bld(JOUEURS)"
                "\n\tttl_blu(3.) bld(RAPPORTS)\n\n"
                "\tttl_blu(4.) Sauvegarder\n\n"
                "\n\tch_up(Q. Quitter)\n"
            )
        )
        return input(ansify("\n\tbld(Choisissez une option :) ")).strip()

    @staticmethod
    def data_saved_msg():
        TournamentView.clear_screen()
        print(
            ansify(
                "\n\n\t\tgld(DONNÉES ENREGISTRÉES)\n\n\n"
            )
        )
        input("\n\n\tAppuyez sur ENTRÉE pour continuer.")

    @staticmethod
    def bye_message():
        """
        Exit message.
        """
        TournamentView.clear_screen()
        print(
            ansify(
                "\n\n\t\t\tch_up(*𝐵𝑦𝑒𝐵𝑦𝑒*)\n\n"
                "\n\n\t\t\tch_up(𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎)\n\n\n\n"
            )
        )
        input()
