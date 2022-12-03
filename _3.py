import numpy as np


def part1(input: str):
    lines = input.splitlines()
    s = 0
    for line in lines:
        l1 = line[:len(line)//2]
        l2 = line[len(line)//2:]
        dup = set(l1).intersection(l2).pop()
        s += (ord(dup) - 96 if dup.islower() else ord(dup) - 38)
    return s


def part2(input: str):
    lines = input.splitlines()
    s = 0
    groups = np.array(np.array_split(lines, len(lines)//3)).tolist()
    for group in groups:
        group_set = map(lambda i: set(i), group)
        dup = set.intersection(*group_set).pop()
        s += (ord(dup) - 96 if dup.islower() else ord(dup) - 38)
    return s
