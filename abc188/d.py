import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, C = map(int, input().split())
abc = [[int(i) for i in input().split()] for _ in range(N)]

memo = defaultdict(int)
for a, b, c in abc:
    memo[a] += c
    memo[b + 1] -= c
schedule = sorted(memo.items())

total = 0
fee = 0
for i in range(1, len(schedule)):
    fr, cost = schedule[i - 1]
    to, _ = schedule[i]
    fee += cost
    total += min(C, fee) * (to - fr)

print(total)
