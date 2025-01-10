class ReportView:

    @staticmethod
    def display_report_menu():
        print("\n" * 100)
        print("\n\n\n\n~~~~~~~~~~~~~~~  \033[1;38;5;118m RAPPORTS DE DONNEES \033[0m  ~~~~~~~~~~~~~~~\n")
        print("\n\033[1;38;5;118m1.\033[0m Afficher tous les joueurs")
        print("\033[1;38;5;118m2.\033[0m Afficher tous les tournois")
        print("\033[1;38;5;118m3.\033[0m Afficher les détails d'un tournoi")
        print("\033[1;38;5;118m4.\033[0m Exporter des données en HTML")
        print("\n\033[1;38;5;202m0. Retour au menu PRINCIPAL\033[0m")
        return input("\nEntrez votre choix : ").strip()

    @staticmethod
    def display_possible_options(tournament):
        print("\n" * 100)
        print("\n\n\n\n~~~~~~~~~~~~~~~  \033[1;38;5;118m DONNEES D'UN TOURNOI\033[0m  ~~~~~~~~~~~~~~~\n\n")
        print(f"\n\033[1;38;5;118m1.\033[0m Afficher nom et dates.")
        print(f"\033[1;38;5;118m2.\033[0m Afficher tous les joueurs ({len(tournament.players)} inscrits).")
        print("\033[1;38;5;118m3.\033[0m Détails des Rounds et matchs.")
        print("\n\033[1;38;5;202m0. Retour au menu PRINCIPAL\033[0m")
        return input("\nEntrez votre choix : ").strip()

    @staticmethod
    def show_name_and_dates(tournament):
        print("\n" * 100)
        print("\n\n\n\n~~~~~~~~~~~~~~~  \033[1;38;5;118m DONNEES D'UN TOURNOI\033[0m  ~~~~~~~~~~~~~~~\n\n")
        print(f"\n        ——————[  \033[1;38;5;118m {tournament.name} \033[0m ]—————\n\n")
        print(f"\033[1;38;5;118m    Ouverture ~~~>    \033[0m {tournament.start_date}")
        print(f"\033[1;38;5;118m    Fin ~~~>    \033[0m {tournament.end_date}")
        print("\n")
        input()
        return

    @staticmethod
    def show_rounds_and_matches(tournament):
        print("\n" * 100)
        print("\n\n\n\n~~~~~~~~~~~~~~~  \033[1;38;5;118m DONNEES D'UN TOURNOI\033[0m  ~~~~~~~~~~~~~~~\n\n")
        print(f"\n  ——————[  \033[1;38;5;118m {tournament.name} \033[0m ]—————")
        for round in tournament.rounds:
            print(f"\033[1;38;5;118m  {round.name} \033[0m~~~> ")
            for i, match in round.matches:
                print(f"\n\033[1;38;5;118m  Match {i +1} \033[0m ~~ {match.player1.name} [{match.score1}] vs [{match.scor2}] {match.player2.name}")
                print("\n")
                input()

    @staticmethod
    def display_export_options():
        print("\n" * 100)
        print("\n\n\n\n~~~~~~~~~~~~~~~  \033[1;38;5;118m EXPORT DE DONNEES \033[0m  ~~~~~~~~~~~~~~~\n")
        print("\n\033[1;38;5;118m1.\033[0m Exporter la liste de tous les joueurs")
        print("\033[1;38;5;118mm2.\033[0m Exporter la liste de tous les tournois")
        print("\033[1;38;5;118m3.\033[0m Exporter les détails d'un tournoi")
        print("\n\n")
        print("\n\033[1;38;5;202m0. Retour au menu PRINCIPAL\033[0m")
        return input("\nEntrez votre choix : ").strip()
