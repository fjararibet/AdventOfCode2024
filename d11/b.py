import sys
from collections import defaultdict

input = open(sys.argv[1]).read().strip()

ans = 0
stones = [int(x) for x in input.split()]

stone_map = defaultdict(int)
for s in stones:
    stone_map[s] += 1
for _ in range(75):
    new_stones = defaultdict(int)
    for s in stone_map:
        if s == 0:
            new_stones[1] += stone_map[s]
            continue
        if len(str(s)) % 2 == 0:
            lh = int(str(s)[:len(str(s))//2])
            rh = int(str(s)[len(str(s))//2:])
            new_stones[lh] += stone_map[s]
            new_stones[rh] += stone_map[s]
            continue
        new_stones[s * 2024] += stone_map[s]
    stone_map = new_stones.copy()
for s in stone_map:
    ans += stone_map[s]
print(ans)
