# Modern version of: Game Theory Simulator
from behaviour import assign_points, boot, declare_winner, display_game_chart
from schemas.bots import BotPlayer
from schemas.player import Player


class Game:
    def __init__(self):
        self.round_number: int = 0
        self.player: Player = Player()
        self.bot: BotPlayer

    def run(
        self,
        menu_settings: list,
    ) -> None:
        self.bot = menu_settings[1]
        self.round_number = 0
        self.player.reset()
        self.bot.reset()

        while self.round_number < menu_settings[2]:
            print(f"\n--- Round number: {self.round_number + 1} ---")

            # Get Player and Bot choices
            p_choice = self.player.player_choice(self.round_number)
            b_choice = self.bot.bot_choice(self.round_number, self.player.history)

            # Assign points based on the round
            points_to_assign = assign_points(p_choice, b_choice)
            self.player.points += points_to_assign[0]
            self.bot.points += points_to_assign[1]

            # Update the user on the game and procede with the next round
            print(f"\n\nPlayer's points: {self.player.points}")
            print(f"Bot's points: {self.bot.points}\n")
            self.round_number += 1

        print("Game Over.\n")
        display_game_chart(self.player.history, self.bot.history, self.bot.name)
        declare_winner(self.player.points, self.bot.points)


if __name__ == "__main__":
    game = Game()
    try:
        settings = boot(is_first_round=True)
        while settings != "exit":
            game.run(settings)
            settings = boot(is_first_round=False)
    except EOFError as err:
        print(f"An error has occurred: {err}")
    except KeyboardInterrupt:
        print("\nBye!")
