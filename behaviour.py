from random import randint
from collections.abc import Mapping

from schemas.bots import BOTS_MENU
from schemas.schemas import Move


def boot(is_first_round: bool) -> list | str:
    if is_first_round:
        print(
            "Welcome to the Prisoner's Dilemma simulator.\n"
            "Here you can explore the mathematical model by playing it.\n\n"
        )

    while True:
        menu_settings: list = [True]

        # Setting up the game by asking the user which bot he wants to play against
        # and how many round he wants to play. Saves the two settings in
        # a list, that gets used when the game runs.
        for k, v in BOTS_MENU.items():
            print(f"{k}) {v.name}")

        user_choice = (
            input("Choose a model you'll want to play with, or 'exit':\n")
            .lower()
            .strip()
        )

        if user_choice == "exit":
            return "exit"

        user_choice = int(user_choice.strip())
        cls = BOTS_MENU.get(user_choice)
        if cls is None:
            print("Invalid number provided.")
            continue
        menu_settings.append(cls())


        user_choice = (
            input(
                "Choose how many rounds you'll want to play (You can choose 'random'): "
            )
            .title()
            .strip()
        )

        if user_choice != "Random":
            try:
                user_choice = int(user_choice.strip())
                if int(user_choice) >= 3:
                    menu_settings.append(int(user_choice))
                else:
                    print("At least 3 rounds.")
                    continue
            except ValueError as err:
                print(f"You did not provide a correct number:\n{err}")
                continue
        else:
            menu_settings.append(randint(5, 20))

        return menu_settings


def assign_points(player_choice_value: Move, bot_choice_value: Move) -> tuple[int, int]:
    """
    First is player, Second is bot.
    :param player_choice_value:
    :param bot_choice_value:
    :return:
    """

    if player_choice_value == Move.COOPERATE and bot_choice_value == Move.COOPERATE:
        return 3, 3
    elif player_choice_value == Move.DEFECT and bot_choice_value == Move.DEFECT:
        return 1, 1
    elif player_choice_value == Move.COOPERATE and bot_choice_value == Move.DEFECT:
        return 0, 5
    elif player_choice_value == Move.DEFECT and bot_choice_value == Move.COOPERATE:
        return 5, 0
    raise ValueError(
        f"Invalid choices passed: Player='{player_choice_value}', Bot='{bot_choice_value}'"
    )


def declare_winner(player_point: int, bot_points: int) -> None:
    if player_point > bot_points:
        print("You WON!")
    elif player_point == bot_points:
        print("Draw!")
    else:
        print("You lost...")
    print(f"You: {player_point} | Bot: {bot_points}\n\n")


ROW_FORMAT = "{:>5} | {:<9} | {:<9} | {:^9} | {:>10} | {:>10}"


def display_game_chart(
    player_history: Mapping[int, Move],
    bot_history: Mapping[int, Move],
    bot_name: str,
) -> None:
    header = ROW_FORMAT.format(
        "Round", "Your move", "Bot move", "Round pts", "Your total", "Bot total"
    )
    print(f"\nOpponent: {bot_name} | Rounds: {len(player_history)}\n")
    print(header)
    print("-" * len(header))

    your_total = bot_total = 0
    for round_number in sorted(player_history):
        your_move = player_history[round_number]
        bot_move = bot_history[round_number]
        your_gain, bot_gain = assign_points(your_move, bot_move)
        your_total += your_gain
        bot_total += bot_gain
        print(
            ROW_FORMAT.format(
                round_number + 1,
                your_move.value,
                bot_move.value,
                f"{your_gain} / {bot_gain}",
                your_total,
                bot_total,
            )
        )

