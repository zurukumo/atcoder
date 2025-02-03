from collections import defaultdict

S = input()

mod = 10**9 + 7
dp = defaultdict(int)
for c in S:
    if c == "c":
        dp["c"] += 1
    if c == "h":
        dp["h"] += dp["c"]
        dp["h"] %= mod
    if c == "o":
        dp["o"] += dp["h"]
        dp["o"] %= mod
    if c == "k":
        dp["k"] += dp["o"]
        dp["k"] %= mod
    if c == "u":
        dp["u"] += dp["k"]
        dp["u"] %= mod
    if c == "d":
        dp["d"] += dp["u"]
        dp["d"] %= mod
    if c == "a":
        dp["a"] += dp["d"]
        dp["a"] %= mod
    if c == "i":
        dp["i"] += dp["a"]
        dp["i"] %= mod

print(dp["i"])
