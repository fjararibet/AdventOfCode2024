import sys

input = open(sys.argv[1]).read().strip()

stones = [int(x) for x in input.split()]

for _ in range(5):
    new_stones = []
    for s in stones:
        if s == 0:
            new_stones.append(1)
            continue
        if len(str(s)) % 2 == 0:
            lh = int(str(s)[:len(str(s))//2])
            rh = int(str(s)[len(str(s))//2:])
            new_stones.append(lh)
            new_stones.append(rh)
            continue
        new_stones.append(s * 2024)
    stones = new_stones
    print(stones)
print(len(stones))
