def play_rpc(enemy, you):
    if enemy == "A":  # Rock
        if you == "X":  # Rock
            return 3  # Draw
        elif you == "Y":  # Paper
            return 6  # Win
        elif you == "Z":  # Scissors
            return 0  # Lose
    elif enemy == "B":  # Paper
        if you == "X":  # Rock
            return 0  # Lose
        elif you == "Y":  # Paper
            return 3  # Draw
        elif you == "Z":  # Scissors
            return 6  # Win
    elif enemy == "C":  # Scissors
        if you == "X":  # Rock
            return 6  # Win
        elif you == "Y":  # Paper
            return 0  # Lose
        elif you == "Z":  # Scissors
            return 3  # Draw


def play_reverse_rpc(enemy, required):
    if enemy == "A":  # Rock
        if required == "X":  # Lose
            return "Z"
        elif required == "Y":  # Draw
            return "X"
        elif required == "Z":  # Win
            return "Y"
    elif enemy == "B":  # Paper
        if required == "X":  # Lose
            return "X"
        elif required == "Y":  # Draw
            return "Y"
        elif required == "Z":  # Win
            return "Z"
    elif enemy == "C":  # Scissors
        if required == "X":  # Lose
            return "Y"
        elif required == "Y":  # Draw
            return "Z"
        elif required == "Z":  # Win
            return "X"


def calc_score(play):
    if play == "X":
        return 1
    elif play == "Y":
        return 2
    elif play == "Z":
        return 3


def part1(input: str):
    rounds = input.splitlines()
    score = 0
    for round in rounds:
        enemy, you = round.split(" ")
        score += play_rpc(enemy, you)
        score += calc_score(you)
    return score


def part2(input: str):
    rounds = input.splitlines()
    score = 0
    for round in rounds:
        enemy, required = round.split(" ")
        to_play = play_reverse_rpc(enemy, required)
        score += play_rpc(enemy, to_play)
        score += calc_score(to_play)
    return score
