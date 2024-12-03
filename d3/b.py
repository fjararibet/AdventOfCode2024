import sys

input = open(sys.argv[1]).read().strip()

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
pos = 0
ans = 0
while (True):
    dont_pos = input.find("don't()", pos)
    do_pos = input.find("do()", pos)
    mul_pos = input.find("mul(", pos)
    if mul_pos == -1:
        break
    if dont_pos != -1 and dont_pos < mul_pos:
        pos = do_pos
        if pos == -1:
            break
        continue
    comma_pos = input.find(",", mul_pos + 4)
    first_half_good = True
    lhs = ""
    for i in range(mul_pos + 4, comma_pos):
        if input[i] not in numbers:
            first_half_good = False
            pos = i
            break
        lhs += input[i]
    if not first_half_good:
        continue
    lhs = int(lhs)

    close_pos = input.find(")", comma_pos + 1)
    if close_pos == -1:
        continue
    second_half_good = True
    rhs = ""
    for i in range(comma_pos + 1, close_pos):
        if input[i] not in numbers:
            second_half_good = False
            pos = i
            break
        rhs += input[i]
    if not second_half_good:
        continue
    rhs = int(rhs)

    pos = close_pos + 1
    ans += lhs * rhs
print(ans)
