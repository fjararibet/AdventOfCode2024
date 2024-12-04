import sys

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
n = len(lines)
m = len(lines[0])
count = 0


def obounds(i, j):
    return i < 0 or i >= n or j < 0 or j >= m


def x_max_neg(i, j):
    m_i, m_j = i - 1, j - 1
    a_i, a_j = i + 1, j + 1
    if obounds(m_i, m_j) or obounds(a_i, a_j):
        return False
    if lines[m_i][m_j] == 'M' and lines[a_i][a_j] == 'S':
        return True
    m_i, a_i = a_i, m_i
    m_j, a_j = a_j, m_j
    if lines[m_i][m_j] == 'M' and lines[a_i][a_j] == 'S':
        return True
    return False


def x_max_pos(i, j):
    m_i, m_j = i + 1, j - 1
    a_i, a_j = i - 1, j + 1
    if obounds(m_i, m_j) or obounds(a_i, a_j):
        return False
    if lines[m_i][m_j] == 'M' and lines[a_i][a_j] == 'S':
        return True
    m_i, a_i = a_i, m_i
    m_j, a_j = a_j, m_j
    if lines[m_i][m_j] == 'M' and lines[a_i][a_j] == 'S':
        return True
    return False


for i in range(n):
    for j in range(m):
        if lines[i][j] != 'A':
            continue
        if x_max_neg(i, j) and x_max_pos(i, j):
            count += 1
print(count)
