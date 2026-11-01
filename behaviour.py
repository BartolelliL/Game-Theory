from schemas.schemas import Move


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
    raise ValueError(f"Invalid choices passed: Player='{player_choice_value}', Bot='{bot_choice_value}'")


def declare_winner(player_point: int, bot_points: int) -> None:
    if player_point > bot_points:
        print("You WON!")
    elif player_point == bot_points:
        print("Draw!")
    else:
        print("You lost...")
    print(f"You: {player_point} | Bot: {bot_points}")

