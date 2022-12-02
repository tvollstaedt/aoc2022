def part1(input: str):
    calories = input.split("\n\n")
    return max(sum(int(line) for line in calorie.splitlines()) for calorie in calories)


def part2(input: str):
    calories = input.split("\n\n")
    sums = [sum(int(line) for line in calorie.splitlines()) for calorie in calories]
    sorted_sums = sorted(sums, reverse=True)
    return sorted_sums[0] + sorted_sums[1] + sorted_sums[2]
