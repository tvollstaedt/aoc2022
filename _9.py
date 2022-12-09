import math


def move_tail(head, tail):
    # Only move if head and tail don't touch each other
    if math.dist((head[0], head[1]), (tail[0], tail[1])) >= 2:
        if head[0] == tail[0]:  # Vertical move
            tail = (tail[0], tail[1] + (1 if tail[1] < head[1] else -1))
        elif head[1] == tail[1]:  # Horizontal move
            tail = (tail[0] + (1 if tail[0] < head[0] else -1), tail[1])
        else:  # Diagonal move
            tail = (tail[0] + (1 if tail[0] < head[0] else -1), tail[1] + (1 if tail[1] < head[1] else -1))
    return tail


def solution(input, tail_length):
    moves = input.splitlines()
    head = (0, 0)
    tails = []
    for _ in range(0, tail_length):
        tails.append((0, 0))
    tail_visits = set()
    for move in moves:
        direction, step = move.split()
        for _ in range(0, int(step)):
            if direction == "R":
                add_pos = (1, 0)
            elif direction == "U":
                add_pos = (0, 1)
            elif direction == "D":
                add_pos = (0, -1)
            elif direction == "L":
                add_pos = (-1, 0)
            head = (head[0] + add_pos[0], head[1] + add_pos[1])
            for i in range(0, tail_length):
                if i == 0:
                    prev = head
                else:
                    prev = tails[i - 1]

                tail = tails[i]
                moved_tail = move_tail(prev, tail)
                if moved_tail != tail:
                    del tails[i]
                    tails.insert(i, moved_tail)
            tail_visits.add(tails[-1])
    return len(tail_visits)


def part1(input: str):
    return solution(input, 1)


def part2(input: str):
    return solution(input, 9)
