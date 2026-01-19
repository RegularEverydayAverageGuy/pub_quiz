from dataclasses import dataclass

@dataclass
class Team:
    name: str
    score: int

    def __init__(self, name: str):
        self.name       = name
        self.unit_price = 0


class GameController:
    def __init__(self, config):
        self.teams = []

    def add_team(self, team_name: str):
        team = Team(team_name)
        self.teams.append(team)

    def create(self, config: str):
        # TBD
        pass
    def submit_answer(self, answer: str) -> bool:
        # TBD
        return True

    def get_state(self) -> dict:
        # TBD
        return dict()

gameController = GameController(None)