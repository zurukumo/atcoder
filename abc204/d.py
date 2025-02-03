N = int(input())
T = [int(i) for i in input().split()]

M = 10 ** 5 + 10
dp = [False] * M
dp[0] = True

for t in T:
    for i in range(M - 1, -1, -1):
        if dp[i] and i + t < M:
            dp[i + t] = True

ret = float('inf')
s = sum(T)
for i in range(M):
    if dp[i]:
        ret = min(ret, max(i, s - i))

print(ret)
