N = int(input())
S = input()

le, lw, re, rw = 0, 0, S.count("E"), S.count("W")
ret = float("inf")
for s in S:
    if s == "E":
        re -= 1
        ret = min(ret, lw + re)
        le += 1
    else:
        rw -= 1
        ret = min(ret, lw + re)
        lw += 1
print(ret)
