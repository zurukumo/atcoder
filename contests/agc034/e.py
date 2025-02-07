import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(2000)

N = int(input())
for K in range(12):
    if 2**K >= N:
        break

S = input()

path = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)


def dfs(parent, current, dp):
    max_dp = 0
    for i in path[current]:
        if i == parent:
            continue
        dp_ = [0] * 3
        dfs(current, i, dp_)
        dp[0] += dp_[0]
        dp[1] += dp_[1]
        max_dp = max(max_dp, dp_[1] + dp_[2])

    if max_dp > dp[1]:
        dp[2] = max_dp - dp[1]
    else:
        dp[2] = dp[1] % 2

    if parent == -1:
        return dp

    else:
        if S[current] == "1":
            dp[0] += 1

        dp[1] += dp[0]
        dp[2] += dp[0]


ret = 10**10

for root in range(N):
    dp = dfs(-1, root, [0] * 3)
    if dp[2] == 0:
        ret = min(ret, dp[1] // 2)

if ret == 10**10:
    print(-1)
else:
    print(ret)
