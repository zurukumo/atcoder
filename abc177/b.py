S = input()
T = input()

ret = float("inf")
for i in range(len(S) - len(T) + 1):
    tmp = 0
    for s, t in zip(S[i:], T):
        if s != t:
            tmp += 1

    ret = min(ret, tmp)

print(ret)
