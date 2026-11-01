from typing import ClassVar

from schemas.schemas import GameModel, Move


class Player(GameModel):
    MOVES: ClassVar[dict[str, Move]] = {
        "C": Move.COOPERATE,
        "COOPERATE": Move.COOPERATE,
        "D": Move.DEFECT,
        "DEFECT": Move.DEFECT
    }

    # Cooperate or Defect
    def player_choice(self, round_number: int) -> Move:
        while True:
            choice = self.MOVES.get(input(
                "Do you decide to 'Cooperate' (C), or to "
                "'Defect' (D)?\n"
            ).strip().upper())
            if choice is not None:
                self.history[round_number] = choice
                return choice
