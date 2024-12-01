import sys

input = open(sys.argv[1]).read().strip()
pairs = input.split("\n")
L1 = []
L2 = []
for p in pairs:
    p = p.split(" ")
    L1.append(int(p[0]))
    L2.append(int(p[3]))

L1.sort()
L2.sort()
i = 0
ans = 0
while i < len(L1):
    ans += abs(L1[i] - L2[i])
    i += 1
print(ans)
