S = input()

ret = 0
u, d = 0, 0
for s in S:
    ret += u + 2 * d
    if s == "U":
        u += 1
    else:
        d += 1

u, d = 0, 0
for s in S[::-1]:
    ret += u * 2 + d
    if s == "U":
        u += 1
    else:
        d += 1

print(ret)
