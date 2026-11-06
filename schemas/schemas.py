from enum import Enum


class Move(Enum):
    COOPERATE = "Cooperate"
    DEFECT = "Defect"


class GameModel:
    def __init__(self):
        self.points = 0
        self.history = {}

    def reset(self):
        self.points = 0
        self.history = {}
