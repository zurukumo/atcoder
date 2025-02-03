import collections

N = int(input())
S = input()


def solve(N, S):
    mod = 998244353

    dp = collections.defaultdict(int)
    dp[("", "")] = 1

    for c in S:
        new_dp = collections.defaultdict(int)
        accum = collections.defaultdict(int)
        for k, v in dp.items():
            accum[k[1]] += v
            accum[k[1]] %= mod

        if c == "?":
            c = "abcdefghijklmnopqrstuvwxyz"

        for pre_c in accum.keys():
            for new_c in c:
                if new_c == pre_c:
                    continue
                new_dp[(pre_c, new_c)] = (accum[pre_c] - dp[(new_c, pre_c)]) % mod

        dp = new_dp

    return sum(dp.values()) % mod


print(solve(N, S))
