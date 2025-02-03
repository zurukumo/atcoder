S = input()

ret = 0
w = 0
for s in S[::-1]:
    if s == "W":
        w += 1
    else:
        ret += w

print(ret)
