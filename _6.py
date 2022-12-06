import collections


def solution(num_chars, signal):
    chars = collections.deque(maxlen=num_chars)
    for i in range(0, len(signal)):
        chars.append(signal[i])
        if len(chars) == num_chars and len(chars) == len(set(chars)):
            return i + 1


def part1(input: str):
    return solution(4, input)


def part2(input: str):
    return solution(14, input)
