from operator import attrgetter
from anytree import Node, Resolver, LevelOrderIter


def build_tree(lines, cur):
    line_num = 0
    for line in lines:
        line_num += 1
        if line.startswith("dir"):  # Found a dir
            Node(line.split()[1], type="dir", parent=cur)
        elif line[0].isdigit():  # Found a file
            f = line.split()
            Node(f[1], type="file", size=int(f[0]), parent=cur)
        elif line.startswith("$ cd"):  # Switching directories
            new_dir = line.split()[-1]
            if new_dir == "..":  # We are traversing up, so count space of current dir
                cur.size = sum([node.size for node in cur.children])
            cur = Resolver().get(cur, new_dir)
        elif line == "$ ls":  # Listing directory contents, recursively build tree of it's contents
            return build_tree(lines[line_num:], cur)

    # last entry, collect dir sizes upwards the tree
    while not cur.is_root:
        cur.size = sum([node.size for node in cur.children])
        cur = cur.parent


def parse(input):
    tree = Node("root", type="dir", size=0)
    build_tree(input.splitlines()[2:], tree)
    tree.size = sum([node.size for node in LevelOrderIter(tree, maxlevel=2)])
    return tree


def part1(input: str):
    tree = parse(input)
    return sum([node.size for node in LevelOrderIter(tree, filter_=lambda n: n.type == "dir" and n.size <= 100000)])


def part2(input: str):
    tree = parse(input)
    used_space = 70000000 - tree.size
    required_space = 30000000 - used_space
    candidate = min(
        [node for node in LevelOrderIter(tree, filter_=lambda n: n.type == "dir" and n.size >= required_space)],
        key=attrgetter("size")
    )
    return candidate.size
