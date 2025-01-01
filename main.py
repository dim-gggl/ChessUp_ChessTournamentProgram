import json
from managers.player_manager import PlayerManager
from controllers.player_controller import PlayerController
from views.player_views import PlayerView
from models.player import Player

def test_player_mvc():
    file_path = "data/test_players.json"
    manager = PlayerManager(file_path)
    view = PlayerView()
    controller = PlayerController(manager, view)

    with open(file_path, 'w') as file:
        json.dump([], file)

    print("=== Test Player MVC ===")

    # Test 1 :
    print("\nTest 1: Créer un joueur")
    player_data = {
        "last_name": "Doe",
        "first_name": "John",
        "birth_date": "1990-01-01",
        "national_id": "AB12345",
        "rank": 1200
    }

    player = Player(**player_data)
    manager.save(player)

    print("Contenu après save :", manager.load_all())  # Diagnostic
    loaded_player = manager.load_by_national_id("AB12345")
    print("Player chargé :", loaded_player)  # Diagnostic
    assert loaded_player is not None, "Le joueur avec l'ID AB12345 n'a pas été trouvé."
    assert loaded_player.national_id == "AB12345"
    print("Joueur créé et sauvegardé avec succès.")

    # Test 2:
    print("\nTest 2: Lister les joueurs")
    controller.list_players()

    # Test 3:
    print("\nTest 3: Afficher les détails d'un joueur")
    controller.show_player("AB12345")

    # Test 4:
    print("\nTest 4: Créer un joueur via la vue et le contrôleur")
    print("(Saisissez les informations demandées)")
    controller.create_player()

    print("\nListe des joueurs après ajout via contrôleur:")
    controller.list_players()

    print("\nTous les tests pour les composants MVC de Player ont été complétés avec succès.")


if __name__ == "__main__":
    test_player_mvc()
