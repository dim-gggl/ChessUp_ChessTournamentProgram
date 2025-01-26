def sort_tournaments(tournaments, reverse=False):
    """
    Sorts tournaments according to the following criteria:
      - First, tournaments open for registration (current_round == 0)
      - Then those with is_holding == True
      - Then those with is_running == True
      - And lastly, those with is_finished == True
    """

    def status_rank(tournament):
        if tournament.current_round == 0 and not (tournament.is_holding or tournament.is_finished):
            return 0
        elif tournament.is_holding:
            return 1
        elif tournament.is_running:
            return 2
        elif tournament.is_finished:
            return 3
        return 4

    return sorted(tournaments, key=status_rank, reverse=False)
