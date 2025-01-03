class MenuView:
    """
    Gère l'affichage du menu principal.
    """

    @staticmethod
    def display_main_menu():
        print("\n=== Menu Principal ===")
        print("1. Ajouter un joueur")
        print("2. Voir tous les joueurs")
        print("3. Créer un nouveau tournoi")
        print("4. Gérer un tournoi existant")
        print("5. Exporter tous les joueurs (HTML)")
        print("6. Exporter tous les tournois (HTML)")
        print("7. Exporter les détails d'un tournoi (HTML)")
        print("8. Voir les joueurs d'un tournoi")
        print("9. Rounds et matches d'un tournoi (rapport)")
        print("q. Quitter")

        return input("Choisissez une option : ")
