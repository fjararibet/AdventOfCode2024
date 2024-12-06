import sys

input = open(sys.argv[1]).read().strip()

lab = input.split("\n")

for i, row in enumerate(lab):
    for j, e in enumerate(row):
        if e == '^':
            start = (i, j)


def next_pos(i, j, c):
    if c == "^":
        return i-1, j
    if c == ">":
        return i, j + 1
    if c == "<":
        return i, j - 1
    if c == "v":
        return i + 1, j


turn_right = {"^": ">", ">": "v", "v": "<", "<": "^"}
visited = set()
dir = "^"
i, j = start
while i >= 0 and i < len(lab) and j >= 0 and j < len(lab[0]):
    visited.add((i, j))
    next_i, next_j = next_pos(i, j, dir)
    try:
        if lab[next_i][next_j] == '#':
            dir = turn_right[dir]
            continue
    except Exception:
        pass
    i = next_i
    j = next_j
print(len(visited))
