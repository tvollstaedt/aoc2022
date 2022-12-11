import math


def parse(input):
    monkeys = []
    for line in input.splitlines():
        if line.startswith("Monkey"):
            monkeys.append(
                {"items": [], "op": "", "div_by": 0, "monkey_if_true": 0, "monkey_if_false": 0, "inspects": 0})
        if line.startswith("  Starting"):
            for item in line.split(":")[1].split(","):
                monkeys[-1]["items"].append(int(item))
        if line.startswith("  Operation"):
            monkeys[-1]["op"] = line.split(" = ")[1]
        if line.startswith("  Test"):
            monkeys[-1]["div_by"] = int(line.split(" by ")[1])
        if line.startswith("    If true"):
            monkeys[-1]["monkey_if_true"] = int(line.split(" monkey ")[1])
        if line.startswith("    If false"):
            monkeys[-1]["monkey_if_false"] = int(line.split(" monkey ")[1])
    return monkeys


def play_round(monkeys, div_or_mod):
    modulo = None
    if not div_or_mod:
        modulo = math.lcm(*[m["div_by"] for m in monkeys])

    for monkey in monkeys:
        items = monkey["items"][:]
        monkey["inspects"] += len(items)
        for item in items:
            op = monkey["op"]
            left_op = item
            right_op = op.split(" ")[2]
            if right_op == "old":
                right_op = item
            else:
                right_op = int(right_op)
            level = (left_op * right_op) if op.startswith("old *") else (left_op + right_op)
            if div_or_mod:
                level = level // 3
            else:
                level %= modulo

            target = (monkey["monkey_if_true"] if level % monkey["div_by"] == 0 else monkey["monkey_if_false"])
            monkey["items"].pop(0)
            monkeys[target]["items"].append(level)


def solution(input, rounds, div_or_mod):
    monkeys = parse(input)
    for _ in range(0, rounds):
        play_round(monkeys, div_or_mod)
    inspects = sorted([monkey["inspects"] for monkey in monkeys], reverse=True)
    return inspects[0] * inspects[1]


def part1(input: str):
    return solution(input, 20, True)


def part2(input: str):
    return solution(input, 10000, False)
