class MainMenuView:

    @staticmethod
    def display_main_menu_intro():
        print("\n" * 100)
        print("\033[1;3m    ~~~~~~~~~~~\033[0m \033[3;94m 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 \033[0m\033[1;3m ~~~~~~~~~~~~~~\033[0m")
        print("\033[1;3m           ~~~~    \033[0m\033[2;3m𝙩𝙤   \033[0m\033[1;3m   ~~~~      \033[0m")
        print("\033[1;3m    ~~~~~~~~~~~\033[0m\033[1;94m⏐ 𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎ ⏐\033[0m\033[1;3m~~~~~~~~~~~~\033[0m")
        print("\n\n\n")
        print("\n\033[0m       ~~~~~~\033[1;38;5;202m  𝙿𝚁𝙴𝚂𝚂 𝙴𝙽𝚃𝙴𝚁 \033[0m\033[1;3m~~~~~~~\033[0m")
        print("\n ")
        input("       Appuyez sur \033[1;94m↵\033[0m pour continuer")
        return

    @staticmethod
    def display_main_menu():
        print("\n" * 100)
        print("      ~~~~~~~~~ \033[1;94m⏐ 𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎ ⏐\033[0m ~~~~~~~~~~\n\n")
        print("\n\033[1;94m𝟷.\033[0m Menu \033[1mTOURNOIS\033[0m")
        print("\033[1;94m𝟸.\033[0m Menu \033[1mJOUEURS\033[0m")
        print("\033[1;94m𝟹.\033[0m \033[1mRAPPORTS\033[0m de données")
        print("\n\033[1;38;5;202m𝟶. Quitter\n\033[0m")
        return input("\nChoisissez une option : ").strip()

    @staticmethod
    def bye_message():
        print("\n" * 100)
        print("\n\n\033[1m      ~~~~~~~~~ ]\033[1;38;5;202m * 𝐵𝑦𝑒 𝐵𝑦𝑒 * \033[1;0m[~~~~~~~\n\033[0m")
        print("      ~~~~~~~~~ \033[1;38;5;202m⏐ 𝗖𝗵𝗲𝘀𝘀𝗨𝗽⬆︎ ⏐\033[0m ~~~~~~~~~~\n\n")
        input()
