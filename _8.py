def traverse(tree_map, x, y, val, direction):
    tree_count = 0
    step = 1
    stop = -1

    if direction == "top":
        start = y - 1
        step = -1
    elif direction == "bottom":
        start = y + 1
        stop = len(tree_map)
    elif direction == "right":
        start = x + 1
        stop = len(tree_map[0])
    else:  # left
        start = x - 1
        step = -1

    for i in range(start, stop, step):
        tree_count += 1
        if direction == "top" or direction == "bottom":
            if tree_map[i][x] >= val:
                return tree_count
        else:
            if tree_map[y][i] >= val:
                return tree_count
    return 0  # special value if tree is fully visible


def part1(input: str):
    trees = list(list(map(int, row)) for row in input.splitlines())
    # Outer row / column is always visible
    visible = len(trees) * 2 + len(trees[0]) * 2 - 4
    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            cur = trees[y][x]
            if traverse(trees, x, y, cur, "top") == 0 or \
                    traverse(trees, x, y, cur, "bottom") == 0 or \
                    traverse(trees, x, y, cur, "right") == 0 or \
                    traverse(trees, x, y, cur, "left") == 0:
                visible += 1
    return visible


def part2(input: str):
    trees = list(list(map(int, row)) for row in input.splitlines())
    scenic_score = 0
    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            cur = trees[y][x]
            cur_score = (traverse(trees, x, y, cur, "top") or y) * \
                        (traverse(trees, x, y, cur, "bottom") or len(trees) - 1 - y) * \
                        (traverse(trees, x, y, cur, "right") or len(trees[0]) - 1 - x) * \
                        (traverse(trees, x, y, cur, "left") or x)
            if cur_score > scenic_score:
                scenic_score = cur_score
    return scenic_score
