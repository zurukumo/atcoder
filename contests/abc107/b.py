H, W = map(int, input().split())
a = [input() for _ in range(H)]

yoko = [False] * H
for i in range(H):
    k = set()
    for j in range(W):
        k.add(a[i][j])
    if len(k) == 1 and "." in k:
        yoko[i] = True

tate = [False] * W
for i in range(W):
    k = set()
    for j in range(H):
        k.add(a[j][i])
    if len(k) == 1:
        tate[i] = True

for i in range(H):
    if yoko[i]:
        continue
    s = ""
    for j in range(W):
        if tate[j] and "." in k:
            continue
        s += a[i][j]
    print(s)
