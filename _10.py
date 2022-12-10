
def part1(input: str):
    X = 1
    cycles = 0
    ops = []
    signal = 0
    # Build operation stack
    for line in input.splitlines():
        if line.startswith("addx"):
            ops.append("noop")
        ops.append(line)

    # Execute
    for op in ops:
        cycles += 1
        if cycles == 20 or (cycles + 20) % 40 == 0:
            signal += cycles * X
        c = op.split()
        if c[0] == "addx":
            X += int(c[1])

    return signal


def part2(input: str):
    X = 1
    cycles = 0
    ops = []

    for line in input.splitlines():
        if line.startswith("addx"):
            ops.append("noop")
        ops.append(line)

    crt_pos = 0
    for op in ops:
        cycles += 1

        if cycles % 40 == 0:
            print("")
            crt_pos = 0
        else:
            if crt_pos in [X - 1, X, X + 1]:
                print("#", end="")
            else:
                print(".", end="")
            crt_pos += 1

        c = op.split()
        if c[0] == "addx":
            X += int(c[1])
