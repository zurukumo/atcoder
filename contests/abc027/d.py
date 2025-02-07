S = input()
M, plus, minus = 0, 0, 0

for s in S:
    if s == "M":
        M += 1
    elif s == "+":
        plus += 1
    else:
        minus += 1

l = []
for s in S:
    if s == "M":
        l.append(plus - minus)
    elif s == "+":
        plus -= 1
    else:
        minus -= 1
l.sort()
print(-sum(l[: M // 2]) + sum(l[M // 2 :]))
