from utils.ansify import ansify


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
                "bld_it(    ~~~~~~~~~~~) it_ttl( 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 ) bld_it(~~~~~~~~~~~~)"
                "\nbld_it(           ~~~~    )  disc_it( 𝙩𝙤   )bld_it(    ~~~~      )"
                "\nbld_it(     ~~~~~~~~~~)ttl_blu(⏐𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎⏐)bld_it(~~~~~~~~~~~~)\n\n\n"
                "\n\n\n\n       bld_it(~~~~~~)  ch_up(𝙿𝚁𝙴𝚂𝚂 𝙴𝙽𝚃𝙴𝚁)  bld_it(~~~~~~~)\n"
                "\n "
            )
        )
        input(ansify("\033[5m          Appuyez sur ttl_blu(↵) pour continuer"))
        return

    @staticmethod
    def display_main_menu():
        """
        Displays the main menu.
        """
        print("\n" * 100)
        print(
            ansify(
                "      bld_it(~~~~~~~~~) ttl_blu(⏐ 𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎ ⏐) bld_it(~~~~~~~~~~)\n\n\n\n"
                "\n      ttl_blu(1.) Menu bld(TOURNOIS)"
                "\n      ttl_blu(2.) Menu bld(JOUEURS)"
                "\n      ttl_blu(3.) bld(RAPPORTS)\n\n"
                "\n       ch_up(Q. Quitter)\n"
            )
        )
        return input(ansify("\n      bld(Choisissez une option :) ")).strip()

    @staticmethod
    def bye_message():
        """
        Exit message.
        """
        print("\n" * 100)
        print(
            ansify(
                "\n\nbld(      ~~~~~   ])  ch_up( * 𝐵𝑦𝑒𝐵𝑦𝑒 * )  bld([  ~~~~\n\n)"
                "\n\nbld_it(      ~~~~~~~~~ )ch_up(⏐ 𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎ ⏐)bld_it( ~~~~~~~~~~)\n\n"
            )
        )
        input()
