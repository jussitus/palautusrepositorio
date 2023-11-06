from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        return sorted(
            filter(lambda player: player.nationality == nationality, self.players),
            key=lambda player: player.points,
            reverse=True,
        )
