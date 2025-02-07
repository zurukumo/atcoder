N, P = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(N)]

ab.sort(reverse=True)

ret = -float("inf")
dp = [0] * 10000
for a, b in ab:
    for i in range(P + a, a - 1, -1):
        dp[i] = max(dp[i], dp[i - a] + b)
        ret = max(ret, dp[i])

print(ret)
