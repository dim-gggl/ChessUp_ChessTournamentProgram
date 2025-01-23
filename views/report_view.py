from utils.ansify import ansify


class ReportView:
    """Displays the report menu and submenus."""

    @staticmethod
    def clear_screen():
        print("\n" * 100)

    @staticmethod
    def header(prompt):
        print(ansify(f"\n\t\t~~~~~~~~~ rpt_gr({prompt})  ~~~~~~~~~      \n"))

    @staticmethod
    def display_report_menu():
        """Displays the report menu."""
        ReportView.clear_screen()
        ReportView.header("RAPPORTS DE DONNEES")
        print(
            ansify(
                "\n\n\trpt_gr(1.) Afficher tous les joueurs (Liste alphabétique)"
                "\n\trpt_gr(2.) Afficher tous les tournois"
                "\n\trpt_gr(3.) Afficher les détails d'un tournoi"
                "\n\trpt_gr(4.) Exporter des données en HTML\n"
                "\n\n\tch_up(R. Retour)\n"
            )
        )
        return input("\n\tEntrez votre choix : ").strip()

    @staticmethod
    def display_possible_options(tournament):
        """Displays the list of details the user can choose from."""
        ReportView.clear_screen()
        ReportView.header("DONNEES D'UN TOURNOI")
        print(
            ansify(
                f"\n\trpt_gr(1.) Afficher nom et dates."
                f"\n\trpt_gr(2.) Afficher tous les joueurs ({len(tournament.players)} inscrits)."
                f"\n\trpt_gr(3.) Détails des Rounds et matchs.\n"
                "\n\n\tch_up(R. Retour)\n"
            )
        )
        return input("\n\tEntrez votre choix : ").strip()

    @staticmethod
    def show_name_and_dates(tournament):
        """Displays the tournament's name and dates."""
        ReportView.clear_screen()
        ReportView.header("DONNEES D'UN TOURNOI")
        print(
            ansify(
                f"\n\t\t——————[   whte({tournament.name})   ]—————\n\n"
                f"\n\trpt_gr(Ouverture ~~~>)\t{tournament.start_date}"
                f"\n\trpt_gr(Fin ~~~>)\t{tournament.end_date}"
            )
        )
        print("\n")
        input("\tAppuyez sur ENTRÉE pour continuer")
        return

    @staticmethod
    def show_rounds_and_matches(tournament):
        """Displays the tournament's rounds and matches."""
        ReportView.clear_screen()
        ReportView.header("DONNEES D'UN TOURNOI")
        print(ansify(f"\n\t\trpt_gr({tournament.name})  \n\n"))
        if tournament.rounds:
            for round in tournament.rounds:
                print(ansify(str(round)))
                input("\tAppuyez sur ENTRÉE pour continuer")
        return

    @staticmethod
    def display_export_options():
        """Displays the export options."""
        ReportView.clear_screen()
        ReportView.header("EXPORT DE DONNEES")
        print(
            ansify(
                "\n\trpt_gr(1.) Exporter la liste de tous les joueurs"
                "\n\trpt_gr(2.) Exporter la liste de tous les tournois"
                "\n\trpt_gr(3.) Exporter les détails d'un tournoi\n\n"
                "\n\tch_up(R. Retour)\n\n"
            )
        )
        return input("\n\tEntrez votre choix : ")

    @staticmethod
    def export_success_msg():
        """Displays the export success message."""
        ReportView.clear_screen()
        print(ansify("\n\n\t~~~~~  gld(Données exportées avec succès !)  ~~~~~\n\n"))
        input("\tAppuyez sur ENTRÉE pour continuer")

    @staticmethod
    def display_all_tournaments(tournaments):
        """Displays the list of all tournaments."""
        ReportView.clear_screen()
        ReportView.header("TOURNOIS")
        for i,tournament in enumerate(tournaments):
            print(ansify("\t||" + str(tournament) + "\n"))
        input("\tAppuyez sur ENTRÉE pour continuer")
        return
