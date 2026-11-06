from enum import Enum


class Move(Enum):
    COOPERATE = "Cooperate"
    DEFECT = "Defect"


class GameModel:
    def __init__(self):
        self.points: int = 0
        self.history: dict[int, Move] = {}

    def reset(self):
        self.points = 0
        self.history = {}
