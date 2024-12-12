import sys

input = open(sys.argv[1]).read().strip()
disk_map = [int(x) for x in input]

disk = []
for i, num in enumerate(disk_map):
    if i % 2 == 0:
        for n in range(num):
            disk.append(i // 2)
    else:
        for n in range(num):
            disk.append(-1)

i = 0
j = len(disk) - 1
while i < j:
    while disk[i] >= 0:
        i += 1
    while disk[j] < 0:
        j -= 1
    disk[i], disk[j] = disk[j], disk[i]
disk[i], disk[j] = disk[j], disk[i]

ans = 0
for i, id in enumerate(disk):
    if disk[i] < 0:
        continue
    ans += i * id
print(ans)
