import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
A = [int(i) for i in input().split()]
mod = 10**9 + 7

dp = [0] * 62
for a in A:
    for i in range(62):
        if a & (1 << i):
            dp[i] += 1

ret = 0
for i in range(62):
    ret += (N * (N - 1) - (N - dp[i]) * (N - dp[i] - 1)) // 2 * (1 << i) % mod
    ret -= dp[i] * (dp[i] - 1) // 2 * (1 << i) % mod
    ret %= mod

print(ret)
