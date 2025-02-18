T = int(input())
S = [input() for _ in range(T)]


for s in S:
    if s > "atcoder":
        print(0)
        continue

    ret = float("inf")
    for i, c in enumerate(s):
        if c > "a":
            ret = min(ret, i)
        if c > "t":
            ret = min(ret, max(0, i - 1))
    if ret == float("inf"):
        print(-1)
    else:
        print(ret)
