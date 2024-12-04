import sys

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
n = len(lines)
m = len(lines[0])
count = 0


def find_next(i, j, c):
    neighbors = [(i-1, j), (i-1, j-1), (i, j-1), (i+1, j-1),
                 (i+1, j), (i+1, j+1), (i, j+1), (i-1, j+1)]
    next_list = []
    for i, j in neighbors:
        if i < 0 or i >= n or j < 0 or j >= m:
            continue
        if lines[i][j] == c:
            next_list.append((i, j))
    return next_list


for i in range(n):
    for j in range(m):
        if lines[i][j] != 'X':
            continue
        m_list = find_next(i, j, 'M')
        for p, q in m_list:
            dir_i = p - i
            dir_j = q - j

            a_i = i+2*dir_i
            a_j = j+2*dir_j
            if a_i < 0 or a_i >= n or a_j < 0 or a_j >= m:
                continue
            if lines[a_i][a_j] != 'A':
                continue
            if a_i < 0 or a_i >= n or a_j < 0 or a_j >= m:
                continue
            s_i = i+3*dir_i
            s_j = j+3*dir_j
            if s_i < 0 or s_i >= n or s_j < 0 or s_j >= m:
                continue
            if lines[s_i][s_j] != 'S':
                continue
            count += 1
print(count)
