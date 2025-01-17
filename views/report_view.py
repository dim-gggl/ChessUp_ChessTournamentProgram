from utils.ansify import ansify


class ReportView:
    """Displays the report menu and submenus."""
    @staticmethod
    def display_report_menu():
        """Displays the report menu."""
        print("\n" * 100)
        print(ansify("\n       ~~~~~~~~~ rpt_gr( RAPPORTS DE DONNEES)  ~~~~~~~~~      \n"
                     "\n\n      rpt_gr(1.) Afficher tous les joueurs"
                     "\n      rpt_gr(2.) Afficher tous les tournois"
                     "\n      rpt_gr(3.) Afficher les détails d'un tournoi"
                     "\n      rpt_gr(4.) Exporter des données en HTML\n"
                     "\n\n       ch_up(R. Retour)\n"))
        return input("\n      Entrez votre choix : ").strip()

    @staticmethod
    def display_possible_options(tournament):
        """Displays the list of details the user can choose from."""
        print("\n" * 100)
        print(ansify(f"\n\n      ~~~~~~~  rpt_gr(DONNEES D'UN TOURNOI)  ~~~~~~~ \n\n\n"
              f"\n      rpt_gr(1.) Afficher nom et dates."
              f"\n      rpt_gr(2.) Afficher tous les joueurs ({len(tournament.players)} inscrits)."
              f"\n      rpt_gr(3.) Détails des Rounds et matchs.\n"
              "\n\n        ch_up(R. Retour)\n"))
        return input("\n      Entrez votre choix : ").strip()

    @staticmethod
    def show_name_and_dates(tournament):
        """Displays the tournament's name and dates."""
        print("\n" * 100)
        print(ansify(f"\n\n\n      ~~~~~~~~~  rpt_gr(DONNEES D'UN TOURNOI)  ~~~~~~~~~\n\n"
              f"\n         ——————[   bld({tournament.name})   ]—————\n\n"
              f"\n      rpt_gr(Ouverture ~~~>)     {tournament.start_date}"
              f"\n      rpt_gr(Fin ~~~>)     {tournament.end_date}"))
        print("\n")
        input()
        return

    @staticmethod
    def show_rounds_and_matches(tournament):
        """Displays the tournament's rounds and matches."""
        print("\n" * 100)
        print(ansify("\n\n\n\n      ~~~~~~~  rpt_gr(DONNEES D'UN TOURNOI)  ~~~~~~~\n"))
        print(ansify(f"\n               rpt_gr({tournament.name})  \n\n"))
        if tournament.rounds:
            for round in tournament.rounds:
                print(str(round))
                input()
        return

    @staticmethod
    def display_export_options():
        """Displays the export options."""
        print("\n" * 100)
        print(ansify("\n\n      ~~~~~~~  rpt_gr(EXPORT DE DONNEES)  ~~~~~~~ \n\n"
                     "\n      rpt_gr(1.) Exporter la liste de tous les joueurs"
                     "\n      rpt_gr(2.) Exporter la liste de tous les tournois"
                     "\n      rpt_gr(3.) Exporter les détails d'un tournoi\n\n"
                     "\n      ch_up(R. Retour)\n\n"))
        return input("\n      Entrez votre choix : ")

    @staticmethod
    def export_success_msg():
        """Displays the export success message."""
        print("\n" * 100)
        print(ansify("\n\n      ~~~~~  gld(Données exportées avec succès !)  ~~~~~\n\n"))
        input()

    @staticmethod
    def display_all_tournaments(tournaments):
        """Displays the list of all tournaments."""
        print("\n" * 100)
        print(ansify("\n\n\n\n      ~~~~~~~  rpt_gr(TOURNOIS)  ~~~~~~~\n\n"))
        for tournament in tournaments:
            print(ansify(f"       ~~~~~~    rpt_gr({tournament.name})    ~~~~~~ \n"
                         f"         ~ bld({tournament.location}) ~ ({tournament.start_date} - {tournament.end_date}) ~"))
        input()
        return
