from secrets import choice as s_choice


class GameModel:
    def __init__(self):
        self.points: int = 0
        self.choices: list[str] = ["Cooperate", "Defect"]
        self.history: dict[int, str] = {}

    def assign_points(self, reward) -> None:
        self.points += reward


class BotPlayer(GameModel):
    name: str


class Player(GameModel):
    def __init__(self):
        super().__init__()
        self.alias_choices: list[str] = ["C", "D"]

    # Cooperate or Defect
    def player_choice(self, round_number: int) -> str | None:
        while True:
            choice = input(
                "Do you decide to 'Cooperate' (C), or to "
                "'Defect' (D)?\n"
            ).title()

            if choice not in self.choices and choice not in self.alias_choices:
                continue
            elif choice in self.alias_choices:
                if choice == "C":
                    choice = "Cooperate"
                if choice == "D":
                    choice = "Defect"
            self.history[round_number] = choice
            return choice


class RandomBot(BotPlayer):
    name = "Random Bot"

    # Cooperate or Defect
    def bot_choice(self, round_number: int) -> str:
        choice = s_choice(self.choices)
        self.history[round_number] = choice
        return choice.title()
