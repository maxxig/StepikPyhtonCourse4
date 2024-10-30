from dataclasses import dataclass, field
@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)

@dataclass(order=True)
class FootballTeam:
    name: str
    players: list = field(default_factory=list, compare=False, repr=False)
    def add_players(self, *args):
        for player in args:
            self.players.append(player)
