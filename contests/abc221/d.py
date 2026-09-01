import collections
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

histories = collections.defaultdict(int)
for a, b in AB:
    histories[a] += 1
    histories[a + b] -= 1

ret = [0] * (N + 1)
cur = 0
pre_day = 0
for day in sorted(histories.keys()):
    ret[cur] += day - pre_day
    cur += histories[day]
    pre_day = day

print(*ret[1:])
