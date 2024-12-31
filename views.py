from models import Tournament


class TournamentView:
    @staticmethod
    def prompt_for_tournament_data():
        print("=== Création d'un tournoi ===")
        name = input("Nom : ")
        location = input("Lieu : ")
        starting_date = input("Date de début (YYYY-MM-DD) : ")
        ending_date = input("Date de fin (YYYY-MM-DD) : ")
        description = input("Description (facultatif) : ")
        return {
            "name": name,
            "location": location,
            "starting_date": starting_date,
            "ending_date": ending_date,
            "description": description
        }

    @staticmethod
    def show_tournament_list(tournaments):
        if not tournaments:
            print("Aucun tournoi trouvé.")
        for tournament in tournaments:
            print(f"- {tournament.name} ({tournament.location}, "
                  f"[{tournament.starting_date})-[{tournament.ending_date}]")

    @staticmethod
    def show_tournament_details(tournament):
        print(f"=== Tournoi : {tournament.name} ===")
        print(f"Lieu : {tournament.location}")
        print(f"Date de début : {tournament.starting_date}")
        print(f"Date de fin : {tournament.ending_date}")
        print(f"Description : {tournament.description}")
        print("Rounds :")
        for round_ in tournament.rounds:
            print(f"  - {round_.name}")

    @staticmethod
    def success_message():
        print("Tournoi créé avec succès !")

    @staticmethod
    def failure_message():
        print("Impossible de créer le tournoi.")