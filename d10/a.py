import sys

input = open(sys.argv[1]).read().strip()

map = [[int(c) for c in line] for line in input.split("\n")]
starts = []
for i, line in enumerate(map):
    for j, n in enumerate(line):
        if n == 0:
            starts.append((i, j))
ans = 0
for start in starts:
    to_check = [start]
    visited = []
    while len(to_check) > 0:
        curr_i, curr_j = to_check.pop(0)
        if map[curr_i][curr_j] == 9 and (curr_i, curr_j) not in visited:
            ans += 1
            visited.append((curr_i, curr_j))
            continue
        neighbors = [
            (curr_i-1, curr_j),
            (curr_i, curr_j-1),
            (curr_i+1, curr_j),
            (curr_i, curr_j+1),
        ]
        for ni, nj in neighbors:
            if ni < 0 or ni >= len(map) or nj < 0 or nj >= len(map[0]):
                continue
            if map[ni][nj] - map[curr_i][curr_j] == 1:
                to_check.append((ni, nj))
                # print(f"{(curr_i, curr_j)} adds {(ni,nj)}")
print(ans)
