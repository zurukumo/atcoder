N = int(input())
S = input()
T = input()

d = sum([1 if s != t else 0 for s, t in zip(S, T)])

if d % 2 == 1:
    print(-1)
    exit()

U = ""
sc, tc = 0, 0
for s, t in zip(S, T):
    if s == t:
        U += "0"
    else:
        if sc * 2 < d and s == "0":
            U += "0"
            sc += 1
        elif tc * 2 < d and t == "0":
            U += "0"
            tc += 1
        elif sc * 2 < d:
            U += "1"
            sc += 1
        elif tc * 2 < d:
            U += "1"
            tc += 1

print(U)
