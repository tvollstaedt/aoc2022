def part1(input: str):
    count = 0
    for line in input.splitlines():
        sets = []
        for pairs in line.split(","):
            p = pairs.split("-")
            sets.append(set(range(int(p[0]), int(p[1])+1)))
        if sets[1].issuperset(sets[0]) or sets[0].issuperset(sets[1]):
            count += 1
    return count


def part2(input: str):
    count = 0
    for line in input.splitlines():
        sets = []
        for pairs in line.split(","):
            p = pairs.split("-")
            sets.append(set(range(int(p[0]), int(p[1])+1)))
        if len(sets[0] & sets[1]) > 0:
            count += 1
    return count
