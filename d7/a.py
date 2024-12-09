import sys

input = open(sys.argv[1]).read().strip()

lines = input.split("\n")

values = {}
for line in lines:
    val, equation = line.split(":")
    values[int(val)] = [int(x) for x in equation.strip().split()]

ops_list = [lambda x, y: x + y, lambda x, y: x * y]


def generate_ops(n, current):
    if len(current) == n:
        yield current
    else:
        yield from generate_ops(n, current + [ops_list[0]])
        yield from generate_ops(n, current + [ops_list[1]])

ans = 0
for val, equation in values.items():
    all_ops = list(generate_ops(len(equation) - 1, []))

    results = []
    for ops in all_ops:
        result = equation.copy()
        for i, op in enumerate(ops):
            result[i+1] = op(result[i], result[i+1])
        results.append(result[-1])
    if val in results:
        ans += val

print(ans)
