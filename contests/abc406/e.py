T = int(input())

mod = 998244353

for _ in range(T):
    N, K = map(int, input().split())

    # dp[popcount][isunder] = [count, sum]
    dp = [[[0] * 2 for _ in range(2)] for _ in range(K + 1)]
    dp[0][0][0] = 1

    keta = len(bin(N)) - 2
    for keta_idx, d in enumerate(bin(N)[2:]):
        d = int(d)
        ndp = [[[0] * 2 for _ in range(2)] for _ in range(K + 1)]
        for i in range(K + 1):
            if d == 0:
                ndp[i][0][0] += dp[i][0][0]
                ndp[i][0][0] %= mod
                ndp[i][0][1] += dp[i][0][1]
                ndp[i][0][1] %= mod

                ndp[i][1][0] += dp[i][1][0]
                ndp[i][1][0] %= mod
                ndp[i][1][1] += dp[i][1][1]
                ndp[i][1][1] %= mod

                if i + 1 <= K:
                    ndp[i + 1][1][0] += dp[i][1][0]
                    ndp[i + 1][1][0] %= mod
                    ndp[i + 1][1][1] += dp[i][1][1] + (1 << (keta - keta_idx - 1)) * dp[i][1][0]
                    ndp[i + 1][1][1] %= mod
            else:
                ndp[i][1][0] += dp[i][0][0]
                ndp[i][1][0] %= mod
                ndp[i][1][1] += dp[i][0][1]
                ndp[i][1][1] %= mod

                ndp[i][1][0] += dp[i][1][0]
                ndp[i][1][0] %= mod
                ndp[i][1][1] += dp[i][1][1]
                ndp[i][1][1] %= mod

                if i + 1 <= K:
                    ndp[i + 1][0][0] += dp[i][0][0]
                    ndp[i + 1][0][0] %= mod
                    ndp[i + 1][0][1] += dp[i][0][1] + (1 << (keta - keta_idx - 1)) * dp[i][0][0]
                    ndp[i + 1][0][1] %= mod

                    ndp[i + 1][1][0] += dp[i][1][0]
                    ndp[i + 1][1][0] %= mod
                    ndp[i + 1][1][1] += dp[i][1][1] + (1 << (keta - keta_idx - 1)) * dp[i][1][0]
                    ndp[i + 1][1][1] %= mod

        dp = ndp

    print((dp[K][0][1] + dp[K][1][1]) % mod)
