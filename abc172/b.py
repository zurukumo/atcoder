S = input()
T = input()

ret = 0
for s, t in zip(S, T):
    if s != t:
        ret += 1

print(ret)
