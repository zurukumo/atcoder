import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


N, M, L = map(int, input().split())
A = [int(i) for i in input().split()]

dp = [[float("inf")] * M for _ in range(L + 1)]

dp[-1][0] = 0

for i in range(L):
    for j in range(M):
        for target in range(M):
            cost = 0
            for l in range(i, N, L):
                cost += (target - A[l]) % M
            dp[i][j] = min(dp[i][j], dp[i - 1][(j - target) % M] + cost)

print(dp[L - 1][0])
