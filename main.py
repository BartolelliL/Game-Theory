# Modern version of: Game Theory Simulator
from behaviour import assign_points, declare_winner
from schemas.bots import AlwaysCooperate, AlwaysDefect, BotPlayer, RandomBot, TitForTat
from schemas.player import Player


class Game:
    def __init__(self):
        self.round_number: int = 0
        self.player: Player = Player()
        self.bot: BotPlayer

    def run(
            self,
            chosen_bot: BotPlayer,
            maximum_rounds: int = 20,
    ):
        # Initialize attrs
        self.bot = chosen_bot
        self.round_number = 0
        self.player.reset()
        self.bot.reset()

        print(f"Opponent: {self.bot.name}\n")

        while self.round_number < maximum_rounds:
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

        declare_winner(self.player.points, self.bot.points)
        print("Game Over.\n")
        print(f"Player points: {self.player.history}\n")
        print(f"Bot points: {self.bot.history}\n")



if __name__ == "__main__":
    game = Game()
    game.run(RandomBot())
    game.run(TitForTat())
    game.run(AlwaysCooperate())
    game.run(AlwaysDefect())
