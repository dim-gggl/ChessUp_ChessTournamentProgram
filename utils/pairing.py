import random


def generate_pairs(players):
    """
    Mélange les joueurs et génère des paires pour le premier round.
    players : liste d'objets Player
    Retourne une liste de tuples (player1, player2).
    """
    print(players)
    shuffled = players[:]
    random.shuffle(shuffled)
    if len(shuffled) % 2 != 0:
        p1 = shuffled.pop(0)
        p1.points += 1
        print(f"{p1.first_name} {p1.last_name} n'a pas d'adversaire. 1 point pour le premier round !")

    # Génération de pairs à partir de la liste shuffled
    return [(shuffled[i], shuffled[i + 1]) for i in range(0, len(shuffled), 2)]


def generate_pairs_by_points(players, previous_matches):
    """
    Trie les joueurs par score et génère des paires
    qui n'ont pas déjà joué ensemble.
    previous_matches : set de tuples (player1, player2) qui se sont déjà affrontés
    Retourne une liste de tuples (player1, player2).
    """
    players_sorted = sorted(players, key=lambda p: p.points, reverse=True)
    pairs = []
    while players_sorted:
        p1 = players_sorted.pop(0)
        paired = False
        for i, p2 in enumerate(players_sorted):
            if (p1, p2) not in previous_matches and (p2, p1) not in previous_matches:
                pairs.append((p1, p2))
                del players_sorted[i]
                paired = True
                break

        if not paired:
            p1.points += 1
            print(f"{p1.first_name} {p1.last_name} n'a pas d'adversaire. 1 point !")
    return pairs
