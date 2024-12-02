import sys

input = open(sys.argv[1]).read().strip()

reports = input.split("\n")

ans = 0
for r in reports:
    line = r.split(" ")
    first = True
    ascending = True
    safe = True
    for i in range(len(line) - 1):
        curr = int(line[i])
        next = int(line[i + 1])
        if first:
            first = False
            if curr > next:
                ascending = False
        if ascending and curr > next:
            safe = False
            break
        if not ascending and curr < next:
            safe = False
            break
        diff = abs(curr - next)
        if diff < 1 or diff > 3:
            safe = False
            break
    if safe:
        ans += 1
print(ans)

