N = int(input())
S = input()
T = input()


if S.count("0") != T.count("0"):
    print(-1)
else:
    ret = 0
    s0 = 0
    t0 = 0
    for s, t in zip(S, T):
        if s == "0" and t == "0" and s0 == t0:
            continue
        if s == "0":
            s0 += 1
            ret += 1
        if t == "0":
            t0 += 1
    print(ret)
