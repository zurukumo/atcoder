import sys
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
XYZ = [[int(i) for i in input().split()] for _ in range(N)]

dp = [[float("inf")] * N for _ in range(2**N)]


def bit_patterns(n):
    for i in range(n + 1):
        for combo in combinations(range(n), i):
            pattern = 0
            for bit in combo:
                pattern |= 1 << bit
            yield pattern


dp[0][0] = 0
for bit in bit_patterns(N):
    for fr in range(N):
        if fr != 0 and bit & (1 << fr) == 0:
            continue

        for to in range(N):
            if fr == to:
                continue
            if bit & (1 << to) != 0:
                continue

            a, b, c = XYZ[fr]
            p, q, r = XYZ[to]

            next_bit = bit | (1 << to)
            dp[next_bit][to] = min(dp[next_bit][to], dp[bit][fr] + abs(p - a) + abs(q - b) + max(0, r - c))

print(dp[(2**N) - 1][0])
