import sys

input = open(sys.argv[1]).read().strip()
disk_map = [int(x) for x in input]

disk = []
sizes = {}  # size, startpos
for i, num in enumerate(disk_map):
    if i % 2 == 0:
        id = i // 2
        sizes[id] = (num, len(disk))
        for n in range(num):
            disk.append(id)
    else:
        for n in range(num):
            disk.append(-1)

ids = []
for key in sizes:
    ids.append(key)
ids.sort(reverse=True)


for id in ids:
    i = 0
    j = 0
    this_size = j - i
    id_size, start_pos = sizes[id]
    while this_size < id_size:
        i = j
        if i >= len(disk):
            break
        while i < len(disk) and disk[i] != -1:
            i += 1
        j = i
        if j >= len(disk):
            break
        while j < len(disk) and disk[j] == -1:
            j += 1
        this_size = j - i
    if id_size <= this_size and i < start_pos:
        for n in range(id_size):
            disk[i], disk[start_pos + n] = disk[start_pos + n], disk[i]
            i += 1

ans = 0
for i, id in enumerate(disk):
    if disk[i] < 0:
        continue
    ans += i * id
print(ans)
