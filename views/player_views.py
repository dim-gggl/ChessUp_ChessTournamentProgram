class PlayerView:
    @staticmethod
    def prompt_for_player_data():
        print("=== Création d'un joueur ===")
        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        birth_date = input("Date de naissance (YYYY-MM-DD) : ")
        national_id = input("ID National (AB12345) : ")
        rank = input("Classement (entier positif) : ")
        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "national_id": national_id,
            "rank": int(rank)
        }

    @staticmethod
    def show_player_list(players):
        if not players:
            print("Aucun joueur trouvé.")
        else:
            for player in players:
                print(f"==={player.national_id}==="
                      f" {player.first_name} {player.last_name} "
                      f"(Classement : {player.rank})")

    @staticmethod
    def show_player_details(player):
        print(f"=== Détails du joueur : {player.first_name} {player.last_name} ===")
        print(f"ID National : {player.national_id}")
        print(f"Date de naissance : {player.birth_date}")
        print(f"Classement : {player.rank}")

    @staticmethod
    def success_message(message):
        print(f"Succès : {message}")

    @staticmethod
    def error_message(message):
        print(f"Erreur : {message}")
