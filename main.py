# Modern version of: Game Theory Simulator
from schemas import Player, RandomBot
from behaviour import assign_points


class Game:
    def __init__(self):
        self.round_number: int = 0
        self.player = Player()
        self.bot = RandomBot()

    def run(self):
        while self.player.points < 30:
            print(f"\n--- Round number: {self.round_number + 1} ---")

            # Get Player and Bot choices
            p_choice = self.player.player_choice(self.round_number)
            b_choice = self.bot.bot_choice(self.round_number)

            # Assign points based on the round
            points_to_assign = assign_points(p_choice, b_choice)
            self.player.points += points_to_assign[0]
            self.bot.points += points_to_assign[1]

            # Update the user on the game and procede with the next round
            print(f"\n\nPlayer's points: {self.player.points}")
            print(f"Bot's points: {self.bot.points}\n")
            self.round_number += 1

        print("Game Over.")
        print(f"Player points: {self.player.history}")
        print(f"Bot points: {self.bot.history}")



if __name__ == "__main__":
    game = Game()
    game.run()
