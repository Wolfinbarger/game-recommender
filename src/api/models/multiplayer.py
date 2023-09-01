class Multiplayer:
    """
    Args:
        player_count (int, optional): Number of players available either local or online.
    Example:
        multiplayer = Multiplayer(player_count=10)
    """
    def __init__(self, player_count=1):
        self._player_count = player_count

    @property
    def player_count(self):
        return self._player_count

    @player_count.setter
    def player_count(self, value):
        self._player_count = value

    def to_json(self):
        return {
            "player_count": self._player_count
        }
