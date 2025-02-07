S = [input() for _ in range(12)]

ret = 0
for i in range(12):
    if len(S[i]) == i + 1:
        ret += 1
print(ret)
