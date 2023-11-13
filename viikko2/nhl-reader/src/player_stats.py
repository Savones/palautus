from player import Player


class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        print(f"Players from {nationality}:")

        players = []

        for player in self.reader.get_players():
            if player.nationality == nationality:
                players.append(player)
        return players
