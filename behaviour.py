def assign_points(player_choice_value, bot_choice_value) -> tuple[int, int]:
    """
    First is player, Second is bot.
    :param player_choice_value:
    :param bot_choice_value:
    :return:
    """

    if player_choice_value == "Cooperate" and bot_choice_value == "Cooperate":
        return (3, 3)
    elif player_choice_value == "Defect" and bot_choice_value == "Defect":
        return (1, 1)
    elif player_choice_value == "Cooperate" and bot_choice_value == "Defect":
        return (0, 5)
    elif player_choice_value == "Defect" and bot_choice_value == "Cooperate":
        return (5, 0)
    else:
        raise ValueError(f"Invalid choices passed: Player='{player_choice_value}', Bot='{bot_choice_value}'")
