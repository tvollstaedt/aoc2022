def parse(crates):
    stacks = crates.splitlines()[-1].split()
    stack = {}
    for s in stacks:
        stack[s] = []
        chars_per_stack = 4
        for crate in crates.splitlines()[:-1]:
            start = (int(s) - 1) * chars_per_stack
            curr = crate[start: start + chars_per_stack][1]
            if not curr.isspace():
                stack[s].append(curr)
    return stack


def part1(input: str):
    [crates, instructions] = input.split("\n\n")
    stack = parse(crates)
    for instruction in instructions.splitlines():
        _, a, _, f, _, t = instruction.split(" ")
        for _ in range(0, int(a)):
            stack[t].insert(0, stack[f].pop(0))
    return "".join([stack[s].pop(0) for s in stack])


def part2(input: str):
    [crates, instructions] = input.split("\n\n")
    stack = parse(crates)
    for instruction in instructions.splitlines():
        _, a, _, f, _, t = instruction.split(" ")
        stack[t] = stack[f][:int(a)] + stack[t]
        stack[f] = stack[f][int(a):]
    return "".join([stack[s].pop(0) for s in stack])
