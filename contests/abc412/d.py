import itertools
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(M)]

abs = set()
for a, b in AB:
    if a > b:
        a, b = b, a
    abs.add((a - 1, b - 1))

ret = float("inf")
for ps in itertools.product(range(2), repeat=N - 1):
    group_x = set([0])
    group_y = set()
    for i, p in enumerate(ps):
        if p == 0:
            group_x.add(i + 1)
        else:
            group_y.add(i + 1)

    if len(group_x) < 3 or len(group_y) < 3:
        continue

    ret_x = float("inf")
    ret_y = float("inf")
    for cycle_x in itertools.permutations(list(group_x)):
        sx = 0
        for i in range(len(cycle_x)):
            a, b = cycle_x[i], cycle_x[(i + 1) % len(cycle_x)]
            if a > b:
                a, b = b, a
            if (a, b) not in abs:
                sx += 1
        ret_x = min(ret_x, sx)
    for cycle_y in itertools.permutations(list(group_y)):
        sy = 0
        for i in range(len(cycle_y)):
            a, b = cycle_y[i], cycle_y[(i + 1) % len(cycle_y)]
            if a > b:
                a, b = b, a
            if (a, b) not in abs:
                sy += 1
        ret_y = min(ret_y, sy)

    ret = min(ret, ret_x + ret_y + (ret_x + ret_y + M - N))


for cycle in itertools.permutations(range(N)):
    s = 0
    for i in range(len(cycle)):
        a, b = cycle[i], cycle[(i + 1) % len(cycle)]
        if a > b:
            a, b = b, a
        if (a, b) not in abs:
            s += 1
    ret = min(ret, s + s + M - N)

print(ret)
