import collections

N, K = map(int, input().split())
S = input()

mod = 998244353

dp = collections.defaultdict(int)
dp[""] = 1
for c in S:
    if c == "A":
        cs = ["A"]
    elif c == "B":
        cs = ["B"]
    elif c == "?":
        cs = ["A", "B"]

    new_dp = collections.defaultdict(int)
    for new_c in cs:
        for k, v in dp.items():
            if v == 0:
                continue

            new_k = (k + new_c)[-K:]
            if not (len(new_k) == K and new_k[:K] == new_k[::-1]):
                new_dp[new_k] += dp[k]
                new_dp[new_k] %= mod
    dp = new_dp

print(sum(dp.values()) % mod)
