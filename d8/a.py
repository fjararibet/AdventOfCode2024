import sys
from collections import defaultdict

input = open(sys.argv[1]).read().strip()

city = [list(x) for x in input.split("\n")]

satellites = defaultdict(list)
for i, line in enumerate(city):
    for j, c in enumerate(line):
        if c == ".":
            continue
        satellites[c].append((i, j))

antinodes = set()
for letter in satellites:
    for curr_pos in satellites[letter]:
        for other_pos in satellites[letter]:
            if curr_pos == other_pos:
                continue
            antinodes.add(curr_pos)
            curr_i, curr_j = curr_pos
            other_i, other_j = other_pos
            diff_i, diff_j = curr_i - other_i, curr_j - other_j
            try:
                while curr_i + diff_i >=0 and curr_i + diff_i < len(city) and curr_j + diff_j >=0 and curr_j + diff_j < len(city[0]):
                    antinodes.add((curr_i + diff_i, curr_j + diff_j))
                    diff_i += curr_i - other_i
                    diff_j += curr_j - other_j
            except IndexError:
                pass
            diff_i, diff_j = curr_i - other_i, curr_j - other_j
            try:
                while other_i - diff_i >= 0 and other_i - diff_i < len(city) and other_j - diff_j >= 0 and other_j - diff_j < len(city[0]):
                    antinodes.add((other_i - diff_i, other_j - diff_j))
                    diff_i += curr_i - other_i
                    diff_j += curr_j - other_j
            except IndexError:
                pass
ans = 0
# for i, j in antinodes:
#     city[i][j] = '#'
#
# for line in city:
#     print(''.join(line))


print(len(antinodes))
