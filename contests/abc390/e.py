N, X = map(int, input().split())
VAC = [[int(i) for i in input().split()] for _ in range(N)]

v1 = [0] * (X + 1)
v2 = [0] * (X + 1)
v3 = [0] * (X + 1)

for v, a, c in VAC:
    if v == 1:
        target = v1
    elif v == 2:
        target = v2
    else:
        target = v3

    for i in range(X - 1, -1, -1):
        j = min(i + c, X)
        target[j] = max(target[j], target[i] + a)

for i in range(1, X + 1):
    v1[i] = max(v1[i], v1[i - 1])
    v2[i] = max(v2[i], v2[i - 1])
    v3[i] = max(v3[i], v3[i - 1])

ret = 0
for i in range(X + 1):
    for j in range(X + 1 - i):
        k = X - i - j
        ret = max(ret, min(v1[i], v2[j], v3[k]))

print(ret)
