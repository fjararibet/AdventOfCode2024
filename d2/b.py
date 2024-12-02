import sys

input = open(sys.argv[1]).read().strip()

reports = input.split("\n")


def is_safe(report):
    first = True
    ascending = True
    safe = True
    for i in range(len(report) - 1):
        curr = int(report[i])
        next = int(report[i + 1])
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
    return safe


ans = 0
for r in reports:
    report = r.split(" ")
    if is_safe(report):
        ans += 1
    else:
        for i in range(len(r)):
            new_r = report[:i] + report[i+1:]
            if is_safe(new_r):
                ans += 1
                break
print(ans)
