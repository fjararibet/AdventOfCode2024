import sys
from collections import defaultdict

input = open(sys.argv[1]).read().strip()
pairs = input.split("\n")
L1 = []
L2 = defaultdict(int)
for p in pairs:
    p = p.split("   ")
    L1.append(int(p[0]))
    L2[int(p[1])] += 1

ans = 0
for e in L1:
    ans += e * L2[e]

print(ans)
