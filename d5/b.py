import sys
from collections import defaultdict

input = open(sys.argv[1]).read().strip()

ordering, updates = input.split("\n\n")

rules = defaultdict(list)
for pair in ordering.split("\n"):
    p, q = [int(x) for x in pair.split("|")]
    rules[p].append(q)

p2 = 0
for update in updates.split("\n"):
    update = [int(x) for x in update.split(",")]
    valid = True
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[i] in rules[update[j]]:
                valid = False
                update[i], update[j] = update[j], update[i]
    if not valid:
        p2 += update[len(update) // 2]
print(p2)
