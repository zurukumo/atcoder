A, B = map(int, input().split())

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

dp = [0] * (1 << 20)
dp[0] = 1
for i in range(A, B + 1):
    c = 0
    for k, p in enumerate(prime):
        if i % p == 0:
            c |= 1 << k

    for j in range((1 << 20) - 1, -1, -1):
        if j & c == 0:
            dp[j | c] += dp[j]

print(sum(dp))
