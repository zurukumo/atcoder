import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
A = [int(i) for i in input().split()]

mod = 998244353

dp = [0] * 10
dp[(A[0] + A[1]) % 10] += 1
dp[(A[0] * A[1]) % 10] += 1
for a in A[2:]:
    new_dp = [0] * 10
    for prev in range(10):
        new_dp[(prev + a) % 10] += dp[prev]
        new_dp[(prev + a) % 10] %= mod
        new_dp[(prev * a) % 10] += dp[prev]
        new_dp[(prev * a) % 10] %= mod
    dp = new_dp

for i in range(10):
    print(dp[i])
