S = input()
MOD = 10**9 + 7


dp = [0] * 13
dp[0] = 1
for s in S:
    dp_ = [0] * 13
    if s == "?":
        for i in range(13):
            for j in range(10):
                dp_[(i * 10 + j) % 13] += dp[i]
                dp_[(i * 10 + j) % 13] %= MOD
    else:
        s = int(s)
        for i in range(13):
            dp_[(i * 10 + s) % 13] += dp[i]
            dp_[(i * 10 + s) % 13] %= MOD
    dp = dp_

print(dp[5])
