from utils.ansify import ansify


class ReportView:
    """Displays the report menu and submenus."""

    @staticmethod
    def clear_screen():
        print("\n" * 100)

    @staticmethod
    def header(prompt):
        print(ansify(f"\n       ~~~~~~~~~ rpt_gr({prompt})  ~~~~~~~~~      \n"))

    @staticmethod
    def display_report_menu():
        """Displays the report menu."""
        ReportView.clear_screen()
        ReportView.header("RAPPORTS DE DONNEES")
        print(
            ansify(
                "\n\n      rpt_gr(1.) Afficher tous les joueurs (Liste alphabétique)"
                "\n      rpt_gr(2.) Afficher tous les tournois"
                "\n      rpt_gr(3.) Afficher les détails d'un tournoi"
                "\n      rpt_gr(4.) Exporter des données en HTML\n"
                "\n\n       ch_up(R. Retour)\n"
            )
        )
        return input("\n      Entrez votre choix : ").strip()

    @staticmethod
    def display_possible_options(tournament):
        """Displays the list of details the user can choose from."""
        ReportView.clear_screen()
        ReportView.header("DONNEES D'UN TOURNOI")
        print(
            ansify(
                f"\n      rpt_gr(1.) Afficher nom et dates."
                f"\n      rpt_gr(2.) Afficher tous les joueurs ({len(tournament.players)} inscrits)."
                f"\n      rpt_gr(3.) Détails des Rounds et matchs.\n"
                "\n\n        ch_up(R. Retour)\n"
            )
        )
        return input("\n      Entrez votre choix : ").strip()

    @staticmethod
    def show_name_and_dates(tournament):
        """Displays the tournament's name and dates."""
        ReportView.clear_screen()
        ReportView.header("DONNEES D'UN TOURNOI")
        print(
            ansify(
                f"\n         ——————[   bld({tournament.name})   ]—————\n\n"
                f"\n      rpt_gr(Ouverture ~~~>)     {tournament.start_date}"
                f"\n      rpt_gr(Fin ~~~>)     {tournament.end_date}"
            )
        )
        print("\n")
        input("      Appuyez sur ENTRÉE pour continuer")
        return

    @staticmethod
    def show_rounds_and_matches(tournament):
        """Displays the tournament's rounds and matches."""
        ReportView.clear_screen()
        ReportView.header("DONNEES D'UN TOURNOI")
        print(ansify(f"\n               rpt_gr({tournament.name})  \n\n"))
        if tournament.rounds:
            for round in tournament.rounds:
                print(str(round))
                input("      Appuyez sur ENTRÉE pour continuer")
        return

    @staticmethod
    def display_export_options():
        """Displays the export options."""
        ReportView.clear_screen()
        ReportView.header("EXPORT DE DONNEES")
        print(
            ansify(
                "\n      rpt_gr(1.) Exporter la liste de tous les joueurs"
                "\n      rpt_gr(2.) Exporter la liste de tous les tournois"
                "\n      rpt_gr(3.) Exporter les détails d'un tournoi\n\n"
                "\n      ch_up(R. Retour)\n\n"
            )
        )
        return input("\n      Entrez votre choix : ")

    @staticmethod
    def export_success_msg():
        """Displays the export success message."""
        ReportView.clear_screen()
        print(ansify("\n\n      ~~~~~  gld(Données exportées avec succès !)  ~~~~~\n\n"))
        input("      Appuyez sur ENTRÉE pour continuer")

    @staticmethod
    def display_all_tournaments(tournaments):
        """Displays the list of all tournaments."""
        ReportView.clear_screen()
        ReportView.header("TOURNOIS")
        for i,tournament in enumerate(tournaments):
            print(ansify("      " + str(tournament) + "\n"))
        input("      Appuyez sur ENTRÉE pour continuer")
        return
