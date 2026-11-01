from abc import ABC, abstractmethod
from collections.abc import Mapping
from secrets import choice as s_choice
from typing import ClassVar

from schemas.schemas import GameModel, Move


class BotPlayer(GameModel, ABC):
    name: ClassVar[str]

    # Cooperate or Defect
    def bot_choice(
            self,
            round_number: int,
            opponent_history: Mapping[int, Move]
    ) -> Move:
        choice = self._decide(round_number, opponent_history)
        self.history[round_number] = choice
        return choice

    @abstractmethod
    def _decide(
            self,
            round_number: int,
            opponent_history: Mapping[int, Move]
    ) -> Move:
        ...


class TitForTat(BotPlayer):
    name = "Tit-For-Tat (TFT) Bot"

    def _decide(
            self,
            round_number: int,
            opponent_history: Mapping[int, Move]
    ) -> Move:
        if round_number == 0:
            return Move.COOPERATE
        else:
            return opponent_history[round_number - 1]


class AlwaysCooperate(BotPlayer):
    name = "Always Cooperate Bot"

    def _decide(
            self,
            round_number: int,
            opponent_history: Mapping[int, Move]
    ) -> Move:
        return Move.COOPERATE


class AlwaysDefect(BotPlayer):
    name = "Always Defect Bot"

    def _decide(
            self,
            round_number: int,
            opponent_history: Mapping[int, Move]
    ) -> Move:
        return Move.DEFECT


class RandomBot(BotPlayer):
    name = "Random Bot"

    def _decide(
            self,
            round_number: int,
            opponent_history: Mapping[int, Move]
    ) -> Move:
        return s_choice(self.choices)
