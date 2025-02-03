from itertools import combinations

c = input()

n = len(c)


def solve():
    for i in range(1, n + 1):
        for comb in combinations(range(n), i):
            ret = [0] * n
            for j in comb:
                for k in range(n):
                    ret[k] |= 1 if c[(j + k) % n] == "o" else 0
            if sum(ret) == n:
                return i


print(solve())
